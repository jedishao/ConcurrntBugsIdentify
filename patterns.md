# Patterns

## pattern 1
\[CMI\]\[COP\](\[TMP\]+\[SYMP\])

### CMI is the subject:

* CMI should not cause deadlock
* The function CMI lock the locked container again.
* CMI is recursively invoked twice.
* The CMI acquires lock_1 and gets stuck.
* The CMI was not released in a for loop and acquired again in the next loop iteration.

There be (attr):
* There are two CMI involved in this deadlock.


### SYMP(deadlock, thread, lock) is the subject, CMI is the object:

* This deadlock is triggered by a unit test CMI.
* Threads using CMI will wait forever for a lock to be released. There is no timeout when waiting for the lock.
* The lock for the struct svm has already been locked when calling CMI.


## pattern 2
\[VERB\]\[SYMP\]\[CMI\]


I can confirm the deadlock in CMI.
If CMI is executed in between, deadlock will happen.
The blocking may also lead to deadlocking the EventLoop in cases where a CMI is used.
It happens that when the channel outbound buffer is full, the write operation drains the buffer on a flush changing the channel writability leading to potential deadlock in CMI.
However, a deadlock can occur due to contention between DB connection pool and CMI whenever a new message (or other mail item) is added.
Servlet calls CMI in synchronized block. In getAttribute method, session object is locked in order to check foreground session lock.
POSTing many buffers to an echoing server gives thread blocked failures when we use CMI approach.
It's seems like at some time, something has kept the monitor of CMI instance, preventing the resume call to execute the method.
CMI is currently a blocking operation. It blocks until the HEADERS frame has been written on the wire.
If you now use a CMI and reuse the EventLoop of the server with the grpc client, the TLS handshake would block the server's EventLoop, which is also the very EventLoop responsible for completing the TLS HandShake.
It seems the async CMI makes the channel in unsubscribing process can be used unexpectedly by another thread.
The problem is that CMI A helds container lock and B helds memoryStore lock, then A is blocked on the unlock of memoryStore which is blocked on container lock.
CMI A enters a loop, which calls wait in each iteration and does not leave the loop until some condition is satisfied.
It has been noticed by the go developers that RLock should not be recursively used in the CMI.

