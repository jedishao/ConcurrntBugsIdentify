# Patterns

## pattern 1
\[CMI\]\[COP\](\[TMP\]+\[SYMP\])

### CMI is the subject:

**strong**
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

### SYM and CMI are object

* I can confirm the deadlock in CMI.
* It's seems like at some time, something has kept the monitor of CMI instance, preventing the resume call to execute the method.

### CMI is the subject:

**weak**
* CMI is currently a blocking operation. It blocks until the HEADERS frame has been written on the wire.
* If CMI is executed in between, deadlock will happen.

### clause
* The blocking may also lead to deadlocking the EventLoop in cases where a CMI is used.
* CMI A enters a loop, which calls wait in each iteration and does not leave the loop until some condition is satisfied.
* POSTing many buffers to an echoing server gives thread blocked failures when we use CMI approach.
