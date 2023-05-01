# 199

SOCKETS - SERVER
----------------------------------------------------------------
sockets can be a combination of an IP Address and a Port!

Sockets allow communication between two different processes (or applications) on the same or different machines

They are used in a client-server application framework.

-------------------------------------------------------------------
Servers are backend applications (or processes) that perform some functions on a request from the client.
------------------------------------------------------------------
Different HTTP Requests are GET,POST,PUT,DELETE

Example:

 when you surf to a website on the browser, the browser is making a GET request to the server of that
website, which returns data. This data could be in the form of a JSON, on HTML content.

In this scenario, your browser running in your machine is the Client.

Both HTTP and HTTPS use sockets to transfer data back and forth between server and client, therefore whenever
your browser makes a request to the website's server, it’s establishing a connection through sockets.
----------------------------------------------------------------
same website can be accessed by multiple browsers running on different machines at the
same time.This is one of the attributes of the server. It can establish connections to multiple clients at a time.
-----------------------------------------------------------------------
**************************************************************************************************
Build a chat App using socket Programming

-->it will be required to build a client and a server and we can do it through socket programming in Python\

Socket.py\
--------\
-->use  "socket" library for creating sockets
-->create a socket with the help of socket.socket() function.

socket.socket() function takes two arguments:address family,socket type


1.address family: is the family of addresses that the socket can communicate with. 
Classic examples of 2 of the most famous address families are IPv4 and IPv6.

AF_INET represents IPv4 while AF_INET6 represents IPv6.

AF_INET is also the default value of the first argument, if not provided. That’s because
IPv4 is still widely used while IPv6 is relatively new.

2.socket type :we are using SOCK_STREAM. It is the default value (if not provided) and it
is used to create a TCP Socket.
We could also use SOCK_DGRAM which is used to create a UDP Socket, however use of it case specific.\

------------------------------------------------------------------------------------------------\
Tcp (TCP (Transmission Control Protocol) :
1.Tries to resend the packets that are lost\
2.Adds a sequence number to the packets and reorders them to ensure the packets do not arrive in wrong order\
3.Slower, as it manages everything \
4.Heavy to use as OS keeps track of ongoing communication sessions between clients and servers\
4.TCP is used by - HTTP,HTTPS,SMTP,FTP etc.\

UDP (User Datagram Protocol)
1.Doesn’t resend the packets that are lost\
2.Packets can arrive in any order.\
3.Faster due to lack of feature\
4.Lighter to use on the machine\
5.UDP is used by - DNS,DHCP etc.\
--------------------------------------------------------------------------------------------------\
UDP doesn’t have many use cases. In our case, since we are building a chat app, we do not want the messages to be received in the wrong
order, or to not receive a few messages at all, therefore we are going with SOCK_STREAM instead of SOCK_DGRAM
---------------------------------------------------------------------------------------------\
Since our localhost IP Address is 127.0.0.1, we will be using that here and we can go
with port 8000, however this port can be any number. Just make sure that it is not
anything lower than 1,024, since those are reserved ports

---------------------------------------------------------------------\
Next, we want to bind our server with the IP Address and the Port that we want to use and then we are ready to
listen for any incoming requests from the clients

Our server is the socket that we created earlier with the socket.socket() function and we are using the bind() function that takes a tuple with ip_address and port in it.
Once our server is binded, we can start listening on this server socket with the listen()
function.

Now multiple clients can connect on our server, therefore we would want to maintain a list
of all the clients that are connected to the server at any given time, so let’s create a list for
that.

In this list, we can store all the clients that are connected with the server at any given
time.
--------------------------------------------------------------------------\
Let’s run this code in the terminal to see what we get?
python3.8 server.py


The job of our server is to listen to clients trying to make a request for as long as it’s running.
------------------------------------------------------------\
while TRUE
Inside this loop, the first thing that we want to do is to accept any connection request
made by a client to our server. Now our server is a Socket object that we created above,
and it has a special method called accept()
   
   
This accept() method accepts any connection request made to the server and returns 2
parameters -
1. The socket object of the client that is trying to connect
2. Their IP Address and Port number in the form of a tuple


Here, first we are accepting any connection requests made to the server with
server.accept() function, and then we are saving the 2 parameters in returns in conn,
which is the socket object of the client that is trying to connect and addr, which is a tuple
containing IP Address and Port Number of the client.
Since we have a client that tried connecting with the server, we can append it’s socket
object conn to our list_of_clients to use later.


Multiple clients can connect with the same server at the
same time! This way, we will have just one server instance
running for multiple clients

-----------------------------------------------------------

Imagine a scenario where there are thousands of users
connected to the same server, making a request that takes
5 seconds to execute. As for how Python runs the code, it
will complete the request for the first user, and only then
move to the second user. How slow would the service be!
How do you think anyone can tackle this?

We can use threading! It allows different parts of the
programs to run concurrently using threads where threads
are a separate flow of execution.
In the same scenario above, the function that takes 5
seconds to execute can be executed concurrently for each
of the requests made on a separate thread.
That way, all the requests would be handled separately on
a different thread and can execute simultaneously!

------------------------------------------------------------------------------------
ere, we can see that if Client 1 and Client 2 make a Request at the same time to the
Server, then our server can perform the task in 2 different Threads simultaneously to
save time, without having to wait for the previous tasks to get finished.


In our chat application, since we are dealing with multiple
clients, we can use threads 


importing Thread from the threading module

