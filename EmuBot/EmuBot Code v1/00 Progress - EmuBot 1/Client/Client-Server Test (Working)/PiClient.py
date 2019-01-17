#!/usr/bin/env python

import socket
import sys

HOST, PORT = "192.168.1.110", 9999
data = "send this data please"

#Create a socket(SOCK_STREAM means a TCP socket)
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    #Connect to server and send data
    sock.connect((HOST, PORT))
    sock.sendall(bytes(data + "\n", "utf-8"))
    
    #Receieve data from the server and shut down
    received = str(sock.recv(1024), "utf-8")
finally:
    sock.close()

print("Sent: {}".format(data))
print("Received: {}".format(received))

'''
#Simple Client example
import socket

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 12345                    # Reserve a port for your service.

s.connect((host, port))
print s.recv(1024)
s.close                         # Close the socket when done.
'''
