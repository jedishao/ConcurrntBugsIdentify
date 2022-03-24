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