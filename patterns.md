# Patterns

## one CMI

## pattern 1
\[CMI\]\[COP\](\[TMP\]+\[SYMP\])

### CMI is the subject:

**strong**
* CMI should not cause deadlock
* The function CMI lock the locked container again.
* CMI is recursively invoked twice.
* The CMI acquires lock_1 and gets stuck.
* The CMI was not released in a for loop and acquired again in the next loop iteration.
* If the CMI was not canceled, it will be blocked forever.
* The CMI returns without releasing the lock, leading to deadlock.
* If CMI is executed in between, deadlock will happen.

There be (attr):
* There are two CMI involved in this deadlock.

### SYMP(deadlock, thread, lock) is the subject, CMI is the object:

* This deadlock is triggered by a unit test CMI.
* Threads using CMI will wait forever for a lock to be released. There is no timeout when waiting for the lock.
* The lock for the struct svm has already been locked when calling CMI.

## pattern 2
\[VERB\]\[SYMP\]\[CMI\]

### SYM and CMI are object

* I can confirm the deadlock in CMI.
* It's seems like at some time, something has kept the monitor of CMI instance, preventing the resume call to execute the method.

### CMI is the subject:

**weak**
* CMI is currently a blocking operation. It blocks until the HEADERS frame has been written on the wire.
* Basically, there are two CMI blocking each other, and both of the two CMI execute select statement.

### clause
* The blocking may also lead to deadlocking the EventLoop in cases where a CMI is used.
* CMI A enters a loop, which calls wait in each iteration and does not leave the loop until some condition is satisfied.
* POSTing many buffers to an echoing server gives thread blocked failures when we use CMI approach.


## two CMIs

## pattern 3

\[CMI\]\[CC\]\[CMI\][SYMP\]

* Circular dependency between CMI and CMI causes thread deadlock.
* CMI function and CMI function can block each other.
* Deadlock occurs when both CMI and CMI are called at the same time.
* There is a chance of deadlock when CMI is linked with an CMI.
* In my case, the deadlock issue is hit when the CMI and CMI happened to be called at same time, one from main thread and another from eventloop thread.
* However, a deadlock can occur due to contention between CMI and CMI whenever a new message (or other mail item) is added.
* Sometimes, even though the lock from the first thread is timed out and released automatically, the CMI and CMI keys are stuck and the second thread can't acquire the lock, even though nobody is holding it.
* From my understanding of these stack traces and the threading model, this essentially means that any CMI call (regardless of the thread it is called from) can deadlock with a 'CMI' call.
* From my simple analysis it seems that the Exception handling and the request response seem to be locking on the CMI and CMI
* If this happens between CMI and CMI, the first goroutine will not be waked up, leading to deadlock.
* Please, find the attachment with the Bamboo report for the deadlock around CMI and CMI.


## pattern 4

\[CMI\]\[ORDER\]\[CMI\]

* In cases when a CMI is being used it might lead to the CMI blocking forever (deadlock effectively).
* The issue is that Thread-1 acquires a lock on CMI when CMI is called.
* On the other hand, when channel layer calls into transport layer, it's possible to form a CMI to CMI lock order, which makes deadlock possible.
* CMI takes CMI but does not drop it if there are not deleted devices.
* It has been noticed by the go developers that CMI should not be recursively used in the CMI.
* And in JDK 1.7_21, you get a deadlock if the CMI is locked while another thread calls CMI.
* This is a problem because CMI holds its 'this' lock while calling CMI in multiple places.
* This can create deadlock in CMI because a CMI may uses different request/websocket (reconnects) and event loops.
* If the second CMI interleaves in between the two lock operations of the first CMI, deadlock will happen.
* However, this pending runnable may never be executed because the eventloop might be executing some other task, like CMI, that is trying to acquire CMI causing a deadlock.
* The anonymous CMI is blocking forever, when context is canceled before the anonymous CMI writing to ???errc??? channel.
* However, these listeners usually call into channel layer code, and may in turn acquire locks from there, which forms a CMI to CMI lock order.
* It seems to be caused by each thread running CMI on the same two CMI instances, but in a different order.
* The basic root cause is that one CMI finishes with holding a RLock, which will block the second CMI.
* The synchronized CMI waits for the synchronized CMI, when the synchronized CMI waits for the synchronized CMI.

## More CMI

* CMI acquires the CMI again, which is already held in CMI.
* Inside podFitsOnNode function, there exists a path, where the CMI acquires CMI and returns without invoking CMI.
* If you call CMI on the completion of a CMI returned by Pulsar Client, like CMI then there is a good chance to create a deadlock.
* Then CMI fails to close the CMI because lock is already held by CMI.
* If two peer instances of CMI and CMI are CMI on different threads at the same time, they can each end up holding their own lock while waiting (forever) for the other's.
* The current implementation of CMI synchronises on the CMI (which is necessary) and holds this lock when calling CMI or CMI.

## NLP/CMI+NLP

* Thread-1 is also attempting to invoke CMI the active sessions (i.e. CMI) which requires a lock on the session.
* Meanwhile, Thread-2 has already acquired a lock on CMI when it called CMI.
* Thread-2 is also attempting to acquire a lock on CMI for CMI, but the lock was already obtained by Thread-1.
* The other thread wants the lock too, but is in the synchronized method CMI.
* This can cause deadlocks when used from external threads or because the transport thread has changed (for instance a session reconnection with an scaled http server).
* We're seeing a deadlock when two different threads load different CMI classes at the same time.
* That way neither the server nor the client would ever make progress again.
* The second thread is stuck for full acquisition timeout. Then, it fails to get the lock eventually, and keys redisson_lock_queue and redisson_lock_timeout disappear, making the lock available again.
* The problem is that goroutine A helds container lock and B helds memoryStore lock, then A is blocked on the unlock of memoryStore which is blocked on container lock.
* While holding a read lock, write lock cannot be acquired.
* But, this can cause a deadlock when multiple threads are trying to load these DataType classes because they each hold a lock on the class and end up waiting for the others to finish.
* I am experiencing deadlock when two different threads attempt to close the database with hsqldb 2.0.0 and 2.1.0.
* This condition continues until the fair wait queue empties, or one of the threads dies and the rest of the threads are forced to wait for the far in the future timeout on the dead thread to lapse (this creates a dead lock-like situation).