#!/usr/bin/env python

import SocketServer
import serial
import sys
import Tkinter as tk
import picamera
import math

import os


import time

MOVE_SPEED = 20

#math.degrees()

#config to fix repeating press error
#os.system("xset r off")

#configure picamera
camera = picamera.PiCamera()
camera.preview_fullscreen = False
camera.preview_window = (600, 320, 640, 480)
camera.resolution = (640, 480)


# important AX-12 constants
AX_WRITE_DATA = 3
AX_READ_DATA = 4

s = serial.Serial()                        # create a serial port object
s.baudrate = 57600                        # baud rate, in bits/second
s.port = "/dev/ttyAMA0"            # this is whatever port your are using
s.timeout = 3.0
s.open()


DXL_REG_CCW_Angle_Limit = 8 #to change control mode
DXL_REG_Goal_Postion = 30
DXL_REG_Moving_Speed = 32

activeDir = {"w":False}

def writeShort(val):
        s.write(chr(int(val)%256))
        s.write(chr(int(val)>>8))

def writeWord(ID, addr, val):
        s.write('W'+'w'+chr(ID))
        writeShort(addr)
        writeShort(val)

def jointMode(ID):
        s.write('W'+'j'+chr(ID))

def setPosition(ID, pos, vel):
        s.write('W'+'p'+chr(ID))
        writeShort(pos)
        writeShort(vel)




def moveToDxAngle(ID,dxlPosition,dxlSpeed):
        setPosition(ID,dxlPosition,dxlSpeed)

def moveToDegAngle(ID, degPosition, pcSpeed): 
        while degPosition > 180:
                degPosition = degPosition - 360
        while degPosition < -180:
                degPosition = degPosition + 360

        if (degPosition < -150):
                degPosition = -150
        if (degPosition > 150):
                degPosition = 150
        moveToDxAngle(ID, int(float(degPosition)*3.41+511.5), int(float(pcSpeed)*10.23))

def spinAtDxSpeed(ID,dxlSpeed):
        writeWord(ID,DXL_REG_Moving_Speed,dxlSpeed)

# Spins at a certain percent of full speed. 
def spinAtPcSpeed(ID,pcSpeed): 
        if pcSpeed >= 0:
                spinAtDxSpeed(ID,int(float(pcSpeed)*10.23))
        else:
                spinAtDxSpeed(ID,1024+int(float(-pcSpeed)*10.23))

def throttleSteeringToLeftRight(inThrottle, inSteering):
        left = min(100, max(-100, inThrottle - inSteering)); 
        right = min(100, max(-100, inThrottle + inSteering)); 
        return (left, right)

class joint(object):        
        def __init__(self, servoID, minLimit, maxLimit, moveSpeed = 20, defaultPos=0):
                self.servoID = servoID
                self.minLimit = minLimit
                self.maxLimit = maxLimit
                self.currAngle = 0
                self.moveSpeed = moveSpeed
                self.defaultPos = defaultPos
                #getting servo object

        def moveToAngle(self, angle):
                if angle <= self.maxLimit and angle >= self.minLimit:
                        moveToDegAngle(self.servoID, angle, self.moveSpeed)
                        self.currAngle = angle
                        time.sleep(0.05)

        def increaseAngle(self, dist = 1):
                self.moveToAngle(self.currAngle+dist)
                self.currAngle += dist

        def gotoDefaultPos(self):
                self.moveToAngle(self.defaultPos)

class Wheel(object):
        def __init__(self, servoID):
                self.servoID = servoID
        
        def spinAtSpeed(self, pcSpeed):
                spinAtPcSpeed(self.servoID, pcSpeed)


class Robot(object):
        
        """
        #Front Left (100 fwd)
        #Front Right (-100 fwd)
        #Back Right (-100 fwd)
        #Back Left (100 fwd)
        """
        
        wheelStates = {"stop":{"fl":0,"fr":0,"br":0,"bl":0},
                "fwd":{"fl":100,"fr":-100,"br":-100,"bl":100},
                "back":{"fl":-100,"fr":100,"br":100,"bl":-100},
                "left":{"fl":100,"fr":100,"br":100,"bl":100},
                "right":{"fl":-100,"fr":100,"br":100,"bl":-100}}
        
        def __init__(self, servoDict, wheelsDict):
                self.servos = servoDict
                self.wheels = wheelsDict
                self.resetJointPos()
        
        def getServo(self, servo):
                return self.servos[servo]
        
        def getWheel(self, wheelID):
                return self.wheels[wheelID]
                
        def wheelMove(self, stateID="stop"):
                stateDict = self.wheelStates[stateID]
                for wheel in stateDict.keys():
                        self.getWheel(wheel).spinAtSpeed(stateDict[wheel])

        def resetJointPos(self):
                for joint in self.servos.values():
                        joint.gotoDefaultPos()

# Purge the first value
time.sleep(0.5) 
shoulderPos = -45
tiltPos = 0
panPos = 0

# Set wheel and joint modes. 
writeWord(1, DXL_REG_CCW_Angle_Limit, 0)
writeWord(2, DXL_REG_CCW_Angle_Limit, 0)
writeWord(3, DXL_REG_CCW_Angle_Limit, 0)
writeWord(4, DXL_REG_CCW_Angle_Limit, 0)

jointMode(5)
jointMode(6)
jointMode(7)


shoulderObj = joint(5, -90, 150, moveSpeed=10)
panObj = joint(7, -90, 90, moveSpeed = 50)
tiltObj = joint(6, -90, 90)

flWheel = Wheel(1)
frWheel = Wheel(2)
blWheel = Wheel(4)
brWheel = Wheel(3)

robotObj = Robot({"shoulder":shoulderObj, "pan":panObj, "tilt":tiltObj}, {"fl":flWheel, "fr":frWheel, "bl":blWheel, "br":brWheel})

def demo():
        #Raymond's original code
        tiltSpeed = 100
        panSpeed = 100
        shoulderSpeed = 100
        shoulderPos = 0

        # Shoulder is limited to -90 and 150. Note that this will hit the ground (which could be desired).
        shoulderPos = max(-90, min(150, shoulderPos))

        tiltcmd = tiltPos + shoulderPos

        # Tilt is limited to 90 degrees, pan to 150.
        tiltcmd = max(-90, min(90, tiltcmd))


        moveToDegAngle(6, shoulderPos,shoulderSpeed)
        moveToDegAngle(6, tiltcmd, max(10, tiltSpeed))

        time.sleep(0.05) 

def resetCamPos():
        pan(0, MOVE_SPEED)
        tilt(0,MOVE_SPEED)
        shoulderObj.moveToAngle(0)
        
def startCamera():
        camera.start_preview()

        camera.sharpness = 10
        camera.contrast = 30
        camera.vflip = True
        camera.hflip = True
        camera.exposure_mode = "auto"
        camera.brightness = 60

        '''
        camera.capture("image.jpg")
        camera.start_recording('video.h264')
        sleep(5)
        camera.stop_recording()
        '''

def stopCamera():
        camera.stop_preview()
        camera.close()

class MyTCPHandler(SocketServer.BaseRequestHandler):
    '''
    The RequestHandler class for our server.
    It is instantiated once per connection to the server, and must override the handle() method to implement communication to the client.
    '''
    def handler(self):
        listmouse = self.data.split()
        posx = int(listmouse[0])
        posy = int(listmouse[1])
        panPos = posx - 90
        tiltPos = -1 * (posy - 90)
        robotObj.getServo("pan").moveToAngle(panPos)
        robotObj.getServo("tilt").moveToAngle(tiltPos)
    
    def handle(self):
        #self.request is the TCP socket connect to the client
        self.data = self.request.recv(1024).strip()
        print("{} wrote:".format(self.client_address[0]))
        self.request.sendall(self.data.upper())

        #handle the data being sent
        x = self.data
        print("info", x, len(x))
        if len(x) == 1:
                if x == "q":


                        robotObj.wheelMove("stop")
                        robotObj.resetJointPos()
                        #resetCamPos()
                        #camera.close()
                        #window.destroy()
                        #window.quit()
                elif x == "w":
                        robotObj.wheelMove("fwd")
                elif x == "a":
                        robotObj.wheelMove("left")
                elif x == "d":
                        robotObj.wheelMove("right")
                elif x == "s":
                        robotObj.wheelMove("back")
                elif x == "1":
                        robotObj.getServo("pan").increaseAngle()
                elif x == "2":
                        robotObj.getServo("pan").moveToAngle(0)
                elif x == "3":
                        robotObj.getServo("pan").moveToAngle(45)
                elif x == "z":
                        robotObj.getServo("tilt").moveToAngle(-90)
                elif x == "x":
                        robotObj.getServo("tilt").moveToAngle(0)
                elif x == "c":
                        robotObj.getServo("tilt").moveToAngle(90)
                elif x == "i":
                        robotObj.getServo("shoulder").moveToAngle(0)
                elif x == "k":
                        robotObj.getServo("shoulder").moveToAngle(90)
                else:
                        print(x)
                        print("press another key please")
        elif len(x) == 2:
                #keyup?
                x = x[0]
                if x == "q":
                        None
                elif x == "w":
                        robotObj.wheelMove("stop")
                elif x == "a":
                        robotObj.wheelMove("stop")
                elif x == "d":
                        robotObj.wheelMove("stop")
                elif x == "s":
                        robotObj.wheelMove("stop")
        else:
                #xy thing
                self.handler()
                
        
        

if __name__ == "__main__":
    HOST, PORT = "", 9999

#Create the server, binding to localhost on port 9999
server = SocketServer.TCPServer((HOST, PORT), MyTCPHandler)

# Activate the server; this will keep running until you
# interupt the program (e.g. Ctrl-C)
server.serve_forever()



'''
#setup GUI Window
window = tk.Tk()
window.resizable(width=False, height=False)
window.geometry("800x600")
window.title("EmuBot")

#camera control interface
frmCamera = tk.Frame(window, height=400, width=400)
frmCamera.grid(row=0, column=0, rowspan=3, columnspan=3)

lblCamera = tk.Label(frmCamera, text="Camera Controls")
lblCamera.grid(row=0, column=0, columnspan=2)
btnCamStart = tk.Button(frmCamera, text="Start Cam", command=startCamera)
btnCamStart.grid(row = 1, column = 0)
btnCamStop = tk.Button(frmCamera, text="Close Cam", command=stopCamera)
btnCamStop.grid(row = 1, column = 1)

lblPos = tk.Label(frmCamera, text="Press numbers 1, 2, and 3 on your keyboard to Pan")
lblPos.grid(row = 3, column = 0, columnspan=3)


leave these here just so you can test with keyboard input
or stop the application if needed

window.bind_all('<KeyPress>', keypress)
window.bind("<KeyRelease>", keyunpress)

window.mainloop()
'''


