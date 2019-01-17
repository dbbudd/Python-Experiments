#!/usr/bin/env python

import SocketServer

class MyTCPHandler(socketserver.BaseRequestHandler):
    '''
    The RequestHandler class for our server.
    It is instantiated once per connection to the server, and must override the handle() method to implement communication to the client.
    '''
    def handle(self):
        #self.request is the TCP socket connect to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        print(self.data)
        #just send back the same data, but upper-case
        self.request.sendall(self.data.upper())

if __name__ == "__main__":
    HOST, PORT = "localhost", 9999

#Create the server, binding to localhost on port 9999
server = socketserver.TCPServer((HOST, PORT), MyTCPHandler)

# Activate the server; this will keep running until you
# interupt the program (e.g. Ctrl-C)
server.serve_forever()

'''
#Simple Server example
import socket                           #This is server.py file

s = socket.socket()                     #Import socket module
host = socket.gethostname()             #Get local machine name
port = 12345                            #Reserve a port for your service.
s.bind((host, port))                    #Bind to the port

s.listen(5)                             #Now wait for client connection
while True:
    c, addr = s.accept()                #Establish connection with client.
    print("Got connection from", addr)
    c.send("Thank you for connecting")
    c.close()                           #Close the connection

'''


