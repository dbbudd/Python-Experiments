#import tkinter for GUI and input control

import socket
import tkinter as tk
from tkinter import *
import os

data = ""

def AttemptConnection():
    connectionmessagetempvar = connectionmessagevar.get()
    connectionmessagevar.set(connectionmessagetempvar + "\n" + "Attempting to connect")

def transmit(data):
    HOST, PORT = "192.168.1.110", 9999

    #Create a socket (SOCK_STREAM means a TCP socket)
    sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    try:
        # Connect to server and send data
        sock.connect((HOST, PORT))
        sock.sendall(bytes(data + "\n", "utf-8"))

        # Receive data from the server and shut down
        received = str(sock.recv(1024), "utf-8")
    finally:
        sock.close()

    print("Sent: {}".format(data))
    print("Received: {}".format(received))


def keypress(event):
    # the logic for handling the individual keys is done by the server script
    data = event.char
    transmit(data)

def keyunpress(event):
    # the logic for handling the individual keys is done by the server script
    data = "unpress"
    transmit(data)



#setup GUI Window
window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("800x600")
window.title("EmuBot")

#connection buttons
connectionbutton = tk.Button(window, text="Connect", command=AttemptConnection)
connectionbutton.grid(row=0, column=4)
connectionmessagevar = tk.StringVar()
connectionmessage = tk.Message(window, textvariable=connectionmessagevar, width=100, )
connectionmessage.grid(row=1, column=1, rowspan=1, columnspan=1)
disconnectionbutton = tk.Button(window, text="Disconnect")
disconnectionbutton.grid(row=0, column=5)

window.bind_all('<Key>', keypress)
window.bind('<KeyRelease>', keyunpress)

connectionmessagevar.set("PiBotController Initiated")

#initialte the root window main loop
window.mainloop()
