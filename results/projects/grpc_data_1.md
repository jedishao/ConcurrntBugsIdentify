

https://github.com/grpc/grpc-java
https://github.com/grpc/grpc-java/issues/1
Update to OkHttp 2.1 final. by JakeWharton · Pull Request #1 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
One less SNAPSHOT to deal with...
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/2
Update to latest OkHttp master. by JakeWharton · Pull Request #2 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We'll probably wait on it a bit, unless I'm missing something. Since there weren't any functional changes, we can still advertise h2-16 with the existing code. There is a non-zero cost to upgrading our okhttp version internally so I figure just wait until we get something for it. (Especially since okhttp doesn't provide SNAPSHOT binaries to Maven Central)
Do note that the change would also need to update the git submodule that we now have in lib/.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/3
Update OkHttp to h2-16. by codefromthecrypt · Pull Request #3 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
See #2
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/4
Resolve drift in Netty http/2 apis. by codefromthecrypt · Pull Request #4 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If you could also update the lib/netty submodule to the commit you are basing this work, that would be helpful (either HEAD or Nathan's commit).
We are definitely interested in inbound flow control, but it also seems like you ported over our usage of it. Did you mean outbound flow control? If so, then the answer is "yes, but not yet."
We haven't yet figured out the method name/API for exposing outbound flow control to applications in the Call/ServerCall class. We actually had an idea of how we wanted it to look, but couldn't quite decide on a name. There is now a conversation of changing flow control to look more like reactive-streams, which would also impact the interface.
We will certainly want to provide outbound flow control feedback to the application, but we don't yet know concretely what that will look like.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/5
Adopt token-based flow control from reactive-streams · Issue #5 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/6
Implement outbound flow control · Issue #6 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Should be token-based a la reactive streams. Although it also seems that maybe we will only ever have at most 1 token passed to the application.
Currently we provide no method of pushback to the application and buffer infinitely as the application sends.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/7
Investigate excessive flushing in Netty · Issue #7 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Determine ways to reduce number of flushes we perform. For example, if the header frame is being sent, flushing afterward is generally a waste since a DATA frame typically follows. We want methods that allow smart semi-automatic flushing or using knowledge from application layer.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/8
Optimize buffer usage in MessageFramer · Issue #8 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We currently allocate a large non-direct buffer per stream due to MessageFramer, only to copy immediately out of it. We should instead write directly to the transport-native buffer, which will cause us to have a WriteableBuffer or some such like our current Buffer class that is ready-only.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/9
Choose benchmark framework: JMH vs Caliper · Issue #9 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/10
Unary requests always send an empty DATA frame with EOS=true to close stream · Issue #10 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is a performance issue. We should be able to set EOS=true on the DATA frame with the request payload rather than having to always write N+1 DATA frames. Likely fix is in frame interfaces.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/11
Update .gitignore for Gradle by ejona86 · Pull Request #11 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM :)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/12
Improve test client for real cert by ejona86 · Pull Request #12 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM ... feel free to cherrypick.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/13
Align server flags with other languages by ejona86 · Pull Request #13 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 it looks like this is based on work in #12 ... can you rebase after #12 is cherrypicked?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/14
Changing gRPC Java inbound flow control symantics by nmittler · Pull Request #14 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look at this?  This is a rather large PR, so you can start by just reviewing the changes to MessageDeframer ... once we're happy with that we can move on to the rest of the PR.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/15
Move to a non-snapshot version of OkHttp by maniksurtani · Pull Request #15 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
See #2 and #3. Although now maybe we it's the right time to do this.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/16
Do we need both gradle and maven? · Issue #16 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Keeping dependencies and other details in pom.xml and build.gradle will become a tedious overhead.  Any reason to support two build systems?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

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

https://github.com/grpc/grpc-java/issues/19
Change base package name to io.grpc · Issue #19 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Lots of renames, but not really hard.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/20
Fix IntelliJ dependency on generated protobufs by louiscryan · Pull Request #20 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/21
Remove Guava's Service from our immediate API · Issue #21 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Service doesn't gain us anything and is just painful for our users. We should remove it and just make our own API (start and stop, plus health-checking API).
This has already been done for Channel. It still needs to be done for Server, but I'm already working on that.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/22
TLS support for OkHttp when not running on Android · Issue #22 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
OkHttp transport current accepts a SSLSocketFactory which when on Android is provided by the OS. For testing when not running on Android we don't have a way to do TLS/ALPN. We need one.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/23
Figure out what names we want for Client Foos vs Server Foos · Issue #23 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We have Call on both Client and Server. When adding the server, we chose ServerCall as the name of the server-side Call, and discussed renaming the client-side to ClientCall. ClientInterceptor was named based on this idea. However, the rename hasn't happened yet and now some have suggested having the Client names simply lack "Client" (so it would remain "Call"). It seems it has simply been too long since the original discussion for us to remember what was decided.
We need to decide to either prefix Client with Client and Server with Server or only prefix Server with Server. After the decision, whatever needs fixing needs to be fixed.
Note that in the transport we must have ClientStream prefixed with Client, since Stream is a shared interface between Client and Server.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/24
Add unit tests to AbstractServerStream · Issue #24 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Some unit tests from NettyServerStream are probably appropriate to move.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/25
Add unit tests for AbstractClientStream · Issue #25 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Some unit tests from NettyClientStream are probably appropriate to move.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/26
Add tests for convert non-200 HTTP status codes to GRPC codes · Issue #26 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The GRPC runtime should handle receiving HTTP2 responses with :status set to something other than 200. The runtime will need to map this to a GRPC status
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/27
Add unit tests for ChannelImpl · Issue #27 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/28
Channel-state API · Issue #28 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
At this moment, creating TCP connections are created lazily on first call of a Channel, and if the TCP connection goes down it isn't reconnected until a subsequent call. However, some users will want the TCP connection to be created and maintained during the lifetime of the Channel.
This "constant connection" behavior does not make as much sense when accessing a third party service, as the service may purposefully be disconnecting idle clients, but is very reasonable in low-latency, intra-datacenter communication.
We need an API to choose between those behaviors and to export failure information about the Channel. All of this is bundled together for the moment under the name "health-checking API," but we can split it apart as it makes sense.
They are tied together for the moment because certain operations like "wait until Channel is healthy" assume that the channel will actively try to connect.
Some notes from @louiscryan:

Do we want to canonicalize transport failure modes into an enum or are we
happy with a boolean indicating transient vs. durable. What failure modes
will we have

wire incompatability which can occur at any time and while is in theory
transient you may not want your application to continue working
unreachable
internal implementation error
redirection. the addressed service has moved elsewhere
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/29
Adding .gitignore for eclipse files. by nmittler · Pull Request #29 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 this should be an easy one :)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/30
Netty HTTP/2 negotiation fails silently if ALPN/NPN in classpath, but jetty_alpn not in bootclasspath · Issue #30 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If you properly have ALPN/NPN in your classpath, but lack jetty_alpn in your bootclasspath, then we just hang after sending a SETTINGS frame. ALPN never happens, but "unsupported" isn't even called because that is normally called by jetty_alpn.
This makes it hard for users to determine what is wrong with their setup.
The only idea I have for a fix is to set a boolean when our ClientProvider is called and detect if it isn't set.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/31
Fixing @GuardedBy annotation to use the correct lock name. by nmittler · Pull Request #31 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/32
Add test target for codegen by zhangkun83 · Pull Request #32 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/33
Remove Service API from ServerImpl by ejona86 · Pull Request #33 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/34
Optimize number of DATA frames for unary requests by ejona86 · Pull Request #34 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM ... feel free to cherry-pick!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/35
Remove Guava's Service from transport API · Issue #35 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For similar reasons as #21, but more for ourselves instead of our users.
This will allow us to be much more precise and have nuances explicitly like how a connection can GOAWAY for new streams but keep the old streams processing.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/36
Idea config breaks clean gradle build · Issue #36 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
$ gradle clean
$ gradle build
FAILURE: Build failed with an exception.

* Where:
Build file '/home/ejona/clients/grpc-java/integration-testing/build.gradle' line: 31

* What went wrong:
A problem occurred evaluating project ':stubby-integration-testing'.
> java.lang.NullPointerException (no error message)

Commenting out line 31 works around the problem, but obviously doesn't solve it:
excludeDirs = [file('.gradle')]
//excludeDirs += files(file("$buildDir/").listFiles())
excludeDirs -= file("$buildDir/generated-sources")
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/37
Improve imports by ejona86 · Pull Request #37 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/38
Add README.md to the compiler directory by zhangkun83 · Pull Request #38 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/39
Migrating run scripts to gradle. by nmittler · Pull Request #39 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/40
Reorder the fields of LogHelper to be consistent with initialization order by zhangkun83 · Pull Request #40 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/41
Removing Maven build by nmittler · Pull Request #41 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 looks like pretty much everything is now handled by gradle.  Removing all the pom.xml files.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/42
Removing all references to "stubby" by nmittler · Pull Request #42 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 @zhangkun83 take a look and make sure everything is in order.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/43
Add compiler and examples to the build · Issue #43 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
There is already a build.gradle file, but we need to be using protoc built from HEAD.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/44
Add examples module into the build · Issue #44 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It's already there, we just need to add a build.gradle file for it and add it to settings.gradle.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/45
Moving decompression to the channel thread. by nmittler · Pull Request #45 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 a little light reading :)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/46
Add Gradle wrapper for building. by JakeWharton · Pull Request #46 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Oh, that is a thing, would you look at that. 68K, not too bad.
Do we want to configure the version in the build.gradle, or is it just redundant?
task wrapper(type: Wrapper) {
    gradleVersion = '2.2.1'
}
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/47
Remove OkHttp submodule as we now depend on a release version. by JakeWharton · Pull Request #47 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/48
Remove explicit Okio dependency. by JakeWharton · Pull Request #48 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Rebased and pushed as 6a93de9
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/49
Updating examples based on recent changes. by nmittler · Pull Request #49 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/50
Have Gradle observe LDFLAGS/CXXFLAGS/CPPFLAGS by ejona86 · Pull Request #50 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/51
Improve Gradle build of protoc grpc plugin by ejona86 · Pull Request #51 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/52
Fixing integration tests by nmittler · Pull Request #52 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/53
Have test server print info about test client by ejona86 · Pull Request #53 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/54
Fixing compiler build on OS X (Clang) by nmittler · Pull Request #54 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 easy fix.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/55
Properly cleaning and ignoring bin directories. by nmittler · Pull Request #55 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan and @ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/56
Protoc build instructions by louiscryan · Pull Request #56 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Don't change the lib/netty subproject.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/57
Implement timeout/deadline in Channel · Issue #57 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/58
Implement timeout/deadline in Server · Issue #58 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/59
netty: Cancel stream if interrupted during create by ejona86 · Pull Request #59 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/60
OkHttp transport has high latency · Issue #60 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For some unknown reason, OkHttp transport regressed in performance dramatically, considering it used to be beating Netty. Unfortunately we don't know when. We need to do some profiling and figure out where the latency is coming from.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/61
"No cached instance found" exception in integration test · Issue #61 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The exception does not cause any problem other than noise, but we should still figure out what is going wrong.
java.lang.IllegalArgumentException: No cached instance found for grpc-default-executor
    at io.grpc.SharedResourceHolder.releaseInternal(SharedResourceHolder.java:144)
    at io.grpc.SharedResourceHolder.release(SharedResourceHolder.java:115)
    at io.grpc.AbstractChannelBuilder$2.run(AbstractChannelBuilder.java:109)
    at io.grpc.ChannelImpl.shutdown(ChannelImpl.java:113)
    at io.grpc.testing.integration.AbstractTransportTest.teardown(AbstractTransportTest.java:128)
    at io.grpc.testing.integration.TestServiceClient.teardown(TestServiceClient.java:160)
    at io.grpc.testing.integration.TestServiceClient.access$000(TestServiceClient.java:51)
    at io.grpc.testing.integration.TestServiceClient$1.run(TestServiceClient.java:65)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/62
Simplify connection callback handling in Netty by ejona86 · Pull Request #62 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/63
Improve thread safety of newStream() by ejona86 · Pull Request #63 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/64
Channel interface needs shutdown/close · Issue #64 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
With the elimination of Service the Channel interface is now insufficient for normal use.
While ChannelImpl has a shutdown Channel does not and intercepting a ChannelImpl immediately converts it into Channel.
Closeable/AutoCloseable would be fine too
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/65
Consider making Channel/Server abstract classes · Issue #65 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
They were interfaces previously because of the bane of Service and the need to extend Abstract*Service in ChannelImpl/ServerImpl. Now that Service is gone from those APIs, we could swap to using abstract classes to give us greater ability to add to the APIs in the future.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/66
Fix shutdown race with negotiation by ejona86 · Pull Request #66 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/67
Perform hostname checking on :authority before issuing call · Issue #67 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We allow users to override the authority per-call, but we currently don't do any verification that that authority would be permitted for the current server. We should verify the provided authority against the TLS cert of the connection and fail in some way if the cert is not good for the requested authority. We would cache these verifications for the connection in a simple hash map.
It is the Java equivalent of grpc/grpc#471
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/68
QPS Client to perform throughput and latency tests. by buchgr · Pull Request #68 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.
It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA) at https://cla.developers.google.com/.
If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check the information on your CLA or see this help article on setting the email on your git commits.
Once you've done that, please reply here to let us know.  If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/69
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/70
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/71
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/72
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/73
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/74
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/75
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/76
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/77
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/78
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/79
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/80
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/81
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/82
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/83
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/84
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/85
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/86
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/87
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/88
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/89
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/90
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/91
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/92
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/93
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/94
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/95
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/96
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/97
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/98
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/99
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/100
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/101
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/102
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/103
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/104
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/105
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/106
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/107
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/108
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/109
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/110
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/111
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/112
Some comment cleanup in the Netty builders. by nmittler · Pull Request #112 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM @nmittler
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/113
Create CONTRIBUTING.md by mugurm · Pull Request #113 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/114
Cleanup Javadoc for Channel, ServerCall and their related classes. by louiscryan · Pull Request #114 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/115
Remove dead GrpcFramingUtil class by louiscryan · Pull Request #115 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
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

https://github.com/grpc/grpc-java/issues/117
Fixing memory leak in stream removal policy by nmittler · Pull Request #117 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/118
Buffer RPC Calls for when the MAX_CONCURRENT_STREAMS limit is hit. · Issue #118 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The number of concurrent RPC calls we can do is limited by HTTP2's MAX_CONCURRENT_STREAMS setting. Currently when using Netty as the client transport, each call made after this limit is reached blocks its calling thread until the number of active streams goes below the maximum again. The blocking is necessary as otherwise Netty would simply reject the stream with a PROTOCOL_ERROR, thus we want to buffer those calls and only pass them to Netty once there is room for new streams again.
Similar to #116 a user would again expect asynchronous behavior here.
The proposed solution to this problem is to remove the before mentioned buffering / blocking from grpc-java and let Netty handle it instead. To do this we will add a new Http2ConnectionEncoder implementation to Netty that acts as a decorator to the DefaultHttp2ConnectionEncoder. It will intercept calls to writeHeaders, writeData and writeRstStream and buffer all frames of streams that have been created after the maximum streams limit was reached and pass through the others. The encoder will also add a listener to the connection so that when an active stream is closed the next stream from the buffer can be created. A call to writeRstStream will cause the buffered stream to be deleted from the buffer. Frames other than HEADERS, DATA and RST_STREAM will be passed directly to the DefaultHttp2ConnectionEncoder.
We propose to contribute this change back to Netty as it will likely also be useful for other people using Netty's HTTP2 codec.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/119
Set encoding for Java source to UTF-8 by ejona86 · Pull Request #119 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/120
Remove blocking parts from NettyClientTransport · Issue #120 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
NettyClientTransport#newStream is currently a blocking operation. It blocks until the HEADERS frame has been written on the wire. This is behavior is not what people who use our asynchronous API would come to expect.
The blocking also is the cause for severe performance issues in the QPS Client as it results in more or less in as many threads being created as there are concurrent calls going on (We have seen ~850 Threads for 1000 concurrent calls, resulting in OOM).
The blocking may also lead to deadlocking the EventLoop in cases where a DirectExecutor is used. One scenario where a deadlock might happen is when the EventLoop is not able to completely flush the HEADERS frame on the wire because then Netty would internally create a task to flush the remaining bytes and put this task in its task queue. This task can never be completed though as the EventLoop Thread is blocked by our very own newStream method waiting for the task to be completed ...
This issue depends on #116 and #118 to be resolved first.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/121
Have SendGrpcFrameCommand constructor take an AbstractStream object instead of a stream id. by buchgr · Pull Request #121 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/122
Cleanup and Nitpicking by buchgr · Pull Request #122 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/123
Polish javadoc for stub/* by zhangkun83 · Pull Request #123 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/124
Update route guide gradle file with task that just generates gRPC code · Issue #124 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently there are two tasks in the gradle file, one of which builds and runs the server, one of which builds and runs the client.
In the tutorial, I'd like the users to just generate the gRPC code with protoc without running anything, it'd be useful if the gradle file offered an option to do this
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/125
Update route guide gradle file with task that just generates gRPC code · Issue #125 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently there are two tasks in the gradle file, one of which builds and runs the server, one of which builds and runs the client.
In the tutorial, I'd like the users to just generate the gRPC code with protoc without running anything, it'd be useful if the gradle file offered an option to do this
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/126
Can't build grpc-java · Issue #126 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Following the installation instructions on a new Ubiquity instance. Installed Maven 3.2, using Java 8 (Google's JDK).
All works fine until I try the final build, then get:

What went wrong:
Could not resolve all dependencies for configuration ':grpc-core:compile'.

Could not find com.google.protobuf:protobuf-java:3.0.0-pre.
Searched in the following locations:
https://repo1.maven.org/maven2/com/google/protobuf/protobuf-java/3.0.0-pre/protobuf-java-3.0.0-pre.pom
https://repo1.maven.org/maven2/com/google/protobuf/protobuf-java/3.0.0-pre/protobuf-java-3.0.0-pre.jar
file:/usr/local/google/home/lcarey/.m2/repository/com/google/protobuf/protobuf-java/3.0.0-pre/protobuf-java-3.0.0-pre.pom
file:/usr/local/google/home/lcarey/.m2/repository/com/google/protobuf/protobuf-java/3.0.0-pre/protobuf-java-3.0.0-pre.jar
Required by:
io.grpc:grpc-core:0.1.0-SNAPSHOT
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/127
Adding HelloWorld example to grpc-java repo. by nmittler · Pull Request #127 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 @tbetbetbe can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/128
Upgrade com.twitter.hpack to v0.10.1 by jpinner · Pull Request #128 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.
It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA) at https://cla.developers.google.com/.
If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check the information on your CLA or see this help article on setting the email on your git commits.
Once you've done that, please reply here to let us know.  If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/129
Polish javadoc for transport/ by zhangkun83 · Pull Request #129 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/130
Add new readme for Auth related issues by louiscryan · Pull Request #130 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86
@jayantkolhe
@LisaFC
FYI. Will add follow up to link to this from common
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/131
Create temporary directory for javanano test if it does not exist. by buchgr · Pull Request #131 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM. Thanks for the fix.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/132
Remove nano codegen test temporarily. Currently I haven't figuired by zsurocking · Pull Request #132 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.
It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA) at https://cla.developers.google.com/.
If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check the information on your CLA or see this help article on setting the email on your git commits.
Once you've done that, please reply here to let us know.  If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/133
Revert "Remove nano codegen test temporarily. Currently I haven't figuir... by zsurocking · Pull Request #133 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.
It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA) at https://cla.developers.google.com/.
If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check the information on your CLA or see this help article on setting the email on your git commits.
Once you've done that, please reply here to let us know.  If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/134
Swap to proto3 by ejona86 · Pull Request #134 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/135
Messages.proto has reference to stubby. · Issue #135 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
/integration-testing/src/main/proto/io/grpc/testing/integration/messages.proto contains the line:
package stubby.testing;
Should this be removed?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/136
Update README.md by jayantkolhe · Pull Request #136 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@LisaFC @nmittler
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/137
Updating integ test protos to be consistent with C by nmittler · Pull Request #137 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/138
Depend on proto 3.0.0-alpha-2 instead of snapshot by ejona86 · Pull Request #138 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/139
Bug fix. frameWriter and frameReader are not initialized when an Excepti... by zsurocking · Pull Request #139 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.
It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA) at https://cla.developers.google.com/.
If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check the information on your CLA or see this help article on setting the email on your git commits.
Once you've done that, please reply here to let us know.  If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/140
Adding SimpleContext back into messages.proto. by nmittler · Pull Request #140 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/141
New auth readme by louiscryan · Pull Request #141 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86
@LisaFC
continuing PR here as switching to public repo borked previous PR
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/142
Code for auth readme pending maven artifact for google auth library · Issue #142 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The maven artifact for https://github.com/google/google-auth-library-java
hasn't shown up in maven central yet. Pull request with supporting code is pending that
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/143
Update compiler/README.md with nano codegen commandline by zsurocking · Pull Request #143 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.
It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA) at https://cla.developers.google.com/.
If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check the information on your CLA or see this help article on setting the email on your git commits.
Once you've done that, please reply here to let us know.  If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/144
Add MAX_CONCURRENT_STREAMS option to NettyServerBuilder · Issue #144 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/145
Integration tests failing · Issue #145 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Occasionally the integration tests AbstractTransportTest#largeUnary and AbstractTransportTest#serverStreaming are failing on the server side with lots of  Exceptions of the like.
Feb 25, 2015 2:58:40 PM io.grpc.transport.netty.NettyServerHandler onStreamError
WARNING: Stream Error
io.netty.handler.codec.http2.Http2Exception$StreamException: Stream closed before write could take place
    at io.netty.handler.codec.http2.Http2Exception.streamError(Http2Exception.java:90)
    at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$FlowState.clear(DefaultHttp2RemoteFlowController.java:431)
    at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$2.streamInactive(DefaultHttp2RemoteFlowController.java:78)
    at io.netty.handler.codec.http2.DefaultHttp2Connection.deactivateInternal(DefaultHttp2Connection.java:222)

We have traced it down to a bug in the HTTP2 Flow Control in Netty, where frames that are pending due to a not yet received WINDOW_UPDATE frame get canceled. For this bug to trigger the server endpoint has to be in the state HALF_CLOSE_REMOTE with no Flow Control Window left.
I have discussed the problem with @nmittler and @ejona86 and I am currently working on a PR for Netty.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/146
Support Unix Domain Socket · Issue #146 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Should be straightforward enough now that Netty supports it
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/147
Create PATENTS by jayantkolhe · Pull Request #147 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/148
Polish javadoc for transport/ by zhangkun83 · Pull Request #148 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan PTAL.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/149
Updating examples to be consistent with proto3 styleguide. by nmittler · Pull Request #149 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/150
Add CallOptions parameter to newCall() · Issue #150 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We need robust per-call configuration. For example, if we were to add configuration for specifying whether to retry, where would it go? Such configuration would need to be per-call, so it must go in Channel.newCall() somewhere. MethodDescriptor is where timeout is now, but putting more in MethodDescriptor seems like a long-term disaster. Metadata.Headers is where authority and path are now, but putting retry configuration there would be very odd.
A CallOptions class would be a natural place for per-call configuration, and would actually be a good home for timeout, authority, and path. Removal of timeout from MethodDescriptor would make it so that nobody ever needs to modify the object, which would allow us to greatly simplify the generated code. Authority and path don't really relate to Metadata; they relate to HTTP headers but not GRPC Metadata. Removal of them from Headers means we would remove the Headers/Trailers distinction and just have Metadata. That would also fix the issue where Headers doesn't make sense to send from ServerCall since authority and path are meaningless for response headers.
The main breakage would be with Interceptors, as it would be adding a new parameter.
I'm also uncertain as to whether CallOptions should be final or not. I think we want final, since we don't want that part of the API to be transport-specific, but it could be useful to have transport-specific options such as inbound flow control window.
@louiscryan and @zhangkun83, what do you think?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/151
More example changes to match style guide. by nmittler · Pull Request #151 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 I think this is the last of the changes.  After this is in, I'll create a bug for the C guys to update theirs.
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

https://github.com/grpc/grpc-java/issues/154
Tests fail with latest Netty version · Issue #154 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When running gradle clean build on master, I get the following unit test failures.
:grpc-netty:processTestResources UP-TO-DATE
:grpc-netty:testClasses
:grpc-netty:test

io.grpc.transport.netty.NettyServerHandlerTest > sendFrameShouldSucceed FAILED
    java.lang.NullPointerException at NettyServerHandlerTest.java:263

io.grpc.transport.netty.NettyServerHandlerTest > inboundDataWithEndStreamShouldForwardToStreamListener FAILED
    java.lang.NullPointerException at NettyServerHandlerTest.java:263

io.grpc.transport.netty.NettyServerHandlerTest > closeShouldCloseChannel FAILED
    java.lang.NullPointerException at NettyServerHandlerTest.java:246

io.grpc.transport.netty.NettyServerHandlerTest > clientCancelShouldForwardToStreamListener FAILED
    java.lang.NullPointerException at NettyServerHandlerTest.java:263

io.grpc.transport.netty.NettyServerHandlerTest > connectionErrorShouldCloseChannel FAILED
    java.lang.NullPointerException at NettyServerHandlerTest.java:263

io.grpc.transport.netty.NettyServerHandlerTest > streamErrorShouldNotCloseChannel FAILED
    java.lang.NullPointerException at NettyServerHandlerTest.java:263

io.grpc.transport.netty.NettyServerHandlerTest > clientHalfCloseShouldForwardToStreamListener FAILED
    java.lang.NullPointerException at NettyServerHandlerTest.java:263

io.grpc.transport.netty.NettyServerHandlerTest > inboundDataShouldForwardToStreamListener FAILED
    java.lang.NullPointerException at NettyServerHandlerTest.java:263

io.grpc.transport.netty.NettyClientHandlerTest > sendFrameShouldSucceed FAILED
    org.mockito.exceptions.verification.NeverWantedButInvoked at NettyClientHandlerTest.java:213

io.grpc.transport.netty.NettyClientHandlerTest > receivedGoAwayShouldFailQueuedStreams FAILED
    java.lang.NullPointerException at NettyClientHandlerTest.java:273

io.grpc.transport.netty.NettyClientHandlerTest > inboundHeadersShouldForwardToStream FAILED
    java.lang.NullPointerException at NettyClientHandlerTest.java:232

io.grpc.transport.netty.NettyClientHandlerTest > inboundDataShouldForwardToStream FAILED
    java.lang.NullPointerException at NettyClientHandlerTest.java:326

io.grpc.transport.netty.NettyClientHandlerTest > createStreamShouldSucceed FAILED
    org.mockito.exceptions.verification.WantedButNotInvoked at NettyClientHandlerTest.java:137

io.grpc.transport.netty.NettyClientHandlerTest > channelShutdownShouldFailInFlightStreams FAILED
    java.lang.NullPointerException at NettyClientHandlerTest.java:307

io.grpc.transport.netty.NettyClientHandlerTest > receivedGoAwayShouldFailUnknownStreams FAILED
    java.lang.NullPointerException at NettyClientHandlerTest.java:284

Example Stacktrace
channelShutdownShouldFailInFlightStreams

java.lang.NullPointerException
    at io.grpc.transport.netty.NettyClientHandler.onStreamError(NettyClientHandler.java:223)
    at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:284)
    at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.error(DefaultHttp2ConnectionEncoder.java:501)
    at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$FlowState$Frame.writeError(DefaultHttp2RemoteFlowController.java:543)
    at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$FlowState.clear(DefaultHttp2RemoteFlowController.java:453)
    at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$2.streamInactive(DefaultHttp2RemoteFlowController.java:79)
    at io.netty.handler.codec.http2.DefaultHttp2Connection.deactivateInternal(DefaultHttp2Connection.java:222)
    at io.netty.handler.codec.http2.DefaultHttp2Connection.access$700(DefaultHttp2Connection.java:52)
    at io.netty.handler.codec.http2.DefaultHttp2Connection$DefaultStream.close(DefaultHttp2Connection.java:402)
    at io.netty.handler.codec.http2.Http2ConnectionHandler.closeStream(Http2ConnectionHandler.java:260)
    at io.netty.handler.codec.http2.Http2ConnectionHandler.channelInactive(Http2ConnectionHandler.java:193)
    at io.grpc.transport.netty.NettyClientHandler.channelInactive(NettyClientHandler.java:204)
    at io.grpc.transport.netty.NettyClientHandlerTest.channelShutdownShouldFailInFlightStreams(NettyClientHandlerTest.java:307)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/155
Note in README that things don't build on Windows by ejona86 · Pull Request #155 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/156
Support building on Windows by ejona86 · Pull Request #156 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/157
Have SendGrpcFrameCommand constructor take an AbstractStream object instead of a stream id. by buchgr · Pull Request #157 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/158
Auth demo by louiscryan · Pull Request #158 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Branch hosed. Moving to another branch
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/159
Add Sonatype OSSRH upload support, with nice POMs by ejona86 · Pull Request #159 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM .. I haven't worked through how it all works yet, but I'll take your word for it :)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/160
Switch to use new leaner auth library for OAuth interceptor by louiscryan · Pull Request #160 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Looks like this is lean enough to be testable now, right (nudge, nudge)
regardless, change LGTM!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/161
Correct small grammar error in comment. by adewale · Pull Request #161 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/162
Add some details for building on Windows. by ejona86 · Pull Request #162 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/163
GO_AWAY can result in cryptic error messages · Issue #163 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In NettyClientHandler, we don't always store the original cause of the GO_AWAY and instead rely on a connection error.  This results in cryptic errors like this:
Caused by: io.grpc.Status$OperationException: UNAVAILABLE: null
at io.grpc.Status.asException(Status.java:396)
at io.grpc.transport.netty.NettyClientHandler.failPendingStreams(NettyClientHandler.java:398)
at io.grpc.transport.netty.NettyClientHandler.createPendingStreams(NettyClientHandler.java:333)
at io.grpc.transport.netty.NettyClientHandler.createStream(NettyClientHandler.java:240)
at io.grpc.transport.netty.NettyClientHandler.write(NettyClientHandler.java:133)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/164
Switch to Netty 4.1 branch · Issue #164 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Since HTTP/2 support has been back-ported to the 4.1 branch, we should start basing our work on it since it will get us closer to an official release of Netty.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/165
Disable Javadoc doclint on Java 8 by nmittler · Pull Request #165 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/166
Tightening up error message for GO_AWAY. by nmittler · Pull Request #166 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/167
Import latest Netty changes · Issue #167 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
FYI, this seems to break unit tests.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/168
Remove AbstractStub.StubConfigBuilder · Issue #168 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Forked from #150
Now we are doing this to reconfigure a stub:
stub = stub.configureNewStub().setDeadline(...).addInterceptor(...).build();

Why not just:
stub = stub.withDeadline(...).withInterceptor(...);

This could make per-call configuration more concise. Instead of:
response = stub.configureNewStub().setDeadline(...).build().foo(request);

we could have:
response = stub.withDeadline(...).foo(request);
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/169
Installation fails due to Javadoc errors · Issue #169 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Installing the library as described in the main README.md fails in the last step, because javadoc finds two errors and exits with status 1 (which makes ./gradlew install sad).
Error 1:
grpc-java/core/src/main/java/io/grpc/ClientInterceptor.java:51: error: self-closing element not allowed
17:25:41.937 [ERROR] [system.err]    * <p/>
17:25:41.937 [ERROR] [system.err]      ^

Error 2:
grpc-java/core/src/main/java/io/grpc/transport/Stream.java:46: error: reference not found
17:25:42.326 [ERROR] [system.err]    * {@link StreamListener#messageRead(java.io.InputStream, int)}. No additional messages will be
17:25:42.328 [ERROR] [system.err]             ^
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/170
Fixes javadoc errors by jcanizales · Pull Request #170 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@jcanizales do we still need this?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/171
Integrate with more data format · Issue #171 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I don't know whether it is possible to use other data format, not just protobuf, for example avro.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/172
Push Java libraries to Maven central · Issue #172 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
As the majority of Java Developer, I am using Maven and not Gradle...
After compiling my self the protoc tool for Mac, and creating the Route sample Maven project, I am still block with the fact that the
import io.grpc.ServerImpl;
import io.grpc.stub.StreamObserver;
import io.grpc.transport.netty.NettyServerBuilder;
are nowhere in Maven...
My Current pom is like this, and the protoc generates correct code:


  4.0.0
  com.google.apphosting.grpc
  grpctest
  1.0
  jar
  
    
      dtrott
      http://maven.davidtrott.com/repository
    
    
  
    
      com.google.guava
      guava
      18.0
      jar
    
    
      javax.json
      javax.json-api
      1.0
      jar
    
    
      com.google.protobuf
      protobuf-java
      3.0.0-alpha-2
    
  
  
    UTF-8
    1.7
    1.7
  
  
    
      
        org.apache.maven.plugins
        maven-compiler-plugin
        3.2
        
          1.5
          1.5
        
      
      
        com.google.protobuf.tools
        maven-protoc-plugin
        0.1.10
        
          /usr/local/bin/protoc
        
        
          
            
              compile
              testCompile
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/173
Please test with broken stream IDs · Issue #173 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi there,
We recently got hit in C with a crash that happened when HTTP/2 stream IDs went unexpected (violating the invariant of increase on a connection) and also aren't prepared for the situation where we approach or cross max stream id (0x7fffffffu). Please check that this case works in Java. If you need some client code to test that, I can let you use the client code that was sent to me.
This is related to C issues: grpc/grpc#946 and grpc/grpc#957
Thanks!
Vijay
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/174
Access to controller (for connection metadata) · Issue #174 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I would like to get the remote client's IP and TLS client-certificate from within a GRPC service. And I guess cancellation information as well.
Protobuf services had the controller argument.  Is there an equivalent in GRPC?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/175
could grpc-java generate jars by modifying gradle files? how? · Issue #175 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I want to package these java files generated by grpc. How could I modify gradle files?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/176
IllegalReferenceCountException for DATA frame with EOS · Issue #176 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If a DATA frame is received with EOS set, an attempt is made to read the Netty ByteBuf after it has been closed.
The problem is this line: 
  
    
      grpc-java/core/src/main/java/io/grpc/transport/Http2ClientStream.java
    
    
         Line 139
      in
      ef87818
    
  
  
    

        
          
           frame.close(); 
        
    
  


Since the buffer was already added to the deframer and the user callback notified, they will then attempt to read from the buffer which has already been closed.  This causes the IllegalReferenceCountException to mask the actual problem with is that a DATA frame was received with EOS set.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/177
Proper buffer closure when receiving DATA with EOS by nmittler · Pull Request #177 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/178
Test receiving invalid stream IDs in okhttp by nmittler · Pull Request #178 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan can you take a look ... should be trivial.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/179
Updating to the latest Netty version. by nmittler · Pull Request #179 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/180
Swap to Netty's NPN/ALPN handling · Issue #180 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This should simplify our code and would allow us to support tcnative for OpenSSL support. Other than being faster, tcnative does not depend on the JRE version and does not need bootclasspath specified, which would help new users trying to use gRPC for the first time.
This is API breaking as it will change how we use SslContexts provided by the user. We will require them to be properly configured with ALPN protocols. Since SslContext does not allow any form of partial configuration or reconfiguration (no way that two parties can work together to configure one), we will probably need a helper class that duplicates almost all the factory methods but without the parameters we want to specify (like ALPN protocols).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/181
Observe MAX_CONCURRENT_STREAMS in OkHttp client · Issue #181 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We ignore it. We shouldn't.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/182
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/183
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/184
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/185
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/186
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/187
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/188
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/189
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/190
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/191
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/192
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/193
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/194
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/195
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/196
Add name and developers to pom by ejona86 · Pull Request #196 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/197
Add WritableBuffer interface for zero copy data writes. Fixes #8 by buchgr · Pull Request #197 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/198
Support netty4 and5 by louiscryan · Pull Request #198 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ick! .... LGTM :)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/199
Fix compile error introduced by previous commit by buchgr · Pull Request #199 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/200
Handle spaces in shell script by ejona86 · Pull Request #200 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/201
Provide Code Style definition file · Issue #201 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Would it be possible to provide the code style definition file you're using with Intellij?
Along these lines: https://www.jetbrains.com/idea/webhelp10.5/exporting-project-code-style-settings.html
This would make it easier to contribute to grpc!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/202
Add GrpcCallContext & GrpcSession, so transports can expose data (client IP, certificate) by justinsb · Pull Request #202 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
So this is a WIP.  Most problematically, it doesn't seem that the integeration test servers are actually using encryption; it looks like they set everything up but when I test the session info (see tls_info test) it is NONE:SSL_NULL_WITH_NULL_NULL.  I think maybe the handshake just isn't happening.
I did change a fair bit of how TLS is actually set up, so I don't know if this is happening on master.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/203
The `-f` flag for readlink is not available on OSX · Issue #203 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
readlink -f, as used in run-test-client.sh and run-test-server.sh is not available on OSX.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/204
Need docs on how to run integration test suite · Issue #204 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It seems that this is the way:
Tab/window/screen 1:
./run-test-server.sh 

Tab/window/screen 2:
./run-test-client.sh --use_test_ca=true --server_host_override=foo.test.google.fr --test_case=empty_unary
./run-test-client.sh --use_test_ca=true --server_host_override=foo.test.google.fr --test_case=large_unary
./run-test-client.sh --use_test_ca=true --server_host_override=foo.test.google.fr --test_case=client_streaming
...

Is that correct?
And is there a way to avoid paying the Groovy/Gradle tax for every test?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/205
Use CreateStartScripts for integration-tests · Issue #205 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This would make the binaries more portable and wouldn't require running Gradle before every execution.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/206
Is there any way to handle cookie in headers？ · Issue #206 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We usually auth user by cookie/token.Should I use ClientInterceptor to set cookie or store cookie?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/207
Add simple HelloWord example handling custom header by zhaohaifeng · Pull Request #207 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.
It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA) at https://cla.developers.google.com/.
If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check the information on your CLA or see this help article on setting the email on your git commits.
Once you've done that, please reply here to let us know.  If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/208
Add checkstyle checking by ejona86 · Pull Request #208 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM ... thanks for doing this!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/209
HttpUtilTest missing package · Issue #209 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/210
Add package statement to HttpUtilTest by ejona86 · Pull Request #210 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/211
Fix checkstyle warnings for examples · Issue #211 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Making example methods private would be easiest, but them being public seemed to be useful in http://www.useopen.net/blog/2015/rpc-performance.html .
getFeature() is also overloaded, and doesn't look like it should be, given that the two methods have different semantics.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/212
Adding outbound flow control API for Call/ServerCall by nmittler · Pull Request #212 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/213
Adding outbound flow control API for the transport API by nmittler · Pull Request #213 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/214
Add missing copyright headers by ejona86 · Pull Request #214 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
lgtm
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/215
OkHttpClientStream.window is only written never read · Issue #215 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86
Should be removed
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/216
Improve CONTRIBUTING.md by ejona86 · Pull Request #216 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/217
Add missing @RunWith. by madongfly · Pull Request #217 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/218
Travis simple by louiscryan · Pull Request #218 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/219
method not found for method name automatically changed · Issue #219 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I use grpc ruby client and java server, the ruby client prompts that method not found, so I choose to debug the grpc java proto code, I got very confused.
the following code which generated by grpc java defines the SearchForum method:
private static final io.grpc.stub.Method<com.search.protoc.SearchRequest, com.search.protoc.SearchResponse> METHOD_SEARCH_FORUM = io.grpc.stub.Method.create( io.grpc.MethodType.UNARY, "SearchForum", io.grpc.proto.ProtoUtils.marshaller(com.search.protoc.SearchRequest.PARSER), io.grpc.proto.ProtoUtils.marshaller(com.search.protoc.SearchResponse.PARSER));
and the following code register the SearchForum method:
public static io.grpc.ServerServiceDefinition bindService( final SearchService serviceImpl) { return io.grpc.ServerServiceDefinition.builder("SearchService") .addMethod(createMethodDefinition( METHOD_SEARCH_FORUM, asyncUnaryRequestCall( new io.grpc.stub.ServerCalls.UnaryRequestMethod< com.search.protoc.SearchRequest, com.search.protoc.SearchResponse>() { @java.lang.Override public void invoke( com.search.protoc.SearchRequest request, io.grpc.stub.StreamObserver<com.search.protoc.SearchResponse> responseObserver) { serviceImpl.searchForum(request, responseObserver); } }))).build();
bug when I debug into the createMethodDefinition method:
public static <ReqT, RespT> ServerMethodDefinition<ReqT, RespT> createMethodDefinition( Method<ReqT, RespT> method, ServerCallHandler<ReqT, RespT> handler) { return ServerMethodDefinition.create(method.getName(), method.getRequestMarshaller(), method.getResponseMarshaller(), handler); }
it shows that the method.getName returns "searchForum".
that is the reason why ruby client cannot find the method SearchForum. but I totally don't understand why method name SearchForum has been renamed to searchForum, the data flow shows that nothing has done to the METHOD_SEARCH_FORUM method name.
I think this is a bug.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/220
Protobuf java/nano are now on Maven Central by ejona86 · Pull Request #220 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM. Want to update the readme to point to the new make_dependencies script
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/221
Improve Status exception message by ejona86 · Pull Request #221 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/222
Move Status.toString next to other methods by ejona86 · Pull Request #222 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/223
OkHttp tests flaky · Issue #223 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Change to shutdown of okhttp has caused tests to become flaky.
This is the location of the most common failure for me:
java.lang.AssertionError at OkHttpClientTransportTest.java:134
Full examples of such failures:
:grpc-okhttp:test

io.grpc.transport.okhttp.OkHttpClientTransportTest > cancelStream FAILED
    java.lang.AssertionError at OkHttpClientTransportTest.java:134

io.grpc.transport.okhttp.OkHttpClientTransportTest > receiveReset FAILED
    java.lang.AssertionError at OkHttpClientTransportTest.java:134

io.grpc.transport.okhttp.OkHttpClientTransportTest > receivedDataForInvalidStreamShouldResetStream FAILED
    java.lang.AssertionError at OkHttpClientTransportTest.java:134

io.grpc.transport.okhttp.OkHttpClientTransportTest > readStatus FAILED
    java.lang.AssertionError at OkHttpClientTransportTest.java:134

io.grpc.transport.okhttp.OkHttpClientTransportTest > streamIdExhausted FAILED
    org.mockito.exceptions.verification.WantedButNotInvoked at OkHttpClientTransportTest.java:450

io.grpc.transport.okhttp.OkHttpClientTransportTest > receivedHeadersForInvalidStreamShouldResetStream FAILED
    java.lang.AssertionError at OkHttpClientTransportTest.java:134

io.grpc.transport.okhttp.OkHttpClientTransportTest > stopNormally FAILED
    org.mockito.exceptions.verification.WantedButNotInvoked at OkHttpClientTransportTest.java:365
    java.lang.AssertionError at OkHttpClientTransportTest.java:134

io.grpc.transport.okhttp.OkHttpClientTransportTest > receiveGoAway FAILED
    org.mockito.exceptions.verification.WantedButNotInvoked at OkHttpClientTransportTest.java:423
    java.lang.AssertionError at OkHttpClientTransportTest.java:134
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/224
Working Travis build, with caching of deps by ejona86 · Pull Request #224 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/225
Remove blocking on netty client stream creation. by buchgr · Pull Request #225 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/226
Cache Gradle and not really Maven by ejona86 · Pull Request #226 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Ping?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/227
Enable parallel Gradle builds for Travis by ejona86 · Pull Request #227 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/228
okhttp: code style fixes by ejona86 · Pull Request #228 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly, this fixes checkstyle warnings displayed during the build.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/229
Fix a race condition in the test, we may notify MockFrameReader to return before it starts waiting. by madongfly · Pull Request #229 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Without this change, the test failed 2~3 times out of 10 runs, with this change, it passed 30 runs.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/230
Make checkstyle failures fatal, and fix last issues by ejona86 · Pull Request #230 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
How do we feel about checkstyles being fatal? I think some may find it annoying, but I also wonder how well people will notice warnings.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/231
Data corruption when receiving payloads larger than 2048 bytes · Issue #231 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Here, OkHttpReadableBuffer is calling Buffer#read only once, even though the contract for Buffer#read is that it reads up to byteCount bytes and returns the number of bytes actually read.
Because Buffer uses a linked list of segments where each segment is at most 2048 bytes, Buffer#read will read only up to 2048 bytes at a time. This will result in corruption of any received payload larger than 2048 bytes (and on some smaller payloads as well, depending on the position in the buffer). In my case, it manifested as a series of '\0' bytes where data should have been.
Instead, we should call read in a loop until we have read all the bytes we need to. And we should also have some unit tests for OkHttpReadableBuffer...
I'm working on a pull request.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/232
Fix data corruption issue receiving payloads > 2kB by ttencate · Pull Request #232 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM. Thank you very much. The Arrays.equals() wasn't very useful, was it...
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/233
Use TLS for Netty integration tests by ejona86 · Pull Request #233 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/234
Remove readlink -f in run-test*.sh scripts by ejona86 · Pull Request #234 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/235
Gradle's testing should show more info on Travis · Issue #235 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
A flaky build on Travis doesn't provide enough information to diagnose what went wrong, because Gradle generally expects you to view the reports in the build directiory.
https://www.gradle.org/docs/current/dsl/org.gradle.api.tasks.testing.logging.TestLoggingContainer.html
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/236
Use tls for netty tests by ejona86 · Pull Request #236 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/237
Making connection and stream windows configurable for Netty. by nmittler · Pull Request #237 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
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

https://github.com/grpc/grpc-java/issues/239
Lacking preconditions for start() in ChannelImpl.CallImpl · Issue #239 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For instance, calling request() before start() has been called results in a NullPointerException.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/240
ClientAuthInterceptor.start() skips super.start() when there is an error, causing subsequent use of the top-level Call to throw IllegalStateException · Issue #240 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
onClose does not log any exception or status, as it is commonly used in cases where there wasn't a server error but instead a client issue. Thus, in the IOException handling of ClientAuthInterceptior, if an exception is thrown it is thrown away, the caller doesn't notice, and will get some odd exception on whatever the next call is (NullPointerException in request() was what led me to this discovery). We discussed that the "proper" exception handling isn't very obvious, but certainly swallowing the exception is worse than the alternatives.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/241
Disable Travis parallel building to reduce memory usage by ejona86 · Pull Request #241 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/242
Default client connection window to 1MiB. by nmittler · Pull Request #242 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The documentation in the builder says that it defaults to Http2CodecUtil#DEFAULT_WINDOW_SIZE. That should be updated.
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/243
Make connection/stream windows configurable for Netty server  · Issue #243 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This has already been done for the client. Default connection window should be 1MiB.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/244
netty: Status should be based on GOAWAY code by ejona86 · Pull Request #244 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 I think we should also change createPendingStreams so that it calls goAwayStatus() inside the loop, only when it's setting the status on the stream.  The go away check should be moved above the stream ID check. And then in the stream ID check, we should augment the description to indicate that it's exhausted the stream IDs.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/245
AbstractTransportTest.streamingOutputShouldBeFlowControlled doesn't test flow control · Issue #245 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It is actually very difficult to test inbound flow control using our API without long sleeps. streamingOutputShouldBeFlowControlled does long sleeps, but doesn't actually assert the number of requests that should have been requested. That makes it the slowest test (4s, x3 transports) without actually verifying anything additional to the other tests.
We should either fix the test or remove it.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/246
ClientAuthInterceptor synchronizes on wrong object · Issue #246 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The "this" in synchronized (this), is not the correct object to synchronize on:
https://github.com/grpc/grpc-java/blob/master/auth/src/main/java/io/grpc/auth/ClientAuthInterceptor.java#L77
It should be ClientAuthInterceptor.this instead. As the code stands, there is no synchronization between threads so you can see NullPointerExceptions as lastMetadata is set but not cached.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/247
Fix synchronization in client auth by ejona86 · Pull Request #247 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/248
Test whether inbound flow control functions by ejona86 · Pull Request #248 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/249
Add precondition to throw more informative exception when calling request() before start() has been called. by zhangkun83 · Pull Request #249 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83, LGTM.
Oh, I had thought the other methods might have been missing Preconditions, but would you look at that, they are there (I think maybe because @louiscryan made me during review :-) ).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/250
Wait for handler registration by ejona86 · Pull Request #250 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/251
Fix an issue caused by the intercepting call failing in start() and skip super.start() by zhangkun83 · Pull Request #251 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I thought we were going to execute getRequestMetadata() immediately when interceptCall and then return either the ForwardingCall on success or a NoopCall on failure. I'm not convinced we should add more API to ForwardingCall (other than having a delegate() method instead of delegate field).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/252
TLS support for okhttp transport. by madongfly · Pull Request #252 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 Please take a look, thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/253
Add clearer message when receiving GOAWAY from the server. · Issue #253 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/254
Document transport layers (netty vs okhttp) · Issue #254 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi, am I right that there are currently two implementations of the transport layer? Netty and okhttp? I was curious if there are any situations in which one might be preferable to the other as I'm not quite sure why there are two implementations.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/255
Implement GrpcCallContext & GrpcSession by justinsb · Pull Request #255 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is a more minimal version of #202, which just takes the step of implementing GrpcCallContext/GrpcSession, with just enough functionality to test it (the remote address, which I hope is less controversial than SSL).
I don't think putting the session into the Metadata.Headers is ideal, but alternatives seem more invasive.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/256
Disable Nagle's algorithm. by madongfly · Pull Request #256 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 Please take a look.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/257
OkHttp may be missing flush after sending headers · Issue #257 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It looks like we aren't flushing after headers. This works okay because we don't have any tests that don't send data. We should add such a test to AbstractTransportTests and add the flush as appropriate.

  
    
      grpc-java/okhttp/src/main/java/io/grpc/transport/okhttp/OkHttpClientTransport.java
    
    
         Line 192
      in
      7865b03
    
  
  
    

        
          
           frameWriter.synStream(false, false, clientStream.id(), 0, requestHeaders); 
        
    
  


On Friday I was playing with a change that allows removing the flush() on headers for unary and server streaming RPCs. We may be more interested in it now.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/258
Upgrading to the latest Netty 4.1 branch. by nmittler · Pull Request #258 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/259
Use codegen for integration testing by ejona86 · Pull Request #259 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/260
"An endpoint that receives a SETTINGS frame with any unknown or unsupported identifier MUST ignore that setting." · Issue #260 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I happened to send an invalid setting id (0x0) to a java server and saw the connection shutdown. The expected behavior as in http2 spec is
An endpoint that receives a SETTINGS frame with any unknown or unsupported identifier MUST ignore that setting.
instead of connection error.
Here is the stack trace:
Mar 31, 2015 5:58:51 PM io.grpc.transport.netty.NettyServerHandler onConnectionError
WARNING: Connection Error
io.netty.handler.codec.http2.Http2Exception: key
at io.netty.handler.codec.http2.Http2Exception.connectionError(Http2Exception.java:72)
at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readSettingsFrame(DefaultHttp2FrameReader.java:496)
at io.netty.handler.codec.http2.DefaultHttp2FrameReader.processPayloadState(DefaultHttp2FrameReader.java:235)
at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readFrame(DefaultHttp2FrameReader.java:130)
at io.netty.handler.codec.http2.Http2InboundFrameLogger.readFrame(Http2InboundFrameLogger.java:39)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder.decodeFrame(DefaultHttp2ConnectionDecoder.java:99)
at io.netty.handler.codec.http2.Http2ConnectionHandler$FrameDecoder.decode(Http2ConnectionHandler.java:276)
at io.netty.handler.codec.http2.Http2ConnectionHandler$PrefaceDecoder.decode(Http2ConnectionHandler.java:183)
at io.netty.handler.codec.http2.Http2ConnectionHandler.decode(Http2ConnectionHandler.java:317)
at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:316)
at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:84)
at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
at io.netty.channel.PausableChannelEventExecutor.invokeChannelRead(PausableChannelEventExecutor.java:86)
at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:389)
at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:956)
at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:127)
at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:514)
at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:471)
at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:385)
at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:351)
at io.netty.util.concurrent.SingleThreadEventExecutor$2.run(SingleThreadEventExecutor.java:116)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1113)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:588)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/261
Change the package option of example protos to be the same as grpc-common's by madongfly · Pull Request #261 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/262
Context API · Issue #262 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Ideally it would not be grpc-specific. It would help with things like #174, but could also maybe provide cancellation support to the async stub and deadline propagation.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/263
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/264
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/265
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/266
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/267
Fix JavaDoc references to non-imported class by ejona86 · Pull Request #267 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/268
Improve JavaDoc for Status by ejona86 · Pull Request #268 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/269
Respect MAX_CONCURRENT_STREAMS in OkHttp client. by madongfly · Pull Request #269 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/270
checkstyle change: by madongfly · Pull Request #270 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/271
Hold lock while reading isThreadScheduled by ejona86 · Pull Request #271 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/272
Fix memory leak by adding the Http2StreamRemovalPolicy to the channel pipeline. by buchgr · Pull Request #272 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/273
how to generate Grpc class with gradle? · Issue #273 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
grpc example use gradle-plugin-protobuf to generate Grpc class with the following config:

protobufCodeGenPlugins = ["java_plugin:$javaPluginPath"]
generateProto.dependsOn ':grpc-compiler:java_pluginExecutable'

but this doesn't succeed when I build with gradle, it prompts:

Could not determine the dependencies of task ':generateProto'.

how to reference grpc complier if I create a stand alone java project with gradle?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/274
OkHttp: Flushes headers out immediately for client streaming and bidi streaming  by madongfly · Pull Request #274 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am curious why this is the way to do. This actually doubles the number of
syscall on client writing path because otherwise header and data can be
fused into a single write syscall (unless the header has some
user-specified metadata). This has some performance impact given the proper
designed benchmarks.
On Tue, Apr 7, 2015 at 12:03 AM, Xudong Ma notifications@github.com wrote:

Flushes headers out immediately for OkHttp transport, so that the server
can be aware of the stream before receiving real data (or half close).
Adds corresponding test to AbstractTransportTest.
You can view, comment on, or merge this pull request online at:
#274
Commit Summary

Fix for #257.

File Changes

M
integration-testing/src/main/java/io/grpc/testing/integration/AbstractTransportTest.java
https://github.com/grpc/grpc-java/pull/274/files#diff-0 (46)
M
integration-testing/src/main/java/io/grpc/testing/integration/TestServiceImpl.java
https://github.com/grpc/grpc-java/pull/274/files#diff-1 (33)
M
integration-testing/src/main/proto/io/grpc/testing/integration/test.proto
https://github.com/grpc/grpc-java/pull/274/files#diff-2 (5)
M
okhttp/src/main/java/io/grpc/transport/okhttp/OkHttpClientTransport.java
https://github.com/grpc/grpc-java/pull/274/files#diff-3 (2)

Patch Links:

https://github.com/grpc/grpc-java/pull/274.patch
https://github.com/grpc/grpc-java/pull/274.diff

—
Reply to this email directly or view it on GitHub
#274.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/275
okhttp: Reset stream when receiving window is negative  Resolves #215 by madongfly · Pull Request #275 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/276
Rename java_plugin to protoc-gen-grpc-java · Issue #276 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This follows a naming convention that allows just placing it in PATH and having protoc discover it.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/277
Fixes Travis breakage caused by wrong order of imports by madongfly · Pull Request #277 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly, LGTM.
@buchgr, using times() from internal doesn't look right. I think you just wanted Mockito.times
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/278
Temporally support Http protocol name "h2-16" for OkHttp client. by madongfly · Pull Request #278 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/279
Clean up stream after AbstractClientStream.inboundTransportError() · Issue #279 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Otherwise the stream object will still be held in the stream map of OkHttpClientTransport.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/280
okhttp:Clean up stream after AbstractClientStream.inboundTransportError by madongfly · Pull Request #280 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This looks like a larger change than is necessary. Let's discuss approaches on #279.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/281
Calls.asyncServerStreamingCall requests only one response · Issue #281 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The method Calls.asyncServerStreamingCall requests only 1 response from the underlying call. The documentation for request(N) states that a call will not deliver more than N responses, so if Call implementations would implement this contract, the resulting server stream would never contain more than one element.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/282
Replace 'internal' import with correct one. by buchgr · Pull Request #282 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/283
netty: Use the bootstrap ClassLoader for ALPN/NPN by ejona86 · Pull Request #283 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM ... great work!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/284
Fix the issue where the intercepting call fails in start(), does not call super.start(), and makes the subsequent use of other methods on the call throw IllegalStateException. by zhangkun83 · Pull Request #284 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/285
Fix bug where the stream id would not get incremented for buffered streams. by buchgr · Pull Request #285 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@buchgr, LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/286
Rename the codegen binary from java_plugin to protoc-gen-grpc-java by zhangkun83 · Pull Request #286 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83, LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/287
Remove unused local variable by ejona86 · Pull Request #287 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/288
Fix warnings (JavaDoc and [deprecated]) by ejona86 · Pull Request #288 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/289
AbstractTransportTest is flaky. · Issue #289 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I've seen several failures of Http2OkHttpTest.pingPong() on Travis, like this one: https://s3.amazonaws.com/archive.travis-ci.org/jobs/57879240/log.txt.
But I couldn't reproduce the same failure in ~30 runs in my local repository.
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

https://github.com/grpc/grpc-java/issues/291
Split protobuf into its own project by ejona86 · Pull Request #291 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/292
Use more precise names for protobuf and nano by ejona86 · Pull Request #292 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/293
OkHttp only connects to "h2" ALPN protocol · Issue #293 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Values "h2-14", "h2-15", and "h2-16" result in Protocol throwing an error from OkHttpTlsUpgrader.
We should support all those options, as we still are seeing them being used since the final HTTP/2 spec hasn't been published.
java.lang.RuntimeException: java.io.IOException: Unexpected protocol: h2-14
            at io.grpc.transport.okhttp.OkHttpClientTransport.start(OkHttpClientTransport.java:300)
            at io.grpc.ChannelImpl.obtainActiveTransport(ChannelImpl.java:188)
            at io.grpc.ChannelImpl.access$600(ChannelImpl.java:55)
            at io.grpc.ChannelImpl$CallImpl.start(ChannelImpl.java:248)
            at io.grpc.ForwardingCall.start(ForwardingCall.java:45)
...
     Caused by: java.io.IOException: Unexpected protocol: h2-14
            at com.squareup.okhttp.Protocol.get(Protocol.java:94)
            at com.squareup.okhttp.OkHttpTlsUpgrader.upgrade(OkHttpTlsUpgrader.java:80)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/294
OkHttp: Temporally support multiple h2-xx protocol on client side. by madongfly · Pull Request #294 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/295
Split protobuf into its own project by madongfly · Pull Request #295 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#291 is a pull request.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/296
Gradle build points to https with self signed certificate · Issue #296 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In installation step for grpc-java
./gradlew install
exec /usr/lib/jvm/jdk1.7.0_51/bin/java -Dorg.gradle.appname=gradlew -classpath /grpc-java/gradle/wrapper/gradle-wrapper.jar org.gradle.wrapper.GradleWrapperMain install
Downloading https://services.gradle.org/distributions/gradle-2.2.1-all.zip
Exception in thread "main" javax.net.ssl.SSLHandshakeException: java.security.cert.CertificateException: No subject alternative DNS name matching services.gradle.org found.
Work around is to modify gradle/wrapper/gradle-wrapper.properties to change to http.
Should change it permanently?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/297
Add missing projects to grpc-all by ejona86 · Pull Request #297 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/298
netty: Add option to set MAX_CONCURRENT_STREAMS by ejona86 · Pull Request #298 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/299
platform issue · Issue #299 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I run a grpc java server on Mac OS, it is ok to test it with java client, but error happened on a linux server,and the error is as follows:

com.google.common.util.concurrent.UncheckedExecutionException: io.grpc.Status$OperationRuntimeException: INTERNAL
at io.grpc.stub.Calls.getUnchecked(Calls.java:117)
at io.grpc.stub.Calls.blockingUnaryCall(Calls.java:129)
at com.engzo.search.protoc.SearchGrpc$SearchBlockingStub.searchForum(SearchGrpc.java:245)
at com.engzo.search.api.SearchClient.searchForum(SearchClient.java:35)
at com.engzo.search.api.SearchClient.main(SearchClient.java:76)
Caused by: io.grpc.Status$OperationRuntimeException: INTERNAL
at io.grpc.Status.asRuntimeException(Status.java:428)
at io.grpc.stub.Calls$UnaryStreamToFuture.onClose(Calls.java:324)
at io.grpc.ChannelImpl$CallImpl$ClientStreamListenerImpl$3.run(ChannelImpl.java:373)
at io.grpc.SerializingExecutor$TaskRunner.run(SerializingExecutor.java:152)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
at java.lang.Thread.run(Thread.java:745)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/300
Reset stream if receive server's halfClose before client sends halfClose. · Issue #300 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This was exposed by the discussion on #279.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/301
okhttp: Clean up stream when error happens. by madongfly · Pull Request #301 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 please take a look, thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/302
De-flake transport test. by madongfly · Pull Request #302 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I feel like we shouldn't be seeing any flakes with 1s, as things should take single-digit milliseconds at most (even with a GC). But I also don't have any other clues as to why we would be getting the timeout for both Netty and OkHttp.
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/303
Remove Guava's Service from server transport by ejona86 · Pull Request #303 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/304
Solution for GRPC codegen deployment by zhangkun83 · Pull Request #304 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/305
Reduce number of flushes · Issue #305 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Each flush causes its own TCP frame to be written because we Nagle is disabled. Reducing the number of flushes would greatly reduce the number of TCP frames and number of syscalls. Even if performance benchmarks don't show a benefit by reduced flushing, if we are able to see improvements to goodput that would be enough for such an optimization.
Reduce number of flushes, in gRPC and maybe Netty.
May need a batch write API. We have the ability internally already, it is deciding a way to expose it.
Allow hint to delay headers until first data write (could maybe be part of batch API).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/306
Upgrading to the latest Netty version. by nmittler · Pull Request #306 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/307
Revisit Lifecycle API · Issue #307 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The current shutdown/shutdownNow/isShutdown/awaitShutdown/isTerminated/awaitTerminated API of ChannelImpl and ServerImpl was chosen when we had time constraints in removing Service from our API. During its addition in #33, @adriancole and @nmittler expressed concern for the API, but the API was left in-place and the decision delayed as part of #28. The Health-checking API is coming, but the current Lifecycle API continues to be contentious in the mean time as it is part of both channel layer and transport layer.
We need to agree on an API.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/308
Fix netty closure check by ejona86 · Pull Request #308 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
oof ... LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/309
Build seems broken on OS/X · Issue #309 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Commit da3c3f8 (Solution for GRPC codegen deployment) seems to have broken the compiler build for me on OS/X. The previous commit builds fine.
$ java -version
java version "1.8.0_40"
Java(TM) SE Runtime Environment (build 1.8.0_40-b25)
Java HotSpot(TM) 64-Bit Server VM (build 25.40-b25, mixed mode)
$ uname -a
Darwin eno.local 14.3.0 Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64 x86_64
$ ../gradlew local_archJava_pluginExecutable
:grpc-compiler:compileLocal_archJava_pluginExecutableJava_pluginCpp UP-TO-DATE
:grpc-compiler:linkLocal_archJava_pluginExecutable
Undefined symbols for architecture x86_64:
  "google::protobuf::io::Printer::Print(char const*)", referenced from:
      java_grpc_generator::PrintImports(google::protobuf::io::Printer*, bool) in java_generator.o
      java_grpc_generator::PrintService(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*, bool) in java_generator.o
      java_grpc_generator::PrintMethodFields(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*, bool) in java_generator.o
      java_grpc_generator::PrintServiceDescriptor(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*) in java_generator.o
      java_grpc_generator::PrintStub(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*, java_grpc_generator::StubType) in java_generator.o
      java_grpc_generator::PrintBindServiceMethod(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*) in java_generator.o
  "google::protobuf::io::Printer::Print(char const*, char const*, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&)", referenced from:
      java_grpc_generator::GenerateService(google::protobuf::ServiceDescriptor const*, google::protobuf::io::ZeroCopyOutputStream*, bool) in java_generator.o
  "google::protobuf::io::Printer::Print(std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator                                            <char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > > const&, char const*)", referenced from:
      java_grpc_generator::PrintService(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*, bool) in java_generator.o
      java_grpc_generator::PrintMethodFields(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*, bool) in java_generator.o
      java_grpc_generator::PrintServiceDescriptor(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::a                                                                    llocator<char> > > > >*, google::protobuf::io::Printer*) in java_generator.o
      java_grpc_generator::PrintStub(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*, java_grpc_generator::StubType) in java_generator.o
      java_grpc_generator::PrintBindServiceMethod(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*) in java_generator.o
  "google::protobuf::io::Printer::Indent()", referenced from:
      java_grpc_generator::PrintService(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1:                                                                                :allocator<char> > > > >*, google::protobuf::io::Printer*, bool) in java_generator.o
      java_grpc_generator::PrintServiceDescriptor(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*) in java_generator.o
      java_grpc_generator::PrintStub(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*, java_grpc_generator::StubType) in java_generator.o
      java_grpc_generator::PrintBindServiceMethod(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf:                          :io::Printer*) in java_generator.o
  "google::protobuf::io::Printer::Outdent()", referenced from:
      java_grpc_generator::PrintService(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*, bool) in java_generator.o
      java_grpc_generator::PrintServiceDescriptor(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*) in java_generator.o
      java_grpc_generator::PrintStub(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*, java_gr                 pc_generator::StubType) in java_generator.o
      java_grpc_generator::PrintBindServiceMethod(google::protobuf::ServiceDescriptor const*, std::__1::map<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::less<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > > > >*, google::protobuf::io::Printer*) in java_generator.o
  "google::protobuf::io::Printer::Printer(google::protobuf::io::ZeroCopyOutputStream*, char)", referenced from:
      java_grpc_generator::GenerateService(google::protobuf::ServiceDescriptor const*, google::protobuf::io::ZeroCopyOutputStream*, bool) in java_generator.o
  "google::protobuf::io::Printer::~Printer()", referenced from:
      java_grpc_generator::GenerateService(google::protobuf::ServiceDescriptor const*, google::protobuf::io::ZeroCopyOutputStream*, bool) in java_generator.o
  "google::protobuf::compiler::PluginMain(int, char**, google::protobuf::compiler::CodeGenerator const*)", referenced from:
      _main in java_plugin.o
  "google::protobuf::compiler::CodeGenerator::~CodeGenerator()", referenced from:
      JavaGrpcGenerator::~JavaGrpcGenerator() in java_plugin.o
  "google::protobuf::compiler::ParseGeneratorParameter(std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, std::__1::vector<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > >, std::__1::allocator<std::__1::pair<std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocat                                                                                                 or<char> > > > >*)", referenced from:
      JavaGrpcGenerator::Generate(google::protobuf::FileDescriptor const*, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> > const&, google::protobuf::compiler::GeneratorContext*, std::__1::basic_string<char, std::__1::char_traits<char>, std::__1::allocator<char> >*) const in java_plugin.o
  "google::protobuf::compiler::java::ClassName(google::protobuf::Descriptor const*)", referenced from:
      java_grpc_generator::MessageFullJavaName(google::protobuf::Descriptor const*) in java_generator.o
  "google::protobuf::compiler::java::ClassName(google::protobuf::FileDescriptor const*)", referenced from:
      java_grpc_generator::ServiceJavaPackage(google::protobuf::FileDescriptor const*) in java_generator.o
  "typeinfo for google::protobuf::compiler::CodeGenerator", referenced from:
      typeinfo for JavaGrpcGenerator in java_plugin.o
  "vtable for google::protobuf::compiler::CodeGenerator", referenced from:
      google::protobuf::compiler::CodeGenerator::CodeGenerator() in java_plugin.o
  NOTE: a missing vtable usually means the first non-inline virtual member function has no definition.
ld: symbol(s) not found for architecture x86_64
clang: error: linker command failed with exit code 1 (use -v to see invocation)
:grpc-compiler:linkLocal_archJava_pluginExecutable FAILED
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/310
Remove call sites of Os.isFamily(). Use osdetector instead by zhangkun83 · Pull Request #310 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83, LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/311
Fix Mac build failure by zhangkun83 · Pull Request #311 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/312
MessageFramer produces too small message chunks · Issue #312 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
MessageFramer uses
bufferAllocator.allocate(maxFrameSize)
to produce chunks that the transport can write. Currently these chunks are always 4096 bytes regardless of transport or payload size.
Transports cannot coalesce these chunks and typically end up writing each one in a syscall. For large payloads this really hurts performance. Instead we should delegate to the buffer allocator and ask it to produce a chunk up to the payload size. E.g.
bufferAllocator.allocate(len)
Experimentation with HBase has shown that for a 51k payload this reduces syscalls on write by 3x.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/313
Allow the message frame to create chunks as large as transport will allow by louiscryan · Pull Request #313 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
FYI  - This PR is work in progress, initially just demonstrates idea.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/314
On Server side, use Status "UNKNOWN" instead of "INTERNAL" for errors ca... by madongfly · Pull Request #314 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Those messages give way too much information. Simply UNKNOWN is probably more appropriate.
But really, we should change Status.fromThrowable to use UNKNOWN instead of INTERNAL as users will be using that.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/315
Fix protobuf-nano build broken by 3666de4427460a307bfb86a7f93b3a04cb28f8... by nobutaka · Pull Request #315 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks! I don't know why we weren't seeing build failures, but yeah, it was messed up.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/316
Upgrade to com.google.protobuf:protobuf-gradle-plugin:0.1.0 by zhangkun83 · Pull Request #316 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83, LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/317
Integration test largeUnary failing · Issue #317 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We recently ran into an issue with one of our services where sending large responses results in transport errors being logged as well as eventual transport failure. I managed to reproduce this behavior in integration test largeUnary as well. When running a single iteration of largeUnary the test passes although connection errors are logged:
Apr 20, 2015 10:43:45 AM io.grpc.transport.netty.NettyServerHandler onConnectionError
WARNING: Connection Error
io.netty.handler.codec.http2.Http2Exception: Stream does not exist 3
    at io.netty.handler.codec.http2.Http2Exception.connectionError(Http2Exception.java:58)
    at io.netty.handler.codec.http2.DefaultHttp2Connection.requireStream(DefaultHttp2Connection.java:110)
    at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder$FrameReadListener.onWindowUpdateRead(DefaultHttp2ConnectionDecoder.java:486)
    at io.netty.handler.codec.http2.Http2InboundFrameLogger$1.onWindowUpdateRead(Http2InboundFrameLogger.java:124)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readWindowUpdateFrame(DefaultHttp2FrameReader.java:560)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader.processPayloadState(DefaultHttp2FrameReader.java:247)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readFrame(DefaultHttp2FrameReader.java:130)
    at io.netty.handler.codec.http2.Http2InboundFrameLogger.readFrame(Http2InboundFrameLogger.java:39)
    at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder.decodeFrame(DefaultHttp2ConnectionDecoder.java:99)
    at io.netty.handler.codec.http2.Http2ConnectionHandler$FrameDecoder.decode(Http2ConnectionHandler.java:291)
    at io.netty.handler.codec.http2.Http2ConnectionHandler.decode(Http2ConnectionHandler.java:332)
    at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
    at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
    at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
    at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:946)
    at io.netty.channel.local.LocalChannel.finishPeerRead(LocalChannel.java:329)
    at io.netty.channel.local.LocalChannel.access$400(LocalChannel.java:45)
    at io.netty.channel.local.LocalChannel$5.run(LocalChannel.java:315)
    at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:322)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:356)
    at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
    at java.lang.Thread.run(Thread.java:745)

However, running largeUnary in a simple loop causes transport failure after a few iterations. This happens with both netty and okhttp client variants, as well as with netty local channel.
Other details:
$ uname -a
Darwin eno.local 14.3.0 Darwin Kernel Version 14.3.0: Mon Mar 23 11:59:05 PDT 2015; root:xnu-2782.20.48~5/RELEASE_X86_64 x86_64
$ java -version
java version "1.8.0_40"
Java(TM) SE Runtime Environment (build 1.8.0_40-b25)
Java HotSpot(TM) 64-Bit Server VM (build 25.40-b25, mixed mode)


David
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/318
Remove String allocation in MutableHandlerRegistryImpl.lookupMethod(String). · Issue #318 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In QPS benchmarks we spend roughly 1% of the total allocations on allocating String objects when doing a substring on the method name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/319
CodedInputStream and CodedOutputStream always allocate a fixed 4KB byte array. · Issue #319 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Protobuf's CodedInputStream and CodedOutputStream always allocate 4KB sized byte arrays in their constructor. For small messages this is overkill and we should investigate if we can reduce this. On QPS benchmarks our heap consists for roughly 30% of those byte arrays. So this can have a big impact for memory usage.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/320
CompositeReadableBuffer and SerializingExecutor allocate a 16 entry ArrayDeque. · Issue #320 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The CompositeReadableBuffer and the SerializingExecutor always allocate a 16 entry ArrayDeque. We should investigate if we can get away with a smaller default size in order to save memory. In benchmarks just over 2% of total allocations are the Object[] that back the ArrayDeque.
A 16 element Object[] uses roughly 80 byte of memory (12 byte obj header + 4 byte length + 4 byte per entry with compressed oops). Initializing it to a more reasonable default value like 4, could save ~50%, but we should figure out how many entries we are likely to actually need.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/321
Set initial size for ArrayList in TransportFrameUtil.toHttp2Headers · Issue #321 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In QPS benchmarks roughly 0.5% of the total heap is spend on growing the ArrayList in TransportFrameUtil.toHttp2Headers(). It seems like we roughly know the size in advance and so we should initialize it to this.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/322
Improve synchronization of SerializingExecutor. · Issue #322 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We are seeing some contention in ChannelImpl.obtainActiveTransport() and SerializingExecutor.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/323
Propagate explicit flushes through MessageFramer by ejona86 · Pull Request #323 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/324
okhttp: Don't allow server half-closes before client's half-close. by madongfly · Pull Request #324 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 Please take a look, thanks!
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

https://github.com/grpc/grpc-java/issues/326
Upgrading to latest Netty version. by nmittler · Pull Request #326 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/327
Log stack traces of test failures to the console. by zhangkun83 · Pull Request #327 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Lgtm
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/328
Create DEPLOYING.md to document deployment instructions. by zhangkun83 · Pull Request #328 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Should this go in a different file since most people shouldn't need to look at it and it could scare new users?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/329
Support setting the HTTP/2 flow control window in grpc. · Issue #329 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It would be nice if we could set the HTTP/2 flow control window from grpc in order to be able to do meaningful throughput tests in different environments e.g. two of my cloud VMs have a bandwidth delay product of 485KByte/s (high latency and high bandwidth). So with the default flow control window of 64KB we can theoretically only ever reach 13% of the possible throughput on that network.
Would be nice to also add this as a command line flag to the QPS benchmarks.
@ejona86 @louiscryan @nmittler
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/330
OkHttpClientTransport.onGoAway() races with startPendingStreams() · Issue #330 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
onGoAway has two phases: do things necessary under lock and final cleanup. In the first phase it collects the streams to terminate in the second and sets goAway.
startPendingStreams() does not observe goAway and also creates new streams that should be failed due to the goAway. From an initial look, it seems it would be best to remove failPendingStreams() and simply integrate its two phases into onGoAway()'s two phases; that is, when holding the lock in onGoAway, replace pendingStreams with an empty list, and then when not holding the lock call transportReportStatus
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/331
Throughput: AbstractServerStream does unnecessary flushes · Issue #331 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 @nmittler

AbstractServerStream.writeMessage if no headers have been sent will immediately flush an empty header to the transport, by triggering internalSendFrame(flush = true)
In the case of a unary response we don't delay the flush of the framed message to allow the trailers to be flushed at the same time.

Will work on a PR
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/332
Throughput: NettyClientTransport does unnecessary flush · Issue #332 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In the case of Unary & Server-streaming calls the immediate flush of request headers is unnecessary as a single payload must immediately follow for a valid call
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/333
Changing the protobuf branch name in the README.md. by sduskis · Pull Request #333 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.  It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA).
📝 Please visit https://cla.developers.google.com/ to sign.
Once you've signed, please reply here (e.g. I signed it!) and we'll verify.  Thanks.


If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check your existing CLA data and verify that your email is set on your git commits.
If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/334
Update QPS Client and Server. by buchgr · Pull Request #334 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/335
Add support for setting the connection and stream flow control window to NettyServerBuilder. by buchgr · Pull Request #335 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan @nmittler @ejona86 Please take a look.
I basically just copied the code from Nathan's commit for the client handler.
@louiscryan I will add a flag to QPS once this stuff is merged.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/336
Memoryleak in Netty Server · Issue #336 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When pushing the server hard I am getting
SEVERE: LEAK: ByteBuf.release() was not called before it's garbage-collected. See http://netty.io/wiki/reference-counted-objects.html for more information.
Recent access records: 0
Created at:
    io.netty.buffer.PooledByteBufAllocator.newDirectBuffer(PooledByteBufAllocator.java:250)
    io.netty.buffer.AbstractByteBufAllocator.directBuffer(AbstractByteBufAllocator.java:155)
    io.netty.buffer.AbstractByteBufAllocator.buffer(AbstractByteBufAllocator.java:91)
    io.grpc.transport.netty.NettyWritableBufferAllocator.allocate(NettyWritableBufferAllocator.java:65)
    io.grpc.transport.netty.NettyWritableBufferAllocator.allocate(NettyWritableBufferAllocator.java:48)
    io.grpc.transport.MessageFramer.commitToSink(MessageFramer.java:240)
    io.grpc.transport.MessageFramer.close(MessageFramer.java:221)
    io.grpc.transport.AbstractStream.closeFramer(AbstractStream.java:136)
    io.grpc.transport.AbstractServerStream.close(AbstractServerStream.java:107)
    io.grpc.ServerImpl$ServerCallImpl.close(ServerImpl.java:434)
    io.grpc.stub.ServerCalls$ResponseObserver.onCompleted(ServerCalls.java:195)
    io.grpc.benchmarks.qps.QpsAsyncServer$TestServiceImpl.unaryCall(QpsAsyncServer.java:177)
    grpc.testing.TestServiceGrpc$2.invoke(TestServiceGrpc.java:193)
    grpc.testing.TestServiceGrpc$2.invoke(TestServiceGrpc.java:188)
    io.grpc.stub.ServerCalls$1$1.onHalfClose(ServerCalls.java:93)
    io.grpc.ServerImpl$ServerCallImpl$ServerStreamListenerImpl.halfClosed(ServerImpl.java:480)
    io.grpc.ServerImpl$JumpToApplicationThreadServerStreamListener$2.run(ServerImpl.java:370)
    io.grpc.SerializingExecutor$TaskRunner.run(SerializingExecutor.java:152)
    com.google.common.util.concurrent.MoreExecutors$DirectExecutorService.execute(MoreExecutors.java:299)
    io.grpc.SerializingExecutor.execute(SerializingExecutor.java:110)
    io.grpc.ServerImpl$JumpToApplicationThreadServerStreamListener.halfClosed(ServerImpl.java:366)
    io.grpc.transport.AbstractServerStream.halfCloseListener(AbstractServerStream.java:243)
    io.grpc.transport.AbstractServerStream.remoteEndClosed(AbstractServerStream.java:200)
    io.grpc.transport.AbstractStream$1.endOfStream(AbstractStream.java:85)
    io.grpc.transport.MessageDeframer.deliver(MessageDeframer.java:245)
    io.grpc.transport.MessageDeframer.request(MessageDeframer.java:142)
    io.grpc.transport.AbstractStream.requestMessagesFromDeframer(AbstractStream.java:226)
    io.grpc.transport.netty.NettyServerStream.access$000(NettyServerStream.java:47)
    io.grpc.transport.netty.NettyServerStream$1.run(NettyServerStream.java:74)
    io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:322)
    io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:356)
    io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
    java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
    java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
    java.lang.Thread.run(Thread.java:745)

and OOM with a 30GB heap after a few minutes. I guess we have a memory leak :-). Working on it.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/337
Fix memeory leak in MessageFramer by louiscryan · Pull Request #337 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@buchgr @ejona86
We've actually always had a leak, it was just very slow.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/338
Client stream flush reduction by louiscryan · Pull Request #338 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/339
Add code generation for the advanced server interface · Issue #339 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I asked on the mailing list (https://groups.google.com/forum/#!topic/grpc-io/1RiPC8XYP_U) whether a callback existed to notify the server that a client had disconnected so it could perform some cleanup actions. Here's the answer I received from Eric Anderson:
Because it is a unary request, there isn't a callback that notifies you of client cancellation (any error is considered a cancellation to the server). The next time you call onValue though, an exception will be thrown notifying you of the cancellation. That is enough in some scenarios.
The "advanced" interface provides such notification though. It has onHalfClose (which is when onComplete is normally called), onComplete (when the RPC gracefully completed), and onCancel (if there was an error or if the client cancelled). We don't have code generation for the advanced interface though, so you would need to implement ServerCallHandler for each method in the service, create ServerMethodDefinitions and add them to a ServerServiceDefinition, which is what you pass to the ServerBuilder's addService. That would be verbose and annoying, but simple code. It would probably make sense for you to create an issue for us to add codegen for the advanced interface.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/340
Buffer writes until flush, before sending to transport thread/lock · Issue #340 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This design could benefit both okhttp, as it reduces synchronization overhead. It also would also improve flush behavior and make flushes predictable when MAX_CONCURRENT_STREAMS is exceeded.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/341
OkHttp does not observe SETTINGS_INITIAL_WINDOW_SIZE · Issue #341 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It only observes MAX_CONCURRENT_STREAMS.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/342
Add Openloop Client to benchmarks. by buchgr · Pull Request #342 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 @nmittler @louiscryan @vjpai
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/343
Update to protobuf-gradle-plugin:0.2.1 by zhangkun83 · Pull Request #343 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83, LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/344
Fix buffer leak from 0-length buffer optimization by ejona86 · Pull Request #344 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
lgtm
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/345
Fix the race between failing and starting pending streams. by madongfly · Pull Request #345 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/346
Cannot compile C++ code on WIndows (VisualCpp) · Issue #346 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
I'm trying to build project under Windows. To do this I added tool chain with visualCpp(VisualCpp) (compiler/build.gradle):
toolChains {
    visualCpp(VisualCpp) {
      installDir "c:/path/Microsoft Visual Studio 12.0"
    }
    gcc(Gcc) {
      target("x86_64") {
    cppCompiler.withArguments { args ->
      args << "-m64"
    }
    linker.withArguments { args ->
      args << "-m64"
    }
      }
      target("x86_32") {
    cppCompiler.withArguments { args ->
      args << "-m32"
    }
    linker.withArguments { args ->
      args << "-m32"
    }
      }
      target('local_arch') { }
    }
    [...]

Sadly VisualCpp plugin does not support target and I get error:
* Exception is:
org.gradle.api.tasks.TaskExecutionException: Execution failed for task ':grpc-compiler:compileLocal_archJava_pluginExecutableJava_pluginCpp'.
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeActions(ExecuteActionsTaskExecuter.java:69)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.execute(ExecuteActionsTaskExecuter.java:46)
    at org.gradle.api.internal.tasks.execution.PostExecutionAnalysisTaskExecuter.execute(PostExecutionAnalysisTaskExecuter.java:35)
    at org.gradle.api.internal.tasks.execution.SkipUpToDateTaskExecuter.execute(SkipUpToDateTaskExecuter.java:64)
    at org.gradle.api.internal.tasks.execution.ValidatingTaskExecuter.execute(ValidatingTaskExecuter.java:58)
    at org.gradle.api.internal.tasks.execution.SkipEmptySourceFilesTaskExecuter.execute(SkipEmptySourceFilesTaskExecuter.java:42)
    at org.gradle.api.internal.tasks.execution.SkipTaskWithNoActionsExecuter.execute(SkipTaskWithNoActionsExecuter.java:52)
    at org.gradle.api.internal.tasks.execution.SkipOnlyIfTaskExecuter.execute(SkipOnlyIfTaskExecuter.java:53)
    at org.gradle.api.internal.tasks.execution.ExecuteAtMostOnceTaskExecuter.execute(ExecuteAtMostOnceTaskExecuter.java:43)
    at org.gradle.api.internal.AbstractTask.executeWithoutThrowingTaskFailure(AbstractTask.java:306)
    at org.gradle.execution.taskgraph.AbstractTaskPlanExecutor$TaskExecutorWorker.executeTask(AbstractTaskPlanExecutor.java:79)
    at org.gradle.execution.taskgraph.AbstractTaskPlanExecutor$TaskExecutorWorker.processTask(AbstractTaskPlanExecutor.java:63)
    at org.gradle.execution.taskgraph.AbstractTaskPlanExecutor$TaskExecutorWorker.run(AbstractTaskPlanExecutor.java:51)
    at org.gradle.execution.taskgraph.DefaultTaskPlanExecutor.process(DefaultTaskPlanExecutor.java:23)
    at org.gradle.execution.taskgraph.DefaultTaskGraphExecuter.execute(DefaultTaskGraphExecuter.java:88)
    at org.gradle.execution.SelectedTaskExecutionAction.execute(SelectedTaskExecutionAction.java:29)
    at org.gradle.execution.DefaultBuildExecuter.execute(DefaultBuildExecuter.java:62)
    at org.gradle.execution.DefaultBuildExecuter.access$200(DefaultBuildExecuter.java:23)
    at org.gradle.execution.DefaultBuildExecuter$2.proceed(DefaultBuildExecuter.java:68)
    at org.gradle.execution.DryRunBuildExecutionAction.execute(DryRunBuildExecutionAction.java:32)
    at org.gradle.execution.DefaultBuildExecuter.execute(DefaultBuildExecuter.java:62)
    at org.gradle.execution.DefaultBuildExecuter.execute(DefaultBuildExecuter.java:55)
    at org.gradle.initialization.DefaultGradleLauncher.doBuildStages(DefaultGradleLauncher.java:149)
    at org.gradle.initialization.DefaultGradleLauncher.doBuild(DefaultGradleLauncher.java:106)
    at org.gradle.initialization.DefaultGradleLauncher.run(DefaultGradleLauncher.java:86)
    at org.gradle.launcher.exec.InProcessBuildActionExecuter$DefaultBuildController.run(InProcessBuildActionExecuter.java:80)
    at org.gradle.launcher.cli.ExecuteBuildAction.run(ExecuteBuildAction.java:33)
    at org.gradle.launcher.cli.ExecuteBuildAction.run(ExecuteBuildAction.java:24)
    at org.gradle.launcher.exec.InProcessBuildActionExecuter.execute(InProcessBuildActionExecuter.java:36)
    at org.gradle.launcher.exec.InProcessBuildActionExecuter.execute(InProcessBuildActionExecuter.java:26)
       at org.gradle.launcher.cli.RunBuildAction.run(RunBuildAction.java:51)
    at org.gradle.internal.Actions$RunnableActionAdapter.execute(Actions.java:169)
    at org.gradle.launcher.cli.CommandLineActionFactory$ParseAndBuildAction.execute(CommandLineActionFactory.java:237)
    at org.gradle.launcher.cli.CommandLineActionFactory$ParseAndBuildAction.execute(CommandLineActionFactory.java:210)
    at org.gradle.launcher.cli.JavaRuntimeValidationAction.execute(JavaRuntimeValidationAction.java:35)
    at org.gradle.launcher.cli.JavaRuntimeValidationAction.execute(JavaRuntimeValidationAction.java:24)
    at org.gradle.launcher.cli.CommandLineActionFactory$WithLogging.execute(CommandLineActionFactory.java:206)
    at org.gradle.launcher.cli.CommandLineActionFactory$WithLogging.execute(CommandLineActionFactory.java:169)
    at org.gradle.launcher.cli.ExceptionReportingAction.execute(ExceptionReportingAction.java:33)
    at org.gradle.launcher.cli.ExceptionReportingAction.execute(ExceptionReportingAction.java:22)
    at org.gradle.launcher.Main.doAction(Main.java:33)
    at org.gradle.launcher.bootstrap.EntryPoint.run(EntryPoint.java:45)
    at org.gradle.launcher.bootstrap.ProcessBootstrap.runNoExit(ProcessBootstrap.java:54)
    at org.gradle.launcher.bootstrap.ProcessBootstrap.run(ProcessBootstrap.java:35)
    at org.gradle.launcher.GradleMain.main(GradleMain.java:23)
    at org.gradle.wrapper.BootstrapMainStarter.start(BootstrapMainStarter.java:30)
    at org.gradle.wrapper.WrapperExecutor.execute(WrapperExecutor.java:127)
    at org.gradle.wrapper.GradleWrapperMain.main(GradleWrapperMain.java:56)
Caused by: org.gradle.api.GradleException: No tool chain is available to build for platform 'local_arch':
  - Tool chain 'visualCpp' (Visual Studio): Don't know how to build for platform 'local_arch'.
  - Tool chain 'gcc' (GNU GCC): Could not find C compiler 'gcc' in system path.
  - Tool chain 'clang' (Clang): Could not find C compiler 'clang' in system path.
    at org.gradle.nativeplatform.toolchain.internal.UnavailablePlatformToolProvider.failure(UnavailablePlatformToolProvider.java:47)
    at org.gradle.nativeplatform.toolchain.internal.UnavailablePlatformToolProvider.newCompiler(UnavailablePlatformToolProvider.java:71)
    at org.gradle.language.nativeplatform.tasks.AbstractNativeCompileTask.compile(AbstractNativeCompileTask.java:83)
    at org.gradle.internal.reflect.JavaMethod.invoke(JavaMethod.java:63)
    at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$IncrementalTaskAction.doExecute(AnnotationProcessingTaskFactory.java:235)

    at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$StandardTaskAction.execute(AnnotationProcessingTaskFactory.java:211)
    at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$IncrementalTaskAction.execute(AnnotationProcessingTaskFactory.java:222)
    at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$StandardTaskAction.execute(AnnotationProcessingTaskFactory.java:200)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeAction(ExecuteActionsTaskExecuter.java:80)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeActions(ExecuteActionsTaskExecuter.java:61)
    ... 47 more
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/347
Upgrading to the latest Netty version. by nmittler · Pull Request #347 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/348
Adding outbound flow control for Netty. by nmittler · Pull Request #348 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan @ejona86 can you take a look?  I still have to add tests for outbound flow control, but I wanted to get thoughts on the implementation first.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/349
okhttp: respect SETTINGS_INITIAL_WINDOW_SIZE in outbound flow control. by madongfly · Pull Request #349 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86, please take a look, thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/350
MessageFramer close on error can recurse · Issue #350 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
MessageFramer.close is not safe for re-entrancy.
A stream write error, triggers an error reported to the stream, which triggers framer.close, which triggers a write, which ....
at io.grpc.transport.netty.NettyServerHandler.onStreamError(NettyServerHandler.java:215)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:470)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledData.error(DefaultHttp2ConnectionEncoder.java:342)
at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$DefaultFlowState.writeError(DefaultHttp2RemoteFlowController.java:697)
at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$DefaultFlowState.cancel(DefaultHttp2RemoteFlowController.java:566)
at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$DefaultFlowState.write(DefaultHttp2RemoteFlowController.java:638)
at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$DefaultFlowState.writeBytes(DefaultHttp2RemoteFlowController.java:580)
at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController.sendFlowControlled(DefaultHttp2RemoteFlowController.java:180)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder.writeData(DefaultHttp2ConnectionEncoder.java:133)
at io.grpc.transport.netty.NettyServerHandler.sendGrpcFrame(NettyServerHandler.java:287)
at io.grpc.transport.netty.NettyServerHandler.write(NettyServerHandler.java:245)
at io.netty.channel.ChannelHandlerInvokerUtil.invokeWriteNow(ChannelHandlerInvokerUtil.java:157)
at io.netty.channel.DefaultChannelHandlerInvoker.invokeWrite(DefaultChannelHandlerInvoker.java:337)
at io.netty.channel.AbstractChannelHandlerContext.write(AbstractChannelHandlerContext.java:265)
at io.netty.channel.AbstractChannelHandlerContext.write(AbstractChannelHandlerContext.java:258)
at io.netty.channel.DefaultChannelPipeline.write(DefaultChannelPipeline.java:1039)
at io.netty.channel.AbstractChannel.write(AbstractChannel.java:252)
at io.grpc.transport.netty.NettyServerStream.sendFrame(NettyServerStream.java:93)
at io.grpc.transport.AbstractServerStream.internalSendFrame(AbstractServerStream.java:146)
at io.grpc.transport.AbstractStream$2.deliverFrame(AbstractStream.java:91)
at io.grpc.transport.MessageFramer.commitToSink(MessageFramer.java:246)
at io.grpc.transport.MessageFramer.close(MessageFramer.java:228)
at io.grpc.transport.AbstractStream.closeFramer(AbstractStream.java:136)
at io.grpc.transport.AbstractServerStream.abortStream(AbstractServerStream.java:226)
at io.grpc.transport.netty.NettyServerHandler.onStreamError(NettyServerHandler.java:215)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/351
Fix issue where MessageFramer.close can be called in a reentrant fashion by louiscryan · Pull Request #351 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/352
Recursion in NettyClientHandler during shutdown caused by channelInactive · Issue #352 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@nmittler @ejona86
Connection termination can trigger recursion in active stream shutdown
channelnactive -> close active streams -> send pending frames -> write headers (fail) -> connection error -> send go_away -> close active streams -> ...
Apr 28, 2015 1:34:55 PM io.netty.handler.codec.http2.DefaultHttp2Connection notifyClosed
SEVERE: Caught RuntimeException from listener onStreamClosed.
java.lang.NullPointerException
at io.grpc.transport.netty.NettyClientHandler.onStreamError(NettyClientHandler.java:237)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:470)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledData.error(DefaultHttp2ConnectionEncoder.java:341)
at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$DefaultState.writeError(DefaultHttp2RemoteFlowController.java:691)
at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$DefaultState.cancel(DefaultHttp2RemoteFlowController.java:578)
at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$DefaultState.cancel(DefaultHttp2RemoteFlowController.java:560)
at io.netty.handler.codec.http2.DefaultHttp2RemoteFlowController$2.onStreamClosed(DefaultHttp2RemoteFlowController.java:87)
at io.netty.handler.codec.http2.DefaultHttp2Connection.notifyClosed(DefaultHttp2Connection.java:263)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.removeFromActiveStreams(DefaultHttp2Connection.java:1150)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams$2.process(DefaultHttp2Connection.java:1097)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.forEachActiveStream(DefaultHttp2Connection.java:1121)
at io.netty.handler.codec.http2.DefaultHttp2Connection.forEachActiveStream(DefaultHttp2Connection.java:135)
at io.grpc.transport.netty.NettyClientHandler.goingAway(NettyClientHandler.java:310)
at io.grpc.transport.netty.NettyClientHandler.access$300(NettyClientHandler.java:65)
at io.grpc.transport.netty.NettyClientHandler$1.onGoAwaySent(NettyClientHandler.java:99)
at io.netty.handler.codec.http2.DefaultHttp2Connection.goAwaySent(DefaultHttp2Connection.java:189)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:555)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:586)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onConnectionError(Http2ConnectionHandler.java:494)
at io.grpc.transport.netty.NettyClientHandler.onConnectionError(NettyClientHandler.java:228)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:477)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.error(DefaultHttp2ConnectionEncoder.java:425)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:472)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:440)
at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
at io.netty.util.concurrent.DefaultPromise.notifyLateListener(DefaultPromise.java:621)
at io.netty.util.concurrent.DefaultPromise.addListener(DefaultPromise.java:138)
at io.netty.channel.DefaultChannelPromise.addListener(DefaultChannelPromise.java:93)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.(DefaultHttp2ConnectionEncoder.java:459)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:411)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:401)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder.writeHeaders(DefaultHttp2ConnectionEncoder.java:169)
at io.netty.handler.codec.http2.DecoratingHttp2FrameWriter.writeHeaders(DecoratingHttp2FrameWriter.java:50)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.writeHeaders(BufferingHttp2ConnectionEncoder.java:118)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$HeadersFrame.send(BufferingHttp2ConnectionEncoder.java:288)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$PendingStream.sendFrames(BufferingHttp2ConnectionEncoder.java:235)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.createNextPendingStream(BufferingHttp2ConnectionEncoder.java:196)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.access$100(BufferingHttp2ConnectionEncoder.java:68)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$1.onStreamClosed(BufferingHttp2ConnectionEncoder.java:95)
at io.netty.handler.codec.http2.DefaultHttp2Connection.notifyClosed(DefaultHttp2Connection.java:263)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.removeFromActiveStreams(DefaultHttp2Connection.java:1150)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams$2.process(DefaultHttp2Connection.java:1097)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.forEachActiveStream(DefaultHttp2Connection.java:1121)
at io.netty.handler.codec.http2.DefaultHttp2Connection.forEachActiveStream(DefaultHttp2Connection.java:135)
at io.grpc.transport.netty.NettyClientHandler.goingAway(NettyClientHandler.java:310)
at io.grpc.transport.netty.NettyClientHandler.access$300(NettyClientHandler.java:65)
at io.grpc.transport.netty.NettyClientHandler$1.onGoAwaySent(NettyClientHandler.java:99)
at io.netty.handler.codec.http2.DefaultHttp2Connection.goAwaySent(DefaultHttp2Connection.java:189)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:555)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:586)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onConnectionError(Http2ConnectionHandler.java:494)
at io.grpc.transport.netty.NettyClientHandler.onConnectionError(NettyClientHandler.java:228)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:477)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.error(DefaultHttp2ConnectionEncoder.java:425)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:472)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:440)
at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
at io.netty.util.concurrent.DefaultPromise.notifyLateListener(DefaultPromise.java:621)
at io.netty.util.concurrent.DefaultPromise.addListener(DefaultPromise.java:138)
at io.netty.channel.DefaultChannelPromise.addListener(DefaultChannelPromise.java:93)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.(DefaultHttp2ConnectionEncoder.java:459)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:411)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:401)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder.writeHeaders(DefaultHttp2ConnectionEncoder.java:169)
at io.netty.handler.codec.http2.DecoratingHttp2FrameWriter.writeHeaders(DecoratingHttp2FrameWriter.java:50)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.writeHeaders(BufferingHttp2ConnectionEncoder.java:118)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$HeadersFrame.send(BufferingHttp2ConnectionEncoder.java:288)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$PendingStream.sendFrames(BufferingHttp2ConnectionEncoder.java:235)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.createNextPendingStream(BufferingHttp2ConnectionEncoder.java:196)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.access$100(BufferingHttp2ConnectionEncoder.java:68)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$1.onStreamClosed(BufferingHttp2ConnectionEncoder.java:95)
at io.netty.handler.codec.http2.DefaultHttp2Connection.notifyClosed(DefaultHttp2Connection.java:263)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.removeFromActiveStreams(DefaultHttp2Connection.java:1150)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams$2.process(DefaultHttp2Connection.java:1097)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.forEachActiveStream(DefaultHttp2Connection.java:1121)
at io.netty.handler.codec.http2.DefaultHttp2Connection.forEachActiveStream(DefaultHttp2Connection.java:135)
at io.grpc.transport.netty.NettyClientHandler.goingAway(NettyClientHandler.java:310)
at io.grpc.transport.netty.NettyClientHandler.access$300(NettyClientHandler.java:65)
at io.grpc.transport.netty.NettyClientHandler$1.onGoAwaySent(NettyClientHandler.java:99)
at io.netty.handler.codec.http2.DefaultHttp2Connection.goAwaySent(DefaultHttp2Connection.java:189)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:555)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:586)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onConnectionError(Http2ConnectionHandler.java:494)
at io.grpc.transport.netty.NettyClientHandler.onConnectionError(NettyClientHandler.java:228)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:477)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.error(DefaultHttp2ConnectionEncoder.java:425)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:472)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:440)
at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
at io.netty.util.concurrent.DefaultPromise.notifyLateListener(DefaultPromise.java:621)
at io.netty.util.concurrent.DefaultPromise.addListener(DefaultPromise.java:138)
at io.netty.channel.DefaultChannelPromise.addListener(DefaultChannelPromise.java:93)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.(DefaultHttp2ConnectionEncoder.java:459)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:411)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:401)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder.writeHeaders(DefaultHttp2ConnectionEncoder.java:169)
at io.netty.handler.codec.http2.DecoratingHttp2FrameWriter.writeHeaders(DecoratingHttp2FrameWriter.java:50)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.writeHeaders(BufferingHttp2ConnectionEncoder.java:118)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$HeadersFrame.send(BufferingHttp2ConnectionEncoder.java:288)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$PendingStream.sendFrames(BufferingHttp2ConnectionEncoder.java:235)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.createNextPendingStream(BufferingHttp2ConnectionEncoder.java:196)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.access$100(BufferingHttp2ConnectionEncoder.java:68)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$1.onStreamClosed(BufferingHttp2ConnectionEncoder.java:95)
at io.netty.handler.codec.http2.DefaultHttp2Connection.notifyClosed(DefaultHttp2Connection.java:263)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.removeFromActiveStreams(DefaultHttp2Connection.java:1150)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams$2.process(DefaultHttp2Connection.java:1097)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.forEachActiveStream(DefaultHttp2Connection.java:1121)
at io.netty.handler.codec.http2.DefaultHttp2Connection.forEachActiveStream(DefaultHttp2Connection.java:135)
at io.grpc.transport.netty.NettyClientHandler.goingAway(NettyClientHandler.java:310)
at io.grpc.transport.netty.NettyClientHandler.access$300(NettyClientHandler.java:65)
at io.grpc.transport.netty.NettyClientHandler$1.onGoAwaySent(NettyClientHandler.java:99)
at io.netty.handler.codec.http2.DefaultHttp2Connection.goAwaySent(DefaultHttp2Connection.java:189)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:555)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:586)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onConnectionError(Http2ConnectionHandler.java:494)
at io.grpc.transport.netty.NettyClientHandler.onConnectionError(NettyClientHandler.java:228)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:477)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.error(DefaultHttp2ConnectionEncoder.java:425)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:472)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:440)
at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
at io.netty.util.concurrent.DefaultPromise.notifyLateListener(DefaultPromise.java:621)
at io.netty.util.concurrent.DefaultPromise.addListener(DefaultPromise.java:138)
at io.netty.channel.DefaultChannelPromise.addListener(DefaultChannelPromise.java:93)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.(DefaultHttp2ConnectionEncoder.java:459)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:411)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:401)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder.writeHeaders(DefaultHttp2ConnectionEncoder.java:169)
at io.netty.handler.codec.http2.DecoratingHttp2FrameWriter.writeHeaders(DecoratingHttp2FrameWriter.java:50)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.writeHeaders(BufferingHttp2ConnectionEncoder.java:118)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$HeadersFrame.send(BufferingHttp2ConnectionEncoder.java:288)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$PendingStream.sendFrames(BufferingHttp2ConnectionEncoder.java:235)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.createNextPendingStream(BufferingHttp2ConnectionEncoder.java:196)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.access$100(BufferingHttp2ConnectionEncoder.java:68)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$1.onStreamClosed(BufferingHttp2ConnectionEncoder.java:95)
at io.netty.handler.codec.http2.DefaultHttp2Connection.notifyClosed(DefaultHttp2Connection.java:263)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.removeFromActiveStreams(DefaultHttp2Connection.java:1150)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams$2.process(DefaultHttp2Connection.java:1097)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.forEachActiveStream(DefaultHttp2Connection.java:1121)
at io.netty.handler.codec.http2.DefaultHttp2Connection.forEachActiveStream(DefaultHttp2Connection.java:135)
at io.grpc.transport.netty.NettyClientHandler.goingAway(NettyClientHandler.java:310)
at io.grpc.transport.netty.NettyClientHandler.access$300(NettyClientHandler.java:65)
at io.grpc.transport.netty.NettyClientHandler$1.onGoAwaySent(NettyClientHandler.java:99)
at io.netty.handler.codec.http2.DefaultHttp2Connection.goAwaySent(DefaultHttp2Connection.java:189)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:555)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:586)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onConnectionError(Http2ConnectionHandler.java:494)
at io.grpc.transport.netty.NettyClientHandler.onConnectionError(NettyClientHandler.java:228)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:477)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.error(DefaultHttp2ConnectionEncoder.java:425)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:472)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:440)
at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
at io.netty.util.concurrent.DefaultPromise.notifyLateListener(DefaultPromise.java:621)
at io.netty.util.concurrent.DefaultPromise.addListener(DefaultPromise.java:138)
at io.netty.channel.DefaultChannelPromise.addListener(DefaultChannelPromise.java:93)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.(DefaultHttp2ConnectionEncoder.java:459)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:411)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:401)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder.writeHeaders(DefaultHttp2ConnectionEncoder.java:169)
at io.netty.handler.codec.http2.DecoratingHttp2FrameWriter.writeHeaders(DecoratingHttp2FrameWriter.java:50)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.writeHeaders(BufferingHttp2ConnectionEncoder.java:118)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$HeadersFrame.send(BufferingHttp2ConnectionEncoder.java:288)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$PendingStream.sendFrames(BufferingHttp2ConnectionEncoder.java:235)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.createNextPendingStream(BufferingHttp2ConnectionEncoder.java:196)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.access$100(BufferingHttp2ConnectionEncoder.java:68)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$1.onStreamClosed(BufferingHttp2ConnectionEncoder.java:95)
at io.netty.handler.codec.http2.DefaultHttp2Connection.notifyClosed(DefaultHttp2Connection.java:263)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.removeFromActiveStreams(DefaultHttp2Connection.java:1150)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams$2.process(DefaultHttp2Connection.java:1097)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.forEachActiveStream(DefaultHttp2Connection.java:1121)
at io.netty.handler.codec.http2.DefaultHttp2Connection.forEachActiveStream(DefaultHttp2Connection.java:135)
at io.grpc.transport.netty.NettyClientHandler.goingAway(NettyClientHandler.java:310)
at io.grpc.transport.netty.NettyClientHandler.access$300(NettyClientHandler.java:65)
at io.grpc.transport.netty.NettyClientHandler$1.onGoAwaySent(NettyClientHandler.java:99)
at io.netty.handler.codec.http2.DefaultHttp2Connection.goAwaySent(DefaultHttp2Connection.java:189)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:555)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:586)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onConnectionError(Http2ConnectionHandler.java:494)
at io.grpc.transport.netty.NettyClientHandler.onConnectionError(NettyClientHandler.java:228)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:477)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.error(DefaultHttp2ConnectionEncoder.java:425)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:472)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:440)
at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
at io.netty.util.concurrent.DefaultPromise.notifyLateListener(DefaultPromise.java:621)
at io.netty.util.concurrent.DefaultPromise.addListener(DefaultPromise.java:138)
at io.netty.channel.DefaultChannelPromise.addListener(DefaultChannelPromise.java:93)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.(DefaultHttp2ConnectionEncoder.java:459)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:411)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:401)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder.writeHeaders(DefaultHttp2ConnectionEncoder.java:169)
at io.netty.handler.codec.http2.DecoratingHttp2FrameWriter.writeHeaders(DecoratingHttp2FrameWriter.java:50)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.writeHeaders(BufferingHttp2ConnectionEncoder.java:118)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$HeadersFrame.send(BufferingHttp2ConnectionEncoder.java:288)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$PendingStream.sendFrames(BufferingHttp2ConnectionEncoder.java:235)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.createNextPendingStream(BufferingHttp2ConnectionEncoder.java:196)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.access$100(BufferingHttp2ConnectionEncoder.java:68)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$1.onStreamClosed(BufferingHttp2ConnectionEncoder.java:95)
at io.netty.handler.codec.http2.DefaultHttp2Connection.notifyClosed(DefaultHttp2Connection.java:263)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.removeFromActiveStreams(DefaultHttp2Connection.java:1150)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams$2.process(DefaultHttp2Connection.java:1097)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.forEachActiveStream(DefaultHttp2Connection.java:1121)
at io.netty.handler.codec.http2.DefaultHttp2Connection.forEachActiveStream(DefaultHttp2Connection.java:135)
at io.grpc.transport.netty.NettyClientHandler.goingAway(NettyClientHandler.java:310)
at io.grpc.transport.netty.NettyClientHandler.access$300(NettyClientHandler.java:65)
at io.grpc.transport.netty.NettyClientHandler$1.onGoAwaySent(NettyClientHandler.java:99)
at io.netty.handler.codec.http2.DefaultHttp2Connection.goAwaySent(DefaultHttp2Connection.java:189)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:555)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:586)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onConnectionError(Http2ConnectionHandler.java:494)
at io.grpc.transport.netty.NettyClientHandler.onConnectionError(NettyClientHandler.java:228)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:477)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.error(DefaultHttp2ConnectionEncoder.java:425)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:472)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:440)
at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
at io.netty.util.concurrent.DefaultPromise.notifyLateListener(DefaultPromise.java:621)
at io.netty.util.concurrent.DefaultPromise.addListener(DefaultPromise.java:138)
at io.netty.channel.DefaultChannelPromise.addListener(DefaultChannelPromise.java:93)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.(DefaultHttp2ConnectionEncoder.java:459)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:411)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:401)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder.writeHeaders(DefaultHttp2ConnectionEncoder.java:169)
at io.netty.handler.codec.http2.DecoratingHttp2FrameWriter.writeHeaders(DecoratingHttp2FrameWriter.java:50)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.writeHeaders(BufferingHttp2ConnectionEncoder.java:118)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$HeadersFrame.send(BufferingHttp2ConnectionEncoder.java:288)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$PendingStream.sendFrames(BufferingHttp2ConnectionEncoder.java:235)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.createNextPendingStream(BufferingHttp2ConnectionEncoder.java:196)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.access$100(BufferingHttp2ConnectionEncoder.java:68)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$1.onStreamClosed(BufferingHttp2ConnectionEncoder.java:95)
at io.netty.handler.codec.http2.DefaultHttp2Connection.notifyClosed(DefaultHttp2Connection.java:263)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.removeFromActiveStreams(DefaultHttp2Connection.java:1150)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams$2.process(DefaultHttp2Connection.java:1097)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.forEachActiveStream(DefaultHttp2Connection.java:1121)
at io.netty.handler.codec.http2.DefaultHttp2Connection.forEachActiveStream(DefaultHttp2Connection.java:135)
at io.grpc.transport.netty.NettyClientHandler.goingAway(NettyClientHandler.java:310)
at io.grpc.transport.netty.NettyClientHandler.access$300(NettyClientHandler.java:65)
at io.grpc.transport.netty.NettyClientHandler$1.onGoAwaySent(NettyClientHandler.java:99)
at io.netty.handler.codec.http2.DefaultHttp2Connection.goAwaySent(DefaultHttp2Connection.java:189)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:555)
at io.netty.handler.codec.http2.Http2ConnectionHandler.goAway(Http2ConnectionHandler.java:586)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onConnectionError(Http2ConnectionHandler.java:494)
at io.grpc.transport.netty.NettyClientHandler.onConnectionError(NettyClientHandler.java:228)
at io.netty.handler.codec.http2.Http2ConnectionHandler.onException(Http2ConnectionHandler.java:477)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.error(DefaultHttp2ConnectionEncoder.java:425)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:472)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.operationComplete(DefaultHttp2ConnectionEncoder.java:440)
at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
at io.netty.util.concurrent.DefaultPromise.notifyLateListener(DefaultPromise.java:621)
at io.netty.util.concurrent.DefaultPromise.addListener(DefaultPromise.java:138)
at io.netty.channel.DefaultChannelPromise.addListener(DefaultChannelPromise.java:93)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledBase.(DefaultHttp2ConnectionEncoder.java:459)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:411)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder$FlowControlledHeaders.(DefaultHttp2ConnectionEncoder.java:401)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionEncoder.writeHeaders(DefaultHttp2ConnectionEncoder.java:169)
at io.netty.handler.codec.http2.DecoratingHttp2FrameWriter.writeHeaders(DecoratingHttp2FrameWriter.java:50)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.writeHeaders(BufferingHttp2ConnectionEncoder.java:118)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$HeadersFrame.send(BufferingHttp2ConnectionEncoder.java:288)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$PendingStream.sendFrames(BufferingHttp2ConnectionEncoder.java:235)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.createNextPendingStream(BufferingHttp2ConnectionEncoder.java:196)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder.access$100(BufferingHttp2ConnectionEncoder.java:68)
at io.grpc.transport.netty.BufferingHttp2ConnectionEncoder$1.onStreamClosed(BufferingHttp2ConnectionEncoder.java:95)
at io.netty.handler.codec.http2.DefaultHttp2Connection.notifyClosed(DefaultHttp2Connection.java:263)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.removeFromActiveStreams(DefaultHttp2Connection.java:1150)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams$2.process(DefaultHttp2Connection.java:1097)
at io.netty.handler.codec.http2.DefaultHttp2Connection$ActiveStreams.forEachActiveStream(DefaultHttp2Connection.java:1121)
at io.netty.handler.codec.http2.DefaultHttp2Connection.forEachActiveStream(DefaultHttp2Connection.java:135)
at io.netty.handler.codec.http2.Http2ConnectionHandler$BaseDecoder.channelInactive(Http2ConnectionHandler.java:151)
at io.netty.handler.codec.http2.Http2ConnectionHandler.channelInactive(Http2ConnectionHandler.java:325)
at io.grpc.transport.netty.NettyClientHandler.channelInactive(NettyClientHandler.java:217)
at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelInactiveNow(ChannelHandlerInvokerUtil.java:56)
at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelInactive(DefaultChannelHandlerInvoker.java:92)
at io.netty.channel.AbstractChannelHandlerContext.fireChannelInactive(AbstractChannelHandlerContext.java:135)
at io.netty.channel.DefaultChannelPipeline.fireChannelInactive(DefaultChannelPipeline.java:928)
at io.netty.channel.AbstractChannel$AbstractUnsafe$7.run(AbstractChannel.java:647)
at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:322)
at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:356)
at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1113)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:588)
at java.lang.Thread.run(Thread.java:724)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/353
Upgrade to protobuf plugin 0.3.1 by zhangkun83 · Pull Request #353 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83, LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/354
Fix style violations added in 986d221 by ejona86 · Pull Request #354 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
java/okhttp/src/test/java/io/grpc/transport/okhttp/OkHttpClientTransportTest.java:406: Line is longer than 100 characters
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/355
Include gradle 2.3 in Travis-CI cache by ejona86 · Pull Request #355 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/356
OkHttpClientTransportTest.pendingStreamFailedByIdExhausted is flaky · Issue #356 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
As seen in the Travis logs:
io.grpc.transport.okhttp.OkHttpClientTransportTest > pendingStreamFailedByIdExhausted FAILED
    java.lang.AssertionError: Failed waiting stream to be closed.
        at org.junit.Assert.fail(Assert.java:88)
        at io.grpc.transport.okhttp.OkHttpClientTransportTest$MockStreamListener.waitUntilStreamClosed(OkHttpClientTransportTest.java:912)
        at io.grpc.transport.okhttp.OkHttpClientTransportTest.pendingStreamFailedByIdExhausted(OkHttpClientTransportTest.java:650)

    java.lang.AssertionError: expected:<0> but was:<1>
        at org.junit.Assert.fail(Assert.java:88)
        at org.junit.Assert.failNotEquals(Assert.java:743)
        at org.junit.Assert.assertEquals(Assert.java:118)
        at org.junit.Assert.assertEquals(Assert.java:555)
        at org.junit.Assert.assertEquals(Assert.java:542)
        at io.grpc.transport.okhttp.OkHttpClientTransportTest.tearDown(OkHttpClientTransportTest.java:142)

The commit was restarted, and succeeded.
Another example of apparent flakiness: https://travis-ci.org/grpc/grpc-java/builds/59916295 . The commit before and after were green. The tested commit only changed Netty code.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/357
Try to allow building java without having to build codegen · Issue #357 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It may be possible to use the last released codegen binary.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/358
De-flake OkHttpClientTransportTest.pendingStreamFailedByIdExhausted. by madongfly · Pull Request #358 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/359
Http2ClientStream overwrites error message · Issue #359 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Http2ClientStream.transportHeadersReceived() is calling withDescription instead of augmentDescription. This hinders debugging what went wrong.
@yang-g, since he is interested in when this is resolved.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/360
Check response content type on client · Issue #360 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It seems we aren't checking the content type of responses on the client. The flag was originally put in place because some implementations were sending the wrong content type, but it seems we should enable it again.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/361
Remove all blocking from the NettyClientTransport. Fixes #116 by buchgr · Pull Request #361 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@nmittler @ejona86
Ready for review. Before this can be merged Netty has to be updated to commit netty/netty@31a6ab9
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/362
Fix build on Windows/VC++ by zhangkun83 · Pull Request #362 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/363
c++ server and java client communications issue · Issue #363 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello.
I try write gRPC communication with java client and c++ server on linux.
But i have exception (below) in client when it runs RPC procedure.
Logs shows that server processed request, sended answer and continues its work.
For test i wrote same client on c++ and same server on java. All communication versions works. And only client(java) with server(c++) failed.
I hope you can help me. Thanks.
Exception in thread "main" com.google.common.util.concurrent.UncheckedExecutionException: io.grpc.Status$OperationRuntimeException: INTERNAL:
Headers(path=null,authority=null,metadata={grpc-status=[0]})
DATA-----------------------------
 at io.grpc.stub.Calls.getUnchecked(Calls.java:117)
 at io.grpc.stub.Calls.blockingUnaryCall(Calls.java:129)
 at rpc_test.ManagerServiceGrpc$ManagerServiceBlockingStub.doGet(ManagerServiceGrpc.java:274)
 at rpc_test.Client.testRPC(Client.java:53)
 at rpc_test.Client.main(Client.java:64)

Caused by: io.grpc.Status$OperationRuntimeException: INTERNAL:
Headers(path=null,authority=null,metadata={grpc-status=[0]})
DATA-----------------------------
 at io.grpc.Status.asRuntimeException(Status.java:428)
 at io.grpc.stub.Calls$UnaryStreamToFuture.onClose(Calls.java:324)
 at io.grpc.ChannelImpl$CallImpl$ClientStreamListenerImpl$3.run(ChannelImpl.java:373)
 at io.grpc.SerializingExecutor$TaskRunner.run(SerializingExecutor.java:152)
 at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
 at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
 at java.lang.Thread.run(Thread.java:745)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/364
Don't overwrite error message if bad headers by ejona86 · Pull Request #364 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/365
Cleaning up some warnings. by nmittler · Pull Request #365 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/366
Swap to Netty's SslContextBuilder by ejona86 · Pull Request #366 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can one of the admins verify this patch?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/367
More flush reduction for Netty by louiscryan · Pull Request #367 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can one of the admins verify this patch?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/368
Don't use SerializingExecutor when running with a direct executor. · Issue #368 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I wanted to know what the impact of the SerializingExecutor is when running with a direct executor.
So I did 3 benchmarks, choosing the best out of 3 runs.
Direct Executor + Serializing (current master)
buchgr@buchgr0:~/Code/grpc-java/benchmarks/build/install/grpc-benchmarks/bin$ ./qps_client --port=33333 --host=localhost --channels=8 --outstanding_rpcs_per_channel=10 --warmup_duration=10s --duration=30s --server_payload=1 --client_payload=1 --directexecutor
Channels:                       8
Outstanding RPCs per Channel:   10
Server Payload Size:            1
Client Payload Size:            1
50%ile Latency (in micros):     669
90%ile Latency (in micros):     1817
95%ile Latency (in micros):     3231
99%ile Latency (in micros):     5727
99.9%ile Latency (in micros):   9255
QPS:                            78642

Direct Executor + Serializing Executor without synchronized blocks.
buchgr@buchgr0:~/Code/grpc-java/benchmarks/build/install/grpc-benchmarks/bin$ ./qps_client --port=33333 --host=localhost --channels=8 --outstanding_rpcs_per_channel=10 --warmup_duration=10s --duration=30s --server_payload=1 --client_payload=1 --directexecutor
Channels:                       8
Outstanding RPCs per Channel:   10
Server Payload Size:            1
Client Payload Size:            1
50%ile Latency (in micros):     655
90%ile Latency (in micros):     1647
95%ile Latency (in micros):     3083
99%ile Latency (in micros):     5679
99.9%ile Latency (in micros):   9607
QPS:                            81500

Direct Executor only, no Serializing Executor
buchgr@buchgr0:~/Code/grpc-java/benchmarks/build/install/grpc-benchmarks/bin$ ./qps_client --port=33333 --host=localhost --channels=8 --outstanding_rpcs_per_channel=10 --warmup_duration=10s --duration=30s --server_payload=1 --client_payload=1 --directexecutor
Channels:                       8
Outstanding RPCs per Channel:   10
Server Payload Size:            1
Client Payload Size:            1
50%ile Latency (in micros):     619
90%ile Latency (in micros):     1096
95%ile Latency (in micros):     1132
99%ile Latency (in micros):     3999
99.9%ile Latency (in micros):   11407
QPS:                            99904

So it seems to me that the potential improvement is significant enough to make some changes and not use a SerializingExecutor when using direct i.e. by adding an option to the Server / Channel Builders.
WDYT @nmittler @louiscryan @ejona86 ?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/369
Update Netty to 9d70cf3 to pick up flush elimination by louiscryan · Pull Request #369 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@nmittler @ejona86
This is just the changes necessary to work with the flush elimination change in Netty
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/370
Don't close streams when sending GOAWAY by ejona86 · Pull Request #370 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can one of the admins verify this patch?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/371
okhttp: Implement outbound flow control · Issue #371 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#6 implemented the outbound flow control API for client and server, as well as support for it in Netty, but it did not implement support for it in OkHttp. We need outbound support in OkHttp, or at least dummy support (that implements the API, but doesn't provide push-back) for the near future.
Dummy support could be implemented on the client-side by calling notifyIfReady on stream creation (similar to in Netty). It seems server-side may work as-is. In either case, this would rely on AbstractStream.isReady() always returning true.
But we should really implement the full feature on OkHttp.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/372
Do not fail pending streams when sending GOAWAY. by nmittler · Pull Request #372 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 @buchgr can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/373
Adding bin to .gitignore for OSX by nmittler · Pull Request #373 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look? I still get these directories popping up on OSX ... it's annoying :/
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/374
netty: Remove goAwayStatus when client closing by ejona86 · Pull Request #374 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can one of the admins verify this patch?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/375
OkHttp: "Platform.getSelectedProtocol() == null" check is problematic · Issue #375 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
May 04, 2015 9:48:24 PM com.squareup.okhttp.internal.Platform$JdkWithJettyBootPlatform getSelectedProtocol
INFO: ALPN callback dropped: SPDY and HTTP/2 are disabled. Is alpn-boot on the boot class path?
I used "Platform.getSelectedProtocol() == null" prior to our TLS hand shake to check whether user has already done the handshake, if they haven't, this log would show up while we are about to do the handshake.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/376
Add comment to satisfy checkstyle by ejona86 · Pull Request #376 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/377
Make checkstyle fail build by default by ejona86 · Pull Request #377 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can one of the admins verify this patch?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/378
Use CreateStartScripts for integration-testing by ejona86 · Pull Request #378 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can one of the admins verify this patch?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/379
Produce combined JavaDoc, add links, exclude internals by ejona86 · Pull Request #379 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can one of the admins verify this patch?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/380
Updating to the latest Netty version. by nmittler · Pull Request #380 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can one of the admins verify this patch?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/381
Add Jacoco code coverage by ejona86 · Pull Request #381 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can one of the admins verify this patch?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/382
Unsupported TLS version exception on server side is not handled. · Issue #382 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
May 05, 2015 11:01:26 AM io.netty.channel.DefaultChannelPipeline$TailContext exceptionCaught
WARNING: An exceptionCaught() event was fired, and it reached at the tail of the pipeline. It usually means the last handler in the pipeline did not handle the exception.
io.netty.handler.codec.DecoderException: javax.net.ssl.SSLHandshakeException: Client requested protocol TLSv1 not enabled or not supported
at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:358)
at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:946)
at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:127)
at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:510)
at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:467)
at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:381)
at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:353)
at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
at java.lang.Thread.run(Thread.java:745)
Caused by: javax.net.ssl.SSLHandshakeException: Client requested protocol TLSv1 not enabled or not supported
at sun.security.ssl.Handshaker.checkThrown(Handshaker.java:1421)
at sun.security.ssl.SSLEngineImpl.checkTaskThrown(SSLEngineImpl.java:535)
at sun.security.ssl.SSLEngineImpl.readNetRecord(SSLEngineImpl.java:813)
security.ssl.SSLEngineImpl.unwrap(SSLEngineImpl.java:781)
at javax.net.ssl.SSLEngine.unwrap(SSLEngine.java:624)
at io.netty.handler.ssl.SslHandler.unwrap(SslHandler.java:1139)
at io.netty.handler.ssl.SslHandler.unwrap(SslHandler.java:1003)
at io.netty.handler.ssl.SslHandler.decode(SslHandler.java:943)
at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
... 14 more
Caused by: javax.net.ssl.SSLHandshakeException: Client requested protocol TLSv1 not enabled or not supported
at sun.security.ssl.Alerts.getSSLException(Alerts.java:203)
at sun.security.ssl.SSLEngineImpl.fatal(SSLEngineImpl.java:1666)
at sun.security.ssl.Handshaker.fatalSE(Handshaker.java:304)
at sun.security.ssl.Handshaker.fatalSE(Handshaker.java:292)
at sun.security.ssl.ServerHandshaker.clientHello(ServerHandshaker.java:504)
at sun.security.ssl.ServerHandshaker.processMessage(ServerHandshaker.java:217)
at sun.security.ssl.Handshaker.processLoop(Handshaker.java:969)
at sun.security.ssl.Handshaker$1.run(Handshaker.java:909)
at sun.security.ssl.Handshaker$1.run(Handshaker.java:906)
at java.security.AccessController.doPrivileged(Native Method)
at sun.security.ssl.Handshaker$DelegatedTask.run(Handshaker.java:1359)
at io.netty.handler.ssl.SslHandler.runDelegatedTasks(SslHandler.java:1173)
at io.netty.handler.ssl.SslHandler.unwrap(SslHandler.java:1025)
... 16 more

The corresponding client exception is:
java.lang.RuntimeException: javax.net.ssl.SSLException: Connection closed by peer
It's hard to understand what was wrong from such limited info.
We should let the client knows its TLS version is problematic.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/383
Cleaning up closing for Netty client/server. by nmittler · Pull Request #383 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 this is a follow up to c8c478e  that addresses both the client and server side.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/384
Updating to the latest Netty version. by nmittler · Pull Request #384 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/385
No ciphers available. · Issue #385 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
With using Http2SecurityUtil.CIPHERS, we are encountering this cipher suites issue, the previous workaround is running with JDK8.
But now this issue is biting Android integration test.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/386
Always checking MAX_CONCURRENT_STREAMS in by nmittler · Pull Request #386 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 @buchgr can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/387
Allow skip codegen build by zhangkun83 · Pull Request #387 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It seems like project properties are exposed as settings in settings.gradle: https://gradle.org/docs/current/dsl/org.gradle.api.initialization.Settings.html
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/388
Re-adding goAwayStatus when client application closes. by nmittler · Pull Request #388 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 can you take a look?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/389
Integration test fails on HEAD · Issue #389 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am on HEAD (commit 111f6dd)
./gradlew :grpc-integration-testing:test keeps failing on both Mac and Linux with:
io.grpc.testing.integration.Http2NettyTest > veryLargeRequest FAILED
    java.lang.Exception: test timed out after 30000 milliseconds

io.grpc.testing.integration.Http2NettyTest > veryLargeResponse FAILED
    java.lang.Exception: test timed out after 30000 milliseconds

io.grpc.testing.integration.Http2NettyTest > exchangeContextUnaryCall FAILED
    com.google.common.util.concurrent.UncheckedExecutionException: io.grpc.StatusRuntimeException: UNKNOWN

        Caused by:
        io.grpc.StatusRuntimeException: UNKNOWN

            Caused by:
            javax.net.ssl.SSLException: SSLEngine closed already

io.grpc.testing.integration.Http2NettyTest > emptyUnary FAILED
    java.lang.Exception: test timed out after 10000 milliseconds

io.grpc.testing.integration.Http2NettyTest > pingPong FAILED
    Wanted but not invoked:
    streamObserver.onValue(
        payload {
...
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/390
Fix the filesets to be checked by checkstyle. by zhangkun83 · Pull Request #390 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/391
Unify build properties by zhangkun83 · Pull Request #391 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/392
Properly removing buffered streams after receiving goAway by nmittler · Pull Request #392 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/393
Adding logging to NettyClientHandler. by nmittler · Pull Request #393 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/394
Examples should use CreateStartScripts · Issue #394 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We are using CreateStartScripts in benchmark and integration-testing, and it seems nice. We should do the same for the examples (so similar changes to 00a7192).
Documentation will need to be updated.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/395
Only complete graceful shutdown after buffered streams complete. by nmittler · Pull Request #395 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
What does this gain us? I thought 77d0042 would be identical behavior unless we overrode the appropriate method.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/396
Improve Contributing by ejona86 · Pull Request #396 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/397
Add build status icon and rephrase title by zhangkun83 · Pull Request #397 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/398
Use protoc artifact from Maven Central. by zhangkun83 · Pull Request #398 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/399
Use CreateStartScripts for examples by ejona86 · Pull Request #399 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/400
Make Channel/Server abstract classes by ejona86 · Pull Request #400 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/401
Stop running gradle in run-test-{client,server}.sh by ejona86 · Pull Request #401 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/402
Adding default implementation of onReady in Call and ServerCall by nmittler · Pull Request #402 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/403
Update generated proto output by ejona86 · Pull Request #403 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/404
Proto files are not recompiled if codegen has been changed · Issue #404 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Since we have checked in the generated code, we must re-generate them if 1) the proto files are changed, or 2) the codegen is changed, or 3) the version of protoc is changed.
The generateProto task uses the proto files as input, and I have confirmed that 1) works, but 2) and 3) don't.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/405
Recompile proto files if codegen has changed. by zhangkun83 · Pull Request #405 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/406
Make README obvious that protobuf building is optional by ejona86 · Pull Request #406 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/407
isReady() should return false until stream allocated by ejona86 · Pull Request #407 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/408
Bad transport may be used for starting stream. · Issue #408 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently we reference activeTransport to the newly created transport before the new transport is started , so if the new transport failed starting with an exception, the subsequent stream still try to use the bad activeTransport.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/409
Handle OkHttp throwing exception during start() by ejona86 · Pull Request #409 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/410
Upgrade to protobuf-gradle-plugin:0.4.0 by zhangkun83 · Pull Request #410 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/411
OkHttp connection window does not reclaim outstanding connection window of closed stream · Issue #411 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Netty will return any unprocessed stream window to the connection window on stream closure, OkHttp does not currently do this.
See onStreamClosed in Nettys DefaultHttp2LocalFlowController.
This will surface if a stream is cancelled and there is a partial message in the Deframer as the Deframer intentionally does not return bytes if there are no pending requests.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/412
routeGuideClient hangs · Issue #412 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
As reported by Martin, (I assume @magx2). @magx2, what git commit were you running at?
Terminal1-server:
$ ./gradlew routeGuideServer
:grpc-core:compileJava UP-TO-DATE
:grpc-core:animalSniffer
...
May 06, 2015 4:56:06 PM io.grpc.examples.routeguide.RouteGuideServer start
INFO: Server started, listening on 8980

Server is started; now running client. Terminal2-client:
$ ./gradlew routeGuideClient
:grpc-core:compileJava UP-TO-DATE
:grpc-core:animalSniffer
...
:grpc-examples:classes UP-TO-DATE
May 06, 2015 4:56:51 PM io.grpc.examples.routeguide.RouteGuideClient info
INFO: *** GetFeature: lat=409,146,138 lon=-746,188,906
// at this point everythings hangs

Stopping client with CTRL+C results in error in server:
May 06, 2015 4:57:50 PM io.netty.channel.DefaultChannelPipeline$TailContext exceptionCaught
WARNING: An exceptionCaught() event was fired, and it reached at the tail of the pipeline. It usually means the last handler in the pipeline did not handle the exception.
java.io.IOException: An existing connection was forcibly closed by the remote host
    at sun.nio.ch.SocketDispatcher.read0(Native Method)
    at sun.nio.ch.SocketDispatcher.read(SocketDispatcher.java:43)
    at sun.nio.ch.IOUtil.readIntoNativeBuffer(IOUtil.java:223)
    at sun.nio.ch.IOUtil.read(IOUtil.java:192)
    at sun.nio.ch.SocketChannelImpl.read(SocketChannelImpl.java:379)
    at io.netty.buffer.PooledUnsafeDirectByteBuf.setBytes(PooledUnsafeDirectByteBuf.java:311)
    at io.netty.buffer.AbstractByteBuf.writeBytes(AbstractByteBuf.java:854)
    at io.netty.channel.socket.nio.NioSocketChannel.doReadBytes(NioSocketChannel.java:242)
    at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:115)
    at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:510)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:467)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:381)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:353)
    at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
    at java.lang.Thread.run(Thread.java:745)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/413
Add more JUnit annotations to list of methods checkstyle will ignore by louiscryan · Pull Request #413 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/414
Fixing benchmarks build in eclipse. by nmittler · Pull Request #414 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/415
okhttp: Catch Exceptions thrown by the frist platform.getSelectedProt… by madongfly · Pull Request #415 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/416
changed the netty-codec-http2 depdendency to released version by marky-mark · Pull Request #416 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.  It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA).
📝 Please visit https://cla.developers.google.com/ to sign.
Once you've signed, please reply here (e.g. I signed it!) and we'll verify.  Thanks.


If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check your existing CLA data and verify that your email is set on your git commits.
If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/417
Add ping to ClientTransport and ChannelImpl by jhump · Pull Request #417 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/418
Slight performance improvment for MutableHandlerRegistryImpl by nmittler · Pull Request #418 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Here are the benchmark results from running on my laptop:
Benchmark                              (methodCountPerService)  (nameLength)  (serviceCount)  (useNewRegistry)   Mode  Cnt    Score    Error  Units
HandlerRegistryBenchmark.lookupMethod                      100            50             100             false  thrpt   20  332.830 ±  9.159  ops/s
HandlerRegistryBenchmark.lookupMethod                      100            50             100              true  thrpt   20  377.629 ± 12.240  ops/s
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/419
Fix a bug that checked-in generated code are not re-compiled. by zhangkun83 · Pull Request #419 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/420
can not compile with genetor code · Issue #420 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
java version "1.8.0_40"
Mac OS X 10.10.3
gradle version 2.4
protobuf version 3.0
I can use gradle compile when skipCodegen=true,but I can not compile when I want code gen.
First,It show me 'google/protobuf/compiler/java/java_names.h' file not found,then I copy the cpp file from protobuf/share to compiler/src/java_plugin/cpp.It show me unknown type name 'Atomic32'.
How can I do it? Thanks.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/421
Deferring stream creation until receiving SETTINGS from server. by nmittler · Pull Request #421 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/422
Add property ``protoc=/path/to/protoc`` by zhangkun83 · Pull Request #422 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/423
Dockerfile for deployment by zhangkun83 · Pull Request #423 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Related to protocolbuffers/protobuf/issues/354
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/424
Allow 100 streams initially rather than 10. by nmittler · Pull Request #424 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/425
Simplify the build instructions now that Netty can be fetched from Maven by benmccann · Pull Request #425 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
So... we aren't confident we won't need to use the submodule in the future.
The plan is that our releases always use Netty artifacts on Maven Central. For the master branch we would try to stay on a Netty released artifact, but if we really need to we would still fallback to submodule. But then we have to delay a release until Netty releases.
That makes me wary of removing the submodule stuff.
Thoughts?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/426
Add documentation saying that transport has weaker API guarantees · Issue #426 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/427
Make it more obvious that JDK 8 is necessary for TLS · Issue #427 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/428
Client-side Load Balancing · Issue #428 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For the moment, all things client-side load balancing. Designs, requirements, etc. Can be split into separate issues as appropriate.
There is an internal load balancing design that needs to be made public. This is on @a11r's plate.
There is want to support ZooKeeper. It may need a different Channel implementation than the one necessary for the doc @a11r will share.
@louiscryan
@jhump
@mzhaom
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/429
Update docs to reflect current status of ALPN on older versions of Android · Issue #429 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/430
okhttp: Sends reset if client receives halfClose before sending halfClose. by madongfly · Pull Request #430 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/431
Implement writes to the channel using a dedicated write queue by louiscryan · Pull Request #431 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Difference in performance from MaxQpsBenchmark
AFTER-------------------------------
Benchmark                                    (channelCount)  (maxConcurrentStreams)   Mode  Cnt      Score      Error  Units
MaxQpsBenchmark.measureUnary:callsPerSecond               1                      10  thrpt   20  17233.925 ±  765.450  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               1                     100  thrpt   20  17494.865 ± 1069.966  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               1                    1000  thrpt   20  16806.718 ± 2000.184  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               2                      10  thrpt   20  26280.909 ± 1800.194  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               2                     100  thrpt   20  30651.307 ± 2506.293  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               2                    1000  thrpt   20  30850.247 ± 2760.220  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               4                      10  thrpt   20  42930.248 ± 1463.644  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               4                     100  thrpt   20  44527.268 ± 1342.846  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               4                    1000  thrpt   20  46026.291 ± 2705.484  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               8                      10  thrpt   20  30151.448 ± 1601.576  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               8                     100  thrpt   20  35231.488 ±  993.181  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               8                    1000  thrpt   20  37890.380 ± 4221.883  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              16                      10  thrpt   20  28447.637 ± 1190.671  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              16                     100  thrpt   20  30699.913 ±  652.101  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              16                    1000  thrpt   20  28769.108 ± 3196.432  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              32                      10  thrpt   20  28440.326 ± 1507.982  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              32                     100  thrpt   20  29217.955 ± 2022.133  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              32                    1000  thrpt   20  26925.591 ± 3144.744  ops/s
AFTER-------------------------------
Benchmark                                    (channelCount)  (maxConcurrentStreams)   Mode  Cnt       Score      Error  Units
MaxQpsBenchmark.measureUnary:callsPerSecond               1                      10  thrpt   20   14919.476 ± 1049.194  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               1                     100  thrpt   20   48554.047 ± 3809.628  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               1                    1000  thrpt   20   55975.008 ± 2687.428  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               2                      10  thrpt   20   27070.917 ±  856.241  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               2                     100  thrpt   20   83444.590 ± 4580.374  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               2                    1000  thrpt   20   85941.249 ± 6032.673  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               4                      10  thrpt   20   48875.571 ± 2497.066  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               4                     100  thrpt   20  110715.074 ± 7999.329  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               4                    1000  thrpt   20  107040.913 ± 3820.023  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               8                      10  thrpt   20   75139.737 ± 1588.738  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               8                     100  thrpt   20   69458.655 ± 2679.446  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond               8                    1000  thrpt   20   72043.815 ± 2902.249  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              16                      10  thrpt   20   64267.215 ± 2748.387  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              16                     100  thrpt   20   52057.030 ± 1480.486  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              16                    1000  thrpt   20   49996.458 ± 3400.733  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              32                      10  thrpt   20   57700.415 ± 1273.293  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              32                     100  thrpt   20   55044.654 ± 1725.707  ops/s
MaxQpsBenchmark.measureUnary:callsPerSecond              32                    1000  thrpt   20   45458.060 ± 7053.582  ops/s
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/432
updates to test native epoll by nmittler · Pull Request #432 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/433
Requesting more messages from the Deframer causes unnecessary context-switching · Issue #433 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In the case of a incoming stream of messages the flow-control window may accommodate more than one message. If the deframer has several messages in its currently held buffer we end up doing a lot of context switching to request more messages out as we end up with a sequence like
deframer.request(1) -> jump to app thread -> onPayload() -> call.request(1) -> jump to event loop -> deframer.request(1)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/434
Fixing benchmarks build on non-linux systems. by nmittler · Pull Request #434 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/435
okhttp: Enable TLS for Http2OkHttpTest. by madongfly · Pull Request #435 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/436
ServerCalls binding utilities are too general · Issue #436 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Generated server bindings use only two methods in ServerCalls to adapt a service. The lack of differentiation between the different modes of streaming causes too many calls to 'request' more messages from flow control in scenarios where no more messages are available.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/437
Delete the generated files only before generateProto. by zhangkun83 · Pull Request #437 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM. Thanks! This will be nice.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/438
Some more minor flush optimizations by louiscryan · Pull Request #438 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 @nmittler
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/439
Make it more obvious JDK 8 is commonly necessary by ejona86 · Pull Request #439 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/440
OkHttp does not return connection flow control for DATA of unknown stream · Issue #440 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It returns early.
https://github.com/grpc/grpc-java/blob/master/okhttp/src/main/java/io/grpc/transport/okhttp/OkHttpClientTransport.java#L501
It seems like we can just move the windowUpdate handling before the return.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/441
WINDOW_UPDATE for unknown streams causes exception · Issue #441 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
As discovered by @madongfly. It is very easy to get a WINDOW_UPDATE for an unknown stream. For instance, if we sent RST_STREAM and there is a WINDOW_UPDATE en route from the server already.
https://github.com/grpc/grpc-java/blob/master/okhttp/src/main/java/io/grpc/transport/okhttp/OutboundFlowController.java#L97
It seems we should just ignore such WINDOW_UPDATES instead.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/442
okhttp: don't crash if receive window_update for an non-exit stream which may have existed. by madongfly · Pull Request #442 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/443
okhttp: update connection window when receives DATA for existed streams. by madongfly · Pull Request #443 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 Please take a look, thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/444
Disable Netty eventloop graceful termination by ejona86 · Pull Request #444 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/445
Update AUTH-README.md with Android TLS/ALPN by zsurocking · Pull Request #445 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.  It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA).
📝 Please visit https://cla.developers.google.com/ to sign.
Once you've signed, please reply here (e.g. I signed it!) and we'll verify.  Thanks.


If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check your existing CLA data and verify that your email is set on your git commits.
If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/446
Adding support for UDS to benchmarks by nmittler · Pull Request #446 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/447
Add new benchmarks by louiscryan · Pull Request #447 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@nmittler - FYI as you're refactoring  benchmarks
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/448
Implement shutdownNow · Issue #448 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For both ChannelImpl and ServerImpl
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/449
Consider delaying terminated state until application no longer processing · Issue #449 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In ServerImpl and ChannelImpl, we proceed to terminated as soon as all the transports have terminated. However, we should probably wait for all the SerializingExecutors to drain, since that is more of what the application would expect and it is useful to know that all the workers are done.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/450
Decrease ArrayDeque memory in SerializingExecutor by ejona86 · Pull Request #450 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/451
Set likely final size of array in toHttp2Headers by ejona86 · Pull Request #451 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/452
Netty streams should reduce the capacity of pooled buffers passed to sendFrame · Issue #452 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When a small write and flush is passed through the framer we hold the full 4k of the buffer until the write completes. By reducing the capacity of a pool direct buffer to the readably byte limit we immediately release the unwritten portion of the buffer back to the pool.
This may or may not have an impact on performance and utility should be evaluated by bencmarking. It may improve performance by making more bytes available to thread-local allocation. The most likely benchmarks to be impacted would be streaming ones that write and flush many messages in a tight loop as it would alleviate buffer-arena locks.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/453
Investigate performance implications of hard-coded outbound flow-control buffer · Issue #453 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The outbound flow-controller assumes as 32k memory buffer as the ideal pending write limit to determine if a stream is available for further writes (as indicated by AbstractStream.isReady).
This may be sub-optimal,  for example in the single stream case it would limit a flow-control aware message producer for exhausting the connection window.
An alternate solution is to allow each stream to accept messages if
(a) The pending writes for a stream are less than the connection window size
(b) A configured memory allocator indicates that more buffers are available in the allocator pool.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/454
Consider implementing pull / batch write to optimize flushing for streams · Issue #454 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For streaming calls that can produce a batch of messages as a unit consider adding an interface that allows for a single flush to propagate through the framer to the transport.
In the case of outbound flow-controlled streams it should be possible for a producer to generate a sequence of messages that produce a single flush in response to the onReady (and onPayload) callbacks where the sequence of writes terminates when isReady becomes false.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/455
Implement compute_engine_creds interop test · Issue #455 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/456
Implement service_account_creds interop test · Issue #456 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/457
Implement jwt_token_creds interop test · Issue #457 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
https://github.com/grpc/grpc/blob/master/doc/interop-test-descriptions.md#jwt_token_creds
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/458
Interop tests and servers should all use the same flow control window · Issue #458 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Right now we are generally using 1 MB as the connection window size and 64 KB as the stream flow control window. However, the tests were written assuming we were using the defaults of 64 KB for both. Also, it seems in the future we will be changing the flow control windows more. Java for instance is considering upping the window to 1 MB after putting in better memory handling. Java is also expecting to auto-tune the flow control window size based on the bandwidth-delay product.
We should specify that interop clients and servers should hard-code a fixed connection and stream window size. Given that we want to find bugs with the interop tests, I suggest 64 KB for both, but I'm open to alternatives.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/459
AbstractTransportTest.veryLarge{Request,Response} very slow with TLS · Issue #459 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I recently noticed that building grpc-java took an additional 30s. I tracked it down to OkHttp enabling TLS for its Http2OkHttpTest. Each test consumes ~12 seconds when using TLS, but is < 200 ms without TLS. It shouldn't take 12s to send 10 MB... The problem exists with Netty as well.
Since each test is run twice (once for OkHttp, once for Netty), that means the tests are ~50 seconds on the critical path of our ~1.5 minute build time.
I don't have many ideas as to why it could be so slow. It could be that the ciphers are really slow, but that is really, really slow. It is important to me that it impacts Netty and OkHttp equally.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/460
Support messages with unknown length in framer · Issue #460 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We will need some tagging interface or similar in order to detect when available() (or some other method) knows the message length.
This does not mean we would make sure that available() in the inbound direction (because compression makes that hard).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/461
Remove thread-hop required for blocking stub · Issue #461 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Once #150 CallOptions is supported, we can use a per-call direct executor for blocking stubs.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/462
Decide whether gRPC will use options in proto for methods · Issue #462 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It would be possible to attach options, such as compression and default timeout, to methods. @a11r was thinking that we wouldn't have such options, but @louiscryan had been thinking we would. It doesn't seem we feel too strongly one way or the other, but we just need to get consensus and move forward.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/463
Making client-side negotiation more pluggable. by nmittler · Pull Request #463 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/464
Rename integration-testing to interop-testing by ejona86 · Pull Request #464 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/465
Commit codegen'd files missing from 43038a5 by ejona86 · Pull Request #465 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/466
Fix minor issues with release scripts/documentation by ejona86 · Pull Request #466 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/467
Using SSLCertificateSocketFactory for TLS handshake doesn't work externally for Android older than 5.0 · Issue #467 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently, internal Android projects are using SSLCertificateSocketFactory for TLS handshake, but since ALPN only works well with Android 5.0 or newer, they use NPN for Android 4.4 and older.
It works just because internal OKHttp has been hacked to support NPN.
With the external OKHttp, it will failed as:
com.google.common.util.concurrent.UncheckedExecutionException: io.grpc.StatusRuntimeException: INTERNAL: Failed starting transport
    at io.grpc.stub.Calls.getUnchecked(Calls.java:117)
    at io.grpc.stub.Calls.blockingUnaryCall(Calls.java:129)
    at io.grpc.android.integrationtest.TestServiceGrpc$TestServiceBlockingStub.emptyCall(TestServiceGrpc.java:331)
    at io.grpc.android.integrationtest.IntegrationTester.emptyUnary(IntegrationTester.java:93)
    at io.grpc.android.integrationtest.IntegrationTester.runTest(IntegrationTester.java:72)
    at io.grpc.android.integrationtest.GrpcTestTask.doInBackground(GrpcTestTask.java:53)
    at io.grpc.android.integrationtest.GrpcTestTask.doInBackground(GrpcTestTask.java:12)
    at android.os.AsyncTask$2.call(AsyncTask.java:288)
    at java.util.concurrent.FutureTask.run(FutureTask.java:237)
    at android.os.AsyncTask$SerialExecutor$1.run(AsyncTask.java:231)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1112)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:587)
    at java.lang.Thread.run(Thread.java:841)
Caused by: io.grpc.StatusRuntimeException: INTERNAL: Failed starting transport
    at io.grpc.Status.asRuntimeException(Status.java:428)
    at io.grpc.stub.Calls$UnaryStreamToFuture.onClose(Calls.java:324)
    at io.grpc.ChannelImpl$CallImpl$ClientStreamListenerImpl$3.run(ChannelImpl.java:402)
    at io.grpc.SerializingExecutor$TaskRunner.run(SerializingExecutor.java:152)
    ... 3 more
Caused by: java.lang.RuntimeException: protocol negotiation failed
    at com.squareup.okhttp.OkHttpTlsUpgrader.upgrade(OkHttpTlsUpgrader.java:95)
    at io.grpc.transport.okhttp.OkHttpClientTransport.start(OkHttpClientTransport.java:293)
    at io.grpc.ChannelImpl.obtainActiveTransport(ChannelImpl.java:199)
    at io.grpc.ChannelImpl.access$600(ChannelImpl.java:55)
    at io.grpc.ChannelImpl$CallImpl.start(ChannelImpl.java:266)
    at io.grpc.stub.Calls.asyncServerStreamingCall(Calls.java:174)
    at io.grpc.stub.Calls.unaryFutureCall(Calls.java:86)
    at io.grpc.stub.Calls.blockingUnaryCall(Calls.java:129)
    at io.grpc.android.integrationtest.TestServiceGrpc$TestServiceBlockingStub.emptyCall(TestServiceGrpc.java:331)
    at io.grpc.android.integrationtest.IntegrationTester.emptyUnary(IntegrationTester.java:93)
    at io.grpc.android.integrationtest.IntegrationTester.runTest(IntegrationTester.java:72)
    at io.grpc.android.integrationtest.GrpcTestTask.doInBackground(GrpcTestTask.java:53)
    at io.grpc.android.integrationtest.GrpcTestTask.doInBackground(GrpcTestTask.java:12)
    at android.os.AsyncTask$2.call(AsyncTask.java:288)
    at java.util.concurrent.FutureTask.run(FutureTask.java:237)
    at android.os.AsyncTask$SerialExecutor$1.run(AsyncTask.java:231)
    ... 3 more
]>
    at io.grpc.android.integrationtest.TesterActivityTest.testGrpc(TesterActivityTest.java:65)
    at java.lang.reflect.Method.invokeNative(Native Method)
    at android.test.InstrumentationTestCase.runMethod(InstrumentationTestCase.java:214)
    at android.test.InstrumentationTestCase.runTest(InstrumentationTestCase.java:199)
    at android.test.ActivityInstrumentationTestCase2.runTest(ActivityInstrumentationTestCase2.java:192)
    at android.test.AndroidTestRunner.runTest(AndroidTestRunner.java:191)
    at android.test.AndroidTestRunner.runTest(AndroidTestRunner.java:176)
    at android.test.InstrumentationTestRunner.onStart(InstrumentationTestRunner.java:554)
    at android.app.Instrumentation$InstrumentationThread.run(Instrumentation.java:1701)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/468
Fail travis build if codegen isn't committed by ejona86 · Pull Request #468 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/469
Simplifying usage of native transports. by nmittler · Pull Request #469 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/470
Don't use a list for benchmarks deps by ejona86 · Pull Request #470 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/471
Improve invalid argument message for address by ejona86 · Pull Request #471 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/472
Don't use reflection for epoll/unix domain sockets by ejona86 · Pull Request #472 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/473
./gradlew fails · Issue #473 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When I run ./gradlew build or ./gradlew install, it fails with:
*** Skipping the build of codegen and compilation of proto files because skipCodegen=true
:grpc-core:compileJava UP-TO-DATE
:grpc-core:animalSniffer
:grpc-core:processResources UP-TO-DATE
:grpc-core:classes
:grpc-core:jar UP-TO-DATE
:grpc-auth:compileJava UP-TO-DATE
:grpc-auth:animalSniffer
:grpc-auth:processResources UP-TO-DATE
:grpc-auth:classes
:grpc-auth:jar UP-TO-DATE
:grpc-netty:compileJava UP-TO-DATE
:grpc-netty:processResources UP-TO-DATE
:grpc-netty:classes UP-TO-DATE
:grpc-netty:jar UP-TO-DATE
:grpc-okhttp:compileJava UP-TO-DATE
:grpc-okhttp:animalSniffer
:grpc-okhttp:processResources UP-TO-DATE
:grpc-okhttp:classes
:grpc-okhttp:jar UP-TO-DATE
:grpc-protobuf:compileJava UP-TO-DATE
:grpc-protobuf:processResources UP-TO-DATE
:grpc-protobuf:classes UP-TO-DATE
:grpc-protobuf:jar UP-TO-DATE
:grpc-protobuf-nano:compileJava UP-TO-DATE
:grpc-protobuf-nano:processResources UP-TO-DATE
:grpc-protobuf-nano:classes UP-TO-DATE
:grpc-protobuf-nano:jar UP-TO-DATE
:grpc-stub:compileJava UP-TO-DATE
:grpc-stub:animalSniffer
:grpc-stub:processResources UP-TO-DATE
:grpc-stub:classes
:grpc-stub:jar UP-TO-DATE
:grpc-all:compileJava UP-TO-DATE
:grpc-all:processResources UP-TO-DATE
:grpc-all:classes UP-TO-DATE
:grpc-all:jar UP-TO-DATE
:grpc-core:javadoc UP-TO-DATE
:grpc-auth:javadoc UP-TO-DATE
:grpc-testing:compileJava UP-TO-DATE
:grpc-testing:processResources UP-TO-DATE
:grpc-testing:classes UP-TO-DATE
:grpc-testing:jar UP-TO-DATE
:grpc-interop-testing:compileJava UP-TO-DATE
:grpc-interop-testing:processResources UP-TO-DATE
:grpc-interop-testing:classes UP-TO-DATE
:grpc-interop-testing:jar UP-TO-DATE
:grpc-benchmarks:compileJava
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/Utils.java:40: error: cannot find symbol
import io.grpc.testing.Payload;
                      ^
  symbol:   class Payload
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/Utils.java:41: error: cannot find symbol
import io.grpc.testing.SimpleRequest;
                      ^
  symbol:   class SimpleRequest
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:37: error: cannot find symbol
import static io.grpc.testing.RpcType.STREAMING;
                             ^
  symbol:   class RpcType
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:37: error: static import only from classes and interfaces
import static io.grpc.testing.RpcType.STREAMING;
^
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:38: error: cannot find symbol
import static io.grpc.testing.RpcType.UNARY;
                             ^
  symbol:   class RpcType
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:38: error: static import only from classes and interfaces
import static io.grpc.testing.RpcType.UNARY;
^
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:42: error: cannot find symbol
import io.grpc.testing.PayloadType;
                      ^
  symbol:   class PayloadType
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:43: error: cannot find symbol
import io.grpc.testing.RpcType;
                      ^
  symbol:   class RpcType
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:79: error: cannot find symbol
  RpcType rpcType = UNARY;
  ^
  symbol:   class RpcType
  location: class ClientConfiguration
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:80: error: cannot find symbol
  PayloadType payloadType = PayloadType.COMPRESSABLE;
  ^
  symbol:   class PayloadType
  location: class ClientConfiguration
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/Utils.java:115: error: cannot find symbol
  static SimpleRequest newRequest(ClientConfiguration config) {
         ^
  symbol:   class SimpleRequest
  location: class Utils
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:42: error: cannot find symbol
import io.grpc.testing.Payload;
                      ^
  symbol:   class Payload
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:43: error: cannot find symbol
import io.grpc.testing.PayloadType;
                      ^
  symbol:   class PayloadType
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:44: error: cannot find symbol
import io.grpc.testing.SimpleRequest;
                      ^
  symbol:   class SimpleRequest
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:45: error: cannot find symbol
import io.grpc.testing.SimpleResponse;
                      ^
  symbol:   class SimpleResponse
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:46: error: cannot find symbol
import io.grpc.testing.TestServiceGrpc;
                      ^
  symbol:   class TestServiceGrpc
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:176: error: package TestServiceGrpc does not exist
  private static class TestServiceImpl implements TestServiceGrpc.TestService {
                                                                 ^
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:179: error: cannot find symbol
    public void unaryCall(SimpleRequest request, StreamObserver<SimpleResponse> responseObserver) {
                          ^
  symbol:   class SimpleRequest
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:179: error: cannot find symbol
    public void unaryCall(SimpleRequest request, StreamObserver<SimpleResponse> responseObserver) {
                                                                ^
  symbol:   class SimpleResponse
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:187: error: cannot find symbol
        final StreamObserver<SimpleResponse> responseObserver) {
                             ^
  symbol:   class SimpleResponse
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:186: error: cannot find symbol
    public StreamObserver<SimpleRequest> streamingCall(
                          ^
  symbol:   class SimpleRequest
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:208: error: cannot find symbol
    private static SimpleResponse buildSimpleResponse(SimpleRequest request) {
                                                      ^
  symbol:   class SimpleRequest
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:208: error: cannot find symbol
    private static SimpleResponse buildSimpleResponse(SimpleRequest request) {
                   ^
  symbol:   class SimpleResponse
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:61: error: cannot find symbol
import io.grpc.testing.Payload;
                      ^
  symbol:   class Payload
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:62: error: cannot find symbol
import io.grpc.testing.SimpleRequest;
                      ^
  symbol:   class SimpleRequest
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:63: error: cannot find symbol
import io.grpc.testing.SimpleResponse;
                      ^
  symbol:   class SimpleResponse
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:64: error: cannot find symbol
import io.grpc.testing.TestServiceGrpc;
                      ^
  symbol:   class TestServiceGrpc
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:65: error: package io.grpc.testing.TestServiceGrpc does not exist
import io.grpc.testing.TestServiceGrpc.TestServiceStub;
                                      ^
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:122: error: cannot find symbol
  private SimpleRequest newRequest() {
          ^
  symbol:   class SimpleRequest
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:133: error: cannot find symbol
  private void warmup(SimpleRequest req, List<Channel> channels) throws Exception {
                      ^
  symbol:   class SimpleRequest
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:142: error: cannot find symbol
  private List<Histogram> doBenchmark(SimpleRequest req,
                                      ^
  symbol:   class SimpleRequest
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:161: error: cannot find symbol
  private Future<Histogram> doRpcs(Channel channel, SimpleRequest request, long endTime) {
                                                    ^
  symbol:   class SimpleRequest
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:172: error: cannot find symbol
  private Future<Histogram> doUnaryCalls(Channel channel, final SimpleRequest request,
                                                                ^
  symbol:   class SimpleRequest
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:212: error: cannot find symbol
  private static Future<Histogram> doStreamingCalls(Channel channel, final SimpleRequest request,
                                                                           ^
  symbol:   class SimpleRequest
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:231: error: cannot find symbol
  private static class ThisIsAHackStreamObserver implements StreamObserver<SimpleResponse> {
                                                                           ^
  symbol:   class SimpleResponse
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:233: error: cannot find symbol
    final SimpleRequest request;
          ^
  symbol:   class SimpleRequest
  location: class ThisIsAHackStreamObserver
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:239: error: cannot find symbol
    StreamObserver<SimpleRequest> requestObserver;
                   ^
  symbol:   class SimpleRequest
  location: class ThisIsAHackStreamObserver
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:241: error: cannot find symbol
    ThisIsAHackStreamObserver(SimpleRequest request,
                              ^
  symbol:   class SimpleRequest
  location: class ThisIsAHackStreamObserver
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:252: error: cannot find symbol
    public void onValue(SimpleResponse value) {
                        ^
  symbol:   class SimpleResponse
  location: class ThisIsAHackStreamObserver
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:56: error: cannot find symbol
import io.grpc.testing.SimpleRequest;
                      ^
  symbol:   class SimpleRequest
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:57: error: cannot find symbol
import io.grpc.testing.SimpleResponse;
                      ^
  symbol:   class SimpleResponse
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:58: error: cannot find symbol
import io.grpc.testing.TestServiceGrpc;
                      ^
  symbol:   class TestServiceGrpc
  location: package io.grpc.testing
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:59: error: package io.grpc.testing.TestServiceGrpc does not exist
import io.grpc.testing.TestServiceGrpc.TestServiceStub;
                                      ^
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:150: error: cannot find symbol
    final TestServiceStub stub;
          ^
  symbol:   class TestServiceStub
  location: class LoadGenerationWorker
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:151: error: cannot find symbol
    final SimpleRequest request;
          ^
  symbol:   class SimpleRequest
  location: class LoadGenerationWorker
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:156: error: cannot find symbol
    LoadGenerationWorker(Channel channel, SimpleRequest request, int targetQps, int duration) {
                                          ^
  symbol:   class SimpleRequest
  location: class LoadGenerationWorker
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:200: error: cannot find symbol
    private void newRpc(TestServiceStub stub) {
                        ^
  symbol:   class TestServiceStub
  location: class LoadGenerationWorker
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/Utils.java:117: error: cannot find symbol
    Payload payload = Payload.newBuilder()
    ^
  symbol:   class Payload
  location: class Utils
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/Utils.java:117: error: cannot find symbol
    Payload payload = Payload.newBuilder()
                      ^
  symbol:   variable Payload
  location: class Utils
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/Utils.java:122: error: cannot find symbol
    return SimpleRequest.newBuilder()
           ^
  symbol:   variable SimpleRequest
  location: class Utils
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:79: error: cannot find symbol
  RpcType rpcType = UNARY;
                    ^
  symbol:   variable UNARY
  location: class ClientConfiguration
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:80: error: cannot find symbol
  PayloadType payloadType = PayloadType.COMPRESSABLE;
                            ^
  symbol:   variable PayloadType
  location: class ClientConfiguration
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/ClientConfiguration.java:278: error: cannot find symbol
        config.rpcType = STREAMING;
                         ^
  symbol: variable STREAMING
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:168: error: cannot find symbol
        .addService(TestServiceGrpc.bindService(new TestServiceImpl()))
                    ^
  symbol:   variable TestServiceGrpc
  location: class AsyncServer
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:178: error: method does not override or implement a method from a supertype
    @Override
    ^
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:180: error: cannot find symbol
      SimpleResponse response = buildSimpleResponse(request);
      ^
  symbol:   class SimpleResponse
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:185: error: method does not override or implement a method from a supertype
    @Override
    ^
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:188: error: cannot find symbol
      return new StreamObserver<SimpleRequest>() {
                                ^
  symbol:   class SimpleRequest
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:190: error: cannot find symbol
        public void onValue(SimpleRequest request) {
                            ^
  symbol: class SimpleRequest
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:191: error: cannot find symbol
          SimpleResponse response = buildSimpleResponse(request);
          ^
  symbol: class SimpleResponse
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:210: error: package PayloadType does not exist
        if (!PayloadType.COMPRESSABLE.equals(request.getResponseType())) {
                        ^
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:215: error: cannot find symbol
        PayloadType type = request.getResponseType();
        ^
  symbol:   class PayloadType
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:217: error: cannot find symbol
        Payload payload = Payload.newBuilder().setType(type).setBody(body).build();
        ^
  symbol:   class Payload
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:217: error: cannot find symbol
        Payload payload = Payload.newBuilder().setType(type).setBody(body).build();
                          ^
  symbol:   variable Payload
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:218: error: cannot find symbol
        return SimpleResponse.newBuilder().setPayload(payload).build();
               ^
  symbol:   variable SimpleResponse
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncServer.java:220: error: cannot find symbol
      return SimpleResponse.getDefaultInstance();
             ^
  symbol:   variable SimpleResponse
  location: class TestServiceImpl
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:97: error: cannot find symbol
    SimpleRequest req = newRequest();
    ^
  symbol:   class SimpleRequest
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:124: error: cannot find symbol
    Payload payload = Payload.newBuilder().setType(config.payloadType).setBody(body).build();
    ^
  symbol:   class Payload
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:124: error: cannot find symbol
    Payload payload = Payload.newBuilder().setType(config.payloadType).setBody(body).build();
                      ^
  symbol:   variable Payload
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:126: error: cannot find symbol
    return SimpleRequest.newBuilder()
           ^
  symbol:   variable SimpleRequest
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:162: error: strings in switch are not supported in -source 1.6
    switch (config.rpcType) {
           ^
  (use -source 7 or higher to enable strings in switch)
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:163: error: cannot find symbol
      case UNARY:
           ^
  symbol:   variable UNARY
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:165: error: cannot find symbol
      case STREAMING:
           ^
  symbol:   variable STREAMING
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:174: error: cannot find symbol
    final TestServiceStub stub = TestServiceGrpc.newStub(channel);
          ^
  symbol:   class TestServiceStub
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:174: error: cannot find symbol
    final TestServiceStub stub = TestServiceGrpc.newStub(channel);
                                 ^
  symbol:   variable TestServiceGrpc
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:178: error: cannot find symbol
    stub.unaryCall(request, new StreamObserver<SimpleResponse>() {
                                               ^
  symbol:   class SimpleResponse
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:182: error: cannot find symbol
      public void onValue(SimpleResponse value) {
                          ^
  symbol: class SimpleResponse
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:214: error: cannot find symbol
    final TestServiceStub stub = TestServiceGrpc.newStub(channel);
          ^
  symbol:   class TestServiceStub
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:214: error: cannot find symbol
    final TestServiceStub stub = TestServiceGrpc.newStub(channel);
                                 ^
  symbol:   variable TestServiceGrpc
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/AsyncClient.java:221: error: cannot find symbol
    StreamObserver<SimpleRequest> requestObserver = stub.streamingCall(responseObserver);
                   ^
  symbol:   class SimpleRequest
  location: class AsyncClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:112: error: cannot find symbol
    SimpleRequest req = newRequest(config);
    ^
  symbol:   class SimpleRequest
  location: class OpenLoopClient
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:157: error: cannot find symbol
      stub = TestServiceGrpc.newStub(checkNotNull(channel, "channel"));
             ^
  symbol:   variable TestServiceGrpc
  location: class LoadGenerationWorker
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:201: error: cannot find symbol
      stub.unaryCall(request, new StreamObserver<SimpleResponse>() {
                                                 ^
  symbol:   class SimpleResponse
  location: class LoadGenerationWorker
/home/k/gitroot/grpc-java/benchmarks/src/main/java/io/grpc/benchmarks/qps/OpenLoopClient.java:206: error: cannot find symbol
        public void onValue(SimpleResponse value) {
                            ^
  symbol: class SimpleResponse
84 errors
:grpc-benchmarks:compileJava FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':grpc-benchmarks:compileJava'.
> Compilation failed; see the compiler error output for details.

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output.

BUILD FAILED

Total time: 10.704 secs
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/474
Document our findings about GCM performance by ejona86 · Pull Request #474 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/475
Change OkHttpClientTransport#start to construct a Socket with the hos… by jonathanjlin · Pull Request #475 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.  It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA).
📝 Please visit https://cla.developers.google.com/ to sign.
Once you've signed, please reply here (e.g. I signed it!) and we'll verify.  Thanks.


If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check your existing CLA data and verify that your email is set on your git commits.
If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/476
okhttp: outbound flow control. by madongfly · Pull Request #476 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86, please take a look, thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/477
Revert swapping to the "canonical HTTP mapping" · Issue #477 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Commit 4332c2f swapped to the status-suggested HTTP mappings, but these are really broken for gRPC. I had actually thought I had already reverted the commit, so I was shocked to see it was still in-place.
grpc/grpc@5b53e35 describes examples of specific issues with the mapping.
I want to revert this change immediately, but I don't want to do it just before a release, so I'll delay until after 0.7.0 is cut.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/478
Add support for indeterminate length messages.  by louiscryan · Pull Request #478 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 @nmittler
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/479
Improve synchronization in obtainActiveTransport() · Issue #479 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Split out of #322
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/480
Making test certs more shareable by nmittler · Pull Request #480 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL ... this is in part to help with development of the Jetty test (in the Netty module).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/481
Adding alpn_boot configuration to the parent build file. by nmittler · Pull Request #481 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/482
Upgrade okhttp to 2.3 by madongfly · Pull Request #482 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/483
Adding test for gRPC clients running inside Jetty. by nmittler · Pull Request #483 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 I think it would be a bit hacky to create a unit test to reproduce the Jetty environment.  To reproduce (and fix) the problem, I ended up just running Jetty locally and deploying a gRPC-enabled web app.  The solution is captured here: #180 (comment).
I'm abandoning this and will create a new PR for the switch to Netty ALPN plus documentation for Jetty.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/484
Add service_account_creds test. by madongfly · Pull Request #484 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I rebased (to have the okhttp upgrade commit) and verified it works for okhttp too.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/485
Add compute_engine_creds test. by madongfly · Pull Request #485 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/486
accidental complication error happend problem · Issue #486 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I compile my grpc project, sometimes it is ok but sometimes it has the following compilation error:

XXXXGrpc.java:22: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SearchRequest.PARSER),
^
XXXXGrpc.java:23: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SearchResponse.PARSER));
^
XXXXGrpc.java:28: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SearchRequest.PARSER),
^
XXXXGrpc.java:29: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SearchResponse.PARSER));
^
XXXXGrpc.java:34: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SearchRequest.PARSER),
^
XXXXGrpc.java:35: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SearchResponse.PARSER));
^
XXXXGrpc.java:40: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SearchRequest.PARSER),
^
XXXXGrpc.java:41: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SearchAllResponse.PARSER));
^
XXXXGrpc.java:46: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SuggestRequest.PARSER),
^
XXXXGrpc.java:47: error: package io.grpc.protobuf does not exist
io.grpc.protobuf.ProtoUtils.marshaller(com.engzo.search.protoc.SuggestResponse.PARSER));

sometimes ok sometimes not. very weird.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/487
Handle IOException thrown by FrameReader.nextFrame() as PROTOCOL_ERROR. · Issue #487 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In current implementation, we treat the IOException thrown by FrameReader.nextFrame() as the "IO" issue, so we just close the connection and don't send anymore.
But actually, it may throw IOException for protocol errors like: invalid frame size, RST_STREAM with stream id 0, invalid values in SETTINGS etc, in such cases, we should send a GOAWAY before closing the connection.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/488
Release commit for 0.7.0 by ejona86 · Pull Request #488 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/489
Add download and usage instructions by ejona86 · Pull Request #489 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/490
Upgrade to OkHttp 2.4 · Issue #490 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Just released. The API changes are known to break us. Let's look at what it'll take to upgrade.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/491
Upgrade OkHttp to 2.4. by madongfly · Pull Request #491 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/492
Let people use compression · Issue #492 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It's been implemented for a while, but no way to turn it on.
We don't have a way to determine if the remote supports compression; that may need to be considered. We should also make sure we interop with C, which is doing compression soon.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/493
Add User-Agent · Issue #493 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/494
Simplify configuration of flow control windows · Issue #494 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Stream window should really always be the same as the connection window.  We should just expose a single lever for this ... default to 1MB.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/495
Add SelectedProtocolQuerier to get protocol selected by NPN on Android. by madongfly · Pull Request #495 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/496
DeferredInputStream has unused generic parameter · Issue #496 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/497
Switching to Netty's ALPN support. by nmittler · Pull Request #497 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL.  I'll rebase once #480 is committed.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/498
Catch Exception thrown when query NPN selected protocol on a socket t… by madongfly · Pull Request #498 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/499
Renaming AUTH_README to SECURITY_README by nmittler · Pull Request #499 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/500
Remove unused imports. by madongfly · Pull Request #500 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM. Please make sure to run with checkstyle enabled before pushing in the future.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/501
okhttp: Call onError for IOException thrown by FrameReader.nextFrame(). by madongfly · Pull Request #501 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I'm concerned about conflating general I/O errors with protocol errors. Can you provide an example of one of those IOExceptions that is a protocol error? If it's in our code, it seems like making a special ProtocolErrorIOException or Http2IOException to communicate clearly would be a good idea.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/502
Allow for batching writes to the framer · Issue #502 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Need to allow applications to perform a sequence of writes that cause a single flush in the framer to improve throughput.
The typical example for this would be an application thats wants to write messages until isReady() is false and to do more writes when onReady() is called. Even if the application is not flow-control aware (i.e is not using isReady) it would still be useful to allow write batching for bursty streams
One simple option for doing this would be to delay the outbound framer flush while executing  onPayload/isReady callbacks though this would only help cases where sends are done inside these callbacks by the same thread. A more thorough API change is probably warranted.
To give some performance context the change described above allows the FlowControlledMessagesPerSecondBenchmark to go from ~700kqps to ~4Mqps on my box
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/503
Instructions to run the examples fail · Issue #503 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Steps:
Clone repo, checkout either "v0.7.x" (at commit 186a9b2) or "master" (at commit 0782c04). Follow instructions here: cd examples/, then ../gradlew installDist --stacktrace.
Output:
[...]
:grpc-core:animalSniffer
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils.class:74: Undefined reference: com.google.protobuf.Descriptors.Descriptor com.google.protobuf.Message.getDescriptorForType()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils.class:74: Undefined reference: String com.google.protobuf.Descriptors.Descriptor.getFullName()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils$1.class:60: Undefined reference: Object com.google.protobuf.Parser.parseFrom(java.io.InputStream)
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils$1.class:60: Undefined reference: com.google.protobuf.MessageLite
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils$1.class:51: Undefined reference: com.google.protobuf.MessageLite
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils$2.class:78: Undefined reference: byte[] com.google.protobuf.Message.toByteArray()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils$2.class:85: Undefined reference: com.google.protobuf.Parser com.google.protobuf.Message.getParserForType()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils$2.class:85: Undefined reference: Object com.google.protobuf.Parser.parseFrom(byte[])
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils$2.class:85: Undefined reference: com.google.protobuf.Message
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/ProtoUtils$2.class:75: Undefined reference: com.google.protobuf.Message
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:74: Undefined reference: int com.google.protobuf.MessageLite.getSerializedSize()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:75: Undefined reference: void com.google.protobuf.MessageLite.writeTo(java.io.OutputStream)
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:87: Undefined reference: byte[] com.google.protobuf.MessageLite.toByteArray()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:99: Undefined reference: int com.google.protobuf.MessageLite.getSerializedSize()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:107: Undefined reference: com.google.protobuf.CodedOutputStream com.google.protobuf.CodedOutputStream.newInstance(byte[], int, int)
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:108: Undefined reference: void com.google.protobuf.MessageLite.writeTo(com.google.protobuf.CodedOutputStream)
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:109: Undefined reference: void com.google.protobuf.CodedOutputStream.flush()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:110: Undefined reference: void com.google.protobuf.CodedOutputStream.checkNoSpaceLeft()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:117: Undefined reference: byte[] com.google.protobuf.MessageLite.toByteArray()
/Users/jcanizales/git/grpc-java/core/build/classes/main/io/grpc/proto/DeferredProtoInputStream.class:129: Undefined reference: int com.google.protobuf.MessageLite.getSerializedSize()
:grpc-core:animalSniffer FAILED

FAILURE: Build failed with an exception.

* What went wrong:
Execution failed for task ':grpc-core:animalSniffer'.
> Signature errors found. Verify them and ignore them with the proper annotation if needed.

* Try:
Run with --info or --debug option to get more log output.

* Exception is:
org.gradle.api.tasks.TaskExecutionException: Execution failed for task ':grpc-core:animalSniffer'.
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeActions(ExecuteActionsTaskExecuter.java:69)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.execute(ExecuteActionsTaskExecuter.java:46)
    at org.gradle.api.internal.tasks.execution.PostExecutionAnalysisTaskExecuter.execute(PostExecutionAnalysisTaskExecuter.java:35)
    at org.gradle.api.internal.tasks.execution.SkipUpToDateTaskExecuter.execute(SkipUpToDateTaskExecuter.java:64)
    at org.gradle.api.internal.tasks.execution.ValidatingTaskExecuter.execute(ValidatingTaskExecuter.java:58)
    at org.gradle.api.internal.tasks.execution.SkipEmptySourceFilesTaskExecuter.execute(SkipEmptySourceFilesTaskExecuter.java:42)
    at org.gradle.api.internal.tasks.execution.SkipTaskWithNoActionsExecuter.execute(SkipTaskWithNoActionsExecuter.java:52)
    at org.gradle.api.internal.tasks.execution.SkipOnlyIfTaskExecuter.execute(SkipOnlyIfTaskExecuter.java:53)
    at org.gradle.api.internal.tasks.execution.ExecuteAtMostOnceTaskExecuter.execute(ExecuteAtMostOnceTaskExecuter.java:43)
    at org.gradle.api.internal.AbstractTask.executeWithoutThrowingTaskFailure(AbstractTask.java:306)
    at org.gradle.execution.taskgraph.AbstractTaskPlanExecutor$TaskExecutorWorker.executeTask(AbstractTaskPlanExecutor.java:79)
    at org.gradle.execution.taskgraph.AbstractTaskPlanExecutor$TaskExecutorWorker.processTask(AbstractTaskPlanExecutor.java:63)
    at org.gradle.execution.taskgraph.AbstractTaskPlanExecutor$TaskExecutorWorker.run(AbstractTaskPlanExecutor.java:51)
    at org.gradle.execution.taskgraph.DefaultTaskPlanExecutor.process(DefaultTaskPlanExecutor.java:23)
    at org.gradle.execution.taskgraph.DefaultTaskGraphExecuter.execute(DefaultTaskGraphExecuter.java:88)
    at org.gradle.execution.SelectedTaskExecutionAction.execute(SelectedTaskExecutionAction.java:29)
    at org.gradle.execution.DefaultBuildExecuter.execute(DefaultBuildExecuter.java:62)
    at org.gradle.execution.DefaultBuildExecuter.access$200(DefaultBuildExecuter.java:23)
    at org.gradle.execution.DefaultBuildExecuter$2.proceed(DefaultBuildExecuter.java:68)
    at org.gradle.execution.DryRunBuildExecutionAction.execute(DryRunBuildExecutionAction.java:32)
    at org.gradle.execution.DefaultBuildExecuter.execute(DefaultBuildExecuter.java:62)
    at org.gradle.execution.DefaultBuildExecuter.execute(DefaultBuildExecuter.java:55)
    at org.gradle.initialization.DefaultGradleLauncher.doBuildStages(DefaultGradleLauncher.java:149)
    at org.gradle.initialization.DefaultGradleLauncher.doBuild(DefaultGradleLauncher.java:106)
    at org.gradle.initialization.DefaultGradleLauncher.run(DefaultGradleLauncher.java:86)
    at org.gradle.launcher.exec.InProcessBuildActionExecuter$DefaultBuildController.run(InProcessBuildActionExecuter.java:80)
    at org.gradle.launcher.cli.ExecuteBuildAction.run(ExecuteBuildAction.java:33)
    at org.gradle.launcher.cli.ExecuteBuildAction.run(ExecuteBuildAction.java:24)
    at org.gradle.launcher.exec.InProcessBuildActionExecuter.execute(InProcessBuildActionExecuter.java:36)
    at org.gradle.launcher.exec.InProcessBuildActionExecuter.execute(InProcessBuildActionExecuter.java:26)
    at org.gradle.launcher.cli.RunBuildAction.run(RunBuildAction.java:51)
    at org.gradle.internal.Actions$RunnableActionAdapter.execute(Actions.java:169)
    at org.gradle.launcher.cli.CommandLineActionFactory$ParseAndBuildAction.execute(CommandLineActionFactory.java:237)
    at org.gradle.launcher.cli.CommandLineActionFactory$ParseAndBuildAction.execute(CommandLineActionFactory.java:210)
    at org.gradle.launcher.cli.JavaRuntimeValidationAction.execute(JavaRuntimeValidationAction.java:35)
    at org.gradle.launcher.cli.JavaRuntimeValidationAction.execute(JavaRuntimeValidationAction.java:24)
    at org.gradle.launcher.cli.CommandLineActionFactory$WithLogging.execute(CommandLineActionFactory.java:206)
    at org.gradle.launcher.cli.CommandLineActionFactory$WithLogging.execute(CommandLineActionFactory.java:169)
    at org.gradle.launcher.cli.ExceptionReportingAction.execute(ExceptionReportingAction.java:33)
    at org.gradle.launcher.cli.ExceptionReportingAction.execute(ExceptionReportingAction.java:22)
    at org.gradle.launcher.Main.doAction(Main.java:33)
    at org.gradle.launcher.bootstrap.EntryPoint.run(EntryPoint.java:45)
    at org.gradle.launcher.bootstrap.ProcessBootstrap.runNoExit(ProcessBootstrap.java:54)
    at org.gradle.launcher.bootstrap.ProcessBootstrap.run(ProcessBootstrap.java:35)
    at org.gradle.launcher.GradleMain.main(GradleMain.java:23)
    at org.gradle.wrapper.BootstrapMainStarter.start(BootstrapMainStarter.java:30)
    at org.gradle.wrapper.WrapperExecutor.execute(WrapperExecutor.java:127)
    at org.gradle.wrapper.GradleWrapperMain.main(GradleWrapperMain.java:61)
Caused by: org.gradle.api.GradleException: Signature errors found. Verify them and ignore them with the proper annotation if needed.
    at be.insaneprogramming.gradle.animalsniffer.AnimalSnifferTask$_performAnimalSniffer_closure3.doCall(AnimalSnifferPlugin.groovy:115)
    at be.insaneprogramming.gradle.animalsniffer.AnimalSnifferTask.performAnimalSniffer(AnimalSnifferPlugin.groovy:104)
    at org.gradle.internal.reflect.JavaMethod.invoke(JavaMethod.java:63)
    at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$StandardTaskAction.doExecute(AnnotationProcessingTaskFactory.java:218)
    at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$StandardTaskAction.execute(AnnotationProcessingTaskFactory.java:211)
    at org.gradle.api.internal.project.taskfactory.AnnotationProcessingTaskFactory$StandardTaskAction.execute(AnnotationProcessingTaskFactory.java:200)
    at org.gradle.api.internal.AbstractTask$TaskActionWrapper.execute(AbstractTask.java:585)
    at org.gradle.api.internal.AbstractTask$TaskActionWrapper.execute(AbstractTask.java:568)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeAction(ExecuteActionsTaskExecuter.java:80)
    at org.gradle.api.internal.tasks.execution.ExecuteActionsTaskExecuter.executeActions(ExecuteActionsTaskExecuter.java:61)
    ... 47 more


BUILD FAILED
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/504
Netty throws exception when creating > 1 TLS transport. · Issue #504 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When attempting to create multiple TLS transports from the same builder, Netty throws an exception:
io.netty.channel.ChannelPipelineException: io.grpc.transport.netty.ProtocolNegotiators$SslBootstrapHandler is not a @Sharable handler, so can't be added or removed multiple times.
    at io.netty.channel.DefaultChannelPipeline.checkMultiplicity(DefaultChannelPipeline.java:564)
    at io.netty.channel.DefaultChannelPipeline.addFirst0(DefaultChannelPipeline.java:114)
    at io.netty.channel.DefaultChannelPipeline.addFirst(DefaultChannelPipeline.java:108)
    at io.netty.channel.DefaultChannelPipeline.addFirst(DefaultChannelPipeline.java:291)
    at io.netty.channel.DefaultChannelPipeline.addFirst(DefaultChannelPipeline.java:246)
    at io.grpc.transport.netty.ProtocolNegotiators$AbstractBufferingHandler.channelRegistered(ProtocolNegotiators.java:192)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelRegisteredNow(ChannelHandlerInvokerUtil.java:32)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRegistered(DefaultChannelHandlerInvoker.java:50)
    at io.netty.channel.AbstractChannelHandlerContext.fireChannelRegistered(AbstractChannelHandlerContext.java:114)
    at io.netty.channel.DefaultChannelPipeline.fireChannelRegistered(DefaultChannelPipeline.java:833)
    at io.netty.channel.AbstractChannel$AbstractUnsafe.register0(AbstractChannel.java:487)
    at io.netty.channel.AbstractChannel$AbstractUnsafe.access$100(AbstractChannel.java:401)
    at io.netty.channel.AbstractChannel$AbstractUnsafe$1.run(AbstractChannel.java:461)
    at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:322)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:356)
    at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
    at io.netty.util.concurrent.DefaultThreadFactory$DefaultRunnableDecorator.run(DefaultThreadFactory.java:137)
    at java.lang.Thread.run(Thread.java:745)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/505
Allowing Netty TLS bootstrap handler to be sharable. by nmittler · Pull Request #505 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/506
Move BufferingHttp2ConnectionEncoder upstream to Netty · Issue #506 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
BufferingHttp2ConnectionEncoder is solving a relatively generic use case.  I would like to explore the possibility of this class being extracted out of gRPC and contributed upstream to Netty.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/507
Blocking stub don't throw StatusRuntimeException · Issue #507 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Instead, it throws RuntimeExecutionException with a StatusRuntimeException as a cause. Is that what we want?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/508
Adding default User-Agent for netty and okhttp. by nmittler · Pull Request #508 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/509
Rename Call to ClientCall by zhangkun83 · Pull Request #509 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 @ejona86 I'm wondering if we should hold off on this until the dust settles from Wolfgang's API work ... I suspect some of this might change again as a result.  WDYT?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/510
Introduce support for calls as composable objects · Issue #510 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Let's suppose we call it "Callable" (actual name may differ), and it is related to Call as is f.i. Iterable to Iterator, or Observable to Observer in the Rx pattern.
The basic contract would be:
class Callable<I, O> {
   abstract Call<I, O> newCall(Channel ch);
}

Basic creation operations for Callable would be:
static Callable<I, O> create(MethodDescriptor<I, O> method);
static Callable<I, O> create(BiFunction<I, O> function);

Sequential composition would be supported, as well as various ways to parallelize execution:
<Q> Callable<I, Q> followedBy(Callable<O, Q> second);
Callable<List<I>, List<O>> inParallel();
...

Building blocks for dealing with API programming patterns would be supported:
Callable<I, O> retrying(RetryOptions options);
<R> Callable<I,R> paging(Class<R> resourceType, PagingOptions options);

Additional scenarios which might be supported by callables or related means:

Resource modification (Read-Modify-Write cycle), with conditions
Media upload and download
Long running operations
PubSub
Conversion to/from Rx and to/from Java 8 streams (no need to reinvent the wheel here. If someone wants to do processing of responses or produce requests, those frameworks should have everything)
...
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/511
Consolidate Method descriptor classes · Issue #511 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Now we have three classes for representing a method: MethodDescriptor, ServerMethodDefinition, Method. They all have the method name and marshallers. We list their differences below:

MethodDescriptor is used on client when making a call. It has options and MethodType (unary, streaming etc)
Method passes information from IDL to the runtime. It has MethodType.
ServerMethodDefinition is used on server for a registered method. It has the ServerCallHandler.

Their content overlap a lot. They should be consolidated. Here is the plan:

Make it clear that MethodDescriptor is a static representation of the method definition from IDL. It will be used on both client-side and server-side.
Change ServerMethodDefinition to contain a MethodDescriptor
Delete Method. Use MethodDescriptor to pass information from IDL.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/512
Enable Travis for all branches by ejona86 · Pull Request #512 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/513
Upgrade to protobuf-3.0.0-alpha-3 by zhangkun83 · Pull Request #513 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83, LGTM.
Nice finding so many places that reference the old version :).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/514
Document how to copy credentials for docker by zhangkun83 · Pull Request #514 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM ... I'll assume it works :)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/515
Support for custom status codes · Issue #515 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
io.grpc.Status seems to be restricted to the built-in status codes provided, although javadoc suggests that new status codes can be used as long as they are not conflicting. Adding a factory method such as "Status.forCode" should be possible although this would require that the status code type be changed from an enum to integer constant. This may be a small price to pay for the added flexibility.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/516
Excessive logging of Status{Runtime}Exception in server · Issue #516 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If a service throws Status{Runtime}Exception it gets logged regardless of error class. There should probably be a distinction between "client" errors such as NOT_FOUND, INVALID_ARGUMENT which should not be logged (or at least not as FATAL) and other server errors (INTERNAL, UNKNOWN, etc) similar to how HTTP errors are categorized.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/517
"WARN java.lang.IllegalStateException: Refcount has already reached zero" during shutdown · Issue #517 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We are frequently seeing this exception during server shutdown but not in all cases. I did a little digging and it looks like the SharedResourceHolder on DEFAULT_EXECUTOR is being called twice in ServerImpl.java: once when transportClosed() is called and again in serverShutdown(). Looks like serverShutdown() first shuts down all transports, so perhaps this is what is triggering the call to transportClosed() before it attempts to release the holder again for a second time.
Thanks,
David
INFO  [2015-06-07 21:52:09,390] org.eclipse.jetty.server.handler.ContextHandler: Stopped i.d.j.MutableServletContextHandler@21bd20ee{/,null,UNAVAILABLE}
WARN  [2015-06-07 21:52:09,400] io.netty.util.concurrent.DefaultPromise: An exception was thrown by io.grpc.transport.netty.NettyServer$2.operationComplete()
! java.lang.IllegalStateException: Refcount has already reached zero
! at com.google.common.base.Preconditions.checkState(Preconditions.java:173) ~[guava-18.0.jar:na]
! at io.grpc.SharedResourceHolder.releaseInternal(SharedResourceHolder.java:147) ~[grpc-core-0.8.0-SNAPSHOT.jar:na]
! at io.grpc.SharedResourceHolder.release(SharedResourceHolder.java:115) ~[grpc-core-0.8.0-SNAPSHOT.jar:na]
! at io.grpc.AbstractServerBuilder$1.run(AbstractServerBuilder.java:120) ~[grpc-core-0.8.0-SNAPSHOT.jar:na]
! at io.grpc.ServerImpl.checkForTermination(ServerImpl.java:204) ~[grpc-core-0.8.0-SNAPSHOT.jar:na]
! at io.grpc.ServerImpl.access$300(ServerImpl.java:64) ~[grpc-core-0.8.0-SNAPSHOT.jar:na]
! at io.grpc.ServerImpl$ServerListenerImpl.serverShutdown(ServerImpl.java:227) ~[grpc-core-0.8.0-SNAPSHOT.jar:na]
! at io.grpc.transport.netty.NettyServer$2.operationComplete(NettyServer.java:140) ~[grpc-netty-0.8.0-SNAPSHOT.jar:na]
! at io.grpc.transport.netty.NettyServer$2.operationComplete(NettyServer.java:134) ~[grpc-netty-0.8.0-SNAPSHOT.jar:na]
! at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680) ~[netty-common-4.1.0.Beta5.jar:4.1.0.Beta5]
! at io.netty.util.concurrent.DefaultPromise$LateListeners.run(DefaultPromise.java:845) [netty-common-4.1.0.Beta5.jar:4.1.0.Beta5]
! at io.netty.util.concurrent.DefaultPromise$LateListenerNotifier.run(DefaultPromise.java:873) [netty-common-4.1.0.Beta5.jar:4.1.0.Beta5]
! at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:322) [netty-common-4.1.0.Beta5.jar:4.1.0.Beta5]
! at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:356) [netty-transport-4.1.0.Beta5.jar:4.1.0.Beta5]
! at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703) [netty-common-4.1.0.Beta5.jar:4.1.0.Beta5]
! at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142) [na:1.8.0_45]
! at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617) [na:1.8.0_45]
! at java.lang.Thread.run(Thread.java:745) [na:1.8.0_45]
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

https://github.com/grpc/grpc-java/issues/519
Reorganizing the deployment docs. by nmittler · Pull Request #519 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 @zhangkun83 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/520
Add ALPN setting path for Android older than 5.0 · Issue #520 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
OkHttp only support setting ALPN on Android 5.0+ since 2.3
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/521
Support setting ALPN for Android older than 5.0, OkHttp(2.3+) impleme… by madongfly · Pull Request #521 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can you please provide more description as to what is different about this code and what was being done previously.
Does this support using jetty_alpn?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/522
Netty Client does not detect when ALPN was not used · Issue #522 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When I tried to reproduce the APLN silence failure, I expected the following change fails our tests, but not, all tests still passed.
diff --git a/interop-testing/src/test/java/io/grpc/testing/integration/Http2NettyTest.java b/interop-testing/src/test/java/io/grpc/testing/integration/Http2NettyTest.java
index 504c815..2ae8160 100644
--- a/interop-testing/src/test/java/io/grpc/testing/integration/Http2NettyTest.java
+++ b/interop-testing/src/test/java/io/grpc/testing/integration/Http2NettyTest.java
@@ -37,6 +37,7 @@ import io.grpc.transport.netty.GrpcSslContexts;
 import io.grpc.transport.netty.NettyChannelBuilder;
 import io.grpc.transport.netty.NettyServerBuilder;

+import io.netty.handler.ssl.ApplicationProtocolConfig;
 import org.junit.AfterClass;
 import org.junit.BeforeClass;
 import org.junit.runner.RunWith;
@@ -74,7 +75,8 @@ public class Http2NettyTest extends AbstractTransportTest {
       return NettyChannelBuilder
           .forAddress(TestUtils.testServerAddress(serverPort))
           .sslContext(GrpcSslContexts.forClient().trustManager(
-                  TestUtils.loadCert("ca.pem")).build())
+                  TestUtils.loadCert("ca.pem"))
+              .applicationProtocolConfig(ApplicationProtocolConfig.DISABLED).build())
           .build();
     } catch (Exception ex) {
       throw new RuntimeException(ex);

The problem itself is not a big deal, but investigating it may expose some hidden bugs.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/523
Allow specification of open-loop vs closed-loop test in qpstest.proto · Issue #523 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi there,
As we move toward interoperable QPS testing, please allow the ClientConfig in qpstest.proto specify the type of load to deliver. I would suggest that you support variable open-loop request arrival processes as in https://github.com/grpc/grpc/tree/master/test/cpp/qps , but ultimately Poisson process is the most important.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/524
Allow specification of open-loop vs closed-loop test in qpstest.proto · Issue #524 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi there,
As we move toward interoperable QPS testing, please allow the ClientConfig in qpstest.proto specify the type of load to deliver. I would suggest that you support variable open-loop request arrival processes as in https://github.com/grpc/grpc/tree/master/test/cpp/qps , but ultimately Poisson process is the most important.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/525
Support NPN with Netty · Issue #525 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It isn't useful for jetty_alpn, but when using OpenSsl, using ALPN_AND_NPN in the netty application negotiation config allows us to support more platforms without needing users to install OpenSSL.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/526
Support NPN on Android when Play Services Security Provider (PSSP) not available · Issue #526 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Attempts and their fallbacks:

If installed, use PSSP with ALPN and NPN
If on Android 5.0 or later, use ALPN and NPN
If on Android 4.1 or later, use NPN
Fail or let the application author install some alternative security provider (e.g., build and ship Conscrypt themselves)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/527
Verify Protocol Negotiation completed · Issue #527 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It seems if neither ALPN nor NPN occur/available we just happily continue connecting and think that negotiation occurred. We should instead check that the protocol negotiated and fail if it didn't.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/528
Properly set inbound and outbound connection and stream window sizes by louiscryan · Pull Request #528 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/529
Cleanup io.grpc package · Issue #529 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Rename DeferredInputStream as it doesn't necessarily have to be deferred.  Consider making it an interface.
 Move SharedResourceHolder into transport
 SerializingExecutor into transport
 Rename KnownLength
 Add available method with documentation to KnownLength
 Move MethodType into MethodDescriptor
 Move Marshaller into MethodDescriptor
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/530
Add the Android interop test App. by madongfly · Pull Request #530 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We should use the same gradlew as in the root of the project. Just do ../gradlew instead of ./gradlew
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/531
ClientAuthInterceptor's ctor requires an Executor, but never use it. · Issue #531 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/532
Changing Netty handlers to properly set initialSettings. by nmittler · Pull Request #532 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/533
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/534
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/535
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/536
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/537
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/538
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/539
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/540
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/541
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/542
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/543
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/544
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/545
Make Channel hierarchy more meaningful · Issue #545 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@nmittler wrote on issue 64:

I think the problem here is that the term "channel" ~= "transport", but "interceptor" != "transport". I think it would be better to provide a more abstract interface that is responsible for creating calls and then all of these "things" would implement/extend that. Something like this:
interface CallFactory {
   Call newCall(MethodDescriptor method);
}
class MyInterceptor implements CallFactory {
    ...
}
interface Channel extends CallFactory {
    ...
    void shutdown();
}
class ChannelImpl implements Channel {
    ...
}

Discussion continued further. This issue is for these class renames/additions.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/546
Throw error for Netty when Jetty ALPN not configured. by nmittler · Pull Request #546 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/547
Recommend tcnative instead of jetty-alpn-boot · Issue #547 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We need to make sure there are builds of tcnative for Debian-compatible OpenSSL, first though.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/548
Have different abstract base types for each stub type; use it instead of Calls · Issue #548 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently, channel (and soon, callOptions) are defined in AbstractStub, but the generated code uses them. It could be a good idea to have abstract base types for each stub type that uses channel so that the generated code doesn't.
This also moves the call of Channel.newCall into non-generated code. In all, this should have the generate code hard-code fewer things.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/549
Update Travis to use protobuf3-alpha3 by ejona86 · Pull Request #549 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/550
Backport the supporting of ALPN on Android older than 5.0. by madongfly · Pull Request #550 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Did you have to do any manual merging?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/551
Some cleanup for okhttp: by madongfly · Pull Request #551 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/552
Use exit() for integration test client by ejona86 · Pull Request #552 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/553
Make ChannelImpl.obtainActiveTransport's fast path lock-free by ejona86 · Pull Request #553 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/554
Blocking calls should error with StatusRuntimeException by ejona86 · Pull Request #554 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/555
Make the code clearer, fixes #531. by madongfly · Pull Request #555 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/556
Add instructions for setting up traffic shaping on loopback by louiscryan · Pull Request #556 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ctiller fyi
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/557
Migrate Windows Jenkins-based testing to grpc-testing · Issue #557 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The Jenkins host we set things up on is going away. We should migrate the setup to the grpc-testing project.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/558
Using grpc with TLS · Issue #558 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello,
I'm working on grpc in android, and I want to use a self signed certificate.
OkHttpChannelBuilder.forAddress(mHost, mPort)
.sslSocketFactory(TestUtils.getSslSocketFactoryForCertainCert(TestUtils.loadCert("my_cert")))
.build();

But when I want to send request, a exception of type io.grpc.StatusRuntimeException is throw.
It's the good way to initialise TLS in grpc ?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/559
In compiler documentation, use grpc-java as plugin name by ejona86 · Pull Request #559 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/560
Rename getSslSocketFactoryForCertainCert to be more clear what cert is provided · Issue #560 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It isn't clear that the File should point to a CA certificate. It should be renamed to be clear.
createSslSocketFactoryWithCa or newSslSocketFactoryForCa or similar.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/561
Exposing AbstractBufferingHandler so it can be used by custom protoco… by nmittler · Pull Request #561 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/562
Initial context API by louiscryan · Pull Request #562 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/563
Use 1MB as the max payload size in benchmarks by louiscryan · Pull Request #563 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/564
Revert swapping to the "canonical HTTP mapping" by ejona86 · Pull Request #564 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/565
Ignore initial HEADERS with a 1xx :status · Issue #565 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Headers with a 1xx status code in HTTP/1.1 are supposed to be ignored. In HTTP/2, there is a clear example of their usage.
I don't think 1xx status codes are all that important/common, but we should follow the spec.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/566
Rename getSslSocketFactoryForCertainCert to be newSslSocketFactoryForCa. by madongfly · Pull Request #566 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Why are we bothering to deprecate a method name in a testing utility?  This seems like overkill.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/567
Update usage of deprecated API, and add back two accidentally removed blank lines. by madongfly · Pull Request #567 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/568
ChannelImpl's constructor shouldn't be public · Issue #568 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ChannelImpl is really expected to be constructed from AbstractChannelBuilder. Using the builder allows us to more easily change the arguments as time goes on.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/569
Stop using intrinsic locks in ChannelImpl/ServerImpl · Issue #569 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I originally used intrinsic locks for expediency. We were still designing quite a bit and we were still using Service. It seems swapping away from intrinsic locks makes sense, as we have no want/need to allow users to compose method calls into higher-order atomic calls.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/570
Are Interceptors are executed in an unintuitive order? · Issue #570 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
// interceptor1 is run before interceptor2
ClientInterceptors.intercept(channel, interceptor1, interceptor2);

// interceptor2 is run before interceptor1
channel = ClientInterceptors.intercept(channel, interceptor1);
channel = ClientInterceptors.intercept(channel, interceptor2);

This seems like it would get really confusing if you call intercept multiple times with multiple interceptors each time:
channel = ClientInterceptors.intercept(channel, interceptor2,
                                                interceptor1);
channel = ClientInterceptors.intercept(channel, interceptor4,
                                                interceptor3);

It seems the first interceptor listed should most likely be the interceptor nearest the library. If there was a single mutable interceptor list then the current behavior would make more sense.
Note that on server-side the application and library are reversed, so reversing the order would make the first interceptor nearest the application.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/571
Refactor OkHttpProtocolNegotiator, move Android related operations into an inner class. by madongfly · Pull Request #571 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/572
ServerServiceDefinition.getMethods should return a Collection · Issue #572 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Right now it has a return type of ImmutableList, which 1) requires a specific Guava implementation and 2) there is no need for order of the methods. For instance, in the current implementation we could use methodLookup.values().
Note that having "Collection" as the return type but actually returning an ImmutableList is fine though.
I could be convinced that returning a List or Set is appropriate, but if we return Collection now we could actually change to using a List or Set in the future and remain API compatible (since the class is final).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/573
The generated Service.methods() should return a Collection · Issue #573 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For similar reasoning to #572. Just limiting our API surface.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/574
Add CallOptions. by zhangkun83 · Pull Request #574 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/575
Maven plugin instructions are incomplete · Issue #575 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The build instructions do not seem to work.  The maven-protoc-plugin is neither in Maven Central nor does it appear to be in the Sonatype snapshot repository.  Which repository should we use?
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

https://github.com/grpc/grpc-java/issues/579
Use hostname instead of InetAddress for Socket creation. by zsurocking · Pull Request #579 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.  It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA).
📝 Please visit https://cla.developers.google.com/ to sign.
Once you've signed, please reply here (e.g. I signed it!) and we'll verify.  Thanks.


If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check your existing CLA data and verify that your email is set on your git commits.
If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/580
For demonstration purpose, will be closed after discussion. by madongfly · Pull Request #580 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/581
Error zero_copy_stream.h file not found during ./gradlew installDists · Issue #581 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When running ./gradlew installDists I receive the following error message:
In file included from /Users/me/projects/grpc-java/compiler/src/java_plugin/cpp/java_generator.cpp:1:
/Users/Sven.Bendel/projects/grpc-java/compiler/src/java_plugin/cpp/java_generator.h:8:10: fatal error: 'google/protobuf/io/zero_copy_stream.h' file not found
#include <google/protobuf/io/zero_copy_stream.h>
         ^

Am I missing something? I am just trying to get the example server up and running via run-test-server.sh.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/582
Simplifying flow control window config for Netty. by nmittler · Pull Request #582 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/583
OkHttp's cancellation is not properly synchronized · Issue #583 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
OkHttpClientStream.sendCancel() calls finishStream() from an application thread. But finishStream() calls transportReportStatus() without any lock held. That is not synchronized correctly, as transportReportStatus() may only be called from the transport thread (i.e., while lock is held).
It seems that all usages of streams is done while lock is held except for within finishStream() and data(). data() can actually race with finishStream() and end up sending DATA frames after the RST_STREAM. It seems it would be best to just have stream protected by lock, because it having its own synchronization isn't providing much benefit and isn't leading to correct code.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/584
Set inboundPhase() when receiving trailers. by nmittler · Pull Request #584 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL ... this is an easy one ;)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/585
Adding handling for stream exhaustion in Netty. by nmittler · Pull Request #585 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/586
Use default type of KeyStore in Android interop test App, so that it can work on lower versions. by madongfly · Pull Request #586 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 Please take a look, thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/587
Migrate from PARSER to parser() as a way of getting the parser of a protobuf message. by zhangkun83 · Pull Request #587 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM. Thanks!
We have the version a lot of places...
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/588
Add the bintray repository for Maven protoc-plugin in the example by zhangkun83 · Pull Request #588 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/589
Add an option to Android interop test. by madongfly · Pull Request #589 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/590
Closing stream buffering encoder when inactive by nmittler · Pull Request #590 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
@Scottmitch @buchgr you may be interested as well, since I'd like to make the same changes to Netty's encoder.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/591
Support NPN fallback for Android. by madongfly · Pull Request #591 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/592
Suggest -PskipCodegen in run-test-{client,server} by ejona86 · Pull Request #592 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/593
Minor fixes by ejona86 · Pull Request #593 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Assigning to @zhangkun83 since these fix some warnings that showed up internally.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/594
benchmark/ has two README.md's · Issue #594 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The readme at "benchmarks/src/jmh/java/io/grpc/benchmarks/netty/README.md" is in the java source directory, which seems a poor place for a readme. It should be integrated into the README.md at "benchmarks/README.md"
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/595
Fix the potential deadlock. by madongfly · Pull Request #595 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/596
Fake infinite timeout; 1s is not a good hard-coded timeout by ejona86 · Pull Request #596 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/597
Improve Exception backtrace for blocked streaming by ejona86 · Pull Request #597 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/598
Memory leaking when using ALPN · Issue #598 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We're experiencing a slow memory leak with 0.7.1 when using ALPN and TLS. The server is built and started with this code :
NettyServerBuilder builder = NettyServerBuilder.forPort(port);
definitions.forEach(builder::addService);
SslContext context = SslContextBuilder.forServer(keyCertPathprivateKeyPath).build();
builder.sslContext(context);
ServerImpl server = builder.build();
server.start();

This is the alpn version that we're using.
-Xbootclasspath/p:/usr/lib/java/alpn-boot-8.1.3.v20150130.jar"
Running a heap dump, we're seeing a huge amount of SSLEngineImpl objects stored in a concurrent hash map :

The server is running behind a Amazon ELB. This might be related since the Amazon load balancer would open connections every once in a while to the server and to ping and make sure the server is live. Unfortunately it takes a long time to replicate, the server would run out of memory after 36 hours or so, but it doesn't seem like the number of requests
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/599
Android interop test: Use proto plugin to generate the needed code. by madongfly · Pull Request #599 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am going to push the protobuf-gradle-plugin to Maven Central today, so that you can depend on it.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/600
Set hard-coded deadline to just under 1 year by ejona86 · Pull Request #600 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/601
Fixing leak of SSLEngine for Jetty ALPN/NPN servers by nmittler · Pull Request #601 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/602
Error message when connecting with TLS to closed port unhelpful · Issue #602 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When I connect to a random port that is not open, the error message is not helpful.
$ ./run-test-client.sh --server_port=1234
Gradle is no longer run automatically. Make sure to run
'./gradlew installDist -PskipCodegen=true' or
'./gradlew :grpc-interop-testing:installDist -PskipCodegen' after any changes.
-PskipCodegen=true is optional, but requires less setup.
Running test empty_unary
Jul 07, 2015 11:02:03 AM io.grpc.transport.netty.ProtocolNegotiators$AbstractBufferingHandler fail
SEVERE: Transport failed during protocol negotiation
io.grpc.StatusRuntimeException: UNAVAILABLE: Channel closed while performing protocol negotiation
    at io.grpc.Status.asRuntimeException(Status.java:428)
    at io.grpc.transport.netty.ProtocolNegotiators.unavailableException(ProtocolNegotiators.java:175)
    at io.grpc.transport.netty.ProtocolNegotiators.access$000(ProtocolNegotiators.java:72)
    at io.grpc.transport.netty.ProtocolNegotiators$AbstractBufferingHandler.close(ProtocolNegotiators.java:261)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeCloseNow(ChannelHandlerInvokerUtil.java:133)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeClose(DefaultChannelHandlerInvoker.java:276)
    at io.netty.channel.AbstractChannelHandlerContext.close(AbstractChannelHandlerContext.java:238)
    at io.netty.channel.AbstractChannelHandlerContext.close(AbstractChannelHandlerContext.java:197)
    at io.netty.channel.DefaultChannelPipeline.close(DefaultChannelPipeline.java:987)
    at io.netty.channel.AbstractChannel.close(AbstractChannel.java:200)
    at io.netty.channel.ChannelFutureListener$2.operationComplete(ChannelFutureListener.java:56)
    at io.netty.channel.ChannelFutureListener$2.operationComplete(ChannelFutureListener.java:52)
    at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
    at io.netty.util.concurrent.DefaultPromise.notifyListeners0(DefaultPromise.java:603)
    at io.netty.util.concurrent.DefaultPromise.notifyListeners(DefaultPromise.java:563)
    at io.netty.util.concurrent.DefaultPromise.tryFailure(DefaultPromise.java:424)
    at io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.fulfillConnectPromise(AbstractNioChannel.java:276)
    at io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.finishConnect(AbstractNioChannel.java:292)
    at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:527)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:467)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:381)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:353)
    at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
    at java.lang.Thread.run(Thread.java:745)

Exception in thread "main" io.grpc.StatusRuntimeException: UNKNOWN
    at io.grpc.Status.asRuntimeException(Status.java:428)
    at io.grpc.stub.ClientCalls.getUnchecked(ClientCalls.java:105)
    at io.grpc.stub.ClientCalls.blockingUnaryCall(ClientCalls.java:115)
    at io.grpc.testing.integration.TestServiceGrpc$TestServiceBlockingStub.emptyCall(TestServiceGrpc.java:257)
    at io.grpc.testing.integration.AbstractTransportTest.emptyUnary(AbstractTransportTest.java:148)
    at io.grpc.testing.integration.TestServiceClient.runTest(TestServiceClient.java:203)
    at io.grpc.testing.integration.TestServiceClient.run(TestServiceClient.java:192)
    at io.grpc.testing.integration.TestServiceClient.main(TestServiceClient.java:79)
Caused by: io.netty.channel.ChannelException: Pending write on removal of SslHandler
    at io.netty.handler.ssl.SslHandler.handlerRemoved0(SslHandler.java:411)
    at io.netty.handler.codec.ByteToMessageDecoder.handlerRemoved(ByteToMessageDecoder.java:209)
    at io.netty.channel.DefaultChannelPipeline.callHandlerRemoved0(DefaultChannelPipeline.java:627)
    at io.netty.channel.DefaultChannelPipeline.callHandlerRemoved(DefaultChannelPipeline.java:621)
    at io.netty.channel.DefaultChannelPipeline.remove0(DefaultChannelPipeline.java:450)
    at io.netty.channel.DefaultChannelPipeline.destroyDown(DefaultChannelPipeline.java:898)
    at io.netty.channel.DefaultChannelPipeline.destroyUp(DefaultChannelPipeline.java:867)
    at io.netty.channel.DefaultChannelPipeline.destroy(DefaultChannelPipeline.java:859)
    at io.netty.channel.DefaultChannelPipeline.fireChannelUnregistered(DefaultChannelPipeline.java:843)
    at io.netty.channel.AbstractChannel$AbstractUnsafe$8.run(AbstractChannel.java:696)
    at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:322)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:356)
    at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
    at java.lang.Thread.run(Thread.java:745)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/603
Remove Method and switch its users to MethodDescriptor. by zhangkun83 · Pull Request #603 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/604
Upgrade to protobuf-gradle-plugin 0.5.0 by zhangkun83 · Pull Request #604 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
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

https://github.com/grpc/grpc-java/issues/606
Improve docs to describe close as being last method called by ejona86 · Pull Request #606 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/607
Metadata.Key's name is non-null; don't check for null by ejona86 · Pull Request #607 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/608
Make sure error status codes are consistent with other implementations · Issue #608 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/609
Implement proper reconnection · Issue #609 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Implies exponential backoff, etc.
https://github.com/grpc/grpc/blob/master/doc/connection-backoff.md
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/610
Fixing some compiler warnings. by nmittler · Pull Request #610 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 should be an easy one :)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/611
Try to simplify server method definition by carl-mastrangelo · Pull Request #611 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/612
Change AbstractServiceDescriptor.methods() to return Collection by zhangkun83 · Pull Request #612 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/613
Sync Android branch to the HEAD. by madongfly · Pull Request #613 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We found a Contributor License Agreement for you (the sender of this pull request), but were unable to find agreements for the commit author(s).  If you authored these, maybe you used a different email address in the git commits than was used to sign the CLA (login here to double check)?  If these were authored by someone else, then they will need to sign a CLA as well, and confirm that they're okay with these being contributed to Google.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/614
go-java interop test fails in large_unary and client_streaming · Issue #614 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The breakage started somewhere between 2015-07-07 and 2015-07-09. Commit efbb655 is likely the trigger. The bug is only in TLS test cases.
To reproduce:
Start Java server:
$ git clone git@github.com:grpc/grpc-java.git
$ cd grpc-java
$ ./gradlew grpc-interop-testing:installDist -PskipCodegen=true
$ ./run-test-server.sh

Start the go client in docker.
$ git clone git@github.com:grpc/grpc-docker-library.git
$ cd grpc-docker-library
$ touch grpc_go/service_account
$ docker build -t grpc/go grpc_go
$ docker run --rm=true -it grpc/go /go/bin/client -server_host_override=foo.test.google.fr \
-tls_ca_file="/go/src/google.golang.org/grpc/test/testdata/ca.pem" -test_case=large_unary \
-server_port=8080 -server_host=10.0.42.1 -use_tls=true

The client fails with
/TestService/UnaryCall RPC failed: rpc error: code = 2 desc = ""

The server prints out this error:
Jul 09, 2015 4:33:17 PM io.grpc.transport.netty.NettyServerHandler onStreamError
WARNING: Stream Error
io.netty.handler.codec.http2.Http2Exception$StreamException: Flow control window exceeded for stream: 1
        at io.netty.handler.codec.http2.Http2Exception.streamError(Http2Exception.java:100)
        at io.netty.handler.codec.http2.DefaultHttp2LocalFlowController$DefaultState.receiveFlowControlledFrame(DefaultHttp2LocalFlowController.java:365)
        at io.netty.handler.codec.http2.DefaultHttp2LocalFlowController.receiveFlowControlledFrame(DefaultHttp2LocalFlowController.java:239)
        at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder$FrameReadListener.onDataRead(DefaultHttp2ConnectionDecoder.java:223)
        at io.netty.handler.codec.http2.Http2InboundFrameLogger$1.onDataRead(Http2InboundFrameLogger.java:46)
        at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readDataFrame(DefaultHttp2FrameReader.java:392)
        at io.netty.handler.codec.http2.DefaultHttp2FrameReader.processPayloadState(DefaultHttp2FrameReader.java:223)
        at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readFrame(DefaultHttp2FrameReader.java:130)
        at io.netty.handler.codec.http2.Http2InboundFrameLogger.readFrame(Http2InboundFrameLogger.java:39)
        at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder.decodeFrame(DefaultHttp2ConnectionDecoder.java:100)
        at io.netty.handler.codec.http2.Http2ConnectionHandler$FrameDecoder.decode(Http2ConnectionHandler.java:293)
        at io.netty.handler.codec.http2.Http2ConnectionHandler.decode(Http2ConnectionHandler.java:336)
        at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
        at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
        at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
        at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
        at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
        at io.netty.handler.ssl.SslHandler.unwrap(SslHandler.java:1069)
        at io.netty.handler.ssl.SslHandler.decode(SslHandler.java:939)
        at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
        at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
        at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
        at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
        at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
        at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:946)
        at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:127)
        at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:510)
        at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:467)
        at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:381)
        at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:353)
        at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
        at java.lang.Thread.run(Thread.java:745)

@ejona86 @nmittler
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/615
May need to tweak ordering of `complete()` and `close()` · Issue #615 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We shouldn't be getting the "successful complete() without close()" exception. It seems it is caused by another exception and us not cleaning up the stream well.
It isn't the point of this issue to fix the "flow control window exceeded" exception. That is being investigated elsewhere.
Jul 09, 2015 4:11:07 PM io.grpc.transport.netty.NettyServerHandler onStreamError
WARNING: Stream Error
io.netty.handler.codec.http2.Http2Exception$StreamException: Flow control window exceeded for stream: 1
    at io.netty.handler.codec.http2.Http2Exception.streamError(Http2Exception.java:100)
    at io.netty.handler.codec.http2.DefaultHttp2LocalFlowController$DefaultState.receiveFlowControlledFrame(DefaultHttp2LocalFlowController.java:365)
    at io.netty.handler.codec.http2.DefaultHttp2LocalFlowController.receiveFlowControlledFrame(DefaultHttp2LocalFlowController.java:239)
    at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder$FrameReadListener.onDataRead(DefaultHttp2ConnectionDecoder.java:223)
    at io.netty.handler.codec.http2.Http2InboundFrameLogger$1.onDataRead(Http2InboundFrameLogger.java:46)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readDataFrame(DefaultHttp2FrameReader.java:392)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader.processPayloadState(DefaultHttp2FrameReader.java:223)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readFrame(DefaultHttp2FrameReader.java:130)
    at io.netty.handler.codec.http2.Http2InboundFrameLogger.readFrame(Http2InboundFrameLogger.java:39)
    at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder.decodeFrame(DefaultHttp2ConnectionDecoder.java:100)
    at io.netty.handler.codec.http2.Http2ConnectionHandler$FrameDecoder.decode(Http2ConnectionHandler.java:293)
    at io.netty.handler.codec.http2.Http2ConnectionHandler.decode(Http2ConnectionHandler.java:336)
    at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
    at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
    at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
    at io.netty.handler.ssl.SslHandler.unwrap(SslHandler.java:1069)
    at io.netty.handler.ssl.SslHandler.decode(SslHandler.java:939)
    at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
    at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
    at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
    at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:946)
    at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:127)
    at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:510)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:467)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:381)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:353)
    at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
    at java.lang.Thread.run(Thread.java:745)

Jul 09, 2015 4:11:07 PM io.netty.util.concurrent.DefaultPromise notifyListener0
WARNING: An exception was thrown by io.grpc.transport.netty.NettyServerHandler$2.operationComplete()
java.lang.IllegalStateException: successful complete() without close()
    at io.grpc.transport.AbstractServerStream.complete(AbstractServerStream.java:198)
    at io.grpc.transport.netty.NettyServerHandler$2.operationComplete(NettyServerHandler.java:262)
    at io.grpc.transport.netty.NettyServerHandler$2.operationComplete(NettyServerHandler.java:259)
    at io.netty.util.concurrent.DefaultPromise.notifyListener0(DefaultPromise.java:680)
    at io.netty.util.concurrent.DefaultPromise.notifyListeners0(DefaultPromise.java:603)
    at io.netty.util.concurrent.DefaultPromise.notifyListeners(DefaultPromise.java:563)
    at io.netty.util.concurrent.DefaultPromise.trySuccess(DefaultPromise.java:406)
    at io.netty.handler.codec.http2.Http2CodecUtil$SimpleChannelPromiseAggregator.trySuccess(Http2CodecUtil.java:288)
    at io.netty.handler.codec.http2.Http2CodecUtil$SimpleChannelPromiseAggregator.trySuccess(Http2CodecUtil.java:192)
    at io.netty.channel.DefaultChannelPromise.trySuccess(DefaultChannelPromise.java:82)
    at io.netty.channel.ChannelOutboundBuffer.safeSuccess(ChannelOutboundBuffer.java:644)
    at io.netty.channel.ChannelOutboundBuffer.remove(ChannelOutboundBuffer.java:260)
    at io.netty.channel.ChannelOutboundBuffer.removeBytes(ChannelOutboundBuffer.java:339)
    at io.netty.channel.socket.nio.NioSocketChannel.doWrite(NioSocketChannel.java:318)
    at io.netty.channel.AbstractChannel$AbstractUnsafe.flush0(AbstractChannel.java:799)
    at io.netty.channel.nio.AbstractNioChannel$AbstractNioUnsafe.flush0(AbstractNioChannel.java:311)
    at io.netty.channel.AbstractChannel$AbstractUnsafe.flush(AbstractChannel.java:766)
    at io.netty.channel.DefaultChannelPipeline$HeadContext.flush(DefaultChannelPipeline.java:1234)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeFlushNow(ChannelHandlerInvokerUtil.java:165)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeFlush(DefaultChannelHandlerInvoker.java:355)
    at io.netty.channel.AbstractChannelHandlerContext.flush(AbstractChannelHandlerContext.java:272)
    at io.netty.handler.ssl.SslHandler.flush(SslHandler.java:478)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeFlushNow(ChannelHandlerInvokerUtil.java:165)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeFlush(DefaultChannelHandlerInvoker.java:355)
    at io.netty.channel.AbstractChannelHandlerContext.flush(AbstractChannelHandlerContext.java:272)
    at io.netty.handler.codec.http2.Http2ConnectionHandler.flush(Http2ConnectionHandler.java:392)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeFlushNow(ChannelHandlerInvokerUtil.java:165)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeFlush(DefaultChannelHandlerInvoker.java:355)
    at io.netty.channel.AbstractChannelHandlerContext.flush(AbstractChannelHandlerContext.java:272)
    at io.netty.channel.DefaultChannelPipeline.flush(DefaultChannelPipeline.java:997)
    at io.netty.channel.AbstractChannel.flush(AbstractChannel.java:210)
    at io.grpc.transport.netty.WriteQueue.flush(WriteQueue.java:131)
    at io.grpc.transport.netty.WriteQueue.access$000(WriteQueue.java:48)
    at io.grpc.transport.netty.WriteQueue$1.run(WriteQueue.java:58)
    at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:322)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:356)
    at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
    at java.lang.Thread.run(Thread.java:745)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/616
During shutdown, Netty should gracefully wait for RPCs to complete before terminating the connection · Issue #616 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently it is just calling "channel.close();" which brings down the TCP connection and cleans up all the RPCs.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/617
Recommended IntelliJ code style settings are out of date · Issue #617 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I downloaded and imported the GoogleStyle code style settings xml, as recommended in Contributing.md. It doesn't seem like this project and its checkstyle are actually conforming to those style settings (which is fine, I like the prevailing gRPC style better!) A few things in particular keep coming up:

Import order: GoogleStyle has static imports at the bottom, doesn't separate grpc imports. This is configured in Code Style > Java > Imports > Import Layout.
Method argument wrapping: GoogleStyle has method call arguments and declaration parameters on the next line aligned to the opening paren. This is configured in Code Style > Java > Wrapping and Braces > Method declaration parameters > Align when multiline, as well as the same option under Method call arguments.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/618
Support TLS for okhttp benchmark. by madongfly · Pull Request #618 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/619
Add simple server timeout  by carl-mastrangelo · Pull Request #619 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/620
OkHttp should use SSLSocketFactory.getDefault() by default · Issue #620 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We should default to using TLS. Right now setting sslSocketFactory enables TLS. We should have a separate option for enabling/disabling TLS. It could easily be a boolean, but we might choose a enum to expand it later; either way.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/621
Separate ServerCall binding utilities per method type. by zhangkun83 · Pull Request #621 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/622
AbstractStream should enforce calling thread · Issue #622 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In AbstractStream, there are several javadoc comments that read:
"This must be called from the transport thread, since a listener may be called back directly."
While this is informative, it would be even better if it was enforced.  It would be a good idea to call Thread.currentThread().getId(), or some similar check to make sure that the transport thread is actually the one making the call.  In cases where holding a lock is tantamount to being threadsafe, checking Thread.holdsLock() would also be possible.  Ideally these cases could be wrapped up in some sort of assertTransportThread() method.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/623
okhttp: make transport.start() async. by madongfly · Pull Request #623 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/624
Reduce flow control window for interop tests by ejona86 · Pull Request #624 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/625
Add basic unit tests to Abstract Stream by carl-mastrangelo · Pull Request #625 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/626
OkHttpClientTransport.newCall should be async · Issue #626 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Our API is async, and so doing blocking for MAX_CONCURRENT_STREAMS is breaking that. We should go fully async.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/627
Redundant/different default window size used in okhttp · Issue #627 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
DEFAULT_INITIAL_WINDOW_SIZE and DEFAULT_WINDOW_SIZE
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/628
Remove OkHttpClientTransport.DEFAULT_INITIAL_WINDOW_SIZE, use Utils.DEFAULT_WINDOW_SIZE instead. by madongfly · Pull Request #628 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The two aren't identical in value or usage; one is used for sending, one for receiving. However, it does seem that the distinction is not very clear; removing DEFAULT_INITIAL_WINDOW_SIZE makes sense.
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/629
okhttp: Enable TLS by default. by madongfly · Pull Request #629 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The negotiation types are really transport-specific. It seems they should really be left as separate. I don't want a enum that is the union of each negotiation type of each transport.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/630
Minor Readability changes by carl-mastrangelo · Pull Request #630 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
R= @ejona86
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/631
Migrate from PARSER to parser() as a way of getting the parser of a protobuf message. by zhangkun83 · Pull Request #631 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/632
Sanitize ClientCalls. by zhangkun83 · Pull Request #632 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/633
Minor readability changes by carl-mastrangelo · Pull Request #633 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I don't think we should add final everywhere unless it adds some value for that particular instance. In these cases, I think it is useless effort because these APIs are internal and we are free to add final later without real issue. Similarly, making package-private classes final seems to have limited benefit. Going through this process with classes in io.grpc package would make more sense, but not for io.grpc.transport.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/634
Use shared scheduler for ServerImpl deadline support · Issue #634 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
#576 was merged slightly before #619, so we are able to use a single thread for deadlines on server-side and client-side. That isn't super-important, since we don't expect more than one server generally, but could is still maybe a nice-to-have. At the very least, the TODO could be removed if we decided not to bother.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/635
Consider renaming DUPLEX_STREAMING to BIDI_STREAMING · Issue #635 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I thought a while back it was decided to use "bidi" or "bidirectional" streaming to describe a call that has both server and client streaming. I appers C, C++, Node.js, Ruby, and PHP use "bidi." It appears C# uses "duplex." It appears Go did not define the concept. I couldn't find what Obj-C and Python use.
We would need to change it in ClientCalls, ServerCalls, and MethodDescriptor.MethodType.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/636
Catch exceptions thrown by Executor.execute · Issue #636 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
direct executor lets RuntimeExceptions pass through the call stack. We need to defend against that in places we would permit direct executor. Even without direct executor, execute can throw with rejected exception, so it is really a case we should handle.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/637
Rename "payload" to "message" · Issue #637 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Call has onPayload and sendPayload. Such things should use "message" instead; little sense in having different names for the entity.
We should try to maintain backward compatibility for a bit for this. We can simply make the new "message" versions of the methods and have the new versions call the old versions. When we remove the old version we make the methods abstract on Call.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/638
Get rid of AbstractServiceDescriptor as it is no longer useful by zhangkun83 · Pull Request #638 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/639
ServerCall.onCancel should not be called for server-initiated close(CANCELLED) · Issue #639 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For reasons possibly lost to history, we decided to notify the server's onCompleted after the server completed with non-OK status codes, except for CANCELLED which notifies onCancel.
For whatever reason CANCELLED triggers onCancel, DEADLINE_EXCEEDED probably should as well. However, it might be good to re-discover the reason for the behavior, and maybe only call onCanel if there was an error.
I don't believe we are following the documentation today. It seems AbstractStream only triggers onCancel when an error occurs.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/640
In-process transport by ejona86 · Pull Request #640 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86, I think this looks pretty good. I started going through reviewing each commit, but maybe that's premature? I'm a little concerned about having to register them by name into a static set. Code that wants to start multiple servers in the same JVM would have to generate unique names.
Do we need the client and server to be so de-coupled? From my perspective, I'd prefer ditch the static registry and require callers to supply an InProcessServer when building the client, to make the link explicit.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/641
Are GRPC support server sends messages to the client driving？ · Issue #641 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello everyone,sometimes I want to send something from server to client directly,not response by client call request,whether GRPC supports such operations currently？
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/642
Improve Metadata by ejona86 · Pull Request #642 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Change looks easy to understand. Nice work.

Forgive me if already discussed, but what's your opinion on just using
LinkedHashMap vs conditionally TreeMap for consistent ordering for tests?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/643
Replace DeferredInputStream with interface Drainable. by zhangkun83 · Pull Request #643 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/644
Minimize context switches between app & net threads when requesting more messages by louiscryan · Pull Request #644 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/645
Cannot find symbol makeImmutable() and isMutable() at compile time · Issue #645 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
I tried to compile my proto with Maven using the configuration reported in the how-to:
      <configuration>
        <protocArtifact>com.google.protobuf:protoc:3.0.0-alpha-3.1:exe:${os.detected.classifier}</protocArtifact>
        <pluginId>grpc-java</pluginId>
        <pluginArtifact>io.grpc:protoc-gen-grpc-java:0.7.1:exe:${os.detected.classifier}</pluginArtifact>
      </configuration>

However I managed to get it work only changing to alpha-2
<protocArtifact>com.google.protobuf:protoc:3.0.0-alpha-2:exe:${os.detected.classifier}</protocArtifact>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/646
Fix flaky OkHttp test · Issue #646 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We're seeing an OkHttp test fail randomly, with the output below.
io.grpc.transport.okhttp.OkHttpClientTransportTest > outboundFlowControl FAILED
    Argument(s) are different! Wanted:
    frameWriter.data(
        false,
        3,
        <any>,
        32773
    );
    -> at io.grpc.transport.okhttp.OkHttpClientTransportTest.outboundFlowControl(OkHttpClientTransportTest.java:462)
    Actual invocation has different arguments:
    frameWriter.data(
        false,
        3,
        Buffer[size=16384 md5=c975385526568787c9110176db80e1ca],
        16384
    );
    -> at io.grpc.transport.okhttp.AsyncFrameWriter$9.doRun(AsyncFrameWriter.java:160)
        at sun.reflect.GeneratedConstructorAccessor3.newInstance(Unknown Source)
        at sun.reflect.DelegatingConstructorAccessorImpl.newInstance(DelegatingConstructorAccessorImpl.java:45)
        at java.lang.reflect.Constructor.newInstance(Constructor.java:422)
        at io.grpc.transport.okhttp.OkHttpClientTransportTest.outboundFlowControl(OkHttpClientTransportTest.java:462)

    java.lang.AssertionError: expected:<0> but was:<1>
        at org.junit.Assert.fail(Assert.java:88)
        at org.junit.Assert.failNotEquals(Assert.java:743)
        at org.junit.Assert.assertEquals(Assert.java:118)
        at org.junit.Assert.assertEquals(Assert.java:555)
        at org.junit.Assert.assertEquals(Assert.java:542)
        at io.grpc.transport.okhttp.OkHttpClientTransportTest.tearDown(OkHttpClientTransportTest.java:170)�
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/647
implement health checking service · Issue #647 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
defined in "gRPC Health Checking Protocol"
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/648
Split ClientCall into its own class by carl-mastrangelo · Pull Request #648 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo +1 to breaking out the call impl ... might be easier to review if you created a separate PR to just move the code.  After it's committed, you could then rebase this PR on it so it's easier to see the diff.  WDYT?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/649
Replace Metadata.Trailers and Metadata.Headers with just Metadata · Issue #649 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In Headers, path can be removed (just use a different MethodDescriptor; if we really need it it the future, it can be added to CallOptions) and authority can move to CallOptions. At that point, there isn't a distinction between headers and trailers and we can just have "Metadata".
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/650
Implement oauth2_auth_token · Issue #650 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I don't know if any API additions need to be done to make this use case easy.
https://github.com/grpc/grpc/blob/master/doc/interop-test-descriptions.md#oauth2_auth_token
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/651
 Server reflection service · Issue #651 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/652
Specify locale for toLowerCase in Metadata by ejona86 · Pull Request #652 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo, FYI
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/653
Q: How to declare rpc method without input and returns messages? · Issue #653 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
is it possible to define rpc method without input and returns messages?
something like:
    service myservice {
        rpc heartbeat() {}
    }
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/654
Fix protobuf plugin usage in README.md by zhangkun83 · Pull Request #654 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Excellent. @zhangkun83, LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/655
Benchmark: Enable/Disable TLS for okhttp accordingly by madongfly · Pull Request #655 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/656
Reverse interceptor execution order by ejona86 · Pull Request #656 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/657
Add ClientInterceptors "inside" ChannelImpl by ejona86 · Pull Request #657 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/658
Allow using in-process transport without the registry · Issue #658 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It would be nice to avoid the registry when you are able to pass objects around. That prevents the need to have to determine a unique name. The most obvious case is in tests, but it is actually just generally useful.
#640 had some discussion about options for doing it.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/659
Add Executor wrapping to Context by ejona86 · Pull Request #659 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
As can be seen in the commit message, I renamed "wrap(Executor)" to wrapDynamic. @louiscryan has suggested "wrapPropagating", which isn't unreasonable. Neither of us cared too much, but I thought that even wrapFixed "propagated" the context. Any other names or +1s for names is appreciated.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/660
Use mutation methods for stub reconfiguration. by zhangkun83 · Pull Request #660 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/661
Change AbstractTransportTest to propagate server delay in request · Issue #661 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Commit 3e26b99#diff-cf14d5396f1bd6ab4bcf9c37e7756356R143 introduced the use of an AtomicLong to manage server delay and also created a server delay interceptor.  Neither of these are needed since the integration test request messages support propagating server delay.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/662
Minor readability changes by ejona86 · Pull Request #662 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/663
Error handling fix and minor improvements by ejona86 · Pull Request #663 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/664
Java warnings in Context API · Issue #664 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In lookup method: found raw type: io.grpc.Context.Key
missing type arguments for generic class io.grpc.Context.Key
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/665
Add reconnection logic by carl-mastrangelo · Pull Request #665 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/666
Add missing generics to Context internals by ejona86 · Pull Request #666 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/667
Simplify locking model of OkHttp Transport, avoid potential deadlock. by madongfly · Pull Request #667 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/668
Invert User-Agent order so application-provided string comes first · Issue #668 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RFC 7231§5.5.3 says:

By convention, the product identifiers are listed in decreasing order of their significance for identifying the user agent software.

Combined with the example, it seems that we should put the application-provided string first.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/669
Send an RST_STREAM frame on server deadline by johnbcoughlin · Pull Request #669 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Is the "Details" link for Visual Studio CI working for you? It sends me to localhost:8080.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/670
Remove ServerDelayInterceptor from AbstractTransportTest by johnbcoughlin · Pull Request #670 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@johnbcoughlin Thanks for the patch!
Cherry-picked as 1ac64bd
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/671
Correctly handle unknown http2 error code. by madongfly · Pull Request #671 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
And do you think we should sync the map with okhttp ErrorCode
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/672
Alternate Channel Reconnect implementation by carl-mastrangelo · Pull Request #672 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

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

https://github.com/grpc/grpc-java/issues/675
OkHttp: sync error map with gRpc spec. by madongfly · Pull Request #675 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/676
Adjust @GuardedBy to pass internal GuardedBy Checking. by madongfly · Pull Request #676 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
And maybe we should start using error prone?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/677
Add a status to Transport shutdown by carl-mastrangelo · Pull Request #677 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/678
Adding support for NPN fallback. by nmittler · Pull Request #678 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/679
Fix flaky test by nmittler · Pull Request #679 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cherry-picked as a36f4af
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/680
Breaking out ClientCallFactory abstract class by nmittler · Pull Request #680 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan @ejona86 @wrwg @zhangkun83 PTAL.  I suspect that this may be a bit controversial, but I'd like to get the discussion started.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/681
Attaching Metadata to error Status responses... · Issue #681 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I'm not sure what the "best practice" is for returning application-level error information (would be very useful to understand Google's own internal practice for guidance), but certainly one approach is to attach trailing headers with application error information to error responses. Setting additional headers via thread-local using a server interceptor seems easy enough, but for client-side it seems particularly awkward capturing metadata on a per-call basis using an interceptor. I see examples in MetadataUtils for capturing "last set headers" on a stub or channel but this is only useful for testing and cannot capture on a per-call basis. Other option would be to use the async stub and a thread-local to pass the metadata information along to StreamObserver.onError() but this loses the convenience of using the blocking and future stubs. I'm not sure if the same approach works for a blocking or future stub since the listener may be invoked in a different thread.
Will the context api once fully integrated make this easy, or would it make sense to have a way to "attach" metadata to a Status object (perhaps this would be desirable anyway for convenience)?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/682
Make new stream call asynchronous when the MAX_CONCURRENT_STREAMS is reached. by madongfly · Pull Request #682 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/683
Add a transport ready for use with retry by carl-mastrangelo · Pull Request #683 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/684
Rename onPayload to onMessage by carl-mastrangelo · Pull Request #684 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/685
Forcibly cast in interop test by carl-mastrangelo · Pull Request #685 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/686
Rename sendPayload to sendMessage by carl-mastrangelo · Pull Request #686 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/687
Fix UNKNOWN status without description · Issue #687 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
grpc-java/core/src/main/java/io/grpc/ChannelImpl.java
    
    
         Line 311
      in
      d2b1b37
    
  
  
    

        
          
           transportShutdown(Status.UNKNOWN); 
        
    
  



  
    
      grpc-java/netty/src/main/java/io/grpc/transport/netty/NettyClientHandler.java
    
    
         Line 212
      in
      3e26b99
    
  
  
    

        
          
           stream.transportReportStatus(Status.UNKNOWN, false, new Metadata.Trailers()); 
        
    
  


We should basically always provide a description, so that users have a hope of distinguishing whether an error is local or remote. The NettyClientHandler should be converting the HTTP/2 error code to a status.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/688
Make ServerImpl Use the common Scheduled Executor Service by carl-mastrangelo · Pull Request #688 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/689
Switch ALPN/NPN to advertise only h2 · Issue #689 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/690
Remove all support for Payload by carl-mastrangelo · Pull Request #690 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/691
Upgrade protobuf-gradle-plugin to 0.6.1 by zhangkun83 · Pull Request #691 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/692
Make any lib-generated UNKNOWN have description by ejona86 · Pull Request #692 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/693
android-interop-testing fails to build due to lint failures · Issue #693 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The installDebug task works, but the build task does not. It seems like some of the warnings could be ignored (like literal strings), but some other ones need to be properly dealt with ("NewApi: Calling new methods on older versions").
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/694
Double-closure of call during interop tests · Issue #694 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I find it in the stderr of the test report of Netty, Netty local channel, and OkHttp. I see it printed out to my console once, so I think that may be from the InProcess test.
This exception very likely means we have a bug and are double-closing.
java.lang.IllegalStateException: call already closed
    at com.google.common.base.Preconditions.checkState(Preconditions.java:173)
    at io.grpc.ServerImpl$ServerCallImpl.close(ServerImpl.java:507)
    at io.grpc.ForwardingServerCall.close(ForwardingServerCall.java:65)
    at io.grpc.testing.TestUtils$1$1.close(TestUtils.java:109)
    at io.grpc.stub.ServerCalls$ResponseObserver.onError(ServerCalls.java:237)
    at io.grpc.testing.integration.TestServiceImpl$ResponseDispatcher.dispatchChunk(TestServiceImpl.java:277)
    at io.grpc.testing.integration.TestServiceImpl$ResponseDispatcher.access$000(TestServiceImpl.java:207)
    at io.grpc.testing.integration.TestServiceImpl$ResponseDispatcher$1.run(TestServiceImpl.java:219)
    at java.util.concurrent.Executors$RunnableAdapter.call(Executors.java:511)
    at java.util.concurrent.FutureTask.run(FutureTask.java:266)
    at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.access$201(ScheduledThreadPoolExecutor.java:180)
    at java.util.concurrent.ScheduledThreadPoolExecutor$ScheduledFutureTask.run(ScheduledThreadPoolExecutor.java:293)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
    at java.lang.Thread.run(Thread.java:745)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/695
Notify transportReady() in Netty by ejona86 · Pull Request #695 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
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
    - waiting to lock <0x000000076eb28a20> (a io.grpc.ChannelImpl)
    at io.grpc.transport.inprocess.InProcessTransport.notifyShutdown(InProcessTransport.java:151)
    - locked <0x000000076c2afb38> (a io.grpc.transport.inprocess.InProcessTransport)
    at io.grpc.transport.inprocess.InProcessTransport.shutdown(InProcessTransport.java:140)
    - locked <0x000000076c2afb38> (a io.grpc.transport.inprocess.InProcessTransport)
    at io.grpc.ServerImpl$ServerListenerImpl.serverShutdown(ServerImpl.java:240)
    - locked <0x000000076bfe81a8> (a io.grpc.ServerImpl)
    at io.grpc.transport.inprocess.InProcessServer.shutdown(InProcessServer.java:77)
    - locked <0x000000076be7fdc0> (a io.grpc.transport.inprocess.InProcessServer)
    at io.grpc.ServerImpl.shutdown(ServerImpl.java:135)
    - locked <0x000000076bfe81a8> (a io.grpc.ServerImpl)
    at com.pexlabs.grpc.AbstractGrpcServer.shutDown(AbstractGrpcServer.java:42)
    at com.google.common.util.concurrent.AbstractIdleService$2$2.run(AbstractIdleService.java:69)
    at com.google.common.util.concurrent.Callables$3.run(Callables.java:95)
    at java.lang.Thread.run(Thread.java:745)
"main":
    at io.grpc.transport.inprocess.InProcessTransport.shutdown(InProcessTransport.java:136)
    - waiting to lock <0x000000076c2afb38> (a io.grpc.transport.inprocess.InProcessTransport)
    at io.grpc.ChannelImpl.shutdown(ChannelImpl.java:128)
    - locked <0x000000076eb28a20> (a io.grpc.ChannelImpl)
    at io.grpc.ChannelImpl.shutdownNow(ChannelImpl.java:149)
    - locked <0x000000076eb28a20> (a io.grpc.ChannelImpl)
    at com.pexlabs.grpc.AbstractGrpcClient.close(AbstractGrpcClient.java:25)
    at com.pexlabs.test.TestUtil$1.doStop(TestUtil.java:25)
    at com.google.common.util.concurrent.AbstractService.stopAsync(AbstractService.java:204)
    at com.google.common.util.concurrent.ServiceManager.stopAsync(ServiceManager.java:327)
    at com.pexlabs.test.TestContext.after(TestContext.java:75)
    at org.junit.rules.ExternalResource$1.evaluate(ExternalResource.java:50)
    at org.junit.rules.RunRules.evaluate(RunRules.java:20)
    at org.junit.runners.ParentRunner.run(ParentRunner.java:363)
    at org.junit.runner.JUnitCore.run(JUnitCore.java:137)
    at com.intellij.junit4.JUnit4IdeaTestRunner.startRunnerWithArgs(JUnit4IdeaTestRunner.java:78)
    at com.intellij.rt.execution.junit.JUnitStarter.prepareStreamsAndStart(JUnitStarter.java:212)
    at com.intellij.rt.execution.junit.JUnitStarter.main(JUnitStarter.java:68)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:497)
    at com.intellij.rt.execution.application.AppMain.main(AppMain.java:140)

Found 1 deadlock.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/697
netty: Vastly improve connection error handling by ejona86 · Pull Request #697 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/698
Don't hold channel/server lock when shutting down transport by ejona86 · Pull Request #698 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/699
Fix shutting down a never-started ServerImpl by ejona86 · Pull Request #699 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/700
Pass URI to Credentials.getRequestMetadata · Issue #700 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
ServiceAccountJwtAccessCredentials needs the URI, or requires the user to specify it ahead of time. Specifying it ahead of time is a pain and hard to know which strings are needed.
We will need to add a way to get the scheme and authority from ClientCall or Channel.
@anthmgoogle, FYI. @louiscryan and I agreed on this and have a gRPC-integration solution in mind. That means we will soon always be specifying the URI and passing the defaultAudience would no longer be necessary for our usage.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/701
Android-Interop-test: fix lint errors/warnings, enable proguard. by madongfly · Pull Request #701 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/702
compute_engine_creds and service_account_creds failing · Issue #702 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
They were added in 926a2c1 and ac4952c, but since 131ba5d the tests look like they have been failing.
@madongfly, do you want to fix it?
$ /var/local/git/grpc-java/run-test-client.sh --use_tls=true --server_port=443 --server_host=grpc-test.sandbox.google.com --server_host_override=grpc-test.sandbox.google.com --default_service_account=<snip> --oauth_scope=https://www.googleapis.com/auth/xapi.zoo --test_case=compute_engine_creds
...
Running test compute_engine_creds
Exception in thread "main" java.lang.NullPointerException
    at com.google.common.base.Preconditions.checkNotNull(Preconditions.java:210)
    at io.grpc.auth.ClientAuthInterceptor.<init>(ClientAuthInterceptor.java:67)
    at io.grpc.testing.integration.AbstractTransportTest.computeEngineCreds(AbstractTransportTest.java:748)Shutting down

    at io.grpc.testing.integration.TestServiceClient.runTest(TestServiceClient.java:219)
    at io.grpc.testing.integration.TestServiceClient.run(TestServiceClient.java:192)
    at io.grpc.testing.integration.TestServiceClient.main(TestServiceClient.java:79)

$ /var/local/git/grpc-java/run-test-client.sh --use_tls=true --server_port=443 --server_host=grpc-test.sandbox.google.com --server_host_override=grpc-test.sandbox.google.com --service_account_key_file=<snip> --oauth_scope=https://www.googleapis.com/auth/xapi.zoo --test_case=service_account_creds
...
Running test service_account_creds
Exception in thread "main" java.lang.NullPointerException
    at com.google.common.base.Preconditions.checkNotNull(Preconditions.java:210)
    at io.grpc.auth.ClientAuthInterceptor.<init>(ClientAuthInterceptor.java:67)
    at io.grpc.testing.integration.AbstractTransportTest.serviceAccountCreds(AbstractTransportTest.java:716)
    at io.grpc.testing.integration.TestServiceClient.runTest(TestServiceClient.java:223)Shutting down

    at io.grpc.testing.integration.TestServiceClient.run(TestServiceClient.java:192)
    at io.grpc.testing.integration.TestServiceClient.main(TestServiceClient.java:79)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/703
Fix serviceAccountCreds test and computeEngineCreds test. by madongfly · Pull Request #703 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
That does mean that we don't shutdown the executor in all cases, but I'm content to let the GC do that in a test.
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/704
Implement per_rpc_creds · Issue #704 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
https://github.com/grpc/grpc/blob/master/doc/interop-test-descriptions.md#per_rpc_creds
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/705
Implement timeout_on_sleeping_server · Issue #705 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
https://github.com/grpc/grpc/blob/master/doc/interop-test-descriptions.md#timeout_on_sleeping_server
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/706
Implement unimplemented_method · Issue #706 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
https://github.com/grpc/grpc/blob/master/doc/interop-test-descriptions.md#unimplemented_method
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/707
Make the change on status effective. by madongfly · Pull Request #707 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM. Note that the colon should have been on the next line ("the break comes before the symbol").
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/708
OkHttp should use plaintext in TransportBenchmark by ejona86 · Pull Request #708 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/709
Backport ef106e0 and 248f575 to 0.7.x by madongfly · Pull Request #709 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/710
Switch ALPN/NPN to advertise only h2 by madongfly · Pull Request #710 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Fixes #689
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/711
Renamed Server payload to message by carl-mastrangelo · Pull Request #711 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo, thanks for noticing. LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/712
Rename Duplex to Bidi by carl-mastrangelo · Pull Request #712 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/713
ServerEssentials needs more Javadoc · Issue #713 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/714
Core gRPC package needs documention · Issue #714 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The default javadoc generated is missing package level documentation
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/715
AbstractChannelBuilder should be renamed AbstractChannelImplBuilder · Issue #715 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is to match ChannelImpl.  If ChannelImpl gets renamed in #680, it should be updated accordingly.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/716
Create a grpc.internal package  · Issue #716 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Some classes that should not be part of the public API should be moved to an internal package.  Additionally, grpc.transport should also be moved to grpc.internal.transport
This shouldn't be api breaking.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/717
Change the javadoc in MutableHandlerRegistry to not say Impl · Issue #717 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
There is already a MutableHandlerRegistryImpl, the javadoc on MutableHandlerRegistry is somewhat confusing.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/718
Remove All Deprecated Classes before Beta · Issue #718 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
There are a number of classes in core that are Deprecated.  Since it will likely be impossible to remove them later without breakage, they should be removed now.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/719
Spell SNAPSHOT correctly, for full effect by ejona86 · Pull Request #719 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/720
Add package descriptions for transport, netty and okhttp by zhangkun83 · Pull Request #720 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/721
Add available() to KnownLength by zhangkun83 · Pull Request #721 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/722
Marshaller should use "deserializing" rather than parsing · Issue #722 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Javadoc verbiage in the Marshaller should use appropriate negative and positive words.
Questions raised:
Are parse() and stream() inverses of each other?  (group says yes)
Are serialize and stream inverses of each other?
Should Marshaller use marshal() and unmarshal()?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/723
Add javadoc to Context.CancellationListener · Issue #723 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/724
NanoProtoInputStream should be package private · Issue #724 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/725
Enforce character restriction for AsciiMarshaller · Issue #725 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
AsciiMarshaller is used for HTTP2 Headers.  Since HTTP2 is more restrictive about what ascii characters can be used, AM should either be more clear about what characters are accepted, or enforce such restrictions.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/726
ServerCall Handler should take a method descriptor rathe than a string · Issue #726 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/727
Move Authority from Headers to ServerCall · Issue #727 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This was a maybe thing to do, but creating an issue for it anyways.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/728
Review the generics on ServerCallHandler · Issue #728 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Maybe add a super and extends.   The context for this issue was how would a proxy be implemented.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/729
ServerInterceptor.interceptCall should take a method descriptor · Issue #729 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently it takes the name of the method.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/730
SharedResourceHolder should be moved to the internal package · Issue #730 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/731
Add "set" and "add" method prefixes to AbstractChannelBuilder (e.g. addInterceptor) · Issue #731 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Our API is currently not consistent between how builders are implemented.  Considering the pervasiveness of the set, get, add, with, and other prefixed methods of Proto and the existing stubby implementations, consistency should be swing towards these style methods.
Also, AbstractServerBuilder should be changed likewise
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/732
AbstractChannelBuilder.buildEssentials should have a javadoc  · Issue #732 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/733
Delete ChannelEssentials · Issue #733 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Since ChannelEssentials only affects transports, it should likely be deleted.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/734
Deprecated Channel.newCall should be deleted  · Issue #734 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Clients should use the non deprecated sibling newCall.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/735
ChannelImpl.awaitTerminated should be renamed awaitTermination · Issue #735 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This makes it make the spelling of ExecutorService shutdown methods.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/736
ChannelImpl.TIMEOUT_KEY should be private  · Issue #736 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Possibly moved to the internal package.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/737
Remove ChannelImpl.ping (or possible mark it experimental) · Issue #737 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It isn't clear that ping will be part of the long term gRPC interface (and is easy to add back in later if needed).  Either remove it or mark it experimental.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/738
Deprecated inner classes of ClientInterceptor should be removed  · Issue #738 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/739
CheckedForwardingClientCall should cancel delegate on failure · Issue #739 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It should also document whether it cancels or not, even if we end up not cancelling the delegate.
@ejona86 do you remember if there were reasons to not do this?  If so, are they stronger than the reason that cancelling should still be done?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/740
Add @Experimental to Context · Issue #740 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Or add some other way to denote that Context is still being tried out, and may change.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/741
Consider shortening generic names (BuilderT, RequestT, MethodDescriptor<>, ServerCall<>, ServerCall.Listener, ServerMethodDefinition etc.) · Issue #741 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
There are a lot of places where the generic parameters are kind of long, and could be made more concise without surrendering readability.   The classes listed in the title are some but not all of classes that could benefit from this.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/742
Metadata.Key.asciiName should be private · Issue #742 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Because the returned value is mutable, it should be limited to being modified by our own code.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/743
Remove second MethodDescriptor.create method · Issue #743 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
currently there are two methods, one that takes the fully qualified name and one that takes the service and method name.  Since the rest of core is using the fully qualified name, the second create method doesn't need to be part of our API.  (and can be easily added back if there is demand).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/744
SerializingExecutor should be moved to be internal · Issue #744 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/745
Maybe remove Server and rename ServerImpl · Issue #745 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It may be worth keeping Server as a base to ServerImpl (in order to add methods later on like getServerAddress)
This was a contentious issue, but needs to be resolved before going beta.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/746
ServerImpl.awaitTerminated should be renamed awaitTermination · Issue #746 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is the same as the change in #735
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/747
Make ServerCall.Listener methods no ops · Issue #747 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Some Listeners may not care about implementing every method.  Thus, ServerCall.Listener methods should provide No-op default methods.  This has the downside that users of this class may not override correctly, or miss understanding how to listen.  However, since this is an advanced api, it may be reasonable to ask clients to understand how this class works.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/748
Make ClientCall.Listener methods no ops · Issue #748 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Same issues raised in #747
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/749
Make ServerServiceDefinition.getMethod private · Issue #749 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This method was only intended for internal use.  ServerServiceDefinition.getMethods should be used instead.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/750
Remove  Status.OperationRuntimeException and Status.OperationException · Issue #750 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
These are deprecated in favor of StatusException and StatusRuntimeException
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/751
Add javadoc to clarify equality on Status · Issue #751 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Are Statuses equal based on code, code and message, or even as far as the throwable?  The javadoc for equals should clarify this.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/752
Fix javadoc on Status.asException · Issue #752 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 I believe you asked for this, but I am now fuzzy on the details of why. Assigning to you.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/753
Make NanoProtoInputStream package private by madongfly · Pull Request #753 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/754
Fix javadoc, and remove deprecated OperationException classes by carl-mastrangelo · Pull Request #754 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/755
Remove Status.OperationRuntimeException and Status.OperationException by madongfly · Pull Request #755 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Doh! You and @carl-mastrangelo raced for #754. If you make sure to assign the issue to yourself, that can prevent duplicated effort.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/756
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/757
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/758
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/759
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/760
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/761
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/762
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/763
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/764
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/765
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/766
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/767
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/768
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/769
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/770
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/771
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/772
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/773
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/774
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/775
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/776
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/777
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/778
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/779
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/780
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/781
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/782
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/783
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/784
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/785
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/786
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/787
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/788
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/789
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/790
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/791
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/792
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/793
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/794
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/795
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/796
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/797
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/798
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/799
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/800
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/801
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/802
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/803
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/804
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/805
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/806
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/807
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/808
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/809
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/810
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/811
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/812
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/813
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/814
Rate limit · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
[]
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/815
Change Metadata.Trailers to Metadata in JavaDoc by ejona86 · Pull Request #815 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/816
Split compiling instructions out of README.md by ejona86 · Pull Request #816 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/817
android-interop-testing doesn't build · Issue #817 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
With the renames to packages, it is now broken. I expect that the generated code needs to be regenerated as well (for other reasons).
We should backport the fix to the 0.8.x branch.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/818
Update android-interop-test's dependency. by madongfly · Pull Request #818 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/819
Fixes for static analysis warnings by ejona86 · Pull Request #819 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/820
Update dependency for android interop test by madongfly · Pull Request #820 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/821
Make interceptors an abstract class? · Issue #821 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
They are an interface today. We can add other interfaces later, but would need instanceof checking in ClientInterceptors/ServerInterceptors to enable features.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/822
Remove Headers in favor of Metadata by carl-mastrangelo · Pull Request #822 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/823
Annotate ServerEssentials and buildEssentials() with @Internal by zhangkun83 · Pull Request #823 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/824
Prevent using metadata with invalid keys · Issue #824 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We should restrict the characters that are permitted in keys, as we have no way to send many characters (like colon, unicode, etc).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/825
Remove unnecessary instanceof check by carl-mastrangelo · Pull Request #825 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM ... make it so! :)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/826
Remove the first MethodDescriptor constructor. by zhangkun83 · Pull Request #826 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/827
Rename parse and stream to marshal and unmarshal by carl-mastrangelo · Pull Request #827 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Out of my own experience, the first time I the word "marshal", I didn't know what it meant. The fact that Marshaller uses "parsing and serialization" in its javadoc indicates that the word "marshal" is not as widely understood as "parse", "serialize" and "deserialize". I would imagine the javadocs of marshal() and unmarshal() would also need to refer to "serialize" and "deserialize" for users to comprehend. If that's the case, I would just name them as serialize() and deserialize() instead.
@ejona86 @nmittler @madongfly WDYT?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/828
Skip io.grpc.internal in javadoc. by zhangkun83 · Pull Request #828 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/829
Call ClientTransport.Listener.transportReady() in a more appropriate time. · Issue #829 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently we call it after the TCP connection is connected, we should call it after receiving the settings frame, so that we know for sure that the server accepted the connection.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/830
OkHttp: Call ClientTransport.Listener.transportReady() after receivin… by madongfly · Pull Request #830 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 ping
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/831
StatusRuntimeException: INTERNAL: Invalid protobuf byte sequence · Issue #831 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
A user of Cloud Bigtable reported a bug on a really large streaming response: googleapis/java-bigtable-hbase#407.  Any advice on how to address the stack trace below?
8, 2015 3:21:15 PM io.grpc.SerializingExecutor$TaskRunner run
GRAVE: Exception while executing runnable io.grpc.ChannelImpl$CallImpl$ClientStreamListenerImpl$2@6965a9c6
io.grpc.StatusRuntimeException: INTERNAL: Invalid protobuf byte sequence
at io.grpc.Status.asRuntimeException(Status.java:428)
at io.grpc.protobuf.ProtoUtils$1.parse(ProtoUtils.java:64)
at io.grpc.protobuf.ProtoUtils$1.parse(ProtoUtils.java:52)
at io.grpc.MethodDescriptor.parseResponse(MethodDescriptor.java:105)
at io.grpc.ChannelImpl$CallImpl$ClientStreamListenerImpl$2.run(ChannelImpl.java:384)
at io.grpc.SerializingExecutor$TaskRunner.run(SerializingExecutor.java:154)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
at java.lang.Thread.run(Thread.java:745)
Caused by: com.google.bigtable.repackaged.com.google.protobuf.InvalidProtocolBufferException: Protocol message was too large. May be malicious. Use CodedInputStream.setSizeLimit() to increase the size limit.
at com.google.bigtable.repackaged.com.google.protobuf.InvalidProtocolBufferException.sizeLimitExceeded(InvalidProtocolBufferException.java:110)
at com.google.bigtable.repackaged.com.google.protobuf.CodedInputStream.tryRefillBuffer(CodedInputStream.java:1131)
at com.google.bigtable.repackaged.com.google.protobuf.CodedInputStream.refillBuffer(CodedInputStream.java:1081)
at com.google.bigtable.repackaged.com.google.protobuf.CodedInputStream.ensureAvailable(CodedInputStream.java:1068)
at com.google.bigtable.repackaged.com.google.protobuf.CodedInputStream.readRawBytesSlowPath(CodedInputStream.java:1203)
at com.google.bigtable.repackaged.com.google.protobuf.CodedInputStream.readBytes(CodedInputStream.java:517)
at com.google.bigtable.v1.Column.(Column.java:52)
at com.google.bigtable.v1.Column.(Column.java:13)
at com.google.bigtable.v1.Column$1.parsePartialFrom(Column.java:822)
at com.google.bigtable.v1.Column$1.parsePartialFrom(Column.java:816)
at com.google.bigtable.repackaged.com.google.protobuf.CodedInputStream.readMessage(CodedInputStream.java:495)
at com.google.bigtable.v1.Family.(Family.java:61)
at com.google.bigtable.v1.Family.(Family.java:13)
at com.google.bigtable.v1.Family$1.parsePartialFrom(Family.java:923)
at com.google.bigtable.v1.Family$1.parsePartialFrom(Family.java:917)
at com.google.bigtable.repackaged.com.google.protobuf.CodedInputStream.readMessage(CodedInputStream.java:495)
at com.google.bigtable.v1.ReadRowsResponse$Chunk.(ReadRowsResponse.java:185)
at com.google.bigtable.v1.ReadRowsResponse$Chunk.(ReadRowsResponse.java:145)
at com.google.bigtable.v1.ReadRowsResponse$Chunk$1.parsePartialFrom(ReadRowsResponse.java:904)
at com.google.bigtable.v1.ReadRowsResponse$Chunk$1.parsePartialFrom(ReadRowsResponse.java:898)
at com.google.bigtable.repackaged.com.google.protobuf.CodedInputStream.readMessage(CodedInputStream.java:495)
at com.google.bigtable.v1.ReadRowsResponse.(ReadRowsResponse.java:60)
at com.google.bigtable.v1.ReadRowsResponse.(ReadRowsResponse.java:13)
at com.google.bigtable.v1.ReadRowsResponse$1.parsePartialFrom(ReadRowsResponse.java:1651)
at com.google.bigtable.v1.ReadRowsResponse$1.parsePartialFrom(ReadRowsResponse.java:1645)
at com.google.bigtable.repackaged.com.google.protobuf.AbstractParser.parsePartialFrom(AbstractParser.java:192)
at com.google.bigtable.repackaged.com.google.protobuf.AbstractParser.parseFrom(AbstractParser.java:209)
at com.google.bigtable.repackaged.com.google.protobuf.AbstractParser.parseFrom(AbstractParser.java:215)
at com.google.bigtable.repackaged.com.google.protobuf.AbstractParser.parseFrom(AbstractParser.java:49)
at io.grpc.protobuf.ProtoUtils$1.parse(ProtoUtils.java:61)
... 7 more
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/832
Provide a way to set client side proto size limit. · Issue #832 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Cloud Bigtable has server size proto message limit of > 64MB. The current size limit on the client size is 64MB (default) in CodedInputStream.java. CodedInputStream.setSizeLimit() can be used to override the default value. Cloud Bigtable would like a way to set the proto message limit on the client side so that users can work with larger data set.
Related reported issue: googleapis/java-bigtable-hbase#407
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/833
Remove deprecated method. by madongfly · Pull Request #833 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/834
Implement Connection Backoff Interop test. by madongfly · Pull Request #834 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM. Very clean, thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/835
Sync branch android to head. by madongfly · Pull Request #835 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We found a Contributor License Agreement for you (the sender of this pull request) and all commit authors, but as best as we can tell these commits were authored by someone else.  If that's the case,  please add them to this pull request and have them confirm that they're okay with these commits being contributed to Google.  If we're mistaken and you did author these commits, just reply here to confirm.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/836
Remove proto size restriction when parsing protos. by nmittler · Pull Request #836 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/837
Removing transport shutdown hooks from channel builder by nmittler · Pull Request #837 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly @ejona86 @zhangkun83 @carl-mastrangelo PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/838
Mark Compression API @Experimental · Issue #838 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Some pieces of compression are already checked in to master. There is a question if they will be api-stable in time for beta. We need to do something with what is checked in to release. Determining whether that is revert the changes or mark the API as @Experimental is the point of this issue.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/839
Add a "comment" attribute to ExperimentalApi · Issue #839 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We can attach link to the issue, doc or issue in there.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/840
Netty: Use status INTERNAL instead of UNKNOWN for underlying Http2Exception. by madongfly · Pull Request #840 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/841
Add some Unit tests to Abstract Client Stream by carl-mastrangelo · Pull Request #841 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/842
gRPC SSL Examples · Issue #842 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
Please advise on where I can find  java examples on client-server authentication for SSL?
Thank you.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/843
Avoid deprecation warning on import by madongfly · Pull Request #843 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/844
Update the code example to use our own API by madongfly · Pull Request #844 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/845
Fix Comment in MutableHandlerRegistry by carl-mastrangelo · Pull Request #845 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/846
Implement unimplemented_method test by zsurocking · Pull Request #846 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Fix #706
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/847
Fix documentation on ClientCall.request(). by zhangkun83 · Pull Request #847 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/848
Reconnect interop test is broken. · Issue #848 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
./interop-testing/build/install/grpc-interop-testing/bin/reconnect-test-client --use_okhttp=true
Starting test:
io.grpc.StatusRuntimeException: UNKNOWN
    at io.grpc.Status.asRuntimeException(Status.java:428)
    at io.grpc.stub.ClientCalls.getUnchecked(ClientCalls.java:154)
    at io.grpc.stub.ClientCalls.blockingUnaryCall(ClientCalls.java:104)
    at io.grpc.testing.integration.ReconnectServiceGrpc$ReconnectServiceBlockingStub.start(ReconnectServiceGrpc.java:127)
    at io.grpc.testing.integration.ReconnectTestClient.runTest(ReconnectTestClient.java:96)
    at io.grpc.testing.integration.ReconnectTestClient.main(ReconnectTestClient.java:123)
Caused by: java.lang.IllegalArgumentException: Unable to find decompressor for message encoding identity
    at com.google.common.base.Preconditions.checkArgument(Preconditions.java:145)
    at io.grpc.internal.AbstractStream.setDecompressor(AbstractStream.java:306)
    at io.grpc.internal.AbstractClientStream.inboundHeadersReceived(AbstractClientStream.java:122)
    at io.grpc.internal.Http2ClientStream.transportHeadersReceived(Http2ClientStream.java:106)
    at io.grpc.netty.NettyClientStream.transportHeadersReceived(NettyClientStream.java:113)
    at io.grpc.netty.NettyClientHandler.onHeadersRead(NettyClientHandler.java:202)
    at io.grpc.netty.NettyClientHandler.access$900(NettyClientHandler.java:78)
    at io.grpc.netty.NettyClientHandler$LazyFrameListener.onHeadersRead(NettyClientHandler.java:528)
    at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder$FrameReadListener.onHeadersRead(DefaultHttp2ConnectionDecoder.java:316)
    at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder$FrameReadListener.onHeadersRead(DefaultHttp2ConnectionDecoder.java:265)
    at io.netty.handler.codec.http2.Http2InboundFrameLogger$1.onHeadersRead(Http2InboundFrameLogger.java:54)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader$2.processFragment(DefaultHttp2FrameReader.java:450)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readHeadersFrame(DefaultHttp2FrameReader.java:459)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader.processPayloadState(DefaultHttp2FrameReader.java:226)
    at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readFrame(DefaultHttp2FrameReader.java:130)
    at io.netty.handler.codec.http2.Http2InboundFrameLogger.readFrame(Http2InboundFrameLogger.java:39)
    at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder.decodeFrame(DefaultHttp2ConnectionDecoder.java:100)
    at io.netty.handler.codec.http2.Http2ConnectionHandler$FrameDecoder.decode(Http2ConnectionHandler.java:293)
    at io.netty.handler.codec.http2.Http2ConnectionHandler.decode(Http2ConnectionHandler.java:336)
    at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
    at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
    at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
    at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:946)
    at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:127)
    at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:510)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:467)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:381)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:353)
    at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
    at java.lang.Thread.run(Thread.java:745)
Test failed!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/849
Travis fails due to un-run codegen · Issue #849 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
https://travis-ci.org/grpc/grpc-java/builds/76536465
# Changes not staged for commit:
#   (use "git add <file>..." to update what will be committed)
#   (use "git checkout -- <file>..." to discard changes in working directory)
#
#   modified:   interop-testing/src/generated/main/grpc/io/grpc/testing/integration/ReconnectServiceGrpc.java
#
no changes added to commit (use "git add" and/or "git commit -a")
Error Working directory is not clean. Forget to commit generated files?

The issue seems caused by an incomplete rebase with #826. The modified code-generated file just needs to be committed.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/850
Commit ReconnectServiceGrpc.java generated by current codegen. by zhangkun83 · Pull Request #850 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hmm how can grpc-protobuf:test be failed by this PR?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/851
Add SERVICE_NAME constant to service container by netdpb · Pull Request #851 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Huh. Oops. Yeah, that is useful :).
@zhangkun83, I'd feel more comfortable if you reviewed this.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/852
Netty: Call ClientTransport.Listener.transportReady() after receiving… by madongfly · Pull Request #852 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/853
Grpc client not invoking gRPC call after establishing SSL handshake (Using ALPN) · Issue #853 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
It seems that the SSL handshake is successful when the client try to establish a connection to the server. The log ends with the following at server-side:
io.netty.handler.ssl.SslHandler (SslHandler.java:setHandshakeSuccess(1251)) - [id: 0x7db3896c, /172.27.41.162:23913 => /172.27.44.228:7001] HANDSHAKEN: TLS_ECDHE_RSA_WITH_AES_128_GCM_SHA256
while the client side log ends with:
SETTINGS: ack=false, settings={HEADER_TABLE_SIZE=4096, ENABLE_PUSH=0, MAX_CONCURRENT_STREAMS=0, INITIAL_WINDOW_SIZE=66560, MAX_FRAME_SIZE=16384, MAX_HEADER_LIST_SIZE=2147483647}

However, after some tracing, the RPC methods that were invoked by the client, seemed to be stucked at  getUnchecked(Future future) in io.grpc.stub.Calls at this line where it does return future.get();
The client code to call the server is as follows:
boolean useTls = config.getString("use.ssl").equalsIgnoreCase("true") ? true : false;
InetAddress address = null;
    try {
        address = InetAddress.getByName(serverHost);
    } catch (UnknownHostException e) {
        // TODO Auto-generated catch block
        e.printStackTrace();
    }

    SslContext sslContext = null;
    if (useTls) {
        try {
            sslContext = GrpcSslContexts.forClient().trustManager(loadCert("serverselfsignedcert.pem","C:\\temp\\serverselfsignedcert.pem")).build();
        } catch (Exception ex) {
            throw new RuntimeException(ex);
        }
    }

    channel = NettyChannelBuilder
            .forAddress(new InetSocketAddress(address, serverPort))
            .streamWindowSize(65*1024).connectionWindowSize(65*1024)
            .negotiationType(
                    useTls ? NegotiationType.TLS
                            : NegotiationType.PLAINTEXT)
            .sslContext(sslContext).build();

    blockingStub = PeerImplGrpc.newBlockingStub(channel);

    ByteString byteStrKey = ByteString.copyFrom(HashUtil.encode("abc", serverHost.getBytes()));
    PeerId request = PeerId.newBuilder().setPeerId(byteStrKey).build();
    checkPeerAlive(request, response);
    Response test = blockingStub.checkPeerAlive(request);

I also amended the implementation of TestUtils loadCert method to the following:
public static File loadCert(String name, String path) throws IOException {
    FileInputStream in = new FileInputStream(new File(path));
    File tmpFile = File.createTempFile(name, "");
    tmpFile.deleteOnExit();

    BufferedWriter writer = new BufferedWriter(new FileWriter(tmpFile));
    try {
        int b;
        while ((b = in.read()) != -1) {
            writer.write(b);
        }
    } finally {
        writer.close();
        in.close();
    }

    return tmpFile;
}

Is there something that I might have missed out?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/854
{Channel,Server}.awaitTerminated should wait for application to complete processing · Issue #854 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
As we discussed, we were going to have awaitTerminated() wait until all application notifications execute. We can achieve that by tracking number of unclosed calls (clientcall or servercall): when creating a new call register it, and after the application listener's close is called de-register it. In awaitTerminated it would wait for the registrations to become empty/zero.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/855
Rename HttpUtil to GrpcUtil. by nmittler · Pull Request #855 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/856
Moving a few common utilities to GrpcUtil. by nmittler · Pull Request #856 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM.
But I see in some of the files the constants are static imported, in other files are referenced as GrpcUtil.XXX, should we keep a consistent style?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/857
MessageDeframer stalled logic needs review · Issue #857 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently there is a bug that results in the MessageDeframer not being stalled when stream is being closed (in error scenarios), resulting in the stream listener not being called immediately.  Specific lines of review include:
return unprocessed.readableBytes() > 0 || (nextFrame != null && nextFrame.readableBytes() > 0);
And a proposed change (WIP):
  stalled = (unprocessed.readableBytes() == 0);

  if (endOfStream) {
    if (!stalled) {
      listener.endOfStream();
    } else if (nextFrame != null || nextFrame.readableBytes() > 0) {//FIXME
      // We've received the entire stream and have data available but we don't have
      // enough to read the next frame ... this is bad.
      throw Status.INTERNAL.withDescription("Encountered end-of-stream mid-frame")
          .asRuntimeException();
    } else if (stalled) {
    }
  }
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/858
Use status UNAVAILABLE for IOException thrown by OkHttp reading path,… by madongfly · Pull Request #858 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/859
:grpc-protobuf:test fails frequently on Travis. · Issue #859 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/860
Reducing the size of the "large" proto in ProtoUtilsTest. by nmittler · Pull Request #860 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/861
Adding maxMessageSize config option by nmittler · Pull Request #861 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/862
OkHttp: Make sure TransportListener.transportReady() can only be call… by madongfly · Pull Request #862 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/863
Remove size restriction when parsing nano protos by madongfly · Pull Request #863 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/864
Quick work around for Rst bug by carl-mastrangelo · Pull Request #864 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/865
Update Java doc for a508c1d4f5024c2a5fd6d103edcab43542293ae7 by madongfly · Pull Request #865 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/866
Add a Shared Executor Service  by carl-mastrangelo · Pull Request #866 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/867
Make ServerImpl constructor pakcage-private by zhangkun83 · Pull Request #867 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/868
Makes application-provided string comes first in User-Agent. by madongfly · Pull Request #868 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/869
Minor cleanup in deframer by carl-mastrangelo · Pull Request #869 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/870
GrpcSslContext bug for mutual authentication  · Issue #870 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
My 1-way SSL authentication is working with the codes below, however, it doesn't seem to work for 2-way. I understand that by declaring the appropriate SslContext, we should be able to enable mutual authentication. I have already invoked the appropriate keyManager/trustManager, any idea why the mutual authentication did not take place?
I followed the steps to set up jetty ALPN at https://github.com/grpc/grpc-java/blob/master/SECURITY.md.

@ Server:
SslContext sslContext = GrpcSslContexts.forServer(new File(pathToOwnCertPemFile), new File(pathToOwnPrivateKeyPemFile)).trustManager(new File(pathToClientCertPemFile)).build();

ServerImpl server = NettyServerBuilder
        .forPort(port)
        .sslContext(sslContext)
        .addService(MyGrpc.bindService(new MyGrpcService()))
        .build().start();

@ Client:
SslContext sslContext = GrpcSslContexts.forClient().trustManager(new File(pathToServerCertPemFile)).keyManager(new File(pathToOwnCertPemFile), new File(pathToOwnPrivateKeyPemFile)).build();

ChannelImpl channel = NettyChannelBuilder.forAddress(host, port)
                .negotiationType(NegotiationType.TLS)
                .sslContext(sslContext).build();

blockingStub = MyGrpc.newBlockingStub(channel);

Upon inspection of the SSL debug logs, I noticed that the CertificateRequest message (as stated in https://en.wikipedia.org/wiki/Transport_Layer_Security#Client-authenticated_TLS_handshake), was never sent to the client to initiate the Client Authentication.
An excerpt of my server log is as follows:

*** ECDH ServerKeyExchange
Signature Algorithm SHA512withRSA
Server key: Sun EC public key, 256 bits
public x coord: 81392923578261760187813715443713168545877454618233337093852615933913992434989
public y coord: 26389586381130695169212775668808794166799180199461581135201001980310825571555
parameters: secp256r1 NIST P-256, X9.62 prime256v1
*** ServerHelloDone
[write] MD5 and SHA1 hashes: len = 1617
0000: 02 00 00 56 03 03 55 DF 34 10 9C 73 B5 00 C2 70 ...V..U.4..s...p
0010: FD B8 CC 36 5B 83 87 70 5B 74 A3 D2 AD B7 75 3B ...6[..p[t....u;

Am I missing out something? Or is it an inherent bug in gRPC?
Appreciate any advice on this problem.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/871
Determine API stability story for Android · Issue #871 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For Android, we are considering alternative transport implementations, for example, Cronet. That would imply we may not support OkHttp in the future. We need to be able to communicate the API stability of OkHttp's presence.
One possibility is that we have an Android-specific class that is able to choose the "correct" transport to use on Android. We would have to communicate that using OkHttp directly would not be API stable.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/872
Enforce content-type on client and server. by nmittler · Pull Request #872 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/873
Jmh Benchmarks don't work · Issue #873 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
$ gradle :grpc-benchmarks:jmh
Trying to run that results in a bunch of errors printed out to the screen.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/874
Design Auth to combine normal credentials with TLS creds · Issue #874 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
There is a want to guarantee that credentials are treated as a whole to guarantee invariants. For example, it is not appropriate to send a JWT over an unencrypted connection.
There may be other constraints that are missing, but it is not fully clear yet. I'll update the issue as more is known.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/875
InProcessTransport doesn't call onReady · Issue #875 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The in-process transport supports flow control and supports isReady(), but it never calls onReady(). It seems to be just an oversight/bug. Since the in-process transport connects immediately, onReady() should probably be called on the client immediately in newStream().
Locking will be a little interesting since for a single request() both client and server listeners may need to be called (because numMessages can be > 1). It looks like {client,server}Requested() could maybe return a boolean for whether {client,server}Requested > 0 && {client,server}Requested <= numMessages, which would imply onReady() should be called.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/876
Add comment field to ExperimentalApi by zhangkun83 · Pull Request #876 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/877
Add experimental api to compression by carl-mastrangelo · Pull Request #877 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM
Just the PR title is a little confusion, I thought you are adding new APIs before seeing the code.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/878
Document equals and hashCode on Status by carl-mastrangelo · Pull Request #878 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/879
Set Minimum Guava version to 18.0 · Issue #879 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Google internally was stuck using Guava 14.0 for legacy reasons, but it appears that the restriction has been lifted.  We should set the minimum supported guava version to 18 since the older one had bugs and  performance issues.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/880
Change ExperimentalApi field 'comment' to 'value' by carl-mastrangelo · Pull Request #880 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks! LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/881
Fixing the benchmarks by nmittler · Pull Request #881 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/882
Rename onValue to onNext in StreamObserver  by louiscryan · Pull Request #882 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@nmittler please review
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/883
Make ClientCall listener methods noops by carl-mastrangelo · Pull Request #883 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/884
Removing unused method in ServerImpl by nmittler · Pull Request #884 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/885
Make ServerCall.Listener methods Nops by carl-mastrangelo · Pull Request #885 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/886
Implement per_rpc_creds test by madongfly · Pull Request #886 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/887
OkHttp: race between sendCancel and sendFrame. · Issue #887 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If sendCancel is called (by timeout for example) before the stream is started, a following sendFrame will cause a NPE:
java.lang.NullPointerException
    at io.grpc.okhttp.OkHttpClientStream.sendFrame(OkHttpClientStream.java:197)
    at io.grpc.internal.AbstractClientStream.internalSendFrame(AbstractClientStream.java:199)
    at io.grpc.internal.AbstractStream$2.deliverFrame(AbstractStream.java:128)
    at io.grpc.internal.MessageFramer.commitToSink(MessageFramer.java:297)
    at io.grpc.internal.MessageFramer.flush(MessageFramer.java:255)
    at io.grpc.internal.AbstractStream.flush(AbstractStream.java:178)
    at io.grpc.ClientCallImpl.sendMessage(ClientCallImpl.java:213)
    at io.grpc.stub.ClientCalls$CallToStreamObserverAdapter.onNext(ClientCalls.java:210)
    at io.grpc.testing.integration.AbstractTransportTest.timeoutOnSleepingServer(AbstractTransportTest.java:843)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:57)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:606)
    at org.junit.runners.model.FrameworkMethod$1.runReflectiveCall(FrameworkMethod.java:47)
    at org.junit.internal.runners.model.ReflectiveCallable.run(ReflectiveCallable.java:12)
    at org.junit.runners.model.FrameworkMethod.invokeExplosively(FrameworkMethod.java:44)
    at org.junit.internal.runners.statements.InvokeMethod.evaluate(InvokeMethod.java:17)
    at org.junit.internal.runners.statements.FailOnTimeout$StatementThread.run(FailOnTimeout.java:74)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/888
Implement timeout_on_sleeping_server test by zsurocking · Pull Request #888 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Fixes #705
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/889
OkHttp: Fix race condition between sendCancel and sendFrame by madongfly · Pull Request #889 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/890
Remove the unnecessary code example of using TLS on Anroid by madongfly · Pull Request #890 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/891
Move grpc common examples by stanley-cheung · Pull Request #891 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thanks for your pull request.  It looks like this may be your first contribution to a Google open source project, in which case you'll need to sign a Contributor License Agreement (CLA).
📝 Please visit https://cla.developers.google.com/ to sign.
Once you've signed, please reply here (e.g. I signed it!) and we'll verify.  Thanks.


If you've already signed a CLA, it's possible we don't have your GitHub username or you're using a different email address.  Check your existing CLA data and verify that your email is set on your git commits.
If you signed the CLA as a corporation, please let us know the company's name.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/892
Add unit tests for AbstractServerStream by carl-mastrangelo · Pull Request #892 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/893
Fix flakiness in test timeoutOnSleepingServer by madongfly · Pull Request #893 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/894
Add a way to distinguish between advertised message encodings, and add tests by carl-mastrangelo · Pull Request #894 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo just so I understand ... what does "advertising an encoding" mean? I don't see any mention of it in the wire spec.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/895
Mark generated MethodDescriptors @ExperimentalAPI · Issue #895 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
For Android, we may want to lazy-create MethodDescriptors in order to prevent cascading of static initializations of all dependent protos for all methods. That would mean making accessor methods instead of static fields.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/896
Upgrade to protobuf3-b1 · Issue #896 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It's released. It's on Maven Central. It's required for beta.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/897
Trash HandlerRegistry.Method · Issue #897 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We only need the ServerMethodDefinition. ServerServiceDefinition requires a list of all contained methods, which would make it painful for proxies. So lookup should just return the method definition.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/898
Add authority to HandlerRegistry.lookupMethod · Issue #898 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It should be possible to do virtual hosting; that requires authority. It would just be an additional string to lookupMethod (presumably as the first parameter).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/899
Move io.grpc.stub.StreamRecorder to testing package · Issue #899 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It really is only used in testing. I'm not wild about the class in general, but reducing its usage to tests addresses the primary concerns.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/900
Remove the hack that generates nano package names. · Issue #900 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We should use a helper function from protobuf, which is more reliable, but not there yet (protocolbuffers/protobuf/issues/778)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/901
Upgrade to protobuf-3.0.0-beta-1 by zhangkun83 · Pull Request #901 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The nano generator from protobuf starts to add .nano to the message package names, while protobuf doesn't provide a helper function to get the proper class name for now. We have to use a hack to add nano for now. Protobuf team will add the helper function in the next release. (Tracking issue #900).
Protobuf also provide an in-file option to go back to the original package name. Because it is carried in the FileOptions which is a proto message, checking this option requires us to generate this C++ class thus would require some change to the build of grpc-compiler. Since protobuf team plans to eliminate this option for good, I don't think it's worth the effort to support it. @ejona86 WDYT?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/902
Draft of Android specific Channel builder by louiscryan · Pull Request #902 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/903
Annotate method descritpor files in the generated code with ExperimentalApi by zhangkun83 · Pull Request #903 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/904
Add test to prove RST closes stream, and remove hack from transport to force closure. by carl-mastrangelo · Pull Request #904 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/905
Fix broken interop test, using new StreamObserver API. by zsurocking · Pull Request #905 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/906
Upgrade to latest netty-tcnative by nmittler · Pull Request #906 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/907
Check javanano_use_deprecated_package in the message's FileDescriptor, not the current file's. by zhangkun83 · Pull Request #907 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/908
Update to protobuf beta for Android interop test by madongfly · Pull Request #908 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/909
ClientAuthInterceptor should signal callers on 401s · Issue #909 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If clients are signaled of 401s, they can do clean up by, for example, invalidating Credentials by calling GoogleAuthUtil.clearToken(Context, String);
https://developers.google.com/android/reference/com/google/android/gms/auth/GoogleAuthUtil.html#clearToken(android.content.Context, java.lang.String)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/910
Fields in MethodDescriptor can't be null by ejona86 · Pull Request #910 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/911
Move StreamRecorder to testing package. by madongfly · Pull Request #911 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/912
Ease use of JWT by passing URI to auth library by ejona86 · Pull Request #912 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/913
Build failed with exception "Failed to apply plugin [id 'com.google.protobuf']" · Issue #913 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I compile protobuf and grpc "by hand" for my system. protobuf is version 3.0.0-beta-1. protoc is in the PATH, and the lib, include and pkgconfig directories are set in CFLAGS, CPPFLAGS, LDFLAGS, LD_LIBRARY_PATH, and PKG_CONFIG_PATH, respectively. The compile of grpc-java worked with 0.7.1 and 0.7.2, but fails with 0.8.0. Here the grpc-java build log as far as it may help:
mkdir -p /data/emmenlau/thirdparty && \
    cd /data/emmenlau/thirdparty/ && \
    rm -fr grpc-java-0.8.0 && \
    tar -xzf /home/emmenlau/thirdparty/grpc-java-0.8.0.tar.gz && \
    cd grpc-java-0.8.0 && \
    export CFLAGS="-fPIC ${CFLAGS}" && \
    export CPPFLAGS="-fPIC ${CPPFLAGS}" && \
    export PATH="/data/emmenlau/thirdparty/bin:${PATH}" && \
    export CFLAGS="-I/data/emmenlau/thirdparty/include ${CFLAGS}" && \
    export CPPFLAGS="-I/data/emmenlau/thirdparty/include ${CPPFLAGS}" && \
    export LDFLAGS="-L/data/emmenlau/thirdparty/lib ${LDFLAGS}" && \
    export LD_LIBRARY_PATH="/data/emmenlau/thirdparty/lib:${LD_LIBRARY_PATH}" && \
    export PKG_CONFIG_PATH="/data/emmenlau/thirdparty/lib/pkgconfig:${PKG_CONFIG_PATH}" && \
    gradle build -x test

Download https://repo1.maven.org/maven2/org/kt3k/gradle/plugin/coveralls-gradle-plugin/2.0.1/coveralls-gradle-plugin-2.0.1.pom
Download https://repo1.maven.org/maven2/org/apache/httpcomponents/httpmime/4.3/httpmime-4.3.pom
Download https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-client/4.3/httpcomponents-client-4.3.pom
Download https://repo1.maven.org/maven2/org/apache/httpcomponents/project/7/project-7.pom
Download https://repo1.maven.org/maven2/org/codehaus/groovy/modules/http-builder/http-builder/0.7.1/http-builder-0.7.1.pom
Download https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.3/httpclient-4.3.pom
Download https://repo1.maven.org/maven2/net/sf/json-lib/json-lib/2.3/json-lib-2.3.pom
Download https://repo1.maven.org/maven2/net/sourceforge/nekohtml/nekohtml/1.9.16/nekohtml-1.9.16.pom
Download https://repo1.maven.org/maven2/xml-resolver/xml-resolver/1.2/xml-resolver-1.2.pom
Download https://repo1.maven.org/maven2/net/sf/ezmorph/ezmorph/1.0.6/ezmorph-1.0.6.pom
Download https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.3/httpcore-4.3.pom
Download https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcomponents-core/4.3/httpcomponents-core-4.3.pom
Download https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.pom
Download https://repo1.maven.org/maven2/org/kt3k/gradle/plugin/coveralls-gradle-plugin/2.0.1/coveralls-gradle-plugin-2.0.1.jar
Download https://repo1.maven.org/maven2/org/apache/httpcomponents/httpmime/4.3/httpmime-4.3.jar
Download https://repo1.maven.org/maven2/org/codehaus/groovy/modules/http-builder/http-builder/0.7.1/http-builder-0.7.1.jar
Download https://repo1.maven.org/maven2/org/apache/httpcomponents/httpclient/4.3/httpclient-4.3.jar
Download https://repo1.maven.org/maven2/net/sf/json-lib/json-lib/2.3/json-lib-2.3-jdk15.jar
Download https://repo1.maven.org/maven2/net/sourceforge/nekohtml/nekohtml/1.9.16/nekohtml-1.9.16.jar
Download https://repo1.maven.org/maven2/xml-resolver/xml-resolver/1.2/xml-resolver-1.2.jar
Download https://repo1.maven.org/maven2/net/sf/ezmorph/ezmorph/1.0.6/ezmorph-1.0.6.jar
Download https://repo1.maven.org/maven2/org/apache/httpcomponents/httpcore/4.3/httpcore-4.3.jar
Download https://repo1.maven.org/maven2/commons-logging/commons-logging/1.1.3/commons-logging-1.1.3.jar
Download https://repo1.maven.org/maven2/com/google/protobuf/protobuf-gradle-plugin/0.6.1/protobuf-gradle-plugin-0.6.1.pom
Download https://repo1.maven.org/maven2/com/google/protobuf/protobuf-gradle-plugin/0.6.1/protobuf-gradle-plugin-0.6.1.jar

FAILURE: Build failed with an exception.

* Where:
Build file '/data/emmenlau/TargetInfectX/screeningBee-ubuntu-x86_64-gcc4.9.2-tmp/screeningBee/Tools/BeeStorageProviderAPI/thirdparty/grpc-java-0.8.0/build.gradle' line: 63

* What went wrong:
A problem occurred evaluating project ':grpc-benchmarks'.
> Failed to apply plugin [id 'com.google.protobuf']
   > Could not generate a proxy class for class com.google.protobuf.gradle.ProtobufSourceDirectorySet.

* Try:
Run with --stacktrace option to get the stack trace. Run with --info or --debug option to get more log output.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/914
Refactoring channel API. by nmittler · Pull Request #914 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/915
Adding missing RunWith annotation for tests. by nmittler · Pull Request #915 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/916
Rename CHECK and FAIL macros to avoid conflict with internal macros when syncing back… by zhangkun83 · Pull Request #916 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/917
Hit the frame size limit of 100MB. Any way to increase this limit? · Issue #917 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
2015-09-01 16:14:57 WARN  ResumingStreamingResultScanner:103 - IOExceptionWithStatus:
com.google.cloud.bigtable.grpc.io.IOExceptionWithStatus: Error in response stream
at com.google.cloud.bigtable.grpc.scanner.ResultQueueEntry.getResponseOrThrow(ResultQueueEntry.java:66)
at com.google.cloud.bigtable.grpc.scanner.StreamingBigtableResultScanner$ResponseQueueReader.getNextMergedRow(StreamingBigtableResultScanner.java:75)
at com.google.cloud.bigtable.grpc.scanner.StreamingBigtableResultScanner.next(StreamingBigtableResultScanner.java:136)
at com.google.cloud.bigtable.grpc.scanner.StreamingBigtableResultScanner.next(StreamingBigtableResultScanner.java:1)
at com.google.cloud.bigtable.grpc.scanner.ResumingStreamingResultScanner.next(ResumingStreamingResultScanner.java:90)
at com.google.cloud.bigtable.grpc.scanner.ResumingStreamingResultScanner.next(ResumingStreamingResultScanner.java:1)
at com.google.cloud.bigtable.hbase.ReadFirstRow.getRow(ReadFirstRow.java:60)
at com.google.cloud.bigtable.hbase.ReadFirstRow.main(ReadFirstRow.java:109)
Caused by: io.grpc.StatusRuntimeException: INTERNAL: Exception deframing message
at io.grpc.Status.asRuntimeException(Status.java:428)
at io.grpc.stub.ClientCalls$StreamObserverToCallListenerAdapter.onClose(ClientCalls.java:264)
at io.grpc.ClientCallImpl$ClientStreamListenerImpl$3.run(ClientCallImpl.java:317)
at io.grpc.internal.SerializingExecutor$TaskRunner.run(SerializingExecutor.java:154)
at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1142)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:617)
at java.lang.Thread.run(Thread.java:745)
Caused by: io.grpc.StatusRuntimeException: INTERNAL: Frame size 155458981 exceeds maximum: 104857600,
at io.grpc.Status.asRuntimeException(Status.java:428)
at io.grpc.internal.MessageDeframer.processHeader(MessageDeframer.java:336)
at io.grpc.internal.MessageDeframer.deliver(MessageDeframer.java:239)
at io.grpc.internal.MessageDeframer.deframe(MessageDeframer.java:175)
at io.grpc.internal.AbstractStream.deframe(AbstractStream.java:270)
at io.grpc.internal.AbstractClientStream.inboundDataReceived(AbstractClientStream.java:154)
at io.grpc.internal.Http2ClientStream.transportDataReceived(Http2ClientStream.java:134)
at io.grpc.netty.NettyClientStream.transportDataReceived(NettyClientStream.java:119)
at io.grpc.netty.NettyClientHandler.onDataRead(NettyClientHandler.java:219)
at io.grpc.netty.NettyClientHandler.access$800(NettyClientHandler.java:79)
at io.grpc.netty.NettyClientHandler$LazyFrameListener.onDataRead(NettyClientHandler.java:546)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder$FrameReadListener.onDataRead(DefaultHttp2ConnectionDecoder.java:234)
at io.netty.handler.codec.http2.Http2InboundFrameLogger$1.onDataRead(Http2InboundFrameLogger.java:46)
at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readDataFrame(DefaultHttp2FrameReader.java:392)
at io.netty.handler.codec.http2.DefaultHttp2FrameReader.processPayloadState(DefaultHttp2FrameReader.java:223)
at io.netty.handler.codec.http2.DefaultHttp2FrameReader.readFrame(DefaultHttp2FrameReader.java:130)
at io.netty.handler.codec.http2.Http2InboundFrameLogger.readFrame(Http2InboundFrameLogger.java:39)
at io.netty.handler.codec.http2.DefaultHttp2ConnectionDecoder.decodeFrame(DefaultHttp2ConnectionDecoder.java:100)
at io.netty.handler.codec.http2.Http2ConnectionHandler$FrameDecoder.decode(Http2ConnectionHandler.java:293)
at io.netty.handler.codec.http2.Http2ConnectionHandler.decode(Http2ConnectionHandler.java:336)
at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
at io.netty.handler.ssl.SslHandler.unwrap(SslHandler.java:1069)
at io.netty.handler.ssl.SslHandler.decode(SslHandler.java:944)
at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:946)
at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:127)
at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:510)
at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:467)
at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:381)
at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:353)
at io.netty.util.concurrent.SingleThreadEventExecutor$4.run(SingleThreadEventExecutor.java:703)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/918
Display the required Protobuf version when building codegen by zhangkun83 · Pull Request #918 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/919
Make shared Executors daemons, and implement shutdownNow() by carl-mastrangelo · Pull Request #919 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/920
Upgrade protobuf-gradle-plugin to 0.7.0 in v0.8.x by zhangkun83 · Pull Request #920 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Resolves #913
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/921
Prevent status from impacting how ServerCall.Listener is invoked by ejona86 · Pull Request #921 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/922
Issues when generating server/client stubs from .proto files.  · Issue #922 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I've generated and ran client and server stubs painlessly for python using
protoc -I . --python_out=. --grpc_out=. --plugin=protoc-gen-grpc=which grpc_python_plugin <protofilename>
I've been trying t generate client stubs for android using
protoc  --java_out=output_folder --plugin=protoc-gen-grpc-java=/home/vagrant/grpc-java-0.8.0/compiler/build/binaries/java_pluginExecutable/protoc-gen-grpc-java  --grpc-java_out=output <protofilename>
Here's my .proto file https://gist.github.com/ybv/95debcb49169e8d8d3d1 After trying to codegen as specified in http://www.grpc.io/docs/tutorials/basic/java.html#generating-client-and-server-code and https://github.com/grpc/grpc-java/tree/master/compiler#compiling-and-testing-the-codegen using the command pasted above, I ended up with these files:
CleanText.java                 LCEProto.java                  TranslatedText.java            TransRequest.java CleanTextOrBuilder.java        LinkContentExtractorGrpc.java  TranslatedTextOrBuilder.java   TransRequestOrBuilder.java
When I try to make a new object (of my request message type) I couldn't set the object properties like this https://github.com/grpc/grpc-java/blob/master/examples/android/app/src/main/java/io/grpc/helloworldexample/HelloworldActivity.java#L64
Also it seems weird that my codegen has created different files for different messages, where as here, https://github.com/grpc/grpc-java/blob/master/examples/android/app/src/main/java/io/grpc/helloworldexample/HelloworldActivity.java#L17-L18 they seem to be classes inside the outer class? What am I missing here?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/923
Implement jwt_token_creds interop test by ejona86 · Pull Request #923 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/924
Require content-type in Headers or Trailers-only · Issue #924 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
By the Spec:

Implementations should expect broken deployments to send non-200 HTTP status codes in responses as well as a variety of non-GRPC content-types and to omit Status & Status-Message. Implementations must synthesize a Status & Status-Message to propagate to the application layer when this occurs.

It appears that unsupported Content Types (such as "text/html; charset=UTF-8") can be returned with error information from some servers, which would be useful to propagate.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/925
Create stable builders that use Netty, like is being done for Android · Issue #925 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
"Default" ChannelBuilder is the current proposed name. This would need to be in its own artifact because it would depend on Netty. It's unclear what its artifact and package name should be.
This is necessary because we are marking Netty's builders as @ExperimentalApi; we need a stable API for client and servers to use.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/926
NettyServer prematurely releases worker event loop · Issue #926 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
777e928 causes flaky server shutdown, as the individual transports out-live the server.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/927
ReferenceCounted is useless · Issue #927 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
777e928 introduced reference counting for channel builders, but nothing ever does a retain(), making it useless.
I thought the original reason to propose having reference counting was so that transports would retain() their factory and then ChannelImpl would release() the factory immediately on shutdown(). As the transports shutdown they would each release() and any shared resources would naturally be released.
@nmittler, FYI
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/928
Fix generated code reference for intellij projects. by madongfly · Pull Request #928 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/929
Document valid characters allowed in metadata keys by zhangkun83 · Pull Request #929 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@zhangkun83 there is a checkstyle failure, but otherwise LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/930
Remove HandlerRegistry.Method by carl-mastrangelo · Pull Request #930 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/931
Document valid characters for AsciiMarshaller by zhangkun83 · Pull Request #931 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/932
Supporting OpenSSL by nmittler · Pull Request #932 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/933
Tracking Issue for Handler Registry being experimental. · Issue #933 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We're currently marking all of the HandlerRegistries as ExperimentalAPI. We should decide on the appropriate interface and move toward making them public.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/934
Fix Travis breakage caused by checkStyle failure. by madongfly · Pull Request #934 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/935
Random Http2NettyTest.deadlineExceeded() failure. · Issue #935 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Saw this failure at https://travis-ci.org/grpc/grpc-java/builds/78476097, may wroth taking a look.
io.grpc.testing.integration.Http2NettyTest > deadlineExceeded FAILED
    java.lang.AssertionError: expected:<Status{code=DEADLINE_EXCEEDED, description=null, cause=null}> but was:<Status{code=UNKNOWN, description=null, cause=io.netty.util.IllegalReferenceCountException: refCnt: 0}>
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/936
Avoid using Parser in Proto · Issue #936 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Swap to passing in MessageLite instead of Parser in ProtoUtils. This would allow optimizing startup time to avoid creating the parser (today we would create the parser, but in the future we wouldn't need to).
(less obvious, but may still be a good idea) Rename Parser to MessageNanoFactory (with newInstance() method). Similiar reasoning to above, but would need nano changes to make possible (but there are several options for nano changes that we could use)

1 should be for beta. If we want to do 2, it should be for beta, but if it slips, we'll just deal with it and not do it.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/937
Replace use of ExecutorService with Executor in builders · Issue #937 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86
We don't depend on ExecutorService so we can downgrade the requirement here.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/938
Add a missing channel builder methods not copied in b687bdc by ejona86 · Pull Request #938 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM ... thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/939
Add an authority header to HandlerRegistry.lookupMethod by carl-mastrangelo · Pull Request #939 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM ... why are we adding it to the api if it's not being used?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/940
Enabling openssl in interop-testing scripts by nmittler · Pull Request #940 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/941
Update comment in MethodDescriptor.Marshaller by carl-mastrangelo · Pull Request #941 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I had a different understanding of the change requested in #722, "Marshaller should use 'deserializing' rather than parsing." I thought that meant instead of:

A typed abstraction over message parsing and serialization.

We would have:

A typed abstraction over message serialization and deserialization.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/942
Daemonize shared threads, and make sure each thread has a name by carl-mastrangelo · Pull Request #942 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM. Note that the daemonizing work is not complete. There are OkHttp and Netty threads that also must be marked daemon.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/943
Use Executor in stable builder APIs instead of ExecutorService by louiscryan · Pull Request #943 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@louiscryan LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/944
Daemonize OkHttp and Netty by carl-mastrangelo · Pull Request #944 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/945
Daemonize InProcess threads by carl-mastrangelo · Pull Request #945 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM. Those threads are expected to be very short lived, but it doesn't hurt.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/946
Support SSL mutual authentication · Issue #946 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Reported by @megapowers
Hi all,
I am currently using gRPC 8.0 with ALPN and I am trying to implement a 2-way SSL authentication between a client and server.
However, upon inspection of the SSL debug logs, I noticed that the CertificateRequest message (as stated in https://en.wikipedia.org/wiki/Transport_Layer_Security#Client-authenticated_TLS_handshake), was never sent to the client to initiate the Client Authentication.
An excerpt of my server log is as follows:
...
*** ECDH ServerKeyExchange
Signature Algorithm SHA512withRSA
Server key: Sun EC public key, 256 bits
public x coord: 81392923578261760187813715443713168545877454618233337093852615933913992434989
public y coord: 26389586381130695169212775668808794166799180199461581135201001980310825571555
parameters: secp256r1 NIST P-256, X9.62 prime256v1
*** ServerHelloDone
[write] MD5 and SHA1 hashes: len = 1617
0000: 02 00 00 56 03 03 55 DF 34 10 9C 73 B5 00 C2 70 ...V..U.4..s...p
0010: FD B8 CC 36 5B 83 87 70 5B 74 A3 D2 AD B7 75 3B ...6[..p[t....u;
...

The code I am using at server is as follows:
SslContext sslContext = GrpcSslContexts.forServer(new File(pathToOwnCertPemFile), new File(pathToOwnPrivateKeyPemFile)).trustManager(new File(pathToClientCertPemFile)).build();

ServerImpl server = NettyServerBuilder
.forPort(port)
.sslContext(sslContext)
.addService(MyGrpc.bindService(new MyGrpcService()))
.build().start();
The code I am using at my client is as follows:
SslContext sslContext = GrpcSslContexts.forClient().trustManager(new File(pathToServerCertPemFile)).keyManager(new File(pathToOwnCertPemFile), new File(pathToOwnPrivateKeyPemFile)).build();

ChannelImpl channel = NettyChannelBuilder.forAddress(host, port)
.negotiationType(NegotiationType.TLS)
.sslContext(sslContext).build();

blockingStub = MyGrpc.newBlockingStub(channel);
asyncStub = MyGrpc.newStub(channel);
Am I missing out something? Or is it an inherent bug in gRPC?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/947
Remove Metadata.Headers and Metadata.Trailers by carl-mastrangelo · Pull Request #947 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/948
Only release event loops when unused by ejona86 · Pull Request #948 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/949
Revert "Merge pull request #940 from nmittler/interop_openssl" by ejona86 · Pull Request #949 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/950
When tcnative is enabled, OkHttp tests timeout · Issue #950 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It fails like https://travis-ci.org/grpc/grpc-java/builds/78663746 . #949 reverted the change. It is unclear what the issue is.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/951
Update auth library to fix jwt_token_creds interop test by ejona86 · Pull Request #951 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/952
okhttp: Skip trash data for finished stream. · Issue #952 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Otherwise the remaining data would pollute the next read.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/953
Port test cases in AbstractTransportTest to android interop test by zsurocking · Pull Request #953 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/954
Replace Parser in proto utils to instance-based API by ejona86 · Pull Request #954 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/955
Travis OOM · Issue #955 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
https://travis-ci.org/grpc/grpc-java/builds/78680055
May be due to addition of Android build. It doesn't yet consistently fail, but we can use this for tracking.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/956
okhttp: Skip trash data for finished stream. by madongfly · Pull Request #956 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/957
Make android interop test buildable by Travis. by madongfly · Pull Request #957 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
FYI - Not sure we should commit this just yet. Requiring the android SDK has made building unstable for some folks
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/958
Remove uncessary javaee_api dependency as it causes trouble on androi… by zsurocking · Pull Request #958 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/959
Cannot compile Android targets · Issue #959 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When trying to do a gradle build from a clean client, I get the following error:
Creating configuration testReleasePublish.
Creating configuration testReleaseProvided.
Creating configuration testReleaseWearApp.
Build tools null missing. Downloading...
Failed to notify ProjectEvaluationListener.afterEvaluate(), but primary configuration failure takes precedence.
org.gradle.internal.event.ListenerNotificationException: Failed to notify project evaluation listener.
    at org.gradle.internal.event.BroadcastDispatch.dispatch(BroadcastDispatch.java:98)
    at org.gradle.internal.event.BroadcastDispatch.dispatch(BroadcastDispatch.java:31)
    at org.gradle.messaging.dispatch.ProxyDispatchAdapter$DispatchingInvocationHandler.invoke(ProxyDispatchAdapter.java:93)
    at com.sun.proxy.$Proxy11.afterEvaluate(Unknown Source)
    at org.gradle.configuration.project.LifecycleProjectEvaluator.notifyAfterEvaluate(LifecycleProjectEvaluator.java:67)
    at org.gradle.configuration.project.LifecycleProjectEvaluator.evaluate(LifecycleProjectEvaluator.java:61)
    at org.gradle.api.internal.project.AbstractProject.evaluate(AbstractProject.java:488)
    at org.gradle.api.internal.project.AbstractProject.evaluate(AbstractProject.java:86)
...


Cause 1: java.lang.NullPointerException: Cannot invoke method startsWith() on null object
    at org.codehaus.groovy.runtime.NullObject.invokeMethod(NullObject.java:88)
    at org.codehaus.groovy.runtime.callsite.PogoMetaClassSite.call(PogoMetaClassSite.java:45)
    at org.codehaus.groovy.runtime.callsite.CallSiteArray.defaultCall(CallSiteArray.java:45)
    at org.codehaus.groovy.runtime.callsite.NullCallSite.call(NullCallSite.java:32)
    at org.codehaus.groovy.runtime.callsite.CallSiteArray.defaultCall(CallSiteArray.java:45)
    at org.codehaus.groovy.runtime.callsite.PogoMetaClassSite.call(PogoMetaClassSite.java:54)
    at org.codehaus.groovy.runtime.callsite.AbstractCallSite.call(AbstractCallSite.java:116)
    at com.jakewharton.sdkmanager.internal.PackageResolver.resolveCompileVersion(PackageResolver.groovy:101)
    at com.jakewharton.sdkmanager.internal.PackageResolver.resolve(PackageResolver.groovy:60)
    at com.jakewharton.sdkmanager.internal.PackageResolver$resolve$0.call(Unknown Source)

...
Cause 2: java.lang.IllegalStateException: buildToolsVersion is not specified.
    at com.google.common.base.Preconditions.checkState(Preconditions.java:176)
    at com.android.build.gradle.BasePlugin.createAndroidTasks(BasePlugin.groovy:444)
    at com.android.build.gradle.BasePlugin$_createTasks_closure13_closure17.doCall(BasePlugin.groovy:415)
    at com.android.build.gradle.BasePlugin$_createTasks_closure13_closure17.doCall(BasePlugin.groovy)
    at sun.reflect.NativeMethodAccessorImpl.invoke0(Native Method)
    at sun.reflect.NativeMethodAccessorImpl.invoke(NativeMethodAccessorImpl.java:62)
    at sun.reflect.DelegatingMethodAccessorImpl.invoke(DelegatingMethodAccessorImpl.java:43)
    at java.lang.reflect.Method.invoke(Method.java:483)
    at org.codehaus.groovy.reflection.CachedMethod.invoke(CachedMethod.java:90)
    at groovy.lang.MetaMethod.doMethodInvoke(MetaMethod.java:324)

....

* Where:
Build file '/tmp/grpc-java/android/delegate.gradle' line: 14

* What went wrong:
A problem occurred evaluating root project 'android'.
> org/gradle/api/publication/maven/internal/DefaultMavenFactory

When running with --stacktrace:
Caused by: java.lang.NoClassDefFoundError: org/gradle/api/publication/maven/internal/DefaultMavenFactory
    at org.gradle.api.plugins.AndroidMavenPlugin.apply(AndroidMavenPlugin.java:88)
    at org.gradle.api.plugins.AndroidMavenPlugin.apply(AndroidMavenPlugin.java:57)
    at org.gradle.api.internal.plugins.ImperativeOnlyPluginApplicator.applyImperative(ImperativeOnlyPluginApplicator.java:35)
    at org.gradle.api.internal.plugins.RuleBasedPluginApplicator.applyImperative(RuleBasedPluginApplicator.java:43)
    at org.gradle.api.internal.plugins.DefaultPluginManager.doApply(DefaultPluginManager.java:144)
    at org.gradle.api.internal.plugins.DefaultPluginManager.apply(DefaultPluginManager.java:112)
    at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction.applyType(DefaultObjectConfigurationAction.java:113)
    at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction.access$200(DefaultObjectConfigurationAction.java:36)
    at org.gradle.api.internal.plugins.DefaultObjectConfigurationAction$3.run(DefaultObjectConfigurationAction.java:80)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/960
Revert "Draft of Android specific Channe builder" by louiscryan · Pull Request #960 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
FYI, if you feel comfortable bumping the min gradle version to 2.4 or 2.5, you may not need to revert this.  (or if possible, selectively pick the dependency based on the current gradle version).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/961
Let transports be service providers for generic usage by ejona86 · Pull Request #961 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/962
Fix flow-control documentation on Stream by zhangkun83 · Pull Request #962 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/963
Adding tc_native to interop test scripts by nmittler · Pull Request #963 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/964
okhttp: Skip trash data for finished stream. by madongfly · Pull Request #964 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/965
Support using client and server with existing FDs · Issue #965 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is the Java equivalent of grpc/grpc#3250.
I think this may just be Netty work; we could possibly enhance the epoll transport to have an address time that allows specifying the fd int directly.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/966
Defer explicit flushing of messages written during the onReady callback. by louiscryan · Pull Request #966 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/967
Update examples in light of daemon threads · Issue #967 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
At the very least, the hello world server example is broken, because it exits immediately. It needs a call to server.awaitTerminated(). This was caused by the swapping to daemon threads in 07a7279.
As reported on StackOverflow.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/968
java.lang.NoClassDefFoundError: com.squareup.okhttp.internal.spdy.Http2 · Issue #968 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
when launch to the following line[ HelloReply reply = stub.sayHello(message) ] , runtime exception occurs,java.lang.NoClassDefFoundError: com.squareup.okhttp.internal.spdy.Http2
Following the the MainActivity:
package grpc.pm.com.grpcclient;

import android.os.AsyncTask;
import android.support.v7.app.ActionBarActivity;
import android.os.Bundle;
import android.util.Log;
import android.view.View;
import android.widget.Button;
import android.widget.EditText;
import android.widget.TextView;

import com.squareup.okhttp.ConnectionSpec;

import java.util.concurrent.TimeUnit;

import io.grpc.ManagedChannel;
import io.grpc.examples.GreeterGrpc;
import io.grpc.examples.nano.Helloworld.HelloRequest;
import io.grpc.examples.nano.Helloworld.HelloReply;
import io.grpc.okhttp.NegotiationType;
import io.grpc.okhttp.OkHttpChannelBuilder;


public class MainActivity extends ActionBarActivity {
    Button mBtn;
    EditText mSendText;
    TextView mResult;
    public static final String TAG = "MainActivity";

    public void findViewById(){
        mBtn = (Button) findViewById(R.id.sendBtn);
        mSendText = (EditText) findViewById(R.id.sendEt);
        mResult = (TextView) findViewById(R.id.result);
    }

    @Override
    protected void onCreate(Bundle savedInstanceState) {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        findViewById();

        initView();

        mBtn.setOnClickListener(new View.OnClickListener() {
            @Override
            public void onClick(View v) {
                sendToServer();
            }
        });

        Thread.setDefaultUncaughtExceptionHandler(new Thread.UncaughtExceptionHandler() {
            @Override
            public void uncaughtException(Thread thread, final Throwable ex) {

                ex.printStackTrace();
                System.exit(0);
            }
        });

    }

    public void initView(){

    }

    public void sendToServer(){
        mBtn.setEnabled(false);
        new GrpcTask().execute();

        /*new Thread(new Runnable() {
            String mHost = "192.168.1.2";
            String mText = mSendText.getText().toString();
            int mPort = 50051;
            @Override
            public void run() {
                ManagedChannel channel = OkHttpChannelBuilder.forAddress(mHost, mPort).build();
                HelloRequest message = new HelloRequest();
                message.name = mText;
                GreeterGrpc.GreeterBlockingStub stub = GreeterGrpc.newBlockingStub(channel);
                HelloReply reply = stub.sayHello(message);
                String res = reply.message;
                Log.d(TAG,res);
                mResult.setText(res);
            }
        }).start();*/
    }

    private class GrpcTask extends AsyncTask<Void, Void, String> {
        private String mHost;
        private String mMessage;
        private int mPort;
        private ManagedChannel mChannel;

        @Override
        protected void onPreExecute() {
            mHost ="192.168.1.2";
            mPort = 50051;
            mMessage = mSendText.getText().toString();
            mResult.setText("");
        }

        private String sayHello(ManagedChannel channel) {
            GreeterGrpc.GreeterBlockingStub stub = GreeterGrpc.newBlockingStub(channel);
            HelloRequest message = new HelloRequest();
            message.name = mMessage;
            HelloReply reply = stub.sayHello(message);
            Log.d(TAG, "send successfully");
            return reply.message;
        }

        @Override
        protected String doInBackground(Void... nothing) {
            try {
                Log.d(TAG,"doInBackground begin......");
                OkHttpChannelBuilder builder = OkHttpChannelBuilder.forAddress(mHost, mPort);
                //builder = builder.connectionSpec(ConnectionSpec.CLEARTEXT);
                builder = builder.negotiationType(NegotiationType.PLAINTEXT);
                mChannel =  builder.build();
                String res = sayHello(mChannel);
                return res;
            } catch (Exception e) {
                e.printStackTrace();
                return "sayHello Failed... : " + e.getMessage();
            }
        }

        @Override
        protected void onPostExecute(String result) {
            try {
                Log.d(TAG, "onPostExecute"+result);
                mChannel.shutdown().awaitTermination(1, TimeUnit.SECONDS);
            } catch (Exception e) {
                Thread.currentThread().interrupt();
            }
            mResult.setText(result);
            mSendText.setEnabled(true);
        }
    }

}
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/969
Move decompressor setting to Server Impl by carl-mastrangelo · Pull Request #969 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/970
Update server to await termination in the main thread by carl-mastrangelo · Pull Request #970 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@carl-mastrangelo, LGTM, but this does not fix #967. Please verify the other examples as well; I know routeguide is also broken.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/971
Add an example compressing client by carl-mastrangelo · Pull Request #971 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/972
Squash generics by carl-mastrangelo · Pull Request #972 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/973
Running ./gradlew build leaves behind a javadoc/ directory · Issue #973 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This makes it difficult to do a "git add ." command after running tests.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/974
Error during servers-side TLS negotiation leads to erroneous stacktrace · Issue #974 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Due to the fact that we always register the HTTP/2 handler on the server side, if a TLS error causes forced shutdown of the connection, the HTTP/2 handler also dumps a stacktrace which is not helpful and could be confusing to the user:
Sep 08, 2015 1:21:09 PM io.grpc.netty.ProtocolNegotiators$1 fail
WARNING: TLS negotiation failed for new client. OpenSSL version: 0x1000105f [OpenSSL 1.0.1e 11 Feb 2013]. ALPN supported: false. Enabled ciphers=[TLS_ECDHE_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDHE_RSA_WITH_AES_128_CBC_SHA, TLS_RSA_WITH_AES_128_CBC_SHA, TLS_ECDH_ECDSA_WITH_AES_128_CBC_SHA, TLS_ECDH_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_RSA_WITH_AES_128_CBC_SHA, TLS_DHE_DSS_WITH_AES_128_CBC_SHA, TLS_ECDHE_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_RSA_WITH_3DES_EDE_CBC_SHA, TLS_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_ECDSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDH_RSA_WITH_3DES_EDE_CBC_SHA, TLS_ECDHE_ECDSA_WITH_RC4_128_SHA, TLS_ECDHE_RSA_WITH_RC4_128_SHA, TLS_RSA_WITH_RC4_128_SHA, TLS_ECDH_ECDSA_WITH_RC4_128_SHA, TLS_ECDH_RSA_WITH_RC4_128_SHA, TLS_RSA_WITH_RC4_128_MD5, TLS_RSA_WITH_RC4_128_MD5]. 
java.lang.Exception: Failed protocol negotiation: Unable to find compatible protocol.
    at io.grpc.netty.ProtocolNegotiators$1.userEventTriggered(ProtocolNegotiators.java:105)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeUserEventTriggeredNow(ChannelHandlerInvokerUtil.java:75)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeUserEventTriggered(DefaultChannelHandlerInvoker.java:135)
    at io.netty.channel.AbstractChannelHandlerContext.fireUserEventTriggered(AbstractChannelHandlerContext.java:149)
    at io.netty.handler.ssl.SslHandler.setHandshakeSuccess(SslHandler.java:1240)
    at io.netty.handler.ssl.SslHandler.setHandshakeSuccessIfStillHandshaking(SslHandler.java:1219)
    at io.netty.handler.ssl.SslHandler.wrapNonAppData(SslHandler.java:613)
    at io.netty.handler.ssl.SslHandler.unwrap(SslHandler.java:1061)
    at io.netty.handler.ssl.SslHandler.decode(SslHandler.java:965)
    at io.netty.handler.codec.ByteToMessageDecoder.callDecode(ByteToMessageDecoder.java:327)
    at io.netty.handler.codec.ByteToMessageDecoder.channelRead(ByteToMessageDecoder.java:230)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelReadNow(ChannelHandlerInvokerUtil.java:83)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelRead(DefaultChannelHandlerInvoker.java:153)
    at io.netty.channel.AbstractChannelHandlerContext.fireChannelRead(AbstractChannelHandlerContext.java:157)
    at io.netty.channel.DefaultChannelPipeline.fireChannelRead(DefaultChannelPipeline.java:946)
    at io.netty.channel.nio.AbstractNioByteChannel$NioByteUnsafe.read(AbstractNioByteChannel.java:125)
    at io.netty.channel.nio.NioEventLoop.processSelectedKey(NioEventLoop.java:510)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeysOptimized(NioEventLoop.java:467)
    at io.netty.channel.nio.NioEventLoop.processSelectedKeys(NioEventLoop.java:381)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:353)
    at io.netty.util.concurrent.SingleThreadEventExecutor$5.run(SingleThreadEventExecutor.java:742)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
    at java.lang.Thread.run(Thread.java:745)

Sep 08, 2015 1:21:09 PM io.netty.handler.codec.http2.Http2ConnectionHandler processGoAwayWriteResult
SEVERE: Sending GOAWAY failed: lastStreamId '0', errorCode '0', debugData ''. Forcing shutdown of the connection.
javax.net.ssl.SSLException: SSLEngine closed already

Sep 08, 2015 1:21:09 PM io.grpc.netty.NettyServerHandler onConnectionError
WARNING: Connection Error
io.netty.handler.codec.http2.Http2Exception: HTTP/2 client preface string missing or corrupt. Hex dump for received bytes: 
    at io.netty.handler.codec.http2.Http2Exception.connectionError(Http2Exception.java:82)
    at io.netty.handler.codec.http2.Http2ConnectionHandler$PrefaceDecoder.readClientPrefaceString(Http2ConnectionHandler.java:322)
    at io.netty.handler.codec.http2.Http2ConnectionHandler$PrefaceDecoder.decode(Http2ConnectionHandler.java:263)
    at io.netty.handler.codec.http2.Http2ConnectionHandler.decode(Http2ConnectionHandler.java:445)
    at io.netty.handler.codec.ByteToMessageDecoder.decodeLast(ByteToMessageDecoder.java:382)
    at io.netty.handler.codec.ByteToMessageDecoder.channelInactive(ByteToMessageDecoder.java:286)
    at io.netty.handler.codec.http2.Http2ConnectionHandler.channelInactive(Http2ConnectionHandler.java:421)
    at io.grpc.netty.NettyServerHandler.channelInactive(NettyServerHandler.java:230)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelInactiveNow(ChannelHandlerInvokerUtil.java:56)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelInactive(DefaultChannelHandlerInvoker.java:92)
    at io.netty.channel.AbstractChannelHandlerContext.fireChannelInactive(AbstractChannelHandlerContext.java:135)
    at io.netty.channel.ChannelInboundHandlerAdapter.channelInactive(ChannelInboundHandlerAdapter.java:75)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelInactiveNow(ChannelHandlerInvokerUtil.java:56)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelInactive(DefaultChannelHandlerInvoker.java:92)
    at io.netty.channel.AbstractChannelHandlerContext.fireChannelInactive(AbstractChannelHandlerContext.java:135)
    at io.netty.handler.codec.ByteToMessageDecoder.channelInactive(ByteToMessageDecoder.java:306)
    at io.netty.handler.ssl.SslHandler.channelInactive(SslHandler.java:706)
    at io.netty.channel.ChannelHandlerInvokerUtil.invokeChannelInactiveNow(ChannelHandlerInvokerUtil.java:56)
    at io.netty.channel.DefaultChannelHandlerInvoker.invokeChannelInactive(DefaultChannelHandlerInvoker.java:92)
    at io.netty.channel.AbstractChannelHandlerContext.fireChannelInactive(AbstractChannelHandlerContext.java:135)
    at io.netty.channel.DefaultChannelPipeline.fireChannelInactive(DefaultChannelPipeline.java:928)
    at io.netty.channel.AbstractChannel$AbstractUnsafe$7.run(AbstractChannel.java:674)
    at io.netty.util.concurrent.SingleThreadEventExecutor.runAllTasks(SingleThreadEventExecutor.java:339)
    at io.netty.channel.nio.NioEventLoop.run(NioEventLoop.java:356)
    at io.netty.util.concurrent.SingleThreadEventExecutor$5.run(SingleThreadEventExecutor.java:742)
    at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1145)
    at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:615)
    at java.lang.Thread.run(Thread.java:745)

The first stacktrace is correct, but the second one is thrown by the HTTP/2 handler's deactivated logic.
We might consider waiting until the TLS negotiation succeeds before registering the HTTP/2 handler.  This should be safe since the server will not be sending anything until it begins receiving data.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/975
Mark ServerCalls, MethodDescriptor.create, MethodDescriptor.Marshaller and a few others ExperimentalApi · Issue #975 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
These are generally used by the generated code. There are some plans for doing Android-driven performance work on the generated code, and there are some options being discussed that would impact these APIs.
For beta, we've agreed that it is fine for generated code to depend on ExperimentalApi. For GA, that will not be allowed to be the case.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/976
Use service provider for server-side  · Issue #976 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is effectively #961 for getting a ServerBuilder. It would only use Netty today.
Whether we extend the current ManagedChannelProvider to allow creating server builders or make a parallel path is up for discussion, but honestly we should just flip a coin and go with one.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/977
Use stub call options for compression by carl-mastrangelo · Pull Request #977 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/978
Fixing erroneous server log when TLS nego fails by nmittler · Pull Request #978 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/979
Fixing okhttp hang when TLS nego fails. by nmittler · Pull Request #979 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@madongfly @ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/980
Add client-side logging for TLS negotiation. by nmittler · Pull Request #980 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/981
VC++ building info seems out of date · Issue #981 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The Visual C++ Protobuf link in ./COMPILING.md seems broken. The following Visual C++ section also needs some update with the default include and lib paths.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/982
Add proper generics to ManagedChannelProvider by carl-mastrangelo · Pull Request #982 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
oof ... thanks :)
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/983
Recommend OpenSSL in  SECURITY.md by nmittler · Pull Request #983 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 PTAL
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/984
Enable warnings for rawtypes by ejona86 · Pull Request #984 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/985
StreamObserver.onError(Throwable t) hard to use or unintuitive · Issue #985 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
public interface StreamObserver<V>  {
  void onError(Throwable t);
  // ... more methods declared.
}
For client calls with streaming responses, when could the error be a Throwable and not a Status?
It seems more fitting that onError(..) would take a Status instead.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/986
StreamObserver used also for unary calls · Issue #986 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
StreamObserver is used for all responses, even when the response is not a stream. To easier understand the generated API it'd be better if unary responses would be treated as such and have a different Observer that suggests that there will only be one response.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/987
Reduce API surface of AbstractStub by ejona86 · Pull Request #987 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/988
Add a server Provider by carl-mastrangelo · Pull Request #988 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/989
PARSER has private access · Issue #989 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am using protoc-3.0.0-beta-1-win32 and protoc-gen-grpc-java-0.7.2-windows-x86_64.exe to generate code from a proto file. But the Grpc file has this line "io.grpc.protobuf.ProtoUtils.marshaller(grpc.grpcsvc.Grpcsvc.HelloRequest.PARSER)". Then java compiler complains because PARSER has private access in another generated file. Am I using the wrong protoc or plugin?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/990
Prevent construction of container classes and reduce API by ejona86 · Pull Request #990 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@ejona86 LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/991
Http2OkHttpTest.receivedDataForFinishedStream is flaky · Issue #991 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
As seen in: https://travis-ci.org/grpc/grpc-java/builds/79687899
io.grpc.testing.integration.Http2OkHttpTest > receivedDataForFinishedStream FAILED
    java.lang.Exception: test timed out after 10000 milliseconds
        at sun.misc.Unsafe.park(Native Method)
        at java.util.concurrent.locks.LockSupport.park(LockSupport.java:175)
        at java.util.concurrent.locks.AbstractQueuedSynchronizer.parkAndCheckInterrupt(AbstractQueuedSynchronizer.java:836)
        at java.util.concurrent.locks.AbstractQueuedSynchronizer.doAcquireSharedInterruptibly(AbstractQueuedSynchronizer.java:997)
        at java.util.concurrent.locks.AbstractQueuedSynchronizer.acquireSharedInterruptibly(AbstractQueuedSynchronizer.java:1304)
        at com.google.common.util.concurrent.AbstractFuture$Sync.get(AbstractFuture.java:285)
        at com.google.common.util.concurrent.AbstractFuture.get(AbstractFuture.java:116)
        at io.grpc.stub.ClientCalls.getUnchecked(ClientCalls.java:149)
        at io.grpc.stub.ClientCalls.blockingUnaryCall(ClientCalls.java:104)
        at io.grpc.testing.integration.TestServiceGrpc$TestServiceBlockingStub.emptyCall(TestServiceGrpc.java:210)
        at io.grpc.testing.integration.AbstractTransportTest.emptyUnary(AbstractTransportTest.java:155)
        at io.grpc.testing.integration.Http2OkHttpTest.receivedDataForFinishedStream(Http2OkHttpTest.java:118)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/992
Discourage users from running the codegen for the example by ejona86 · Pull Request #992 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/993
Enable license header checking in checkstyle by ejona86 · Pull Request #993 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/994
Implement cork/uncork in client and server calls · Issue #994 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
By adding a cork/uncork to defer flushing messages we can significantly improve throughput for streaming operations when messages sizes are significantly smaller than the flow-control window
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/995
Mark classes in testing as ExperimentalApi by ejona86 · Pull Request #995 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/996
Basic implementation of corking by louiscryan · Pull Request #996 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TLDR;  Impact is significant across the board but in particular it helps in the non-direct executor case significantly more
With corking
Benchmark                                                          (channelCount)  (clientExecutor)  (maxConcurrentStreams)  (responseSize)   Mode  Cnt        Score        Error  Units
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1           DEFAULT                       1           SMALL  thrpt   20   748010.445 ±  11056.456  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1           DEFAULT                       2           SMALL  thrpt   20   787603.691 ±   9216.387  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1           DEFAULT                      10           SMALL  thrpt   20   833604.307 ±  20504.497  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1           DEFAULT                     100           SMALL  thrpt   20   747409.964 ±  20994.393  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1            DIRECT                       1           SMALL  thrpt   20  1182869.604 ±  61495.293  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1            DIRECT                       2           SMALL  thrpt   20  1039064.457 ±  20749.094  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1            DIRECT                      10           SMALL  thrpt   20  1085170.265 ±  24539.003  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1            DIRECT                     100           SMALL  thrpt   20   910051.011 ±  74268.573  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2           DEFAULT                       1           SMALL  thrpt   20  1444956.843 ±  81101.309  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2           DEFAULT                       2           SMALL  thrpt   20  1609690.720 ± 108433.473  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2           DEFAULT                      10           SMALL  thrpt   20  1560337.018 ± 152004.123  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2           DEFAULT                     100           SMALL  thrpt   20  1379330.221 ± 112759.558  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2            DIRECT                       1           SMALL  thrpt   20  1672837.571 ±  70588.569  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2            DIRECT                       2           SMALL  thrpt   20  1769621.126 ±  33891.535  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2            DIRECT                      10           SMALL  thrpt   20  1716542.116 ±  49576.274  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2            DIRECT                     100           SMALL  thrpt   20  1459977.770 ±  31524.513  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4           DEFAULT                       1           SMALL  thrpt   20  2758350.501 ±  90416.723  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4           DEFAULT                       2           SMALL  thrpt   20  2868168.313 ± 103377.954  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4           DEFAULT                      10           SMALL  thrpt   20  2584746.771 ±  88402.278  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4           DEFAULT                     100           SMALL  thrpt   20  2127286.038 ±  93638.693  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4            DIRECT                       1           SMALL  thrpt   20   824270.235 ±  26016.129  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4            DIRECT                       2           SMALL  thrpt   20   904179.135 ±  37499.004  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4            DIRECT                      10           SMALL  thrpt   20   920983.094 ±  35914.129  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4            DIRECT                     100           SMALL  thrpt   20   858945.797 ±  55156.034  ops/s

Baseline
Benchmark                                                          (channelCount)  (clientExecutor)  (maxConcurrentStreams)  (responseSize)   Mode  Cnt       Score       Error  Units
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1           DEFAULT                       1           SMALL  thrpt   20  463224.233 ± 15075.820  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1           DEFAULT                       2           SMALL  thrpt   20  418996.088 ± 39517.380  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1           DEFAULT                      10           SMALL  thrpt   20  419147.532 ± 35825.976  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1           DEFAULT                     100           SMALL  thrpt   20  365772.704 ± 39481.162  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1            DIRECT                       1           SMALL  thrpt   20  486607.330 ±  4937.475  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1            DIRECT                       2           SMALL  thrpt   20  431439.527 ± 34487.554  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1            DIRECT                      10           SMALL  thrpt   20  440799.390 ± 19609.886  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               1            DIRECT                     100           SMALL  thrpt   20  384496.307 ± 30644.773  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2           DEFAULT                       1           SMALL  thrpt   20  623000.712 ± 57579.747  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2           DEFAULT                       2           SMALL  thrpt   20  677841.301 ± 44452.386  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2           DEFAULT                      10           SMALL  thrpt   20  710803.468 ± 59832.742  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2           DEFAULT                     100           SMALL  thrpt   20  541989.044 ± 68496.324  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2            DIRECT                       1           SMALL  thrpt   20  782277.645 ± 42270.805  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2            DIRECT                       2           SMALL  thrpt   20  725217.369 ± 29801.642  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2            DIRECT                      10           SMALL  thrpt   20  744944.708 ± 61464.357  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               2            DIRECT                     100           SMALL  thrpt   20  591086.072 ± 90409.945  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4           DEFAULT                       1           SMALL  thrpt   20  782448.903 ± 27561.783  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4           DEFAULT                       2           SMALL  thrpt   20  811964.327 ± 19292.966  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4           DEFAULT                      10           SMALL  thrpt   20  808832.437 ± 27356.478  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4           DEFAULT                     100           SMALL  thrpt   20  713170.043 ± 37491.770  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4            DIRECT                       1           SMALL  thrpt   20  805919.726 ± 18514.909  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4            DIRECT                       2           SMALL  thrpt   20  793134.550 ± 30305.765  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4            DIRECT                      10           SMALL  thrpt   20  808890.842 ± 23483.865  ops/s
FlowControlledMessagesPerSecondBenchmark.stream:messagesPerSecond               4            DIRECT                     100           SMALL  thrpt   20  734703.539 ± 46585.597  ops/s
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/997
Add overrideAuthority for Channel construction by ejona86 · Pull Request #997 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/998
Add usePlaintext to ManagedChannelBuilder by ejona86 · Pull Request #998 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
LGTM
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/999
Possible race condition ServerImpl between start() and shutdown() · Issue #999 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I believe it may be possible if start and stop are called concurrently that the shared executor may not get released.  I'm not sure if this is an actual problem, but it does go against the @ ThreadSafe annotation.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/grpc/grpc-java/issues/1000
Support starting a Server with basic TLS configuration · Issue #1000 · grpc/grpc-java · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
It should be able to start a secure server using just stable APIs. There should be some way to specify the cert chain and private key.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

