https://github.com/eclipse-vertx/vert.x/issues/57
Race condition in clustering · Issue #57 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
No description provided.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/60
Race condition in event bus sending 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When two or more event loops attempt to send to the new server concurrently and the connection has not yet been setup.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/78
Fix for incorrectly ordered code in JS web-app tutorial 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I was following the JS tutorial using beta5 and got stuck at the point after adding the SockJSBridge to web_server.js. The chrome console showed a 404 for http://localhost:8080/eventbus/info and none of the static data appeared in the page.

After Googling I found this thread which suggested that the SockJSBridge needs to be initialized only after the request handler is attached to the server. Sure enough, switching the example code around fixed the problem.

I've patched the markdown file with a corrected code sample.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/117
remove redundant inner class by pidster · Pull Request #117 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The thread pool factory defined as an inner class is redundant, so is removed by this commit
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/124
Experimental boot loader by pidster · Pull Request #124 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Some corrections, should work in parallel with the original version so the Windows .bat file should still work.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/250
Vert.x embedded capabilities and API · Issue #250 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This is to follow up the discussion thread at https://groups.google.com/forum/?fromgroups#!topic/vertx/dkFMoE-aq5I
For the purpose of this request, I will call the application that is embedding Vert.x as MAIN application,
and I will call EMBEDDED application the Vert.x system.
In regards to the Vert.x embedded capabilities I would like to have when I use Vert.x in custom application are:

Ability to start, stop Vert.x for a given configuration all via APIs
Ability to run multiple isolated Verticles as per normal Vert.x design
Ability to leverage thread-model with configurable options (thread pool sizes)
Ability to leverage/run existing bus modules from a give package or a configured repo
Ability to join Vert.x clusters
Ability to run Verticles written in others languages (Ruby, Javascript, etc)
Ability to install Verticle and bus handlers that live in MAIN application class loader

this last ability is very important to give easy access from the EMBEDDED verticles to the MAIN application beans.
A common example can be: expose REST/Web interface of an existing application. Somehow the Verticle must have access
to the MAIN application beans with the given limitations that this verticle won't be isolated from the MAIN classloader
and therefore there is no guarantee of state isolation. In other words even if the given verticle will be (classloader)
isolated from the others verticle, will share the MAIN application classloader making his state vulnerable to access
from other threads living in the MAIN classloader. It will be developer responsibility to guarantee consistency.
Things that don't make sense while embedding Vert.x

the main() and other startup scritps won't be used, a clean API must be provided
configuration files, directory locations, and other external resources must be provided
container functionality such as module-autodeployment or auto-relaod won't be required.

The key abilities of Vert.x reside in the threading model, the polyglot engines, and the bus modularity,
I would like to preserve those capabilities while embedding Vert.x
regards
Bruno
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/303
Race condition in deploying modules · Issue #303 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If deploy two modules of same name at same time, can result in one not being deployed.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/325
HttpClient really not designed for resuse · Issue #325 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I have written once before in google groups about the about limitations in the current design of HttpClient given that it was intended to be reused and requests pipelined. I have recently come across another problem that is a serious issue and I think can really only be addressed by redesigning the HttpClient, which is something I'm happy to take on. However, I want to make sure that I have a full understanding of intents and reasons for the initial design, so I would like some peer review of the idea before I go off and do this.
Let's start with the easy problem: HttpClient is supposed to be reusable with pipelined requests being executed on a pool of connections. The first problem is that the client has setter methods, allowing mutation of some of the operating parameters mid use. While by the nature of a verticle only one thread will be using the HttpClient at a time, the same instance may be used in various parts of the code, and since the properties can be mutated, can be left in an unexpected state for the next place that uses it.
A more serious problem is that connection exceptions are reported on the HttpClient exception handler, and NOT on the HttpClientRequest's exception handler. This means either each user of the HttpClient sets it's exception handler (which overwrites the last) OR there is one generic exception handler that can do little more than log the error. The problem with the first case: Imagine two requests are made one after the other, potentially via different code paths. The second's use of the HttpClient overwrites the first's exception handler. Now, since the connections are made on a separate thread in the case of a pool, this means that if a connection exception occurs connecting on the first request, and there is enough delay such that the exception handler has already been set by the second use of HttpClient, the exception for the connection of the first attempt is reported to the second handler, even though the second attempt to connect may succeed. This makes it impossible to know which request actually had the error and act on closing down, cleaning up, reporting accordingly. There is a simple test case provided below. Finally, If the second method is used, where we set the HttpClient's exception handler once, and provide some generic logging implementation, the HttpClientRequest's exception handler is never invoked either. To make matters worse, since there is no timeout feature on HttpClient, this results in a dead end; neither the HttpClientRequest's end nor exception handler is ever invoked. There is no way to know that the HttpClientRequest will never complete.
I propose and would like comment on the following changes:

Deprecate both HttpClient and Vertx.createHttpClient()
Create the interface SharedHttpClient that is immutable, in that is has no setters and no way to set an exception handler. It has an isClosed() method so that a new client can be created if some code path decided to close the Client for some reason. All connection exceptions are passed to the exception handler of the HttpClientRequest, the HttpClient has no exceptionHandler() method. I would create a new interface to preserve backward compatibility, with the idea we would eventually remove the current HttpClient.
Create a new interface/class called HttpClientParams that has all of the setters on the current HttpClient.
Create a new method on Vertx: public SharedHttpClient createSharedHttpClient(HttpClientParams params);
Add a setTimeoutMs(long) method to HttpClientRequest the idea being if the HttpClient.request() (and related) does not complete and call the passed in response handler before the timeout, the exception handler for the request will be called with TimeoutException(). This would default to -1 which means no timeout and has the current behavior.
Add a setTimeoutMs(long) method to HttpClientResponse the idea being if the HttpClientRepsonse.end() (or exceptionHandler()) is not called the timeout, the exception handler for the response will be called with TimeoutException(). This would default to -1 which means no timeout and has the current behavior.
Alternatively to 5 and 6, there is one setTimeoutMs(long) on the SharedHttpClient, and the implementations of the DefaultHttpClientRequest and DefaultHttpClientResponse, handle each half of the timeout.
The implementation of DefaultSharedHttpClient is largely based on the current implementation of DefaultHttpClient, but delegates the connection exceptions to the appropriate HttpClientRequest so that code can know which request failed because of a connection error. It also does not need to implement any of the mutator methods that were present in DefaultHttpClient.

I believe without these changes (and from hours of debugging and trying to work around the current design) the HttpClient is not really reusable, the internal connection pool and boss threads notwithstanding.
Test Case to prove non-reuasbility of HttpClient when shared among code paths:
/**
 * Show that HttpClient is really not reusable as intended.
 *
 * @author Nathan Pahucki, <a href="mailto:nathan@gmail.com"> nathan@gmail.com</a>
 */
public final class TestHttpClientReuse extends Verticle {

Results when run:
Got exception during connect for code path Two.
There was an exception on code path Two
You can see the exception handler for the first request was never called, so so it would just hang there, never having the exception handler nor end handler called.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/363
Thread context classloader not being set · Issue #363 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
TCCL is not set in all places in vert.x. It should be.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/423
DefaultEventBus not thread safe · Issue #423 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I wrote a prototype for our project, I chose vert.x as a middleware which involves consumes messages from kafka and redirecting it to mongoDB, since consumer api in kafka is a blocking api so I create a work verticle, after consuming about 50k messages, I found my cpu utilization was nearly 100% and consuming verticle stuck , I then found it was cause by a infinitive loop in HashMap.put() which was called by getHandlerCloseHook(context).entries.add(new HandlerEntry(address, handler)) in DefaultEventBus.registerHandler().
I think it was caused by concurrently calling the put or remove on the HashMap by a worker verticle, thus causing the HashMap to be broken.
After I change the
private class HandlerCloseHook implements Runnable {
}
It seems everything was ok.
I wondering if it is proper to change the HashSet to ConcurrentHashSet, if so shall I make a pull request?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


https://github.com/eclipse-vertx/vert.x/issues/473
Little vertx threads improvement by jdonnerstag · Pull Request #473 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Unfortunately the code has diverged too much to apply this, so closing.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/477
Container.exit() doesn't undeploy modules · Issue #477 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
While trying to figure out why one of my new worker modules doesn't allow Vert.x to shut down cleanly, I realized that the approach I was taking doesn't work.  Container#exit() only calls VerticleManager#unblock(); it does not undeploy any verticles.  This means that a Verticle's stop() method is never called, and that any non-daemon threads spawned by a worker will keep the JVM from exiting.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/525
Regression : ensure threads names are not modified (eg. by Jython) by julien3 · Pull Request #525 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Regression from d564f0a
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/584
Document thread safety of core classes · Issue #584 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In the JavaDoc.
People using them embedded need to know this
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/646
Rare exception during auto-redeploy. · Issue #646 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When using the auto-redeploy feature in beta6 (and it is great, really great) I sometime get an exception like this:
INFO: Module dk.bckfnn~mymod~1.0.0-SNAPSHOT has changed, reloading it.
jun 17, 2013 10:06:46 AM io.netty.util.concurrent.SingleThreadEventExecutor$2 run
WARNING: An event executor terminated with non-empty task queue (2)
Exception in thread "vert.x-eventloop-thread-1" jun 17, 2013 10:06:48 AM org.vertx.java.core.logging.impl.JULLogDelegate error
SEVERE: Failed to run task
java.util.concurrent.RejectedExecutionException: event executor terminated
        at io.netty.util.concurrent.SingleThreadEventExecutor.reject(SingleThreadEventExecutor.java:702)
        at io.netty.util.concurrent.SingleThreadEventExecutor.addTask(SingleThreadEventExecutor.java:295)
        at io.netty.util.concurrent.SingleThreadEventExecutor.execute(SingleThreadEventExecutor.java:690)
        at io.netty.util.concurrent.SingleThreadEventExecutor.schedule(SingleThreadEventExecutor.java:793)
        at io.netty.util.concurrent.SingleThreadEventExecutor.schedule(SingleThreadEventExecutor.java:721)
        at org.vertx.java.core.impl.DefaultVertx.scheduleTimeout(DefaultVertx.java:244)
        at org.vertx.java.core.impl.DefaultVertx.setTimer(DefaultVertx.java:158)
        at org.vertx.java.platform.impl.Redeployer.setTimer(Redeployer.java:77)
        at org.vertx.java.platform.impl.Redeployer.checkForChanges(Redeployer.java:225)
        at org.vertx.java.platform.impl.Redeployer.access$000(Redeployer.java:32)
        at org.vertx.java.platform.impl.Redeployer$1.run(Redeployer.java:52)
        at org.vertx.java.platform.impl.Redeployer$3.run(Redeployer.java:233)
        at java.util.concurrent.ThreadPoolExecutor.runWorker(ThreadPoolExecutor.java:1110)
        at java.util.concurrent.ThreadPoolExecutor$Worker.run(ThreadPoolExecutor.java:603)
        at java.lang.Thread.run(Thread.java:722)

The exception is rare, much less than 1% of the reloads, so it does not prevent the use of redeploy.
I can not reproduce it but it have occured a couple of times.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/682
Synchronize require() in Ruby verticles · Issue #682 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When starting multiple instances of the same module/verticle type concurrently, and where the verticle does a require(), this can result in failures because require() in the shared ruby runtime is not threadsafe.
We can fix this by overriding the require() method with a version that synchronizes access to the original version.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/759
Adding possibility to use thread context class loader to load cluster.xml for embedded vert.x by gaol · Pull Request #759 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Can you make sure your commits are signed off as describer here https://groups.google.com/forum/?fromgroups#!topic/vertx/WjKTl9FXvjc ?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/799
Remove usage of Thread-Local for performance reasons by normanmaurer · Pull Request #799 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@purplefox ok to merge in ?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/978
Fix sendHead() in http client request by untoldwind · Pull Request #978 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If the underlying connection is already establish (e.g. by a previous GET request with keep alive), the connected() callback is invoked in the very same thread as sendHead(). Since the writeHead flag is set after the connect the HTTP header is actually never written.
ATM the only workaround is to call sendHead() twice (which is very ugly).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/998
Bug fix : unset the TCCL on wrong thread when executing blocking handler by vietj · Pull Request #998 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/663
Problem with shared map · Issue #663 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I'm currently debugging an issue I have with a shared map. It might be due to a misunderstanding on my part. If so, I'm sorry for the noise. Below is a minimal test case that demonstrates the problem. In the Putter verticle, I add a new map entry, and in the Getter verticle I

Print the keySet().
Print the result of containsKey() with the inserted key.

But for some reason the two don't agree on the contents of the map. E.g. I get the output:
[gameId: 1, playerId: 4]
false

So I'm guessing there's some concurrency issue at play here.
I ran this test case with:
$ javac -cp "/home/estan/Projekt/dynastica/client-proxy/lib/vert.x-1.3.1.final/lib/*" *.java
$ /home/estan/Projekt/dynastica/client-proxy/lib/vert.x-1.3.1.final/bin/vertx run Starter
$ telnet 6000
$ telnet 6001
The last two commands are just to trigger the Putter and Getter to do their jobs, respectively.
Best regards,
Elvis Stansvik
Test case:
Starter.java
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/926
Enhanced RouteMatcher so routes can be updated and removed while in use by tcollinsworth · Pull Request #926 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Technically the try/finally should surround the for loop in the removeMatchingBindings method otherwise any concurrent route additions or concurrent removeMatchingBindings might cause ConcurrentModificationException.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/421
Remove Context singleton by jdonnerstag · Pull Request #421 · eclipse-vertx/vert.x · GitHub
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
static Context is a Singleton thus causing side effect during testing but more importantly, if more than one Vertx instance is running on one VM. The proposed change moves the threadlocal from Context into vertx (without static; no more singleton), which is already forwarded to almost all all major components and hence required only little changes. Most changes look like Context.getContext() => vertx.getContext().
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/497
Extend thread pool executor implementation 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The existing ThreadPoolExecutor implementations do not expose their metrics.

Provide a custom ThreadPoolExecutorFactory that simplifies this and exposes the metrics, in preparation for the addition of JMX support.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/500
Move language tests to associated language implementation. 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Moving the language tests to each language implementations test source set will make it easier for contributors to see the requirements for developing a language implementation.

It may also mean that builds of the project can run faster through Gradle's parallelisation features.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/739
Should vert.x add support for stm(software transaction memory) 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I dare think that vert.x should add support for stm(software transaction memory) for while developing we could not ignore the configuration for database transaction currently most of us make choice to integration with spring framework(for it provide the transaction feature) but it also has us to include many third party framework jar to support 
it(or integrated with jboss transcation) and most also have us to make vert.x under the embedded mod for developing.
As akka itself provides support for stm, so why not vert.x adds support for it(or provide the third party solution for it in the manual)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/958
Thread safety 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Some Java8-ification, cleanup and tweaks but mainly thread-safety work - need to make sure that some of our objects are usable from other threads - this is important for the non verticle embedded case.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/959
Java8-ification, tweaks, and thread safety. Make sure Vert.x objects can... 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
... be used from other threads - important in the embedded without verticle use case

I assume the addition of the synchronization primitives at method scope are to allow for threaded use in varying contexts. What's the justification for this approach versus an internal lock?

I like the new handling of Codecs. I've always thought that the Codec stuff should be completely removed from the EventBus into an external class/manger type thing. The EB is starting to look a bit crowded IMO.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/eclipse-vertx/vert.x/issues/967
Thread safety 
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
synchronized is removed but synchronization still occurs at line 1034. this was the only way to make the callback not under the lock (in a case runOnContext is called with the same thread and not in a new task in the eventloop).

 
@purplefox purplefox on Nov 14, 2014
agreed. although if a thread already owns the lock and encounters another synchronized for the same object, the overhead is zero aiui.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
