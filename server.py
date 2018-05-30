# def create_server():
#   print('Do your work here!')

# if __name__ == '__main__':
#   create_server()

# import socket
# from thread import * 
# #import all functions from the thread library by their own name

# #IP addy of our server
# HOST = '127.0.0.1'

# #port to listen for connections
# PORT = 4444

# #create socket object
# s = socket.socket()

# #bind to the specified host and port
# s.bind((HOST, PORT))

# #listen for a max of 5 connections
# s.listen(5)


# def clientthread(conn):
#   #send a message back to the user that connected over this socket conenction
#   conn.send('You have summoned the Security Eight Ball, what is your question?\n')

#   while True:
#     #receive new messages from the client
#     data = conn.recv(1024)
#     reply = 'You asked: ' + data
#     if not data:
#       break
    
#     conn.sendall(reply)
#   conn.close()

# while True:
#   #wait for someone to try to connect and accept the connection
#   conn, addr = s.accept()
#   print('Got connection from', addr)

#   start_new_thread(clientthread, (conn, ))

#   #send a response
#   # c. send('Hear you loud and clear')

#   #close the connection
# s.close()

import socket
from thread import * #import all functions from the thread library by their own name
import random

host = '127.0.0.1'
port = 4445

def clientthread(conn):
    #Send a message back to the user that connected over this socket connection
    conn.send('You have summoned the Security Eight Ball, what is your question?\n')

    responses = ['sorry to hear that cuz', 'buy a Mac immediately', 'dats too bad', 'holla big fella!']
   

    while True:
        #Receive new messages from the client
        data = conn.recv(1024)
        reply = (responses[random.randint(0, len(responses)-1)]+'\n')
        if not data:
            break
        conn.sendall(reply)
    conn.close() #close only this connection


def create_server():
    # create a socket object
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    # bind to the host and port
    s.bind((host, port))
    # listen and accept a max of 5 connections
    s.listen(5)

    while True:
        # Wait for someone to try to connect and accept the connection
        c, addr = s.accept()
        print('Got connection from', addr)
        # send a response
        start_new_thread(clientthread, (c, ))
    # close the connection
    c.close()

if __name__ == '__main__':
    create_server()