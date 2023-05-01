import socket
"""library for creating sockets"""

from threading import Thread
""" In our chat application, since we are dealing with multiple clients, we can use threads """

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
"""creating a socket with the help of socket.socket() function"""

"""AF_INET represents IPv4 while AF_INET6 represents IPv6"""

"""
SOCK_STREAM is used to create a TCP Socket.
SOCK_DGRAM is used TO create a UDP Socket
"""

"""we are building a chat app, we do not want the messages to be received in the wrong
order, or to not receive a few messages at all, therefore we are going with
SOCK_STREAM instead of SOCK_DGRAM"""


ip_address = '127.0.0.1'
port = 8000
"""Since our localhost IP Address is 127.0.0.1, we will be using that here and we can go
with port 8000, however this port can be any number. Just make sure that it is not
anything lower than 1,024, since those are reserved ports."""


server.bind((ip_address, port))
server.listen()

"""bind our server with the IP Address and
the Port that we want to use and then we are ready to
listen for any incoming requests from the clients!"""

list_of_clients = []
"""Now multiple clients can connect on our server, therefore we would want to maintain a list
of all the clients that are connected to the server at any given time, so let’s create a list for
that """

print("Server has started...")


"""let’s create the function clientthread().In this function, the first thing that we’d like to do is to
welcome the client to the chat app -"""
def clientthread(conn, addr):
    """the client’s socket object conn has a special function called send(), which can send
    any message to that client."""
    conn.send("Welcome to this chatroom!".encode('utf-8'))
    
    """this function clientthread() will only be called once, that’s when the client will try to
   make a connection request with the server.
   The main use of this function is to receive the messages sent by the clients, and send
   those messages to the other clients connected.
   For example, if you are sending a message to your friend, then it’s the server’s
   responsibility to receive the message first, and then send it to your friend


   Now since this will be an active chat, the messages will be sent and received at any time,
   therefore it only makes sense to add another while True loop here 
   """
   
   
    while True:
        try:
            message = conn.recv(2048).decode('utf-8')
            """we have a recv() function to
            receive a message. 2048 is the maximum length of the message that can be received by
            the server. Any message exceeding 2048 characters will be stripped down to 2048
            characters max.
            Also, just how we were encoding our messages with utf-8, this time, we will be decoding
            the messages with the decode() function.
            Now one thing to note is that if the user closes the client app, then too, the server will
            receive a message but there would be no content in the message."""
            if message:
                print ("<" + addr[0] + "> " + message)
                """if the message is there, we will want to send this message to all the other clients
                connected with our server"""
                message_to_send = "<" + addr[0] + "> " + message
                broadcast(message_to_send, conn)
            else:
                remove(conn)
                
            """if the message is there, then we will perform something otherwise we will want to
            remove the client’s socket object stored with us in our client_list!"""
        except:
            continue
        
"""we are yet to create the remove() and the broadcast() functions."""
def broadcast(message, connection):
    for clients in list_of_clients:
        if clients!=connection:
            try:
                clients.send(message.encode('utf-8'))
            except:
                remove(clients)

def remove(connection):
    if connection in list_of_clients:
        list_of_clients.remove(connection)

"""Here, we can see that inside the broadcast() function, we are iterating over all the client
socket objects we have in list_of_clients list.
Inside this for loop, we have an if condition that checks if the socket object is the same
as the one which sent the message or not. If not, then we have a try-except block where
inside the try statement, we are trying to send the message with utf-8 encoding using the
send() function"""






"""The job of our server is to listen to clients trying to make a request for as long as it’s running. """
while True:
    """Inside this loop, the first thing that we want to do is to accept any connection request
    made by a client to our server. Now our server is a Socket object that we created above,
    and it has a special method called accept()."""
    
    conn, addr = server.accept()
    """This accept() method accepts any connection request made to the server and returns 2
    parameters -
    1. The socket object of the client that is trying to connect -conn
    2. Their IP Address and Port number in the form of a tuple   -addr """
    
    list_of_clients.append(conn)
    """we have a client that tried connecting with the server, we can append it’s socket
    object conn to our list_of_clients to use later."""
    print (addr[0] + " connected")
    
    
    """threading! It allows different parts of the programs to run concurrently using threads where threads
    are a separate flow of execution""" 
    new_thread = Thread(target= clientthread,args=(conn,addr))
    new_thread.start()
    """target here, is the name of the function that we want this thread to execute, and args are
     the parameters that you may want to pass into that function.
     In our case, we are calling a function clientthread with arguments (conn, addr). 
     
     we are yet to create the function clientthread.
     o start this thread, we can simply call the start() function on our newly created thread"""