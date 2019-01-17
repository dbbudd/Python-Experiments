import socket
import tkinter as tk
from tkinter import *
import os

os.system("xset r off")

data = ""

def transmit(data):
        #HOST, PORT = "192.168.1.110", 9999
        HOST, PORT = "192.168.100.1", 9999

        #Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
                #Connect to server and send data
                sock.connect((HOST, PORT))
                sock.sendall(bytes(data + "\n", "utf-8"))

                received = str(sock.recv(1024), "utf-8")
        finally:
                sock.close()

        print("Sent: {}".format(data))
        print("Received: {}".format(received))

def keypress(event):
        #the logic for handling the individual keys is done by the server script
        data = str(event.char)
        transmit(data)

def keyunpress(event):
        #the logic for handling individual keys is done by the server script
        data = str(event.char)*2
        transmit(data)



#setup GUI Window
window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("800x600")
window.title("EmuBot")

#camera control interface
frmCamera = tk.Frame(window, height=400, width=400)
frmCamera.grid(row=0, column=0, rowspan=3, columnspan=3)
'''
lblCamera = tk.Label(frmCamera, text="Camera Controls")
lblCamera.grid(row=0, column=0, columnspan=2)
btnCamStart = tk.Button(frmCamera, text="Start Cam", command=startCamera)
btnCamStart.grid(row = 1, column = 0)
btnCamStop = tk.Button(frmCamera, text="Close Cam", command=stopCamera)
btnCamStop.grid(row = 1, column = 1)
'''
lblPos = tk.Label(frmCamera, text="Press numbers 1, 2, and 3 on your keyboard to Pan")
lblPos.grid(row = 3, column = 0, columnspan=3)

window.bind_all('<KeyPress>', keypress)
window.bind("<KeyRelease>", keyunpress)

# ----------------------------- <Josh's code> -----------------------------
sizeMouseFrame = 180
active = True

def handler(event):
    if active:
            mousePosLabel.config(text = "Mouse: X:%s Y:%s" % ((event.x - 90), -1*(event.y - 90)))
            unmousePosLabel.config(text = "Mouse: X:%s Y:%s" %  ((event.x - 90), -1*(event.y - 90)))
            data = [str(event.x), str(event.y)]
            data = " ".join(data)
            transmit(data)
        
activate = tk.Label(window, text="MOUSE", fg = "green")
frame = tk.Frame(window, height = sizeMouseFrame, width = sizeMouseFrame, bg = "grey")
mousePosLabel = tk.Label(window, text="Mouse: ---")
activate.grid(row = 1, column = 1)
frame.grid(row = 2, column = 1)
frame.bind('<Motion>', handler)
mousePosLabel.grid(row = 3, column = 1)

unactivate = tk.Label(window, text="MOUSE", fg = "red")
unframe = tk.Frame(window, height = sizeMouseFrame, width = sizeMouseFrame, bg = "grey")
unmousePosLabel = tk.Label(window, text = "Mouse: ---")
unactivate.grid(row = 1, column = 1)
unframe.grid(row = 2, column = 1)
unmousePosLabel.grid(row = 3, column = 1)
unactivate.grid_forget()
unframe.grid_forget()
unmousePosLabel.grid_forget()

def upKey(event):
        activate.grid()
        frame.grid()
        mousePosLabel.grid()
        unactivate.grid_forget()
        unframe.grid_forget()
        unmousePosLabel.grid_forget()
        active = True

def downKey(event):
        unactivate.grid()
        unframe.grid()
        unmousePosLabel.grid()
        activate.grid_forget()
        frame.grid_forget()
        mousePosLabel.grid_forget()
        active = False
    
window.bind('<Up>', upKey)
window.bind('<Down>', downKey)

# ----------------------------- </Josh's code> -----------------------------

window.mainloop()

#config to fix repeating press error
os.system("xset r on")
