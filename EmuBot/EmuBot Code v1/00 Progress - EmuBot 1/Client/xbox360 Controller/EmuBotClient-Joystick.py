import socket

#required for video streaming script
import subprocess
import os
import time

import pygame

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

CONNECTION_ATTEMPT = True
buttonPressed = False

xboxButtons = {0:"w", 1:"s", 2:"a", 3:"d", 4:"u", 5:"i", 8:"r", 9:"t", 10:"q" }
xboxAxis = {2:"x", 3:"y", 1:"y1"}

xboxB = [0, 1, 2, 3, 4, 5, 8, 9, 10]
xboxA = [2, 3, 1]

#-------------<Alex Code>-------------#

class KeyPressEvent(object):
        def __init__(self, char):
                import time
                self.time = time.clock()
                self.char = char
                self.released = False

class KeyPressHandler(object):
        
        RE_PRESS_TIME = 0.005

        def __init__(self):
                self.dictChar = {}

        def isKeyPressed(self, keyChar):
                if keyChar in self.dictChar:
                        return True
                return False

        def getPressObj(self, keyChar):
                return self.dictChar[keyChar]

        def getPressed(self):
                return self.dictChar.keys()
        
        def checkRelease(self):
                import time
                released = []
                for pressChar in self.dictChar:
                        if self.getPressObj(pressChar).released == True:
                                if self.getPressObj(pressChar).time + self.RE_PRESS_TIME < time.clock():
                                        released += [pressChar]
                                        #self.dictChar.pop(pressChar)
                                        

                for pressChar in released:
                        self.dictChar.pop(pressChar)
                                        
                return released

        def keyPress(self, event):
                import time
                if not str(event) in self.dictChar:
                        #Update or add object
                        pressObj = KeyPressEvent(str(event))
                        self.dictChar[str(event)] = pressObj
                else:
                        pressObj = self.getPressObj(str(event))
                        pressObj.released = False
                        pressObj.time = time.clock()

        def keyRelease(self, event):
                pressObj = self.getPressObj(str(event))
                pressObj.released = True                       
                
keyPressHandler = KeyPressHandler()                                             

def mainLoop():
        reled = keyPressHandler.checkRelease()

        for pressChar in reled:
                data = pressChar*2
                if CONNECTION_ATTEMPT: transmit(data)
                print("wrote:", pressChar*2)
                
        
        window.after(20,mainLoop)


#-------------<Alex Code>------------#

data = ""

def transmit(data):
        #HOST, PORT = "192.168.1.110", 9999
        HOST, PORT = "192.168.100.1", 9999

        #Create a socket (SOCK_STREAM means a TCP socket)
        sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

        try:
                #Connect to server and send data
                sock.connect((HOST, PORT))
                
                data = data + chr(10)
                #print(isinstance(data, str))
                
                #print("=" + data + "=")

                #data = data.encode("hex")
                sock.sendall(str(data))#, "utf-8"))

                received = str(sock.recv(1024))#, "utf-8")
        finally:
                sock.close()

        print("Sent: {}".format(data))
        print("Received: {}".format(received))

def keypress(event):
        #the logic for handling the individual keys is done by the server script
        data = str(event)
        if CONNECTION_ATTEMPT: transmit(data)
        print("wrote:", event)
        keyPressHandler.keyPress(event)

def keyunpress(event):
        #the logic for handling individual keys is done by the server script
        #Release is transmited in mainLoop()
        keyPressHandler.keyRelease(event)


def startVideo():
        port = 5000
        fps = 60
        cache = 1024
        start_command = "netcat -l -p %s | mplayer - fps %s -cache %s -" %(port, fps, cache)
        subprocess.call(start_command, shell=True)
        #os.system(start_command)

        print("client started")

        #send message to EmuBot to start sending
        command = "startCamera"
        transmit(command)

def stopVideo():
        os.system("killall -9 netcat")
        os.system("killall -9 mplayer")
        print("Client video stopped")

        command = "stoppCamera"
        transmit(command)

class TextPrint:
        def __init__(self):
                self.reset()
                self.font = pygame.font.Font(None, 20)

        def printWords(self, screen, textString):
                textBitmap = self.font.render(textString, True, BLACK)
                screen.blit(textBitmap, [self.x, self.y])
                self.y += self.line_height

        def reset(self):
                self.x = 10
                self.y = 10
                self.line_height = 15

        def indent(self):
                self.x += 10

        def unindent(self):
                self.x -= 10

pygame.init()

#width adn height
size = [500, 700]
screen = pygame.display.set_mode(size)

pygame.display.set_caption("joystick")

done = False

# used to mange how fast the screen upadates
clock = pygame.time.Clock()

pygame.joystick.init()

textPrint = TextPrint()

def joystickHandler(eventx, eventy, eventy1):
    eventx = int(float(eventx) * 90)
    eventy = int(float(eventy) * 90)
    eventy1 = int(float(eventy1) * 90)

    deadZone = 15
    
    if abs(eventx) < deadZone:
        eventx = 0

    if abs(eventy) < deadZone:
        eventy = 0

    if abs(eventy1) < deadZone:
        eventy1 = 0
        
    data = [str(eventx), str(eventy), str(eventy1)]
    data = " ".join(data)
    if CONNECTION_ATTEMPT: transmit(data)

def buttonHandler(button, state):
        if state == 1:
                #buttonPressed = True
                data = str(xboxButtons[button])
                if CONNECTION_ATTEMPT: transmit(data)

        elif state == 0 & buttonPressed == True:
                #buttonPressed = False
                data = str(xboxButtons[button]) * 2
                if CONNECTION_ATTEMPT: transmit(data)

        

# -------- Main Program Loop -----------
while done==False:

        screen.fill(WHITE)
        textPrint.reset()

        joystick_count = pygame.joystick.get_count()
        textPrint.printWords(screen, "Number of joysticks: {}".format(joystick_count) )
        textPrint.indent()

        for i in range(joystick_count):
                for event in pygame.event.get():
                        if event.type == pygame.QUIT: # If user clicked close
                                done=True
                        if event.type == pygame.JOYBUTTONDOWN:
                                print("Joystick button pressed.")
                                
                        if event.type == pygame.JOYBUTTONUP:
                                print("Joystick button released.")

                joystick = pygame.joystick.Joystick(i)
                joystick.init()
            
                textPrint.printWords(screen, "Joystick {}".format(i) )
                textPrint.indent()
            
                name = joystick.get_name()
                textPrint.printWords(screen, "Joystick name: {}".format(name) )
                
                # Usually axis run in pairs, up/down for one, and left/right for
                # the other.
                axes = joystick.get_numaxes()
                textPrint.printWords(screen, "Number of axes: {}".format(axes) )
                textPrint.indent()

                
                axis1 = 0
                axis2 = 0
                axis3 = 0
                for i in range(axes):
                        axis = joystick.get_axis(i)
                        if i in xboxA:
                                if i == 2:
                                        axis2 = ("%.2f" % axis)
                                if i == 3:
                                        axis3 = ("%.2f" % axis)
                                if i == 1:
                                        axis1 = ("%.2f" % axis)

                        textPrint.printWords(screen, "Axis {} value: {:>6.3f}".format(i, axis))
                        
                joystickHandler(axis3, axis2, axis1)
                textPrint.unindent()
                    
                buttons = joystick.get_numbuttons()
                textPrint.printWords(screen, "Number of buttons: {}".format(buttons) )
                textPrint.indent()

                for i in range(buttons):
                        button = joystick.get_button(i)
                        if i in xboxB:
                                buttonHandler(i, button)

                        '''for i in xboxB:
                                if button == 1:
                                        keypress(xboxButtons[i])
                                elif button == 0:
                                        keyunpress(xboxButtons[i])'''
                                        
                        '''for event in pygame.event.get():
                                # Possible joystick actions: JOYAXISMOTION JOYBALLMOTION JOYBUTTONDOWN JOYBUTTONUP JOYHATMOTION
                                if event.type == pygame.JOYBUTTONDOWN & i in xboxButtons:
                                        print("Joystick button pressed. =", i, xboxButtons[i])
                                        keypress(str(xboxButtons[i]))
                                        
                                if event.type == pygame.JOYBUTTONUP & i in xboxButtons:
                                        print("Joystick button released. ==", i, xboxButtons[i])
                                        keyunpress(str(xboxButtons[i]))'''
                        

                        textPrint.printWords(screen, "Button {:>2} value: {}".format(i,button))
                textPrint.unindent() 
                
                textPrint.unindent()
            
        #update the screen
        #pygame.display.flip()

        # 20fps
        #clock.tick(20)
    
# Close the window and quit.
pygame.quit ()

'''
#setup GUI Window
window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("400x600")
window.title("EmuBot")

#camera control interface
frmCamera = tk.Frame(window, height=400, width=400)
frmCamera.grid(row=4, column=0, rowspan=3, columnspan=3)

lblCamera = tk.Label(frmCamera, text="Camera Controls")
lblCamera.grid(row= 0, column=0, columnspan=4)
btnCamStart = tk.Button(frmCamera, text="Start Cam", command=startVideo)
btnCamStart.grid(row = 1, column = 1)
btnCamStop = tk.Button(frmCamera, text="Close Cam", command=stopVideo)
btnCamStop.grid(row = 1, column = 2)

lblControls = tk.Label(frmCamera, text = "The Contols:")
lblControls.grid(row = 3, column = 0, columnspan = 4)

lblPan = tk.Label(frmCamera, text="Press numbers 1, 2, and 3 to move the Pan")
lblPan.grid(row = 4, column = 0, columnspan=4)

lblTilt = tk.Label(frmCamera, text = "Press Z, X and C to move the Tilt")
lblTilt.grid(row = 5, column = 0, columnspan = 4)

lblShoulder = tk.Label(frmCamera, text="Press J, K and L to move the Shoudler")
lblShoulder.grid(row = 6, column = 0, columnspan = 4)

lblTilt = tk.Label(frmCamera, text = "Press W, A, S, D to move in a Direction")
lblTilt.grid(row = 7, column = 0, columnspan = 4)

lblDevide = tk.Label(frmCamera, text = "-- Please Note --")
lblDevide.grid(row = 8, column = 0, columnspan = 4)

lblJoystick = tk.Label(frmCamera, text = "- If the mouse is in the centre of the Joystick it will stop moving")
lblJoystick.grid(row = 9, column = 0, columnspan = 4)

lblJoy = tk.Label(frmCamera, text = "- The joystick is inverted")
lblJoy.grid(row = 10, column = 0, columnspan = 4)

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
            if CONNECTION_ATTEMPT: transmit(data)
        
activate = tk.Label(window, text="MOUSE", fg = "green")
frame = tk.Frame(window, height = sizeMouseFrame, width = sizeMouseFrame, bg = "grey")
mousePosLabel = tk.Label(window, text="Mouse: ---")
activate.grid(row = 1, column = 1)
frame.grid(row = 2, column = 1)
frame.bind('<Motion>', handler)
mousePosLabel.grid(row = 3, column = 1)

#==== Inactive
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
'''
#==== /Inactive
'''    
window.bind('<Up>', upKey)
window.bind('<Down>', downKey)
'''
# ----------------------------- </Josh's code> -----------------------------
'''
window.after(20,mainLoop)
window.mainloop()
'''
