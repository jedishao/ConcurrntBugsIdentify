https://github.com/redisson/redisson/issues/5
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi there!
As I understand, Future returned by RedisAsyncConnection moves API user back to the blocking world. Java futures are NOT non-blocking by nature, they have blocking get(). Thus API user needs to spawn new threads and say hello to threading overhead again. Then why Netty is used?
I propose to return promises (Java's 8 CompletableFuture, Guava's ListenableFuture or jdeferred's promises).
Thanks,
Denis
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/26
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In RBucket we have:
    @Override
    public V get() {
        RedisConnection<String, V> conn = connectionManager.connectionReadOp();
        try {
            return conn.get(getName());
        } finally {
            connectionManager.release(conn);
        }
    }


get connection
do something
return back to pool

Before using this, I was simply getting a RedisConnection from the connection manager like this:
        Field field = Redisson.class.getDeclaredField("connectionManager");
        field.setAccessible(true);
        return (ConnectionManager) field.get(redisson);

The RedisConnection class javadoc states that the connection is thread-safe. So I was keeping a singleton reference over one connection to issue some simple commands like get, set, del, ... from several threads.
Questions:

Is a RedisConnection class is intended to be used this way (multiple threads doing get/set/del ops) ?
If yes, would it be possible to expose this behavior so that users could get from Redisson a connection (with auto-reconnect) ? This connection could be kept as a singleton ref during the entire lifetime of the server and not be returned back to the pool, because this connection will be used often (i.e. session management). This will avoid the burden of the get from pool / return to pool code.

Thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/35
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Note: I don't really know if there is a better place to ask for these sorts of questions... ;-)
Besides all the cool features added to Redisson to use locks, queues, maps, etc... How does Redisson performs compared to Jedis in terms of:

memory usage
speed
number of concurrent connections supported
use in multi-threading app requiring in both case using a pool
thread-safety
etc...

For having used both, I strongly prefer the api of Redisson (using publish subscribe in a reliable way with Jedis is a pain, and also there is no codec). But I am wondering, since their implementation only rely on simple sockets and a pool, how it compares to Redisson, which is based on Netty.
Also concerning thread-safety, having already aked a question about it, and in both libraries a connection pool is used for each operation and it is better to do so. So does thread-safety on a connection level really used ?
Thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/39
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I'm trying to use Lock and Unlock on Jersey Resource.

User makes a POST request
System LOCK "A"
System does some stuff
System UNLOCK "A"
User makes another POST request
System LOCK "A"
System does some stuff
System UNLOCK "A"

The system crashes at point 6 (view attachment).
If i try to make some LOCK-UNLOCK in a while loop it works, but when i make these LOCK-UNLOCK from different Threads it does not works.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/40
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Any plan to add TTL to a Lock operation? Don't confuse with tryLock with TIME.
I refer to a situation where a thread is dead and leave a resource locked (deadlock).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/49
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Using Distributed Map, put obj is ok, when get some obj by key, an exception will occur:
Exception in thread "main" com.lambdaworks.redis.RedisException: Command timed out
at com.lambdaworks.redis.RedisAsyncConnection.await(RedisAsyncConnection.java:1179)
at com.lambdaworks.redis.RedisConnection.await(RedisConnection.java:843)
at com.lambdaworks.redis.RedisConnection.hget(RedisConnection.java:283)
at org.redisson.RedissonMap.get(RedissonMap.java:89)
at dispatcher.RedisRef.main(RedisRef.java:573)
the exception will not occur when get naive java obj (String, int, ...)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/64
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I didn't catch your code example above. What is FastThreadLocal ?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/162
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I run into a thread dead lock problem when using distributed lock on 1.2.1:
public static CryptorInstance getCryptorInstanceFromCluster(Redisson redisson) throws NoAvailableCyrptorException
{
boolean successGetFlag = false;
CryptorInstance returnInstance = null;
RLock portLock = null;
try
{
    portLock = DAO_Redisson.redisson.getLock(CryptorMessageConstant.DISTRIBUTED_LOCK_CRYPTOR_SELECTOR_NAME);

portLock.lock(CryptorMessageConstant.DISTRIBUTED_LOCK_CRYPTOR_SELECTOR_TIMEOUT, TimeUnit.SECONDS);
   //Do other work

}
catch (NoAvailableCyrptorException ex)
{
    throw new NoAvailableCyrptorException();
}
catch (Exception ex)
{
    logger.error(ex, ex.fillInStackTrace());
}
finally
{
    if (portLock != null)
        portLock.unlock();
}

return returnInstance;

}
There are 10 ten thread call this function:
public class MinaExecutorCallable implements Callable
{
@OverRide
public Object call() throws Exception
{
try
{
while (!Thread.interrupted())
{
this.tmaInstance.cryptorInstance = CryptorSelector.getCryptorInstanceFromCluster(DAO_Redisson.redisson);
        }
    }
    catch (InterruptedException ex)
    {
        logger.warn("InterruptedException");
    }

    return null;
}

}
After a certain period, some threads will be dead lock, and we can tell this by VisualVM's thread dump:
"pool-1-thread-12" #29 prio=5 os_prio=0 tid=0x16050800 nid=0x121c waiting on condition [0x1786f000]
java.lang.Thread.State: WAITING (parking)
at sun.misc.Unsafe.park(Native Method)
- parking to wait for  <0x0b462068> (a java.util.concurrent.Semaphore$NonfairSync)
at java.util.concurrent.locks.LockSupport.park(Unknown Source)
at java.util.concurrent.locks.AbstractQueuedSynchronizer.parkAndCheckInterrupt(Unknown Source)
at java.util.concurrent.locks.AbstractQueuedSynchronizer.doAcquireSharedInterruptibly(Unknown Source)
at java.util.concurrent.locks.AbstractQueuedSynchronizer.acquireSharedInterruptibly(Unknown Source)
at java.util.concurrent.Semaphore.acquire(Unknown Source)
at org.redisson.RedissonLock.lockInterruptibly(RedissonLock.java:269)
at org.redisson.RedissonLock.lock(RedissonLock.java:224)
at com.xxxxxx.xxxx.xxx.cryptor.CryptorSelector.getCryptorInstanceFromCluster(CryptorSelector.java:33)
at com.xxxx.xxxx.xxxxx.xxxxx(xxxxxx.java:150)
at com.xxxxx.xxxx.xxxx.executor.MinaExecutorCallable.call(MinaExecutorCallable.java:116)
at java.util.concurrent.FutureTask.run(Unknown Source)
at java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
at java.lang.Thread.run(Unknown Source)
Locked ownable synchronizers:
- <0x0a7568a8> (a java.util.concurrent.ThreadPoolExecutor$Worker)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/163
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I run into a thread dead lock problem when using distributed lock on 1.2.1:
public static CryptorInstance getCryptorInstanceFromCluster(Redisson redisson) throws NoAvailableCyrptorException
{
boolean successGetFlag = false;
CryptorInstance returnInstance = null;
RLock portLock = null;
try
{
    portLock = DAO_Redisson.redisson.getLock(CryptorMessageConstant.DISTRIBUTED_LOCK_CRYPTOR_SELECTOR_NAME);

portLock.lock(CryptorMessageConstant.DISTRIBUTED_LOCK_CRYPTOR_SELECTOR_TIMEOUT, TimeUnit.SECONDS);
   //Do other work

}
catch (NoAvailableCyrptorException ex)
{
    throw new NoAvailableCyrptorException();
}
catch (Exception ex)
{
    logger.error(ex, ex.fillInStackTrace());
}
finally
{
    if (portLock != null)
        portLock.unlock();
}

return returnInstance;

}
There are ten threads call this function like this in a thread pool:
public class MinaExecutorCallable implements Callable
{
@OverRide
public Object call() throws Exception
{
try
{
while (!Thread.interrupted())
{
this.tmaInstance.cryptorInstance = CryptorSelector.getCryptorInstanceFromCluster(DAO_Redisson.redisson);
        }
    }
    catch (InterruptedException ex)
    {
        logger.warn("InterruptedException");
    }

    return null;
}

}
After a certain period, some threads will be dead lock, and we can tell this by VisualVM's thread dump:
"pool-1-thread-12" #29 prio=5 os_prio=0 tid=0x16050800 nid=0x121c waiting on condition [0x1786f000]
java.lang.Thread.State: WAITING (parking)
at sun.misc.Unsafe.park(Native Method)
- parking to wait for  <0x0b462068> (a java.util.concurrent.Semaphore$NonfairSync)
at java.util.concurrent.locks.LockSupport.park(Unknown Source)
at java.util.concurrent.locks.AbstractQueuedSynchronizer.parkAndCheckInterrupt(Unknown Source)
at java.util.concurrent.locks.AbstractQueuedSynchronizer.doAcquireSharedInterruptibly(Unknown Source)
at java.util.concurrent.locks.AbstractQueuedSynchronizer.acquireSharedInterruptibly(Unknown Source)
at java.util.concurrent.Semaphore.acquire(Unknown Source)
at org.redisson.RedissonLock.lockInterruptibly(RedissonLock.java:269)
at org.redisson.RedissonLock.lock(RedissonLock.java:224)
at com.xxxxxx.xxxx.xxx.cryptor.CryptorSelector.getCryptorInstanceFromCluster(CryptorSelector.java:33)
at com.xxxx.xxxx.xxxxx.xxxxx(xxxxxx.java:150)
at com.xxxxx.xxxx.xxxx.executor.MinaExecutorCallable.call(MinaExecutorCallable.java:116)
at java.util.concurrent.FutureTask.run(Unknown Source)
at java.util.concurrent.ThreadPoolExecutor.runWorker(Unknown Source)
at java.util.concurrent.ThreadPoolExecutor$Worker.run(Unknown Source)
at java.lang.Thread.run(Unknown Source)
Locked ownable synchronizers:
- <0x0a7568a8> (a java.util.concurrent.ThreadPoolExecutor$Worker)
I don't know why, is it a bug?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/169
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Bug found that can cause MasterSlaveConnectionManager to hang forever on get() call if exception is thrown anywhere in CommandHandler.
To replicate the bug, you can use RedissonMap with JsonJacksonCodec to put instance of class that doesn't have default constructor. When you try to fetch that object by using RedissonMap.get() call, deserialization of object will fail in MapOutput because of missing appropriate constructor and thread calling RedissonMap.get() will block forever.
In more details, this is happening because get() method awaits forever on Future object, which is released when Command.complete() is called. This complete() call is executed in decode() method of CommandHandler after RedisStateMachine processes Redis response. If, for example, RedisStateMachine throws an exception, complete() won't be called and result/exception will never be set to the Future object. This is causing calling thread to block forever in MasterSlaveConnectionManager.get() method.
Pull request with test case that is proving this bug and bug fix proposition will be published shortly.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/171
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In my project, I have a servlet, that call a utility class.
Utility class calls a wrapper class that  I have implemented over redisson lock.
Wrapper class holds RLock object for a thread and provides lock and unlock methods that call RLock's lock and unlock method
But while running a apache ab-test tool for concurrency, Following exception occurs.
Can you tell me if I am missing something over here?
java.lang.IllegalMonitorStateException: Attempt to unlock lock, not locked by current id: 286dad3d-dd4b-434e-bca7-30c35eec01eb thread-id: 158
at org.redisson.RedissonLock$4.execute(RedissonLock.java:416)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/199
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Today I tried some tests to experiment with Redisson's performance using a build from /master and discovered significant concurrency issues. I'm not sure what the state of this code is, so perhaps these issues are known ones, but wanted to make sure you guys are aware of them.
I have a very simple app that a) Creates a Redisson instance with a connection pool of 50 to masters and 50 to slaves, then b) creates a quick thread pool using Executors.newFixedThreadPool() and then c) feeds it Runnables, each of which generates a random string and adds it to the end of a Deque.
Whenever I do any of these three things: 1) Add >1 millions of queued Runnables or 2) Increase the number of threads >20 or 3) add a .contains() call on the Deque (more on that in a sec), I get a ton of exceptions that don't include any of my code in the stack trace. Here's one such snippet:
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/216
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I wound up pulling my hair out after upgrading from 1.3.1 to 2.1.0 and starting some new projects - the root cause being my attempt to use the SerilizationCodec with objects that were not Serializable. Simplest reproduction:
    protected static class NonSerializable {
        // empty
    }

    public void testSerializationFailure() {
        final Redisson redisson = Redisson.create(createConfig().setCodec(new SerializationCodec()));
        redisson.getBucket("serialization").set(new NonSerializable());
    }
Expected: a warning about serialization with a root cause of a java.io.NotSerializableException.
Actual: nothing in the logs, threads just hang around wait()ing on DefaultPromise.
I'm not a netty expert so unfortunately I have no PR to fix this. My best guess at root cause lies in CommandExecutorService#async. If I modify the ChannelFutureListener to
            future.addListener(new ChannelFutureListener() {
                @Override
                public void operationComplete(ChannelFuture future) throws Exception {
                    if (future.cause() != null) {
                        throw new RedisConnectionException("Failed command " + command, future.cause());
                    }
                    ...
                }
            });
I get a nice warning message:
[nioEventLoopGroup-3-3] WARN io.netty.util.concurrent.DefaultPromise - An exception was thrown by org.redisson.CommandExecutorService$6.operationComplete() org.redisson.client.RedisConnectionException: Failed command RedisCommand [name=SET, subName=null] <snip />
The listener originated in 2019283
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/223
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Rmap.addAndGetAsync (and any *Async methonds) - as i understand it shouldn't lock the calling thread, and return value (Future) as soon as possible.
But if for any reason connection is not established yet the calling thread will be blocked.
And if redis server is not available at all it will be blocked for very long period of time.
Maybe i'm wrong but it doesn't look like async nor lock-free.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/355
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I use redis as required data store, but in high concurrence, there are almost 50% connection failed. I want to know whether to optimize my redis server(use cluster) or my client? Is there any great suggestion? infinity retry until success? And My test code are list after:
RedissonFactory redissonFactory = new RedissonFactory();
    final RedissonClient redissonClient = redissonFactory.getRedissonClientInstance();

    final AtomicInteger atomicInteger = new AtomicInteger(0);

    ArrayList<Thread> threads = new ArrayList<Thread>();

    //使用1000个并发线程去连接并且获取数据
    for (int i = 0; i < 1000; i++) {

        final int i_inner = i;

        Thread thread = new Thread(new Runnable() {
            public void run() {

                RBucket<String> rBucket = null;
                try {
                    rBucket = redissonClient.getBucket("aaa");

                    rBucket.set("1", 2, TimeUnit.SECONDS);

                    System.out.println(rBucket.get() + ":" + i_inner);


                } catch (Exception e) {

                    e.printStackTrace();

                    atomicInteger.addAndGet(1);

                    System.out.println("Failed:" + i_inner);

                }


            }
        });

        threads.add(thread);

        //开启线程
        thread.start();



    }

    //等待全部线程终结
    threads.stream().forEach(thread->{
        try {
            thread.join();
        } catch (InterruptedException e) {
            e.printStackTrace();
        }
    });

    System.out.println("Final:" + atomicInteger.get());

}

I use 1000 threads, and find that if i set the connection pool size to 500, the successful proportion achieves maximum。
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/505
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Juste a little something.
In the FstCodec, when an object in encoded, an FSTObjectOutput is first borrowed from the FSTConfiguration, then used to write the object and then closed.
In the FST Serialization Recommended threadsafe Use, they recommend, when using the factory method, not closing this stream in order for it to be reused.
I think that only an oos.flush() instead of a oos.close() will do the job here.
Not a big deal, but still....
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/514
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi, we have been using RedissonSortedSet and just found that on certain cases the order can be broken and I assume RedissonSortedSet is supposedly thread safe.
Assuming RedissonSortedSet of integers are added with the following integers : 103, 101, 102. RedissonSortedSet state (list in the redis server) should be: 101, 102, 103. However, there are cases when it is not. It may become 102, 101, 103 instead. And looking at RedissonSortedSet's source code, it uses binary search that requires the list/state to be always sorted. Therefore it breaks many other functionality.
The use case that breaks (in my case) is when we are adding multiple items and there is another thread that delete an item in between. Looking the source code implementation briefly, it may be because when removing an item it does not consider getCurrentVersion() (just a quick guess).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/521
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Sorry for using an issue for my question, but I couldn't find a mailing list to post this question to :)
I am using Redisson to store key/value pairs and was wondering whether it makes more sense to use just plain RBuckets for each pair or a single RMap. I am especially interested in the possibility of sharding these across nodes in a cluster setup (PRO feature?). The key/value pairs are immutable and I would expect a lof of PUTs and DELETEs of them. Any pros and cons?
I do also use a lot of different "types" (around 8) of caches (with different serializations and TTLs). Currently I am using a different redis databases  for each type. This means I have to create a new connection (aka RedisonClient) for each of these. This also means a lot of Threads in the different ThreadPools, though I am already sharing the EventLoopGroup between the instances. Would there be any particular drawback in storing all of these in just one database to avoid the Thread overhead?
Thanks in advance!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/530
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
I want to raise the issue with deadlocks again.
This bug is still exist and making big headache. As before, It present itself only on very heavy loaded tasks, but in this case I is happens only when client talks to the claster which is located remotely.
With a single-local or claster-local servers I was unable to reproduce it, but with remote server it happens with rate 1 / 20 (means from 20 runs of "heavy-load" JUnit test it happens only once)
I can see where thread is locked down, it always stuck in CommandAsyncService.get(Future), on l.await() line and never exits from it. As I understand something wrong with mainPromise object, it is staying in incomplete state... and nobody change it. I tried to understand the logics in CommandAsyncService.async(...) function, which is actually deals with connection, retry, redirections and at end should release (or fail) the mainPromise object, but it is nightmare. All these spagetty with promises and futures made the code difficult to read and impossible to analyse. For sure BUG is there, but I am near to give-up. Any thoughts?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/543
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Found this in 2.2.16, seems like this was not around in 2.2.10. But still verifying.
When tryLock is called with 0 wait time, the thread blocks forever. I took a thread dump and it looks like the stack pasted below.
A note on the environment: We are running this against an Elasticache cluster in AWS and accessing from 4 EC2 instances. We have seen a lot of command timeouts. I am not sure if that is some way leading to this.
"pool-4-thread-5" #86 prio=5 os_prio=0 tid=0x00007f15ca23f800 nid=0xcd4 waiting for monitor entry [0x00007f15b90e5000]
java.lang.Thread.State: BLOCKED (on object monitor)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/545
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am using RedissonLock in my system.
The lock realted logic in service is like this:
    public boolean tryLock(String key, long time, TimeUnit unit) 

But in the log I found:
2016-07-04 15:15:39,533 DEBUG [http-nio-18090-exec-2] OrderService: Got lock for:ticket.lock.order.86
2016-07-04 15:15:39,541 DEBUG [http-nio-18090-exec-2] OrderService: Not hold lock for:ticket.lock.order.86

I can see the the thread name is same, so the thread got the lock and the thread try to unlock is same thread.
Is there any problem in my code? Or in the logic of lock.isHeldByCurrentThread() ?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/548
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
There are times we don't want to explicitly call RedissonClient::shutdown,
but because redisson creates some non-daemon threads when using the MasterSlaveConnectionManager (by using HashedWheelTimer's default thread factory)
then the JVM will never be able to quit without calling the shutdown method.
Please add support or change the default behaviour to start HashedWheelTimer with daemon threads.
https://github.com/mrniko/redisson/blob/master/src/main/java/org/redisson/connection/MasterSlaveConnectionManager.java#L202
new HashedWheelTimer(new DefaultThreadFactory("HashedWheelTimer", true), minTimeout, TimeUnit.MILLISECONDS);
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/573
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When set rertyAttemps to 0. connection pool size is 100. use 100 threads to read the redis cluster,it will throw exception like "Connection pool exhausted! for slots: [[8192-12287]] Disconnected hosts: [/10.2.30.72:6389] Hosts with fully busy connections: [/10.2.30.70:6381]".
In my point of view,it's caused by LoadBalance.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/656
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
it's reproducible, my code is below.
RLock singlelock = redissonClient.getLock("lock2");
   
redlock lock result will be success, but when I check redis, I found the multi locks belong to different thread.
like:
lock1 : 8d3c3d43-03b0-4cd8-8966-8bbd088f8c58:1
lock2 : 8d3c3d43-03b0-4cd8-8966-8bbd088f8c58:29
lock3 : 8d3c3d43-03b0-4cd8-8966-8bbd088f8c58:1
I did more test and found:

if the single lock is the first of redlock, it's ok.
when I move multilock2 to first position ,it will return false correctly.
the code below

RedissonRedLock redlock = new RedissonRedLock(multilock2,multilock1,multilock3);
boolean redlock_result = redlock.tryLock(5,300, TimeUnit.SECONDS);

if there are just 2 multi locks, it's ok.
the code below will return false.

RedissonRedLock redlock = new RedissonRedLock(multilock1,multilock2);
boolean redlock_result = redlock.tryLock(5,300, TimeUnit.SECONDS);

I am wondering if it is a bug or not?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/674
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I use 1000 mutliple thread to test the list operation. the costTime is average 1000~2000ms. But when single thread it costs 1ms.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/683
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
I have a thread stuck in the CommandAsyncService#get() indefinitely waiting for the CountdownLatch. I don't have a particular repro case but this happens every once in a while on our servers (under load). Redis itself is still delivering events and the instance receives objects on other threads as well.
Would it make sense instead of waiting indefinitely on the latch to only wait as long as the timeout is configured (as a safe belt) and abort the action if there hasn't been any success/failure by then?
Cheers,
Philipp
Redisson-Version: 3.0.0
Redis-Server: ElasticCache w/ engine 3.2.4
Redis-Config: SingleServerConfig w/ mostly the default values
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/693
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If you run the JUnit tests for Redisson a lot of client and their associated connections/threads are leaking because they are not properly shutdown. This will prevent the build to be successful on system with limited number of user-processes/open-files (i.e. MacOS El Capitain).
To verify this, build the project with an attached debugger and watch the constantly growing amount of threads.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/828
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We test this in case of a multi cluster setup and sometimes went the java.net.URL.factory to null instead of the original factory.
Scenario:
Thread 1
replaceURLFactory
currentFactory is original value
start create URL
Thread 2
replaceURLFactory
currentFactory == newFactory -> currentFactory = null
start create URL
Thread 1 and 2
restoreURLFactory
set URL.factory to null
Next “new URL(…)” from different call cause to load new handlers.
Best,
ebersb
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


https://github.com/redisson/redisson/issues/867
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello,
I'm trying to use redisson for my project that will run on AWS lambda and will use AWS Elasticache Redis Cluster. I have the following snippet:
URL redissonConfig = RedisCacheClient.class.getResource("/redisson.yaml");
logger.debug("URL is " + redissonConfig);
File configFile = new File(redissonConfig.toURI());
Config config;

I had the threads and nettyThreads as 0 and that was even worse. I now set it up to 4... and the startup is about 1440 ms.
Can someone please advise the right cluster configuration for Redisson in AWS Lambda?
Rgds.
Dheepak
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1190
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am scheduling tasks on a Redisson executor. On every schedule a massive chunk of tasks are submitted on two Redisson executors. I have equal number of workers assigned to each of the two executors 500 and a maximum redisson thread count of 1000.
I took periodic heap dumps of the JVM and the following was the last dump I captured before the container (my code is running in a docker container) went OOM. It appears to me that the netty's PoolThreadCache continues to increase.
Here is a screenshot of the leak suspect report of the last dump I took:

I am unable to get the crash dump report of the JVM. Will attach that as soon as I am able to figure out the issue with crash dumps not getting generated.
I am using Redisson 3.5.5. The bundled Netty version is 4.1.16.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1302
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We are trying to use updateMode=AFTER_REQUEST to make sure all the session data will be saved into Redis server. After reviewing the source code, looks it may cause performance issues since we keep a lot of data in the session, and store function will be called on every request no matter there is session changes or not.


Currently when updateMode=AFTER_REQUEST is on, session data will be saved twice in the Redis server if session.setAttribute(..) is called. First time is triggered by setAttribute() method, second time is triggered by AFTER_REQUEST. Can the first insert/update can be removed when AFTER_REQUEST is set?


Is it possible put save session data to Redis after tomcat request code to a separate thread?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1331
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We are Trying to add a mechanism to re-subscribe to topics after restarting redis.
Setting UP:

ttempting more than maxFailAttemp, make sure redisson regards all the redis server box down
=====================================================================
We were initially at Redisson version 2.9.1, but when we following the previous steps, in step 5, we encountered the same issue as in #1268, which is removeListener thread blocks forever, so make the switch to 2.11.1
We also simulate the scenario with 2.9.1 version,  without doing removeListener (we found out there is pubsub Listener leak issue with 2.9.1, that is why we remove the old listener first), the MasterConnectionPool was able to re-establish.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1356
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Is my code has any problem?
there are two different  thread get the same  multilock.
thanks!
public Lock tryMultiLock(List names, Long waittime, Long expiretime, TimeUnit timeUnit) {
if (names == null || names.size() == 0) {
throw new IllegalArgumentException("names is illegal!");
}
waittime = Math.max(waittime, this.miniWaitSecond);
RLock[] rLocksarr = new RLock[names.size()];
try {
for (int i = 0; i < names.size(); i++) {
rLocksarr[i] = this.redisson.getLock(names.get(i));
}
RedissonMultiLock lock = new RedissonMultiLock(rLocksarr);
}
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1481
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
Redisson is able to send read and write commands to the 2nd newly elected Master.
Actual behavior
This is the topology:
71a80a4554db9893e194545a45e4caeaf159a726 10.45.248.93:6379 master - 0 1527887027479 76 
When testing various failover situations, I ran into a situation which causes the redisson client to get stuck using a bad connection when making the write calls, however the thread that is polling for the topology is fine. The situation is the redis process dies on a Master node I am writing to, a slave is then promoted to master. The redisson client is still in a GOOD state. The redis process dies on the new Master, a floating slave is then promoted to Master. At this point, the redisson client is now STUCK using a bad connection to a dead master.
Steps to reproduce or test case
Run 7 node cluster, I believe this is the minimum to reproduce this as you need an extra floating slave to promote after the first Master/Slave pair dies. For Master 1 slots 0-5460 (M1), kill the redis process. This should cause it's slave (S1) to promote to master and the floating slave (FS2) to attach to this new master. Then repeat kill the redis process on S1 which was promoted to master and FS1 should be promoted to master. The redisson client will now fail reads/writes because the redisson client connections are to the old S1 node despite FS1 now being the new master but does not fail to poll for CLUSTER NODES because I believe it is using a separate connection pool/thread to do that.
Redis version
Default redis cluster config with 7 nodes. 3 Master 4 Slave.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1534
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>

SourceCode------------------------------------------------------------
on each servlet request, i send read command like below to redis, in this case, it is problem.
result = redissonClient.getScript().eval(Mode.READ_ONLY, script, RScript.ReturnType.VALUE), keyList, argvList.toArray());

on each servlet request, i send read or write command like below to redis,  in this case, it is ok
result = redissonClient.getScript().eval(Mode.READ_WRITE, script, RScript.ReturnType.VALUE), keyList, argvList.toArray());

slave is loading data for syncing with master. it takes 10 minutes to load all data completely.
during 10 minutes, servlet server is going strange behavior and throuput is very lower and don't return any exception. i think some threads is hanging around Redisson connection with new slave loading data.
actually i expected returning error with timeout. why it is not returning any error until slave is completed loading data.
after 10 minutes which completed load data from slave. it is going back to normal and throuput become higer.
however, read operation with Mode.ReadOnly is going both master and slave not going to slave only.

problem.

when loading data at slave, redisson is sending read operation to slave. and read opeartion thread is hanging aroud somewhere in redisson.
read operation with Mode.ReadOnly is going well to slave only. however after failover, read operation is going both master and slave not going to slave only.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1667
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thread gets stuck while obtaining lock.

at org.redisson.RedissonLock.lock(RedissonLock.java:86)
The same lock name was likely concurrently obtained and held by another thread possibly on another jvm, and then released.
Observed intermittently.
Redisson Version used : 3.4.3
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1824
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If threadId can be replaced with a generated controlId it will be perfect to use in no thread centric programmation like, fibers or kotlin coroutine.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1975
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We are on version 3.7.2 and only using RMap, RScoredSet and are facing the same issue in production where netty threads used by redisson consumed 12GB of total 16GB of allocated heap space in one application and 8GB out of 16 GB on another application . One observation i have made is that netty threads had created around 275,000 thread local maps with each consuming around a fixed amount of heap. It all seems to be related with weblogic context aware classloader because it is shared by all the netty threads.
Since the heap dump is quite large I will be attching the screenshots.
@mrniko setting  -Dio.netty.allocator.useCacheForAllThreads=false had no effects
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2144
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RedissonReadLock.class#tryLockInnerAsync
redis.call('pexpire', KEYS[1], ARGV[1]); 

If thread1 set expire 5000ms ,and then thread2 set expire 1000ms, then thread2 shutdown.
In this case,thread1 will lose its lock.
I think we can change code like this
local remainTime = redis.call('pttl', KEYS[1])
redis.call('pexpire', KEYS[1], math.max(remainTime,ARGV[1])); 

And the rwlock_timeout key will be not required.
Am I right? Where is the problem?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2149
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
     }        
===================================================
when frequent calls  formatCode,this config rateLimiter.tryAcquire(1,0, TimeUnit.SECONDS);
does not work normly above the version 3.7.2,here is the doc
current version:3.7.2
/**
* Acquires the given number of permits only if all are available
* within the given waiting time.
*
* Acquires the given number of permits, if all are available and returns immediately,
* with the value {@code true}, reducing the number of available permits by one.
*
* If no permit is available then the current thread becomes
* disabled for thread scheduling purposes and lies dormant until
* the specified waiting time elapses.
*
* If a permits is acquired then the value {@code true} is returned.
*
* If the specified waiting time elapses then the value {@code false}
* is returned.  If the time is less than or equal to zero, the method
* will not wait at all.
*
* @param permits amount
* @param timeout the maximum time to wait for a permit
* @param unit the time unit of the {@code timeout} argument
* @return {@code true} if a permit was acquired and {@code false}
*         if the waiting time elapsed before a permit was acquired
*/
boolean tryAcquire(long permits, long timeout, TimeUnit unit);
All code can see  (https://gitee.com/bootstrap2table/boot_master/tree/feature/boot-simple),
need help to fixed this bug,thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2172
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RedissonRedLock lock = new RedissonRedLock(lock1, lock2, lock3);
boolean res = lock.tryLock(-1, 10, TimeUnit.SECONDS);
if waitTime == -1  and leaseTime != -1，multiple threads get the lock at the same time
Thank you
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2183
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
As can be seen from the above, transaction committing occurs after the unlocking operation. Is there a possibility that other threads will have concurrent problems because the thread has been unlocked before the transaction has been submitted?
(Similar to @transaction and synchronized concurrency issues)
2.我用jmeter做了测试，却发现好像没有在解锁和提交事务之间发生并发问题，个人疑惑，希望大佬解解惑，谢谢
I tested it with JMeter and found no concurrency problems between unlocking and committing transactions.If you know, please let me know. Thank you.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2206
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When we are saving some data in redis using FST codec then data is not cleared from ThreadLocal after data saved to the redis. This is causing issue of OutOfMemory as tomcat thread's ThreadLocalMap is filled with huge data which was used while FST serialization.
Detail:

Main code requested for putting some data in Redis.
Redisson uses FST serialization to serialize data and then stores into Redis.
FSTObjectOutput which was used while serialization has stored data in ThreadLocal object and it has not cleared data from ThreadLocal after it was saved in the Redis.

I can see ThreadLocalMap contains all the data which was used while FST serialization. Please see below snapshot of heap dump:

Ideally it should clear the data from ThreadLocal, once the data stored in Redis.
Sample Code:
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2304
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello,
We are facing an an issue where some threads get blocked indefinitely waiting on the CountDownLatch in CommandAsyncService.get(). Relevant section of the thread dump:
- waiting on java.util.concurrent.CountDownLatch$Sync@1f2311a9

The reason for why the requests aren't able to complete isn't relevant here (we are deploying redis in kubernetes, and are working through various upgrade/failure scenarios that currently can result in severed connections). However, it's strange to me that the CommandAsyncService.get() method doesn't respect timeout configuration, and simply calls l.await().
Is there any way around this? Please let me know if I am misunderstanding the situation.
Expected behavior
CommandAsyncService.get() should throw an exception if the future is unable to complete within a timeout.
Actual behavior
Many threads are hanging indefinitely in the CommandAsyncService.get() method.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2319
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
Multithread concurrency can be unlocked successfully
Actual behavior
Multithread concurrency with only one thread successfully unlocked

Are there any problems with the script here?
When a thread finds the corresponding key, it deletes the whole key. Is it impossible for other threads to find it?
Steps to reproduce or test case
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2355
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
Calls to RedissonLock.unlock() are expected to finish after the lock has been deleted from Redis.
Actual behavior
We have experienced several threads locked forever waiting inside calls to RedissonLock.unlock() in our production system within a few hours after upgrading to Redisson 3.11.4 from Redisson 3.8.0.
Steps to reproduce or test case
Unfortunately I am unable to reproduce the problem on my own computer. We have however experienced it on several of our production servers within just a few hours after starting our newer version of the application with updated Redisson version. We upgraded from 3.8.0 in order to receive fixes for bug #1966 - Deadlock after Redis timeout, which we also experienced a couple of times. However right after start we have found some (29) exceptions in our logs coming from internal redisson threads:
After that we were investigating issues with blocked threads by analyzing thread dumps. All stuck threads had exactly the same stack trace as below:

After examining the source code of RedissonLock.java we have found that the NullPointerException occurs probably due to missing timeout object inside task:
329:        if (threadId == null || task.hasNoThreads()) {
330:            task.getTimeout().cancel();
331:            EXPIRATION_RENEWAL_MAP.remove(getEntryName());
332:        }
I'm not sure if it would solve the root cause why task.getTimeout() returns null, but calls to cancelExpirationRenewal method should not fail with an exception, otherwise, e.g. in RedissonLock.unlockAsync method the future will never receive a result (or a failure):

Please add null check for timeout inside the ExpirationEntry object.
We had to return to 3.8.0 version because of this problem. I think it is quire severe.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2503
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Do we have a way to provide class loader when using FST codec. we are facing classNotfound exceptions as the FSTConfiguration is picking up the current thread class loader which is used by RedisExecutor as shown in the below stack trace.

Our proprietary classes are loaded from our class loader. So wanted to understand if we can set the classloader which is used by FSTCodec.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2506
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
After running into some threading/scalability issues I'm moving over redission. Would be great if there was a guide for porting from Jedis.
For example, what is the closest resembling API to the jedis.get() and jedis.set() methods?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2543
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
trylock and unlock success
Actual behavior
RLock unlock always throw an exception what like 'not lock by current thread'
Steps to reproduce or test case
According to the stack information, the underlying asynchronous unlocking may cause the unlocking to throw an exception.This phenomenon can be reproduced 100%.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2701
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When I was doing the stress test, there were more than 180 threads （like:org.redisson.spring.data.connection.RedissonConnection.write() ,OR org.redisson.spring.data.connection.RedissonConnection.read(),and org.redisson.spring.data.connection.RedissonConnection.del()）waiting for "org.redisson.spring.data.connection.RedissonConnection.sync()". What is the reason for this? And how to solve it?Thank you very much!
//untDownLatch$Sync)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2704
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
hi,@mrniko
in the following scenarios, i do not know how to use the API, can you give me some advice?
since the password of the server will be changed, the client needs to get a new redisson object every time to access redis server. then, how to configure the codec？
1、redissonClient.getBucket("a", new JsonJacksonCodec()).set(new Animal());
Whether the above code will cause OOM when used in multiple threads，described in #2574
2、redissonClient.getBucket("a", JsonJacksonCodec.INSTANCE).set(new Animal());
if so, is there performance issue with json serialization and deserialization？
Gilberto Torrezan said "the ObjectMapper is indeed Thread safe. But reusing the same object can decrease the performance of your application, since all - 1 threads can be locked at a given time waiting for the owner of the lock to complete the serialization/deserialization of JSON." in
https://stackoverflow.com/questions/18611565/how-do-i-correctly-reuse-jackson-objectmapper/18615839
and, wheather you provide this  instance(JsonJacksonCodec.INSTANCE) to advise not to new  instance every time?
thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2718
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
return lock.tryLock(100,10,TimeUnit.SECONDS).flatMap(lockk -> { System.out.println(lockk); System.out.println(Thread.currentThread().toString()); return redissonReactiveClient.getLexSortedSet(redisKey) .readAll() .flatMap(strings -> { //some map operation using result }) .onErrorResume(throwable -> { System.out.println(Thread.currentThread().toString()); 
print result -
true
Thread[redisson-netty-2-6,5,main]
Thread[redisson-timer-4-1,5,main]
So here lockk is printed as true, but redissonReactiveClient.getLexSortedSet(redisKey) cannot execute and directly goes to onErrorResume as it is executing in different thread than lock.tryLock(). I'm new to this reactive style of programming, I don't know what I'm doing wrong maybe there is a better way to lock and get the sortedset? please help.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2836
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@mrniko on occasion we are seeing timeouts like this..
at
from what I gather all connections are free, none are in queue yet it still didn't manage to acquire a connection.. does this indicate all Netty threads are busy decoding a response, in which case we should consider adopting the dedicated executor for decoding, or something else? Currently running redisson-3.11.5
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2847
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
Does lockAsync / unlockAsync and bucket async APIs work with Akka actor using Scala/Play?
I am getting the exceptin below:
java.lang.IllegalMonitorStateException: attempt to unlock lock, not locked by current thread by node id
Is that because of unlockAsync being triggered inside Future of lockAsync? I am using Scala converters to get Scala Futures from these APIs.
If I generate my own thread ids using random long then it does work.
Thanks
Rakesh
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2870
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
yesterday,i test the redisson lock，i use  Apache JMeter to test the concurrency。param: thread number = 1000,  loop = 1。i found when i not release the lock .but other thread can get the lock.
example:

but i set params : thread number = 10,  loop = 1. No problem ....
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2872
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
yesterday,i test the redisson lock，i use  Apache JMeter to test the concurrency。param: thread number = 1000,  loop = 1。i found when i not release the lock .but other thread can get the lock.
example:

but i set params : thread number = 10,  loop = 1. No problem ....
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2987
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I currently have an application where I first create a RRateLimiter. I then acquire one permit in a loop and do an operation. This application is intended to run in a distributed fashion. To test the behavior, I set off concurrent invocations of this program. While it works well for the most part, it does throw an error occasionally as described below.
Expected behavior
No error. The thread waits to acquire a permit and does so.
Actual behavior
Occasionally, the  limiter.acquire() in the below code throws the following error -
 
Steps to reproduce or test case
Code snippet in AWS lambda talking to elasticache -
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3004
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
Threads that are alive and waiting for a RedissionFairLock will always get ownership of the lock it tried to acquire.
Actual behavior
When a RedissonFairLock is locked by long-running Thread T1, and other Threads (T2, ..., Tn) attempts to access the lock and waits for longer than 5 minutes (the default threadWaitTime), even when T1 releases the lock all waiting Threads T2 to Tn hang indefinitely.
This is due to future threads removing "expired" threads from the Queue, when in reality these threads are still alive and waiting for the lock. These "expired" threads never receive the PUBLISH message on unlock.
Steps to reproduce or test case

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3016
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
In one of my java application we are connected with Redis Server running on low compute machine (2 GB Ram, 1 Core) just for shared memory purpose.
Configuration of Redisson is as below
Config config = new Config();
config.useSingleServer().setPingConnectionInterval(0).setKeepAlive(true).setDnsMonitoringInterval(-1);
config.setNettyThreads(0);
redisson = Redisson.create(config);
At Redis server side, we also changed tcp-keepalive and timeout as 0 value.
But i am not getting any exception and application is closing after 1 hour. I just only received the update in shutdownhook and thread dump is as below.

hreadPoolExecutor.getTask(ThreadPoolExecutor.java:1054)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3023
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@mrniko

RBucket.set() method is fully thread-safe, but I wouldn't recommend to use blocking operations in netty threads

Doesn't it mean that the blocking operation (such as "RBucket.set()") cannot be thread-managed (multithreaded) only by the logic in redisson without using another library (such as "Spring's ThreadPoolTaskExecutor")?
Originally posted by @mrniko in #3022 (comment)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3024
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
@mrniko

RBucket.set() method is fully thread-safe, but I wouldn't recommend to use blocking operations in netty threads

Doesn't it mean that the blocking operation (such as "RBucket.set()") cannot be thread-managed (multithreaded(parallelization)) only by the logic in redisson without using another library (such as "Spring's ThreadPoolTaskExecutor")?
Originally posted by @mrniko in #3022 (comment)
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3158
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
When having one producer and at least two consumer threads (or instances of an application) I expect RQueue's removeIf(lambda) method to remove elements without negative side effects.
I expect the same when using an iterator to iterate over the queue and calling remove() on the iterator.
Actual behavior
There are multiple types of errors that I observed:

I've seen NullPointerExceptions inside the removeIf lambda (e.g. q.removeIf(element -> element.getId().equals("id"))), where element is null (we don't add null elements to the queue).
Other times removeIf does not actually remove the elements from the queue, probably because it did not find the elements in the first place.

As the default implementation of removeIf uses the iterator my guess is that basically the iterator causes this issue and may not work properly when another consumer of a queue modifies the queue while it is used.
Steps to reproduce or test case
I have the following test case which can be used to reproduce the issue. It uses Lombok, Awaitility and Apache's RandomStringUtils for convenience (in case you want to run it without modification). Below I will explain steps to modify the test to get different results.
The test has one producer thread pushing 200 random Strings (wrapped with QueueEntry objects) and one or more consumer threads "processing" these objects (parking them in an "in-progress-queue" - which is the problematic queue).


If you run the test as it is here it will fail because the "in-progress-queue" is not empty.
Modifications to change the test results:

Change the number of consumer threads to 1 in the line marked with (4). Now the test should pass. Change the number back to something larger than 1.
Comment in the RLock and its usages marked with (1). Now the test should pass. Comment the lines out again.
Comment out the removeIf(...) statement (marked with (2)) and comment in the remove(...) statement (marked with (3)) instead. Now the test should pass.

Instead of using removeIf() you could also modify the test to use an iterator and remove elements with it. The results will be similar.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3159
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I have a map stored in redis cluster. When I try to get this map to know if a given key exists in it, I am using
        String key = "mykey";
        RMap<String, String> rmap = redissonClient.getMap("mapK", new StringCodec());
        if(rmap.isEmpty() || rmap.get(key) == null){
            throw new RuntimeException("no value found with key: " + key);
        }
        ....

It works at most times. But somehow the RuntimeException I defined above will be throw out sometimes unexpectedly. Which means rMap.isEmpty returns true with no exception, while the fact is we do have this key stored in redis.
In addition, I found a exception in another thread,

Does this exception impact the result when I was calling `rMap.isEmpty()'?  And how can I avoid this problem?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3182
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
With retries enabled WriteRedisConnectionException shouldn't happen.
Actual behavior
We have set netty threads and max connections to 250. When Redission is retrying will it use different netty connection, or attempt using same channel which is throwing newClosedChannelException/ClosedChannelException? It's not clear from below error what other tuning is required in application code.
DefaultPromise.setFailure0(DefaultPromise.java:608)\n\tat io.netty.util.concurrent.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3202
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The waiting time is necessary. Because we don’t know whether last thread is completed or not. I finally thought this way to make each redission fair lock client has status. But this may affect tps a little. Kindly help to advise
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3203
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Getting below exception intermittently during execution of a multi-threaded batch process.
org.redisson.client.RedisTimeoutException: Command still hasn't been written into
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3303
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
An Attempted Optimization:
I was benchmarking an application and realized that the majority of time was being spent waiting on a jedis socket.
The slowness appeared to be from the accumulated network round trip of a particular jedis call.

Seems like a good use-case for a cached redisson container, so I opted for SetMultimapCache.
And sure enough, it reduced the overall time spent in my function from 24% to .1%

A new problem:
However this seems to have caused even more time to be spent in io.netty.  So much so that the overall duration (from the client's perspective), is significantly slower.
Do you know why this is happening?  My understanding so far is that both grpc and redisson are using netty, and maybe they aren't playing well together?  Or I have some kind of bottleneck which is now being stressed further by optimizing the main worker thread.  Or I don't understand netty or redisson enough to see what's happening.
Attempts to fix:
I've tried to setup the resisson client in many different ways.

I've tried a different number of nettythreads.  I've tried different eventloop groups with different thread counts.  I've tried changing the IO ratio to something lower/higher than 50.  If it helps, I'll show you the diff of how I integrated the container.  It basically just shows how I moved away from jedis calls in place of the redisson container:


^ The diff shouldn't be that important, but I didn't want to leave anything out.  These are the changes I've made with the configured redisson client that result in speedup where I was trying to optimize, but signifcant slow down on the client side and increased time spent in io.netty?
Do you know why this is happening?  What else can I try?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3324
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If an InterruptedException is thrown while waiting for RedissonBuckets.get, redisson throws a  RedisException with the message Unexpected exception while processing command.


Steps to reproduce or test case
Interrupt the caller thread while invoking RedissonBuckets.get.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3334
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Both applications are waitting for the same lock by using lock without leasetime.
Assume app a got lock and start processing. Then execute slow lua script(eg, withing 5 seconds blocking) in redis server (single mode). The app a watchdog thread will then throw a busy script exception and stop further renewing lock.
This will cause app b get lock later.  So it looks like app a and app b both got the lock.
Watch dog mechanism should provide exception tolerance.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3351
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
when i use redisson in spring cloud getway filter ,
public class AuthenticationFilter implements GlobalFilter {
    
but when i unlock this rLock report error log not locked by current thread , this rLock is not the same thread when i locked, how can i fix this problem
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3372
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
I am working on a API which is a high TPS one (around 10000 TPS) for both read and write.My API makes use of Redisson Open Source to connect to AWS Redis and I am making use of RLocalCachedMap so that frequently used objects will be fetched directly from LocalCache. I have the following questions:

What is the unit of cacheSize? Is it the number of records. If it is number of records that this local cache can hold, then I am getting many errors related to server crash and restart if I increase the count to higher values. Each object size should be around 800 bytes. I am not sure why that is happening. Do you think it might be with the RAM of the server on which it is deployed?
What happens if I dont set the cacheSize. Per documentation it is unbounded (default value is 0). So what would be the max limit this local cache size occupies and does it do the cache eviction internally if the LocalCacheMap feels the memory is nearing its capacity.
This question is with respect to the Redisson default Thread Pool size. Right now, I am using the default thread pool options. Do I need to fine tune the thread pools or the default thread pools can handle 10000 TPS
This question is with respect to CODEC Types.

I am having an object which has generic as one of its attribute. When I push the object to AWS Redis through redission using the codec types SNAPPYV2, SNAPPY it pushes the value and while retrieving from AWS Redis I could see the object having the values populated except the values of generics attribute (guess this codec type skips the generics at the time of deserialization). If I use JSON Jackson Codec, I could see the complete values being retrieved from AWS Redis. Would there be any codec that you suggest that handles generics or do i need to write custom serialization logic to handle.

What would be the best codec type if I am going to push the object as Map<String, Object> to AWS Redis. I ran performance test with different codec types and almost each of them returned in the same time (JSON Jackson COdec being little faster).


To meet the High TPS, what should be the object i need to consider while inserting it into AWS Redis, should the object be the regular POJO or can I have it as Map<String, Object>


Also, it would be helpful, if you can share any articles that helps in improving the performance using Redisson to connect to AWS Redis
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3440
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Redisson Version - 3.13.0
We are noticing following exceptions in our logs and then thread just get hung post that:
org.redisson.client.RedisTimeoutException: Command still hasn't been written into connection! Increase nettyThreads and/or retryInterval settings. Payload size in bytes: 0. 


Trying to understand what is causing this? Especially what does it mean - currentCommand=null
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3444
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
No error when trying to acquire a RRLimiter lock.  Error seen when multiple threads from one application try to acquire a lock from a 3 member redis cluster.
Actual behavior
Intermittent error seen,

I am not so sure why v would be nil.
Steps to reproduce or test case
Not easily reproducible as of yet.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3484
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
tryLockInnerAsync(long waitTime, long leaseTime, TimeUnit unit, long threadId, RedisStrictCommand<T> command) {
    
    internalLockLeaseTime = unit.toMillis(leaseTime);  

if two thread get the same lock subject and run the method at same time, one's leaseTime is -1, and another's leaseTime is bigger than 30, the "-1" thread first cam in and set internalLockLeaseTime, then another thread came in set the internalLockLeaseTime bigger than 30, then if the bigger leaseTime one get the real redis lock! It while cause watchDog invaild and the lock be expired ahead of time

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


https://github.com/redisson/redisson/issues/3492
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
the method 'tryAcquireAsync' of RedissonLock class,use current thread IDas redis value.
if two machine have same thread ID,a machine have held the lock,another machine will unlock successfully?
RedissonLock class can use a map to store current application have own Lock,if service reentrant or unlock,
verify that it have the lock before.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3493
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
Is it possible to perform transaction on Redis Live Object?
I want write a new instance of MyClass - only if new instance is newer than previous one.
I need method similar to 'merge' in RMap.

So I need to compare dates of old and new objects and then save new object only if it newer. It has be executed in one transaction. In other thread someone can update fields in this object.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3503
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hey, while writing plugins for BungeeCord proxy I ran into a problem with ClassLoader.  Plugins use the redisson library to create the network It works like this:

BungeeCord loads available plugins
One of the plugins contains the redisson library and connects to redis
Another plugin use the previously loaded plugin with the library to synchronize the objects

All plugins are loaded using the same ClassLoader, so the same ClassLoader also loads the redisson library, and knows about classes that we serialize and keep in redis. Unfortunately the plugin that is loaded in step 3 throws a error like:
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3829
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
Actual behavior
Production environment with a large number of requests queued
At around 19:23 on the night of September 9, due to the existence of a large Key in the store, after submitting a work order to delete the large Key, there was still an imbalance of data in the cluster slice, and the DBA tried to perform a memory analysis of the cluster, resulting in a Redis slice switch and the loss of some of the Keys.
Redisson's unlock mechanism will go to determine the LockKey Delete state, if Delete succeeds then publish a message to notify other clients subscribed to this lock to compete for the lock, if Delete fails then there is no message notification (Delete is a failure state when Key does not exist), thus causing the clients subscribed to the lock to wait until the thread wait timeout time (default is 5 minutes) to compete for the lock again.
Steps to reproduce or test case

Creating a large number of concurrent requests for locks
The business processing request time to obtain the lock is set longer than 30s
If thread A acquires the lock and manually deletes the key of the lock, i.e. RawName
Observing other threads acquiring locks, you will find that you need to wait a long time to get the lock, and after restarting the main method of Test, you cannot empty the last waiting queue, but can only wait for the default 5 minutes to clear the non-running state LockName(id:ThreadId)
5. RedissonFairLock.lock will not automatically renew
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3858
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
when start new thread using CompletableFuture.runAsync we have no class definition found
we have useThreadClassLoader: true
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3984
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Sometimes Redisson seems to be stuck when calling Redisson.shutdown(). Some Services are stuck for mutliple days. But it seems to be a very rare event,

This is the Thread netty tries to join. Stack trace does not seem to change over time (took multiple thread dumps

Expected behavior
Redisson.shutdown() should be blocking but not for ever
Actual behavior
Redisson.shutdown() is stuck for days (in some rare cases) and the Timer thread is taking huge amounts of processing power (this is not a typical profiler bug with parking threads but acutally showing in the process list)
Steps to reproduce or test case
Not tried but maybe if you could point us in a direction.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4023
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Steps to reproduce or test case
Let me simplify the reproduce process:

Thread x get Lock "A" and hold the Lock
Thread y get ReadLock "A" and also hold the ReadLock
Thread x and thread y all acquired lock
Thread y call method unlock to release ReadLock y
After a few seconds, thread x also call method unlock to release Lock x，and then it causes an exception

Here is stacktrace
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4172
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I submit tasks to RExecutorService with ExecutorOptions.taskRetryInterval=5m and expect the tasks will be resumed by another nodes after 5m if some nodes are down.
In my test , I submit 32 tasks to 2 nodes ( Server A/B , each have 20 threads to consume tasks ) , each consume 16 tasks.
The tasks take 30 seconds to complete and I manually kill one node (Server B) before tasks complete.
I expect Server A will consume all 32 tasks after 5m
Expected behavior
Server A will consume all 32 tasks after 5m.
Actual behavior
Server A only consume 16 tasks, another 16 tasks consume by Server B ( but not complete) remain in scheduler and tasks and are NOT processed by Server A.
Steps to reproduce or test case
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4176
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Using RRateLimiter if the thread which acquired the permit crashed or is long-running the permits never again become available again. Have created a rate limiter as below and once the permit is acquired even if the thread crashes or is closed the permit doesn't get available again.

Expected behaviour
Permits should get available again when the thread crashes or is closed
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4178
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I have an annotation RLock which works with an aspect, it work well in some programs.
Here is the codes:

Someday a program throws Exception at every tryLock in two of three containers. I checked ELK and find RedisTimeoutException before the first exception.
By the way, every container works with only one thread to consume kafka messages.
It seems taht  the first RLock unlock timeout and then redisson treats next RLocks as reentrant cause they have the same thread Id.
How to ensure that the lock could be released correctly after unlock timeout.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4184
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RedissonMultiLock cannot use the public boolean tryLock(long waitTime, long leaseTime, TimeUnit unit) with RedissonSpinLock
It will throw such exception like this:
stack trace:
java.lang.ClassCastException: org.redisson.RedissonSpinLock cannot be cast to org.redisson.RedissonLock

In the method public boolean tryLock(long waitTime, long leaseTime, TimeUnit unit) of RedissonMultiLock, there is such a block of codes.

But RedissonSpinLock cannot cast to RedissonLock. It inherit from RedissonBaseLock but not RedissonLock.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/174
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello,
I am using redis and redisson for my service deployed on Amazon server. Server has older kernel version that suffers from leap second bug. Will it affect redis or redisson lock in any manner? If so what is the possible solution to it?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/183
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The idea is go away from lettuce due to some api limitiations and absence of commands pipeline support. Also command handling - encoding/decoding should be implemented with lock free approach.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/345
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I use Redisson 2.2 to implement distributed lock in my project and use Redis cluster.  And I found the Redisson client will create new connection and do not use the connection in the pool while invoke some readOnly methods which execute evalRead. So when I start to run the test it will produce lots of TIME_WAIT connection on my server. The followings are some logs on my server.

The codes are very spectacular and I only understand a bit. But I doubt whether the client get the connection from the pool but also create a new one?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/386
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I use Elasticache Redis as my redis server, 1 master, 1 slave (fairly large machine, this is an autoscaling micro webservice).  I used to use an older version and it worked good (from a connections point of view), but I had to upgrade from 2.1.2 due to distributed lock fixes. I am currently using 2.2.4, but after about 12-24 hours I see the " RedisConnectionException:Can't aquire connection from pool! " exceptions.
I expected it had to do with Elasticache closing idle connections, so I turned that back off for now, but it didn't effect this behavior, it seems to be related with my update from 2.1.2 to 2.2.4.
Does redisson not refresh its connection pool as connections close, do they timeout, or is this something else entirely?
I am using SingleServer or MasterSlave Configuration, with defaults, the current behavior is seen with SingleServer. (I haven't added configurations for slaves yet)
The only functionality I currently use in Redisson is the Distributed lock mechanism, to control 2 sets of locks.
Flow of using lock: get lock, set expire to 15s, (try) process,(finally) unlock (or set lock to expire in 500ms)
Redis has plenty of connections available. only 1300 or so used out of about 7k
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/533
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I have 5 independent masters and I use single server config to create Redission instance.

The RedissonMultiLock works fine if all the redis nodes are alive.
If I shutdown one of the redis nodes, it will throw RedisConnectionException
Exception in thread "main" org.redisson.client.RedisConnectionException: Can't init enough connections amount! Only 0 from 5 were initialized. Server: /192.168.223.128:8000
According to The Redlock algorithm, it should try to lock another node but not throw exception. Do I use RedissonMultiLock correctly?
It tries to acquire the lock in all the N instances sequentially, using the same key name and random value in all the instances. During step 2, when setting the lock in each instance, the client uses a timeout which is small compared to the total lock auto-release time in order to acquire it. For example if the auto-release time is 10 seconds, the timeout could be in the ~ 5-50 milliseconds range. This prevents the client from remaining blocked for a long time trying to talk with a Redis node which is down: if an instance is not available, we should try to talk with the next instance ASAP.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/542
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RedissonRedlLock overrides unlock() of RedissonMultiLock and it will force to unlock all instances.
Is it more reasonable to use unlock method of RedissonMultiLock?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/549
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I got redisson org.redisson.client.RedisException: NOAUTH Authentication required. exception in 2.1.0

The codes I used with Redisson are like this:

When I try to call DistributedRedisLock.lock, it throws the exception described above
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/554
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
hi：
i have use ression ,ression version is:2.2.15
problem for: my code is mylock.lock(2L, TimeUnit.SECONDS);
why ttl key value is loop for 20-30 ,  un locked.
please help me,  thank you.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/558
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
redisson version: 2.2.21
redis version: 3.2.1
description: after master-slave failover , the test code blocked forever .
redis cluster :
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/670
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
when redis unlock publish the message,where is deal with the message and release semaphore?I can't find
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/682
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
we sometimes run into OutOfMemoryException while Redisson is trying to log a warning, since it includes the content in the log message [1]. Would it be possible to check for the instance type and in case of byte[] just log something else? I.e.
From what I can see that's the only place where large content might be locked, though I am not sure about the log.error in CommandDecoder#decode, as it is using the CommandData.toString() content.
Thanks,
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/877
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
This  bug could be a duplicate of #349 but this is not the same method.
The following code:
RBlockingQueue<Message> messageQueue = redissonClient.getBlockingQueue(Constants.MESSAGE_QUEUE);
Message message = messages.pollLastAndOfferFirstTo(Constants.PROCESSING_QUEUE);

Does not block until a message is available
In the documentation https://github.com/redisson/redisson/wiki/11.-Redis-commands-mapping, it is said that BRPOPLPUSH can be replaced by a call to RBlockingQueue.pollLastAndOfferFirstTo().
So this call should bock until a message is available.
As a workaround, I can use RBlockingQueue.pollLastAndOfferFirstToAsync() or pollLastAndOfferFirstTo(String queueName, long timeout, TimeUnit unit) throws InterruptedException.
By the way,  Reddis is a fantastic framework and I love it 👍
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/955
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If i want to lock a MultiLock in a web request,and unlock it in another web request, what is the best
way to store the multilock ? Maybe  the two web request will been distribute to different tomcat server.
The root cause is we can not unlock a multilock with a lock name .
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/956
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I have build the cluster of redis, 3 master, 3 slave. According to the Redlock algorithm: 'It tries to acquire the lock in all the N instances sequentially, using the same key name and random value in all the instances'.'
i think every lock name is must same, it's right?the following is my example, this is right?
Thanks!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/971
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
We are trying to figure out the cause of an error we are seeing in our logs.  We are using AWS Lambdas and using a Redisson read write lock, with a lease time of 10 seconds.  There is no obvious place where there error is raised so we are wondering if this is a background task that is timing out as a result of the AWS life cycle see The Freeze/Thaw Cycle https://aws.amazon.com/blogs/compute/container-reuse-in-lambda/
Is this an exception we should be worried about?
Thanks,
John
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1001
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I need a exclusive lock,but it not work,my code is :
RedissonRedLock lock = getRedLock(lockKey);
lock.tryLock(-1, 30*1000, TimeUnit.MILLISECONDS);

this is work，but i need a leaseTime.
lock.tryLock()

Is that what I'm using not right?
redisson 2.9.4
java 1.7
redis_version 2.8.6
thanks
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1003
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
as we all know，redisson lock implemts java.util.Lock，so dose it enforce the same memory synchronization semantics as provided by the built-in monitor lock  just like ReentrantLock??
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1022
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
alll client try to get  lock fair .
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1160
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The program execution sequence is as follows：

Thread A locked the 'lockSoundbox' of lockA. It's OK?
Thread B locked the 'lock2000' of lockB. It's OK?
Thread A locked the 'lock2000' of lockA. It's OK?
Thread B locked the 'lockSoundbox' of lockB. It's OK?

I think there's a deadlock between 3 and 4, but I'm not going to try it out.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1332
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
We have detect an issue on our redis (sentinel) cluster when there is a redis master switching .
During a performance test, we use PriorityQueue (~ 10 calls / seconds). All transaction are closed on 20-50 milli-seconds.
When master switching, on JConsole we have seen Redisson place some locks on redis databases, and all application are slow down... All transaction are closed on 3-10 seconds !
On our Redis cluster we have, 1 master, 5 slaves.
This is our using components versions :

Can you help us please ?
Thanks you
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1333
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
we should implement a distributed lock system for our clustered Spring Boot application.
We have a Redis "cluster" (no cluster mode enabled) with Sentinel.
Now, reading the documentation it seems that RedissonRedLock should be used as locks wrapper class to use lock/unlock api.
It seems that RedissonRedLock should be used with different RedissonInstance e multiple RLock's.
But what kind of lock should we use to implement single distributed lock with single redisson instance per-node?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1353
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
Right now we are using regular lock in our system. I found out in the documentation there is also fair lock option.
I am trying to find in the documentation any explanation about performance of fair lock vs regular lock.
Is there any performance penalty? I mean is there a reason not so use fair lock always by default?
Thanks
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1364
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi there,
Thanks for the quick fix on the ticket #1268 . We tested it and the block on RedissonTopic.removeAllListeners no longer happened.
However, we started see another issue: After a fairly long time running with the new code, subscriptions( by calling RedissonTopic.addListener) to the topics which are assigned to the same AsyncSemaphore lock from the method MasterSlaveConnectionManager.getSemaphore() are all encountering the same timeout error like "Subscribe timeout 9500ms". It's very consistent. But for other subscription calls to other topics which assigned to different AsyncSemaphore locks, everything works fine.
It's possibly related to #1268. Please help advice how to tune and debug this problem.
Thanks
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1485
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
hello, I have test the tryLock with waitTime, but find it has bug. My test is as follows:

As you can see, the second thread faild to acquire lock but the lock is released during 2 seconds...please tell me ,thanks
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1505
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi I have a distributed application that servers user requests. I want to implement distributed locking to synchronize access to user's data if multiple requests for the same user come in.
I'm using redisson with azure redis cache in cluster mode with 3 masters, 3 slaves for this purpose. My incoming request rate is 700/s, with total request processing times ~30-40ms. I've set the redisson cluster config as below (pool size=320, lock_wait_time=3000ms, lock_expiry_time=3000ms). However, I notice that in spite of tuning the connection pool size from 250-700, a small portion of requests fail while waiting to acquire the lock.
Questions:

Is my usage of redisson redlock below correct?
Any recommendations on how I can tune the config to resolve the "failed to acquire lock" errors?
The average redisson lock times i'm seeing are ~20-30ms. Is that expected? I also write user data to redis with JedisCluster in the same application and the cache get/set times are ~1-2ms.

Application algorithm
Thanks
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1524
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The acquire method should block until a permit is available, but it blocks indefinitely instead of the remaining time until a new permit becomes available. From my testing I have found that it doesn't acquire a permit when one should be available based on the rate and interval I tested. If I set the rate to 1 every 5 seconds, it should take a loop of 10 single permit acquires approximately 50 seconds to complete. Instead it acquires the first permit, then blocks forever on the next acquires call.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2000
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello,
Its a Question and NOT an issue
Currently we are using Redisson with our self-compiled and installed Redis Server on an ec2 instance and due to scalability concern, we are moving with AWS ElastiCache Redis Cluster.  Already our application is using Redisson Library, not just as a client, but also our application heavily using acquire Lock and Unlock on any given key using either "RLock" or "RReadWriteLock"
Now, I have aws ElastiCache Redis (cluster mode enabled) Cluster's Endpoints and Node Endpoints - but I am unable to connect to Redis Server;
I followed this Redisson Configuration Wiki -  I tried

Cluster Mode
Replicated Mode

Neither configuration was able to connect to Redis Cluster. I can connect to these server using Redis CLI, however with Redisson Library, I am not able to connect.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2037
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
If the lock key no longer exist the refresh should cease
Actual behavior
The renewExpiration() method ignores the return value of renewExpirationAsync() and reschedules itself forever
Steps to reproduce or test case
Should be as simple as manually removing a lock entry key from redis.
Redisson version
3.10.6
On a side note, another thing we noticed while looking into this is that renewExpirationAsync() does a scripted call that returns 0 or 1 depending on HEXISTS. It seems unnecessary as according to the redis docs about PEXPIRE, it does the same thing out of the box in a single command call (https://redis.io/commands/pexpire).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2215
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
renewExpiration  normal
Actual behavior
1.Multiple spring boot services have been started
2.Get the lock every 2 seconds
3.After the lock is acquired, the lock key is removed through the redis client
4.After deletion, the first few times can be normal, or it may not update the expiration event
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


https://github.com/redisson/redisson/issues/2515
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
After a connection problem during expiration renewal, if a new lock is created (with the same key), the expiration renewal should be working.
Actual behavior
If an error ocurred in the expiration renewal (ex: connection to redis timeout), it stops working for new locks.
Steps to reproduce or test case

Create a Redisson lock
Force a expiration renewal timeout (ex: restarting redis-server)
unlock (it will throw a exception, as expected)
Create a new lock with the same key
wait for the expiration renewal time
unlock (it will throw a exception, because the expiration renewal is not working)

Default, SingleServer, (LockWatchdogTimeout reduced just for testing)
I believe the problem is in RedissonLock.unlockAsync method, when opStatus is null, the cancelExpirationRenewal method should be called.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2547
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
in my app, sometimes there are some dead locks in redis
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2556
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The code is as follows, the lock cannot be automatically deleted, the lock will continue to live
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2557
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I have a redisson lock implementation in my code like:
Distributed lock implementation:

SonarQube complains not having the lock unlocked in the same path as lock. Is there any solution for this? Or can we not have this implementation for redisson locks? It does always execute the unlock but relies on the client to do so.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2648
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
1、assume a Redis cluster has a 5 master node; A , B, C ,D ,E representative node name.
2、Client A  lock to A,B,C three node. lock success.
3、This time B，C Node happen Network partition。
4、Client B lock to D,E tow node, lock success，Satisfy N/2 + 1 ，because have A，D，E three node。
5、Violation of mutual exclusion。
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2714
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
when tryLock is interrupted, watchdog renew listener is cancelled too
Actual behavior
when tryLock is interrupted, watchdog keeps renewing lock, this makes ifinite lock
Steps to reproduce or test case
private volatile boolean threadTwoScheduled = false;
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2828
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello,
I have a quick question about the redisson lock.
Does the redisson lock is share between all clients ? We have several services/jvm and we want to be sure that these services cannot read / write in concurrently on the same ressources.
We use AWS redis with 1 master and 2 slave.
Thank you
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3018
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I have a question about lock acquisition.
assume two services A and B acquire locks to access shared resources.

A has acquired the lock.
When B tries to acquire the lock. it will find the lock is held by other service(A).
So B will subscribe to the channel, for acquiring the lock.
before B subscribe to the channel,A release the lock and publish some messages.
What happens next?
B is waiting for the messages that is published by the lock holder(A), but A has published the messages and released the lock.
How did you solve it?

I'm sorry I didn't understand the source code,Thank you very much for your work.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3187
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello everyone,
Couldn't find my answer in docs or by looking briefly at the implementation, so posting the question here.
Let's assume a system, where X instances of the same application are working concurrently on processing some data. In general, the instances can work concurrently, but some specific data items must not be processed at the same time by more than one instance, as this would produce race condition.
To synchronize application instances and avoid race conditions, we've set up a Redis instance, and we use Redisson's locking mechanism to achieve exclusive execution. In general, the workflow for an instance looks like this:
(take a lock A) -> (process data) -> (release lock A)
Then, obviously, the other instances, that want to process the conflicting data item, need to wait for lock A to be released. Processing an item can take anywhere between several seconds and several days. so a lock might be held for a long time (and we use this auto-renewal feature for locks to have the lock prolonged as needed behind the scenes by Redisson).
My question is - what happens if an instance, that is currently holding the lock, loses connectivity to Redis (and therefore the lock times out and is then taken by another instance), and then after some time it regains the connectivity? Will it finish processing the data without holding the lock, and then fail on releasing the lock? Or maybe something else would happen?
I'd really appreciate your feedback on this.
Best Regards,
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3317
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi
i have strange behavior in my program. I am trying to implement something like "getAndLock then PutAndRelease".

i can see that after 1-st rLock.unlock(); lock is still alive (presented in reddis and rLock.isLocked() == true)
and after 2-d rLock.unlock() it is released (removed from reddis and rLock.isLocked() == false)
Why is it so? why do i need to trigger rLock.unlock(); multiple times until it finally removes lock?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3349
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RedissonLock uses pubsub mechanism to get notified about changes to lock. According to the cluster spec (https://redis.io/topics/cluster-spec), currently messages are simply broadcasted to all nodes in the cluster. It makes this lock inefficient in clusters with more than 5 nodes.
It would be great to have a spin lock with exponential backoff, because it works well with Redis's horizontal scaling.
If the idea seems fine to you, I can prepare a PR in a few days, just let me know. If not - sorry for taking your time, feel free to close the feature request.
Best regards,
Danila Varatyntsev
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3474
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am using redisson lock in my project, but the redis cluster i use in product env forbidden to use WAIT command, so the redisson lock alway ends up to and RedisException with message " wait command not found", I try every lock implements in redisson, all the same, so what should i do to fix this ? change anothe redis or write a lock by myselft ?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3490
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
set internalLockLeaseTime only when the lock acquired
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3500
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
is this a bug ? when read lock try lock but write lock is held
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3614
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
RLockReactive fail to unlock with RedissonShutdownException when un lock it at the end of the reactive sequence with doFinally() or with then() operators. When testing it with StepVerifier the unlock is complete sucessfully but fail with subscribe().
Example:
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3636
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am looking to use Redis for exclusive locks of resources.
If they fail and two workers will think they are holding the lock, that can end up in, let's say, really bad data corruption.
I know that a lot of edge cases in Redisson have been covered, however how about this one:

Worker1 acquires lock with time of "infinity" (until manual release)
Worker1 loses connection to Redis instance, while access to everything else still works and it continues operation on data, databases etc....
Lock gets removed from the database, because it expired in 30s (lock watchdog timeout), because of no bump by watchdog
Worker2 has good connection to Redis and is able to acquire the lock and start it's operation on data (leading to corruption)
Worker1 gets Redis connection back, it's watchdog tries to recreate the lock in background ASAP, however it lost the race because the lock was already acquired by Worker2
Both Worker1 and Worker2 now think they are holding the lock :(

Looking by the code comments, this seems to be expected behavior/known edge case - one of very few in regards to locks.
If I am correct with this scenario, what would you recommend? Going with non-redis solution like etcd or zookeeper, for example?
or maybe set the watchdog timeout to a value that will always be more than the execution time of task under that lock and have some custom code for removing failed locks on boot?
(so if Worker1 is down I either wait for it come back and automatically clean it's locks that are no longer valid or manually remove the locks owned by Worker1 assuming I want to safely get rid of it)
And is there a mechanism to check periodically whether watchdog has lost the race to reacquire the lock and allow application to act on it?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3644
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Why is isEvalCacheActive hardcoded to false inside CommandBatchService?

Due to CommandBatchService being used by RedisBaseLock this means regardless of whether you have useScriptCache set to true in the Redisson config all Redisson locks will be sending the whole script across the network for every lock call.
I assume there's a reason for this but is there any way I can use evalsha for locks instead?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3852
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
long id = Thread.currentThread().getId();
... lock.tryLock(0, 10, TimeUnit.SECONDS, id) ...
Expect this to exit immediately - reporting "true" if it can get the lock now ; and reporting "false" if it can not.
Actual behavior
It seems to block and wait until the lock becomes available.
The waitTime (set as 0 above) does not seem to influence the behaviour.
Steps to reproduce or test case
Invoke "lock.tryLock(0, 10, TimeUnit.SECONDS, id)", when the lock is already taken.
Expect it to instantly return with "false". It does not.
((Note: I am working inside Quarkus, and using "reactor.core.publisher.Mono" to convert the Redisson Reactive Core (Mono) into Mutiny (Uni) - this does not seem related ; but it makes it harder for me to frame a pure-Redission test case))
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3854
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello. Wondering how to be notified of a lock's expired lease?
I've tried adding an ExpiredObjectListener and a DeletedObjectListener to my lock, but neither of those received an event when my lock's lease expired.
I do see that I can call lock.remainTimeToLive, but wonder if there's a way to configure a listener for that.
Thanks for any suggestions.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3994
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I tried RLock(Redisson master branch, redis 5.0.5) with the following config and tried to test whether synchronous replication works with master-slave. After I killed one replica and the lock can still be granted(there was only one client trying to get the lock), what I expect is that the client failed to acquired the lock cause the command was not able to propagate to all the replicas.

After debug for a while, I found that BatchResult for EVAL & WAIT command was not checked in RedissonBaseLock.evalWriteAsync method,  i.e the syncedSlaves in BatchResult was not checked.
// org.redisson.RedissonBaseLock

So is it because i misunderstand the synchronous replication mechanism used in Redisson or it's a bug
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4025
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
你好，最近遇到一些并发调用的问题，想通过redisson的锁来解决，于是写了下面的方法去封装一个加锁执行的逻辑。
现在测试的时候遇到一个问题，就是在tryLock时，我把redis停了，模拟redis链接失败，发现请求会一直卡在tryLock那里。我们想实现如果redis挂了就不加锁，继续往下执行，不影响原业务。请问有合适的方法达到这种效果么。

Hello, I recently encountered some concurrent call problems and wanted to solve it through redisson's lock, so I wrote the following method to encapsulate the logic of locking execution.
When I was testing, I encountered a problem. I stopped redis during tryLock, and the simulated redis link failed, and I found that the request would always be stuck in tryLock. We want to realize that if redis hangs, there will be no lock and continue execution without affecting the original business. Is there a suitable way to achieve this effect?
public static final int DEFAULT_LOCK_WAIT_TIME_SECONDS = 2;

public static final int DEFAULT_LOCK_RELEASE_TIME_SECONDS = 30;
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4031
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I'd say it's a bug for unlockAsync() to fail because of internally trying to unlock a lock that was never acquired.
I hope this PR can be accepted, or that some way to address the problem can be found.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4033 /4044
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
lock successful
lock fail when get first lock in multi lock case
Steps to reproduce or test case
when I set waitTime=0in multi lock , it fail, but I set waitTime=0 in RLock, it success, why?

boolean flag = lock.tryLock(0,  TimeUnit.SECONDS);

I think it is a bug in RedissonMultiLock
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4050
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
Deadlocks don't happen every time. After running the program for a while, I found that the process stopped and the keys in redis were fixed, not added or reduced. What is even more strange is that the expiration time I added the lock is 800ms, and if I use the ttl command to get the expiration time, the result should be 0 or 1, or a negative number. But, I found a number greater than 1! And it keeps changing, like this: 4s -> 3s -> 2s -> 4s
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4050
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>  
Deadlocks don't happen every time. After running the program for a while, I found that the process stopped and the keys in redis were fixed, not added or reduced. What is even more strange is that the expiration time I added the lock is 800ms, and if I use the ttl command to get the expiration time, the result should be 0 or 1, or a negative number. But, I found a number greater than 1! And it keeps changing, like this: 4s -> 3s -> 2s -> 4s
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<


https://github.com/redisson/redisson/issues/4052
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Is your feature request related to a problem? Please describe.
Describe the solution you'd like
auto unlock with try...with...resource
maybe code like this
RLock lock = redisson.getLock("KEY");

Describe alternatives you've considered
haha. just make code eaiser.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4153
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In my code, I am trying to acquire a fair lock with a fixed waitTime and leaseTime as so
fairLock.tryLockAsync(waitTime, leaseTime, timeUnit, ID)
Occasionally, I face this error

I also see a queue is being formed for the fair lock, even though it is not currently held.
The waiting requests eventually time out after the waitTime expires.
The queue is being formed for the same lock that this exception is being thrown for.
At times, I have also seen the queue being formed for no reason without this error being thrown.
I am not able to reproduce this locally,
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/4167
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In my code, I am trying to acquire a fair lock with a fixed waitTime and leaseTime as so
fairLock.tryLockAsync(waitTime, leaseTime, timeUnit, ID)
Sometimes, all the requests will get queued up for apparently no reason, while no request has acquired the lock.
I can see a wait queue being formed for the lock, but the actual lock is not held by anyone.
Eventually, all of these waiting requests will time out and fail, and new requests will work fine.
This seems to happen randomly when there are a lot of simultaneous requests.
I am not able to reproduce this locally.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/669
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
From Gitter user @cdeszaq:

Wanting to keep memory usage within my app as low as possible. We're getting large collection-like responses from a backend system, processing them "item" at a time, and we want to be able to cache that response in a streamy way
Needs to keep memory low are many concurrent requests, large collections of things processed a streamy way, and we're hitting issues with OOM due to having large strings flying around
It's a CSV response from a back-end webservice, so we process it in a streamy way, but it'll easily get to sizes of 100MB for each response, and we often have to have 30+ of these responses being processed at once. We process it 1 row at a time within our code to keep memory low, but hit OOM when we go to/from our current caching layer because it converts to/from massive strings
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1513
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
I was wondering what the standard approach is to Mitigate possible Concurrency issues when using Redisson as a spring data source.
I am working on an application that gets information from a source application and then layers updated over the top before delivering the updated information to the client.
The updates in this case are built for several sources, each one has its own queue.
When a new message is placed on any given queue my app reads the message from the queue, and attempts to create or update an updateObject in my redis cache.
My problem stems form the fact that messages are constantly being placed on these queues and updates to the updateObject are likely to come in quick succession.
Im concerned that this will lead to concurrent read write issues:
existing updateObject[id:1, foo:false, bar:false]
msg 1[foo:true]---> get existing updateObject[id:1, foo:false, bar:false]
msg2[bar:true]--> get existing updateObject[id:1, foo:false, bar:false]
msg 1[foo:true]---> update existing updateObject[id:1, foo:true, bar:false]
msg2[bar:true]--> get existing updateObject[id:1, foo:false, bar:true]
resulting updateObject[id:1, foo:false, bar:true]
I have attempted to solve this using @transactional and the RedissonTransactionManager but it doesn't seem to be halting the second messages update while the first message is still updating.
Any advice would be really appreciated,
Thank you
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1694
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am running redisson in AWS Lambda functions connecting to a Elasticache redis cluster. The worflow of each lambda consist in 3 batch requests on average (2 read and 1 write).
Expected behavior
No command execution timeout errors
Actual behavior
Every once in a while redisson returns command execution timeout while fetching the cluster status through the command CLUSTER_NODES. Stacktrace is:


Worth mentioning that this happens with few concurrent execution at the time and I cannot understand why this is happening.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/1838
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
Actual behavior

the code run in high concurrent environment appear so many of the exception
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2325
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I use a semaphore in a complex system with 300 permits while the background workflow has 1000 concurrent requests. It takes about 7ms for processing after permit acquired.
For unfair semaphore, the delay for acquiring the permit is less than 1ms while delay for fair semaphore is more than 30ms.
I understand unfair semaphore may have a slightly better performance. But why it differs so much?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2358
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
redisson version is 2.15.2，In a concurrent environment, the number of maps continues to grow, with 4000,000 pieces of data. When replaced by redisTemplate, only 100,000 pieces of data are run at the same time and remain unchanged. All data is set to an hour timeout
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/3804
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Rate limit decreases over the time in highly concurrent environment.
Demo of such drift is on screenshot. Rate there has been limited by only RRateLimiter.

Expected behavior
Limit should not change without explicit call of setRate() with new value.
Actual behavior
Limit changes over hours. As a workaround I explicitly call setRate() with the same values time to time.
Steps to reproduce or test case
Just regular usage, nothing special:
    final long limitPerSecond = 115;
    final RRateLimiter limiter = redisson.getRateLimiter(name);
    limiter.setRate(RateType.OVERALL, limitPerSecond, 1000, RateIntervalUnit.MILLISECONDS);
    // ...
    limiter.acquire();
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2169
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Here's how I use it：
DragonBoatActivityVo dragonBoatActivityVo = this.dragonBoatService.getActivity();
Integer statusCode = 100;
if (dragonBoatActivityVo.getStatus()==1){
RLock rLock = redissonClient.getLock(openid);
try {
rLock.lock();
statusCode = this.dragonBoatService.addShareDrawNum(openid,sOpenid);
}catch (Exception e){
e.printStackTrace();
}finally {
rLock.unlock();
}
}
But there are still high concurrency issues
Two of the same information is generated
Request to solve
thank
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2711
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hello, Ask a question:
We want to control the data through redis in a high concurrency scenario, but now we have a problem. After reading the methods inside, all of them are asynchronous. It seems that the data retrieval is not correct. Please ask me how to solve this problem. It is my object. Is it wrong?
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/987
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We are running two redis servers in AWS, one master, and a replica. The read mode is the default (slave).
In our application code we have something like this.
  Integer newRank = redisSet.revRank(playerId);
The issue is that since reads go to the slave, addasync returns from master and before the data replicates to the other server it tries to pull the new revrank and returns null. imo the following api would make more sense and avoid that race condition..  .....
In the meantime I will either add retry logic or change the read mode to master but that's not going to scale in the long run so it would be nice to have this addressed.
Cheers!
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2175
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Expected behavior
Redisson throws RedisTimeoutException after timeout has exceeded.
Actual behavior
There is a race condition where Redisson may throw RedisTimeoutException after retryInterval has exceeded but before timeout has exceeded (in a nutshell when there are bursts of commands, commands will timeout even if timeout hasn't passed if retry interval is set to 0).
line 765 in CommandAsyncService seems suspect as it uses retry interval for the initial timeout value..
     Timeout timeout = connectionManager.newTimeout(retryTimerTask, connectionManager.getConfig().getRetryInterval(), TimeUnit.MILLISECONDS);
Steps to reproduce or test case
On faster machines you may need to create some artificial load then run the reproducer..
stress --cpu 8 --timeout 120
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2680
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We’ve been experiencing intermittent NullPointerExceptions (stacktrace at end) that appeared to be race condition. The root seems to be that del(byte[] keys...) doesn’t properly participate when a connection is pipelined.
I believe the simplest reproduction is:
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/2692
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
We have a number of instances of our app in production, and we’ve encountered a race condition where the same session might have changeSessionId invoked on the same session separate servers. This means one server might receive -2 from PTTL, which isn’t currently handled.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/53
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Does redisson support local cache?
For some usage scenario, local read is very heavy, local write is not much, and the delay of data synchronization can be tolerated in seconds. Some configurable cache mechanism could be helpful.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/71
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Use Case:
1)Extending the Redisson data types as part of a data abstraction layer.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/83
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Thread gets stuck while obtaining lock. Running 'keys L*' in redis-cli returns an empty list.

The same lock name was likely concurrently obtained and held by another thread possibly on another jvm, and then released.

<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/84
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
in RedissonLock.tryLockInner(long, TimeUnit):

At line A the lock key is set only if it doesn't exist (NX), but on line B it's set assuming it still exists. If the lock timeouts between A and B, another process may obtain the lock, which is then overwritten at B.

Here's a test case:

This will reliably fail if:

run in debug mode with a breakpoint placed in RedissonLock.tryLockInner(long, TimeUnit) on line B (line 306 for 508b903).
the breakpoint is released after waiting at least half a second
The same problem is also present in the no-args method RedissonLock.tryLockInner(). (though a race condition is possible only if upgrading an expiring lock)

I wonder if reentrancy support shouldn't be done purely in java.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/87
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Unhandled IllegalStateException in RedissonLock #87

I make heavy use of RLock in my app, and from time to time I find this in my logs.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/88
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Changed the semaphore initial value to 0, since every time
we try to acquire it is because we subscribed and know we have
to wait for another thread to signal it. This way, we just acquire
it once, and avoid useless operations.
Since the value was 1, the first thread to subscribe would go through
the subscribe() method twice, meaning the entry's counter would be raised
to 2, and on unsubscribe() decremented to 1, therefore, it would
never be removed from ENTRIES.
All tests are still passing, it's just slightly faster and allows the ENTRIES map to be cleaned up, which in turn means PubSub Connections are released.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/89
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Under heavy use on production, Redisson's locks get all locked up, and the application stalls. I'm using Redisson 1.1.5

I have 1 thread locked trying to release a lock:

Also of note, I have about 30 other threads locked awaiting for a lock (a different one from the one used by the previous thread).

I checked the threads with jstack, here is the relevant output:

this key is the one corresponding to the thread blocked trying to release a lock. The other threads, that are waiting for a separate lock are locked even though there is no-one taking up such lock....
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/93
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Race condition with lock/unlock notification fixed

Thanks everyone for the effort and time. I greatly appreciate it. However, I fear these changes do not fix the issue. Nothing has really changed, the race condition persists (it's just a little trickier to trigger).

Once again, the bug can be reproduced as follows:

Thread A gets the lock
Thread B tries to get the lock, fails, subscribes and waits for the subscription
Thread C tries to get the lock and fails, and is sitting on the call to subscribe()
Thread A releases the lock
Thread B wakes up, acquires the lock, and proceeds to unsubscribe, removes the entry from ENTRIES and sits on the synchronized (connectionManager) without having acquired it.
Thread C resumes, goes into subscribe, finds no available entry in ENTRIES and creates a new one, taking the already subscribed connection from connectionManager to listen on the channel and proceeds to wait for it.
Thread B immediately resumes, acquiring the lock on connectionManager and requesting connectionManager to unsubscribe from the channel and remove all listeners (including the one added by Thread C). Thread C will never get notified, it's dead. All future requests for that lock that can't be fulfilled right away will just use the existing entry in ENTRIES and wait on the same promise, all getting locked forever. The application is dead.
I would recommend reverting the changes from fd29bed, along with those introduced in bca4a17; and look into alternative solutions. I made a suggestion on #89 for which I was hoping to get some feedback.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/95
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When a connection is reused, the listener should still be subscribed.
This, along with all previous fixes, finally removes all known deadlock conditions for #89
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://github.com/redisson/redisson/issues/100
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently if redisson client was shutdown abnormally locks created by this client will remain forever.
This solution will create all locks as keys with expiration time set in redis. I'm not sure if this is best solution and what to do with lock() - lock(time, unit) - lock() sequences but it works for me.
Any suggestions or changes are welcome.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<