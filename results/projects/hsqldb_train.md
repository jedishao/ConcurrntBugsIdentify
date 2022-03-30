https://sourceforge.net/p/hsqldb/bugs/2
HyperSQL Database Engine (HSQLDB) / Bugs / #2 Please Support multiple ResultSets!
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Currently, the jdbcStatement class does NOT support 
multiple ResultSets. (This is clearly documented in 
the javadocs, and is also obvious from looking at the 
source code.) 
However, this makes this class USELESS for executing 
general stored procedures (which OFTEN do mutiple 
queries -- doing complex stuff like this is usually 
the whole point behind using stored procedures).

Requires multi-threading model accepted for future version
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/63
HyperSQL Database Engine (HSQLDB) / Bugs / #63 Extraneous sleep  in Log class
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
In version 1.61 of hsqldb in the Log.isAlreadyOpen() method there is a 3 second sleep that seems to be there to do some sort of concurrency checking. I could not find anyplace where the lock file is actually created. I believe this is unnecessary code and can be removed. It would significantly improve start-up time.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/235
HyperSQL Database Engine (HSQLDB) / Bugs / #235 ClassLoader problem causing file lock error
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
If you attempt to open a connection on Windows 
through two seperate ClassLoader(CL) who each have 
their parent set to null you will get the &quot;DB in use by 
another process error&quot;. This occurs even if the first CL 
has been null'd because either the lock hasn't been 
GC'd or it has to do with Windows not releasing the lock 
properly.
The easiest way to reproduce this is to create two JUnit 
tasks which both attempt to open a connection then run 
those JUnit tasks through ANT.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/329
HyperSQL Database Engine (HSQLDB) / Bugs / #329 NIO lock problem
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I am getting an exception when trying to allocate a
connection. I tried to clean database files before
running the program, with no success. 
It was tested on Compaq Tru64 platform, &quot;java version
&quot;1.4.0&quot;
Java(TM) 2 Runtime Environment, Standard Edition
Fast VM (build 1.4.0-1.p2, native threads, mixed mode,
12/10/2002-19:05)&quot;.
The same code _works_ on Win2000 or Linux (also java
ver 1.4) with no problem, so maybe this is just a buggy
Java NIO API on Tru64. But I need to make it running on
Tru64 somehow. 
Is there any way to avoid using NIO API in hsqldb?
Right now I just commented all code in
org.hsqldb.NIOLockFile in my sources (and it works fine).
WBR,
Maxim
import java.sql.*;
class Test {
public static void main(String args[]) throws
Exception {
Class.forName(&quot;org.hsqldb.jdbcDriver&quot;);
String path = &quot;jdbc:hsqldb:qq&quot;;
Connection conn1 =
DriverManager.getConnection(path, &quot;sa&quot;, &quot;&quot;);
System.out.println(conn1);
}
}
/*
java.io.IOException: No locks available
at sun.nio.ch.FileChannelImpl.lock0(Native Method)
at
sun.nio.ch.FileChannelImpl.tryLock(FileChannelImpl.java:528)
at
java.nio.channels.FileChannel.tryLock(FileChannel.java:967)
at
org.hsqldb.NIOLockFile.lockImpl(NIOLockFile.java:82)
at org.hsqldb.LockFile.tryLock(LockFile.java:804)
at org.hsqldb.Logger.acquireLock(Logger.java:343)
at org.hsqldb.Logger.openLog(Logger.java:93)
at org.hsqldb.Database.reopen(Database.java:257)
at org.hsqldb.Database.open(Database.java:220)
at
org.hsqldb.DatabaseManager.getDatabase(DatabaseManager.java:182)
at
org.hsqldb.DatabaseManager.newSession(DatabaseManager.java:100)
at
org.hsqldb.jdbcConnection.&lt;init&gt;(jdbcConnection.java:2418)
at
org.hsqldb.jdbcDriver.getConnection(jdbcDriver.java:214)
at
org.hsqldb.jdbcDriver.connect(jdbcDriver.java:198)
at
java.sql.DriverManager.getConnection(DriverManager.java:512)
at
java.sql.DriverManager.getConnection(DriverManager.java:171)
at Test.main(Test.java:8)
java.sql.SQLException: The database is already in use
by another process:
org.hsqldb.NIOLockFile@c7305c97[file =/home/mve/qq.lck,
exists=true, locked=false, valid=false, fl =null]:
at
org.hsqldb.jdbcDriver.sqlException(jdbcDriver.java:140)
at
org.hsqldb.jdbcConnection.&lt;init&gt;(jdbcConnection.java:2432)
at
org.hsqldb.jdbcDriver.getConnection(jdbcDriver.java:214)
at
org.hsqldb.jdbcDriver.connect(jdbcDriver.java:198)
at
java.sql.DriverManager.getConnection(DriverManager.java:512)
at
java.sql.DriverManager.getConnection(DriverManager.java:171)
at Test.main(Test.java:8)
*/
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/393
HyperSQL Database Engine (HSQLDB) / Bugs / #393 Server hangs on select statement
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
The attached zip file contains a SELECT statement that 
worked in 1.7.1 but in 1.7.2 RC1 doesn't work. In 1.7.2 
the server gets locked up and CPU utilization goes to 
100%. I then have to kill the server.
I tested this statement with org.hsqldb.util.
DatabaseManagerSwing and with DbVisualizer (commercial 
SQL manager) and with my Java application. I got the 
same results.
This statement works fine with a MySQL version of my 
database.
The zip files contains the SELECT statement, the db 
script (pinyin.script), the server.properties and pinyin.
properties and db.properties
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/37
HyperSQL Database Engine (HSQLDB) / Bugs / #37 Recovery commits broken transactions
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
When HSQL restarted after a system crash, it will made 
the changes made by the last *uncommited* -- thus 
possibly inclompete -- transaction permanent. HSQL 
should drop all changes after the last succesfull 
commit from the log (providing that auto commit was 
set to off).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/197
HyperSQL Database Engine (HSQLDB) / Bugs / #197 transaction not rolled back
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
I'm using Hsqldb 1.7.1 (latest stable). The database is
in multi-user mode with the following flags:
-trace &quot;true&quot; -silent &quot;false&quot;
If a JDBC client is interrupted abruptly then his
undergoing transaction(autocommit = false) is not
aborted (rolled back), although the server displays the
fact that it has disconnected this interrupted client!
So, the server is aware of the transaction voidness but
doesn't roll it back.
There's another thing to add here. The DatabaseMetaData
for hsql says that it supports ONLY the READ_UNCOMMITED
level of transaction isolation.
Isn't it a pitty? I personally like Hsql for it's light
load in terms of memory and cpu time.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/227
HyperSQL Database Engine (HSQLDB) / Bugs / #227 Transaction, UK constraint, Rolback produce lost of data
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi,
I found some problems while using last stable version of 
hsqldb (1.7.1.).
Transaction and Unique Constraint violation and 
Rollback could produce unreliable db, and lost of data.
I try this (from Database Manager):
CREATE TABLE TUKR(
ID integer NOT NULL PRIMARY 
KEY,
NAME varchar(20) NOT NULL,
VALUE integer,
CONSTRAINT TUKR01
UNIQUE (NAME)
);
INSERT INTO TUKR(ID, NAME, VALUE)VALUES
(1, 'Name 1', 1);
INSERT INTO TUKR(ID, NAME, VALUE)VALUES
(2, 'Name 2', 2);
INSERT INTO TUKR(ID, NAME, VALUE)VALUES
(3, 'Name 3', 3);
INSERT INTO TUKR(ID, NAME, VALUE)VALUES
(4, 'Name 4', 4);
SET AUTOCOMMIT FALSE;
UPDATE TUKR
SET NAME='Name 1'
WHERE ID=4;
// unique constraint violation occures
// off course in general case try:
ROLLBACK;
//S1000 General error java.lang.NullPointerException 
in ... Code -40/S1000
After that depend of the amount and type of data in 
destination table (in this case TUKR), some data would 
be lost, additonaly many other commands produce 
same S1000 error (including SHTUDOWN).
From JDBC connection behaviour is exactly the same.
PK violation lads to similar results.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/276
HyperSQL Database Engine (HSQLDB) / Bugs / #276 Connection Problems in standalone mode
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hypersonic DB when running in standalone(In-process - 
not in memory) mode does not allow the Process which 
created the DB to use nested transcation(nested 
connection) or transcation across threads and throws 
the below Error
ERROR: The database is already in use by another 
process
ERROR: Cannot open connection
java.sql.SQLException: The database is already in 
use by another process
Let me explain the scenario.
1. Gets the DB connection with security user 
(Username=security1, pwd=&quot;pwd&quot;, 
url=jdbc:hsqldb:myDB&quot;). Get all the necessary data. 
close the connection. 
2. Now get the DB connection with real user 
(Username=real, pwd=&quot;123&quot;, url=jdbc:hsqldb:myDB&quot;). Do 
a lot of initialization.
3. Now I have this part of code which executes a nested 
transaction. And I get the above error when the inner 
transcation is executed.
{
getConnection() 
beginTranscation()
doWork
{
some work......
getConnection() --------
--- fails here with above mentioned error. 
beginTranscation()
doWork
{
some work.....
} 
} 
So when i tried to debug hsqldb, I found the following 
bug with the implementation.
1. org.hsqldb.jdbcConnection holds a static instance of 
HashTable-tdatabase(url,org.hsqldb.Database Objects). 
When closing connection the corresponding entry is 
removed and the Database objects goes out of scope.
2. Now when i reconnect to the same DB, it creates an 
entry in tdatabase. And if the finalizer for the previously 
freed Database objects is called now the entry in the 
tdatabase(jdbcConnection class) is removed and if you 
try to get any more connection it reports with the above 
bug as it tries to create a new instance of DB instead of 
creating a new connection(openStandalone(...) method 
in jdbcConnection Class).
Solution.
1. We must not depend on the finalizer method as we 
have no controll over it.
2. never call close to a connection(will be a bad 
solution).
3. As a temporary solution i have commented method 
lines in removeDatabase(...) in jdbcConnection Class and 
everything appears to work fine for me. 
Other Details.
jdk - 1.4.1_01
hiberate - 2.0 --- which gives a connection pool
hypersonic - 1.7.1
my stack trace example.
Creating DB : org.hsqldb.Database@1594a88 -- 
jdbc:hsqldb:myDB user-security1 pwd-pwd
Closing DB org.hsqldb.Database@1594a88 in thread 
Thread[main,5,main] -- -- jdbc:hsqldb:myDB user-
security1 pwd-pwd
Creating DB : org.hsqldb.Database@11d2066 ---- 
jdbc:hsqldb:myDB user-real pwd-123
Closing DB org.hsqldb.Database@1594a88 in thread 
Thread[Finalizer,8,system]
TW1 -- Top level Transcation started
Trying to start inner Transcation 
ERROR: The database is already in use by another 
process
ERROR: Cannot open connection
java.sql.SQLException: The database is already in 
use by another process
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/333
HyperSQL Database Engine (HSQLDB) / Bugs / #333 Transactions and closing server from dos bug!
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
http://sourceforge.net/forum/forum.php?
thread_id=945623&amp;forum_id=73674
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/222
HyperSQL Database Engine (HSQLDB) / Bugs / #222 Log-Thread not exiting if any connect fails before
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Hi, 
Using the henplus JDBC Shell 
&lt;http://henplus.sourceforge.net/&gt; 
I noticed, that the Logger thread in hsqldb is not exiting 
properly, if any of the connect attempts to a database 
failed because of user/password failure for instance. 
Why I noticed this with henplus is, because henplus first 
tries to connect to the database just with the JDBC-URL 
alone and if this fails, prompts for the password. 
This means, that the first connect will always fail, while 
the second will succeed, if the user/password is right. 
The problem is, that hsqldb starts the Logger thread with 
the first attempt to connect to the database and 
increments the usage count .. however that connection 
never gets used, because connecting fails and throws 
an SQL-Exception (see 
jdbcConnection::openStandalone()). This means, that the 
usage count is always the number of all _attempted_ 
connects not real connects. 
I did a simple fix, see attached patch. This patch 
initializes the usage count with zero and _after_ the 
connect is successful (i.e. if no Exception has been 
thrown), the usage count is incremented. This will make 
sure, that the last active connection, that is close()ed, 
will shut down the Logger thread correctly. 
Note, however, that this is not a complete fix to the 
problem. If we get _any_ connection that connection that 
connects correcly, then this solution will work, since the 
database is removed and the Logger thread is closed in 
the close() of that very connection if the usage count 
turns out to be zero. However, if _no_ connection will 
succeed, then we will still have one database in the 
hashtable since no close() will run through (this is 
another problem: in finalize(), close() is called; however if 
this is a jdbcConnection that failed to connect, then the 
session is 'null' and executing a shutdown on that 
session will fail as well -- so the finalizer thread throws a 
NullPointerException. The finalaizer-Thread better should 
catch any Throwable instead of only a SQL-Exception).
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/239
HyperSQL Database Engine (HSQLDB) / Bugs / #239 Thread SQL Scripts in Help Forum
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
Enclosed is the SQL Script that I do not manage to have
run by the ScriptTool. It is the same that produces the
&quot;Wrong data type or data too long in DEFAULT clause&quot;
error from my DatabaseManager thread.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/250
HyperSQL Database Engine (HSQLDB) / Bugs / #250 count distinct rolls back when no records counted
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
executing a count distinct query, when there are no 
records counted, fails. a rollback is executed an null is 
returned.
trace when there are records:
1049962192937|0|0|statement|SELECT count(distinct 
A0.ID) FROM IBANX_PERMIT A0|SELECT count
(distinct A0.ID) FROM IBANX_PERMIT A0
1049962192937|0|0|commit||
trace when there are no records:
1049962192781|16|0|statement|SELECT count(distinct 
A0.ID) FROM IBANX_PERMIT A0|SELECT count
(distinct A0.ID) FROM IBANX_PERMIT A0
1049962192796|0|0|rollback||
roger janssen
roger.janssen@ibanx.nl
iBanx
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<

https://sourceforge.net/p/hsqldb/bugs/288
HyperSQL Database Engine (HSQLDB) / Bugs / #288 SAVEPOINT and ROLLBACK
>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>
SAVEPOINT savepoint_name ;
and
ROLLBACK TO SAVEPOINT savepoint_name ;
Are not document in hsqlSyntax.html but exists in
javadoc class org.hsqldb.jdbcConnection. 
Affected versions 1.7, 1.7.1, 1.7.2-alpha M.
<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<<
