https://github.com/grpc/grpc-java/issues/17
Race for Netty between cancel and stream creation · Issue #17 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
AbstractClientStream.cancel won't cancel the stream on the wire if it appears the stream has not yet been allocated, as is described by the comment:
// Only send a cancellation to remote side if we have actually been allocated
// a stream id and we are not already closed. i.e. the server side is aware of the stream.
However, what happens if this is the case, is that the transport is not notified of the stream destruction, and the stream will still eventually be created by the transport and not be cancelled. This issue does not seem a problem with the OkHttp transport, since it allocates the stream id before returning any newly created stream. However, Netty delays id allocation until just before the stream headers are sent, which 1) is always done asynchronously and 2) may be strongly delayed due to MAX_CONCURRENT_STREAMS.
It appears that the optimization in AbstractClientStream should be removed outright and sendCancel's doc be updated to specify the expectation to handle such cases (as opposed to directly cause RST_STREAM). Both OkHttp and Netty seem to be handling such cases already. More importantly, the optimization seems highly prone for races given that id allocation is occurring in the transport thread whereas AbstractClientStream.cancel is happening on some application thread; using the normal synchronization between application and transport threads seems more than efficient enough and simpler.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/18
Decompression occurring in Transport thread · Issue #18 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Apparently we are decompressing in the transport thread just so that we are able to provide the correct byte length to messageRead(). It seems we should remove the length argument to messageRead(), use Buffers.openStream(nextFrame, true), pass that stream to messageRead() (instead of calling toByteArray), and then set nextFrame = null.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/45
Moving decompression to the channel thread. by nmittler · Pull Request #45 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 a little light reading :)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/63
Improve thread safety of newStream() by ejona86 · Pull Request #63 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/116
Buffer Messages until TLS Handshake and HTTP2 Negotiation complete · Issue #116 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When grpc uses Netty as the client transport all RPC calls (aka HTTP2 Streams) block until the TLS Handshake and the HTTP2 negotiation is complete.
This blocking implementation (in grpc) is currently required as Netty's SslHandler doesn't buffer messages until the Handshake is complete ("You must make sure not to write a message while the handshake is in progress unless you are renegotiating."), and there is nothing to stop the user from starting to make RPC calls immediately.
This behavior comes with two problems:

With RPC calls blocking until the TLS Handshake is complete, every call launched before the TLS Handshake and HTTP2 Negotiation are done will block its thread from which one would expect async behavior though.
In cases when a DirectExecutor is being used it might lead to the EventLoop blocking forever (deadlock effectively). There is several scenarios how a deadlock could happen. One such scenario is when you are writing a server in Netty and within that server you want to connect to a grpc service to fetch some data. If you now use a DirectExecutor and reuse the EventLoop of the server with the grpc client, the TLS handshake would block the server's EventLoop, which is also the very EventLoop responsible for completing the TLS HandShake. That way neither the server nor the client would ever make progress again.

@nmittler , @ejona86 and I talked about this problem earlier today and we agreed to get rid of the blocking behavior by adding an additional ChannelHandler to the end of the pipeline (tail) that will buffer any data until TLS & HTTP2 are working. After that it will send the buffered messages through the pipeline and remove itself from the pipeline.
@nmittler @ejona86 @louiscryan
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/118
Buffer RPC Calls for when the MAX_CONCURRENT_STREAMS limit is hit. · Issue #118 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The number of concurrent RPC calls we can do is limited by HTTP2's MAX_CONCURRENT_STREAMS setting. Currently when using Netty as the client transport, each call made after this limit is reached blocks its calling thread until the number of active streams goes below the maximum again. The blocking is necessary as otherwise Netty would simply reject the stream with a PROTOCOL_ERROR, thus we want to buffer those calls and only pass them to Netty once there is room for new streams again.
Similar to #116 a user would again expect asynchronous behavior here.
The proposed solution to this problem is to remove the before mentioned buffering / blocking from grpc-java and let Netty handle it instead. To do this we will add a new Http2ConnectionEncoder implementation to Netty that acts as a decorator to the DefaultHttp2ConnectionEncoder. It will intercept calls to writeHeaders, writeData and writeRstStream and buffer all frames of streams that have been created after the maximum streams limit was reached and pass through the others. The encoder will also add a listener to the connection so that when an active stream is closed the next stream from the buffer can be created. A call to writeRstStream will cause the buffered stream to be deleted from the buffer. Frames other than HEADERS, DATA and RST_STREAM will be passed directly to the DefaultHttp2ConnectionEncoder.
We propose to contribute this change back to Netty as it will likely also be useful for other people using Netty's HTTP2 codec.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/120
Remove blocking parts from NettyClientTransport · Issue #120 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
NettyClientTransport#newStream is currently a blocking operation. It blocks until the HEADERS frame has been written on the wire. This is behavior is not what people who use our asynchronous API would come to expect.
The blocking also is the cause for severe performance issues in the QPS Client as it results in more or less in as many threads being created as there are concurrent calls going on (We have seen ~850 Threads for 1000 concurrent calls, resulting in OOM).
The blocking may also lead to deadlocking the EventLoop in cases where a DirectExecutor is used. One scenario where a deadlock might happen is when the EventLoop is not able to completely flush the HEADERS frame on the wire because then Netty would internally create a task to flush the remaining bytes and put this task in its task queue. This task can never be completed though as the EventLoop Thread is blocked by our very own newStream method waiting for the task to be completed ...
This issue depends on #116 and #118 to be resolved first.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/238
Race in Server handler initialization · Issue #238 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When initializing an incoming client connection, we call startAsync() on the transport, which registers the handler on a separate thread. This is obviously a race, and it would have probably been fixed if I had finished Service removal in #35.
Symptom:
DEBUG i.n.channel.DefaultChannelPipeline - Discarded inbound message SimpleLeakAwareByteBuf(PooledUnsafeDirectByteBuf(ridx: 0, widx: 259, cap: 1024)) that reached at the tail of the pipeline. Please check your pipeline configuration.

The quickest fix would be to call awaitRunning() from initChannel(). That reduces the rate new connections can connect, but is probably the most expedient solution, until #35 is finished.
@nmittler, thoughts?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/246
ClientAuthInterceptor synchronizes on wrong object · Issue #246 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The "this" in synchronized (this), is not the correct object to synchronize on:
https://github.com/grpc/grpc-java/blob/master/auth/src/main/java/io/grpc/auth/ClientAuthInterceptor.java#L77
It should be ClientAuthInterceptor.this instead. As the code stands, there is no synchronization between threads so you can see NullPointerExceptions as lastMetadata is set but not cached.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/340
Buffer writes until flush, before sending to transport thread/lock · Issue #340 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This design could benefit both okhttp, as it reduces synchronization overhead. It also would also improve flush behavior and make flushes predictable when MAX_CONCURRENT_STREAMS is exceeded.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/452
Netty streams should reduce the capacity of pooled buffers passed to sendFrame · Issue #452 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When a small write and flush is passed through the framer we hold the full 4k of the buffer until the write completes. By reducing the capacity of a pool direct buffer to the readably byte limit we immediately release the unwritten portion of the buffer back to the pool.
This may or may not have an impact on performance and utility should be evaluated by bencmarking. It may improve performance by making more bytes available to thread-local allocation. The most likely benchmarks to be impacted would be streaming ones that write and flush many messages in a tight loop as it would alleviate buffer-arena locks.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/461
Remove thread-hop required for blocking stub · Issue #461 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Once #150 CallOptions is supported, we can use a per-call direct executor for blocking stubs.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/502
Allow for batching writes to the framer · Issue #502 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Need to allow applications to perform a sequence of writes that cause a single flush in the framer to improve throughput.
The typical example for this would be an application thats wants to write messages until isReady() is false and to do more writes when onReady() is called. Even if the application is not flow-control aware (i.e is not using isReady) it would still be useful to allow write batching for bursty streams
One simple option for doing this would be to delay the outbound framer flush while executing  onPayload/isReady callbacks though this would only help cases where sends are done inside these callbacks by the same thread. A more thorough API change is probably warranted.
To give some performance context the change described above allows the FlowControlledMessagesPerSecondBenchmark to go from ~700kqps to ~4Mqps on my box
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/518
In-Process Transport · Issue #518 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It would be useful to have a light-weight, low-overhead, in-process transport. It could be used in testing, using gRPC to an endpoint that may be in the same process, and bridging from other protocols (like REST or SOAP).
Today, we recommend using Netty's in-process transport for testing. This has the same benefit of using fakes, in that it tests more of the system's actual behavior. This still seems preferred for testing, but it does cause messages to be serialized and de-serialized.
For the design, I propose we implement an in-memory client/server transport (not a Channel/Server). Implementing a transport instead of Channel/Server lets Channel/Server continue to handle the listener threading model and would keep more behavior in sync (especially error handling). In order to prevent serializing messages, the InputStream passed to the transport would be the same InputStream passed out of the transport. Marshaller.parse() could then do an instanceof check and avoid serialization.
For example, for proto we would add something like the following to parse() in ProtoUtils, since messages are immutable:
if (stream instanceof DeferredProtoInputStream) {
  return ((DeferredProtoInputStream) stream).message();
}
The transport itself would not create any threads and do all its work in the caller's thread. I think it wouldn't even need to use locks for thread safety, as Stream is not thread-safe. If the application uses directExecutor for Channel and Server, then no threads would be created.
@jhump
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/576
Apply client side timeouts by johnbcoughlin · Pull Request #576 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The contract to close() is very important, but it's also not as hard to satisfy at it would seem.
Firstly, you should realize that almost all stream processing occurs within the transport, and the transport is single-threaded. In Netty's case, this is because it runs on its own thread. In OkHttp, it acquires a lock. So state checking, in general, is already thread-safe.
It appears that OkHttp does not acquire the lock in these code paths, but instead uses an atomic operation on a map. I do find it very difficult to reason about the thread-safety of various calls; it requires way too much knowledge of how the pieces interact to verify. But I also do believe that the current code is relatively bug-free of thread safety issues.
Secondly, we guarantee to serialize all callbacks, thus we can even have non-volatile state that prevents any notifications after closed. It would be good not to rely on that, though, because it means somewhere else our code was in an inconsistent state, but in general it can be a good safety net. I see some bugs with it now though (like we don't close the message if closed).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/577
Android interop test should create channel in background thread. · Issue #577 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When the host is not an ip address, addressing resolving will cause NetworkOnMainThreadException.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/578
OkHttpClientTransport.start should be async · Issue #578 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Connecting should be run in an executor. The main problem is that we currently can't create the frameWriter (an AsyncFrameWriter) until we have connected. The frameReader doesn't seem to be as big of an issue as we can just delay executing clientFrameHandler.
We could try to use the same SerializingExecutor that is used inside AsyncFrameWriter. We would need to lazily initialize some things used on that thread, but we would be able to guarantee that the connection is started before real writes occur and they would be automatically queued.
This would fix the true problem that is causing #577.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/583
OkHttp's cancellation is not properly synchronized · Issue #583 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
OkHttpClientStream.sendCancel() calls finishStream() from an application thread. But finishStream() calls transportReportStatus() without any lock held. That is not synchronized correctly, as transportReportStatus() may only be called from the transport thread (i.e., while lock is held).
It seems that all usages of streams is done while lock is held except for within finishStream() and data(). data() can actually race with finishStream() and end up sending DATA frames after the RST_STREAM. It seems it would be best to just have stream protected by lock, because it having its own synchronization isn't providing much benefit and isn't leading to correct code.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/622
AbstractStream should enforce calling thread · Issue #622 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In AbstractStream, there are several javadoc comments that read:
"This must be called from the transport thread, since a listener may be called back directly."
While this is informative, it would be even better if it was enforced.  It would be a good idea to call Thread.currentThread().getId(), or some similar check to make sure that the transport thread is actually the one making the call.  In cases where holding a lock is tantamount to being threadsafe, checking Thread.holdsLock() would also be possible.  Ideally these cases could be wrapped up in some sort of assertTransportThread() method.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/634
Use shared scheduler for ServerImpl deadline support · Issue #634 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#576 was merged slightly before #619, so we are able to use a single thread for deadlines on server-side and client-side. That isn't super-important, since we don't expect more than one server generally, but could is still maybe a nice-to-have. At the very least, the TODO could be removed if we decided not to bother.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/644
Minimize context switches between app & net threads when requesting more messages by louiscryan · Pull Request #644 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/681
Attaching Metadata to error Status responses... · Issue #681 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I'm not sure what the "best practice" is for returning application-level error information (would be very useful to understand Google's own internal practice for guidance), but certainly one approach is to attach trailing headers with application error information to error responses. Setting additional headers via thread-local using a server interceptor seems easy enough, but for client-side it seems particularly awkward capturing metadata on a per-call basis using an interceptor. I see examples in MetadataUtils for capturing "last set headers" on a stub or channel but this is only useful for testing and cannot capture on a per-call basis. Other option would be to use the async stub and a thread-local to pass the metadata information along to StreamObserver.onError() but this loses the convenience of using the blocking and future stubs. I'm not sure if the same approach works for a blocking or future stub since the listener may be invoked in a different thread.
Will the context api once fully integrated make this easy, or would it make sense to have a way to "attach" metadata to a Status object (perhaps this would be desirable anyway for convenience)?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/696
In-process transport deadlock during shutdown · Issue #696 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Simultaneously shutting down both server and client sharing the same in-process transport can lead to a deadlock. During server shutdown, the transport lock is held while calling transportShutdown on the channel listener, which attempts to lock the channel. At the same time, channel.shutdownNow() holds the channel lock while also trying to lock the transport which leads to a deadlock:
Found one Java-level deadlock:
=============================
"AccountServer STOPPING":
  waiting to lock monitor 0x00007f88221d72a8 (object 0x000000076eb28a20, a io.grpc.ChannelImpl),
  which is held by "main"
"main":
  waiting to lock monitor 0x00007f8824015488 (object 0x000000076c2afb38, a io.grpc.transport.inprocess.InProcessTransport),
  which is held by "AccountServer STOPPING"

Java stack information for the threads listed above:
===================================================
"AccountServer STOPPING":
    at io.grpc.ChannelImpl$TransportListener.transportShutdown(ChannelImpl.java:281)

Found 1 deadlock.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/942
Daemonize shared threads, and make sure each thread has a name by carl-mastrangelo · Pull Request #942 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM. Note that the daemonizing work is not complete. There are OkHttp and Netty threads that also must be marked daemon.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/945
Daemonize InProcess threads by carl-mastrangelo · Pull Request #945 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM. Those threads are expected to be very short lived, but it doesn't hurt.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/967
Update examples in light of daemon threads · Issue #967 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
At the very least, the hello world server example is broken, because it exits immediately. It needs a call to server.awaitTerminated(). This was caused by the swapping to daemon threads in 07a7279.
As reported on StackOverflow.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/970
Update server to await termination in the main thread by carl-mastrangelo · Pull Request #970 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo, LGTM, but this does not fix #967. Please verify the other examples as well; I know routeguide is also broken.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/595
Fix the potential deadlock. by madongfly · Pull Request #595 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/667
Simplify locking model of OkHttp Transport, avoid potential deadlock. by madongfly · Pull Request #667 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/31
Fixing @GuardedBy annotation to use the correct lock name. by nmittler · Pull Request #31 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/271
Hold lock while reading isThreadScheduled by ejona86 · Pull Request #271 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/325
Determine upper-bound for Netty buffer sizes used in frame · Issue #325 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
As a follow on to
#312
we need benchmarks to determine whether we should be placing an upper-bound on the buffers allocated to the MessageFramer from Netty. We are already setting a lower-bound to page-size (default is 8k) to facilitate buffer object caching within Netty as well as allowing for follow-on writes.
Setting an upper-bound should probably be done by benchmark (unless one already exists)
Above the Netty arena size (currently 16MB) Netty will allocate an Unpooled buffer. Above 32k Netty takes an arena lock to allocate a buffer out of the arena (i.e. it will not cache the buffer itself)
See https://www.facebook.com/notes/facebook-engineering/scalable-memory-allocation-using-jemalloc/480222803919
for the scheme Netty follows
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/330
OkHttpClientTransport.onGoAway() races with startPendingStreams() · Issue #330 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
onGoAway has two phases: do things necessary under lock and final cleanup. In the first phase it collects the streams to terminate in the second and sets goAway.
startPendingStreams() does not observe goAway and also creates new streams that should be failed due to the goAway. From an initial look, it seems it would be best to remove failPendingStreams() and simply integrate its two phases into onGoAway()'s two phases; that is, when holding the lock in onGoAway, replace pendingStreams with an empty list, and then when not holding the lock call transportReportStatus
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/553
Make ChannelImpl.obtainActiveTransport's fast path lock-free by ejona86 · Pull Request #553 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/569
Stop using intrinsic locks in ChannelImpl/ServerImpl · Issue #569 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I originally used intrinsic locks for expediency. We were still designing quite a bit and we were still using Service. It seems swapping away from intrinsic locks makes sense, as we have no want/need to allow users to compose method calls into higher-order atomic calls.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/673
Stop using intrinsic lock in ServerImpl by carl-mastrangelo · Pull Request #673 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo, LGTM. Please improve the commit message.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/674
Stop using intrinsic locking in ChannelImpl by carl-mastrangelo · Pull Request #674 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM. Please improve commit message.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/698
Don't hold channel/server lock when shutting down transport by ejona86 · Pull Request #698 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/66
Fix shutdown race with negotiation by ejona86 · Pull Request #66 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/229
Fix a race condition in the test, we may notify MockFrameReader to return before it starts waiting. by madongfly · Pull Request #229 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Without this change, the test failed 2~3 times out of 10 runs, with this change, it passed 30 runs.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/290
Improve documentation of contract of io.grpc.Call · Issue #290 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This class seems to be underspecified. A couple of issues which can't be easily derived:

Can request(N) be called multiple times before the next payload is received, and is it accumulating.
If not accumulating, what does it mean if request(0) is called after request(N) but before payload is received. Does it suppress the already scheduled output? How strong is the contract that there are never more than N responses?
Can there be race conditions for request() calls and onPayload() calls on the listener.
Is request() always be called before sendPayload() or can it be also called afterwards.
What happens if any of the Call methods is called after halfClose, cancel, or onClose.
if cancel is called, should it eventually report onClose(Status.CANCELLED) on the listener.

There might be more. Ideally we would specify the allowed sequences and interferences between call and listener.
I may follow up with a suggestion for the spec later.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/345
Fix the race between failing and starting pending streams. by madongfly · Pull Request #345 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/605
BufferingHttp2ConnectionEncoder does not shutdown properly on channelInactive · Issue #605 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@nmittler
There is a nasty race condition during the handling of channelInactive in NettyClientHandler which goes a bit like this....

NettyClientHandler.channelInactive -> for each active stream report closure to GRPC
NettyClientHandler.channelInactive -> Http2ConnectionHandler.channelInactive -> Http2ConnectionHandler.BaseDecoder.channelInactive -> for each active stream call close -> BufferingHttp2ConnectionEncoder.Http2ConnectionAdapter.onStreamClose -> try creating new stream -> adds stream to active list (OOPS! this stream is never closed)

This reproduces for NettyClientTransportTest.bufferedStreamsShouldBeClosedWhenTransportTerminates with 5.0beta5.
Having streams being created as a side-effect of channel inactivation is undesirable. Potential fixes include

Reorder teardown in Http2ConnectionHandler.BaseDecoder.channelInactive so encoders are closed() before streams are closed.
Make BufferedHttp2ConnectionEncoder check channel.isActive() when trying to create streams.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/755
Remove Status.OperationRuntimeException and Status.OperationException by madongfly · Pull Request #755 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Doh! You and @carl-mastrangelo raced for #754. If you make sure to assign the issue to yourself, that can prevent duplicated effort.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/887
OkHttp: race between sendCancel and sendFrame. · Issue #887 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If sendCancel is called (by timeout for example) before the stream is started, a following sendFrame will cause a NPE:
java.lang.NullPointerException
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/889
OkHttp: Fix race condition between sendCancel and sendFrame by madongfly · Pull Request #889 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/999
Possible race condition ServerImpl between start() and shutdown() · Issue #999 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I believe it may be possible if start and stop are called concurrently that the shared executor may not get released.  I'm not sure if this is an actual problem, but it does go against the @ ThreadSafe annotation.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/80
Daemon Threads in grpc
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We have to decide how to deal with daemon threads. Grpc uses non-daemon threads by default and so the pattern

ServerImpl server = NettyServerBuilder. ...
// non blocking
server.start()
works fine.

However, if one was to provide a custom executor that uses daemon threads the above would terminate immediately. It's quite likely that people will unknowingly provide daemon threads to grpc by passing in custom Netty EventLoopGroup.

e.g.
EventLoopGroup boss = new NioEventLoopGroup(1);
Netty's EventLoops use a ForkJoinPool executor by default, which uses daemon threads.

The same issue exists on the client.
OkHttp uses non-daemon threads by default as @ejona86 pointed out to me.

One solution would be to add an infinite awaitTermination() method that does what the name suggests. Another solution would be to create a dummy non-daemon thread on startup and thus ensure that the JVM doesn't exit prematurely.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/82
netty: Use DEFAULT_WORKER_EVENT_LOOP_GROUP for both client and server 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We have separate thread pool for client workers vs server workers. We would be better suited by using a single worker thread pool for client and server (still likely having a separate boss thread pool on server). It would use fewer threads and reduce thrashing on a server that was also a busy client.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/99
Add duration paramter to QPS Client and remove "server_threads" parameter
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Add duration paramter to QPS Client and remove "server_threads" parameter.

The QpsClient no longer executes a fixed number of RPCs but runs for a period of time now (see #83).
After some discussion with @ejona86, we also agreed to remove the "server_threads" parameter
and to no longer use a DirectExecutor and thus run the QPS Server without any tweaks and
modifications. We believe/hope that this change will make the comparison between the C++ and
Java versions less "Apples and Oranges".

The "client_threads" parameter was renamed to "concurrent_calls" to better reflect what it
acutally does.

Furthermore, I updated the gradle build script to create separate executables for the
client and the server.

I also added a README.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/152
The Future interface doesn't implement cancellation · Issue #152 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently Future returned by the future interface is a SettableFuture and it doesn't implement the RPC cancellation. It should be as easy as implementing AbstractFuture.interruptTask().
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/153
Implement cancellation for the Future interface. by zhangkun83 · Pull Request #153 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/182
Vendorize our usages of OkHttp internal classes
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Using the normal OkHttp API didn't quite seem to work for us. The blocking style made it seem like we would need a thread per stream, flow control wasn't exposed enough (although this may no longer be an issue due to how we are now using flow control, other than blocking), RST_STREAM, and other similar advanced HTTP/2 features didn't have quite as much support as we needed. Oh, and trailers...

So that led us to use internals of OkHttp that we shouldn't be, because it will be brittle. Instead, we should propose/upstream an API that supports advanced usage and can be stable.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/227
Enable parallel Gradle builds for Travis by ejona86 · Pull Request #227 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/241
Disable Travis parallel building to reduce memory usage by ejona86 · Pull Request #241 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/976
Use service provider for server-side  · Issue #976 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is effectively #961 for getting a ServerBuilder. It would only use Netty today.
Whether we extend the current ManagedChannelProvider to allow creating server builders or make a parallel path is up for discussion, but honestly we should just flip a coin and go with one.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/317
Integration test largeUnary failing · Issue #317 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We recently ran into an issue with one of our services where sending large responses results in transport errors being logged as well as eventual transport failure. I managed to reproduce this behavior in integration test largeUnary as well. When running a single iteration of largeUnary the test passes although connection errors are logged:
(ThreadPoolExecutor.java:1142)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/239
Lacking preconditions for start() in ChannelImpl.CallImpl · Issue #239 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For instance, calling request() before start() has been called results in a NullPointerException.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/247
Fix synchronization in client auth by ejona86 · Pull Request #247 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/322
Improve synchronization of SerializingExecutor. · Issue #322 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We are seeing some contention in ChannelImpl.obtainActiveTransport() and SerializingExecutor.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/479
Improve synchronization in obtainActiveTransport() · Issue #479 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Split out of #322
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/682
Make new stream call asynchronous when the MAX_CONCURRENT_STREAMS is reached. by madongfly · Pull Request #682 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/642
Improve Metadata by ejona86 · Pull Request #642 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Change looks easy to understand. Nice work.

Forgive me if already discussed, but what's your opinion on just using
LinkedHashMap vs conditionally TreeMap for consistent ordering for tests?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<