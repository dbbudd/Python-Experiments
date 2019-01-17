#!/usr/bin/env python

import SocketServer
import serial
import sys
import Tkinter as tk
import picamera
import math
import subprocess
import os
import time

MOVE_SPEED = 20

#math.degrees()

#config to fix repeating press error
#os.system("xset r off")

#configure picamera
"""camera = picamera.PiCamera()
camera.preview_fullscreen = False
camera.preview_window = (600, 320, 640, 480)
camera.resolution = (640, 480)"""


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

def writeStop(ID):
        s.write('C' + 's' + chr(ID))

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

        def increaseAngle(self, speed = 1.0):
                temp = self.moveSpeed
                self.moveSpeed *= speed
                self.moveToAngle(self.maxLimit)
                self.moveSpeed = temp

        def decreaseAngle(self, speed = 1):
                temp = self.moveSpeed
                self.moveSpeed *= speed
                self.moveToAngle(self.minLimit)
                self.moveSpeed = temp

        def increaseAngleAtSpeed(self, speed):
                moveToDegAngle(self.servoID, self.maxLimit, speed)
                time.sleep(0.05)
                
        def decreaseAngleAtSpeed(self, speed):
                moveToDegAngle(self.servoID, self.minLimit, speed)
                time.sleep(0.05)
                
        def stop(self):
                writeStop(self.servoID)
        
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
                "left":{"fl":-50,"fr":-50,"br":-50,"bl":-50},
                "right":{"fl":50,"fr":50,"br":50,"bl":50}}
        
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
panObj = joint(7, -90, 90, moveSpeed = 20)
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
        robotObj.getServo("pan").moveToAngle(0)
        robotObj.getServo("tilt").moveToAngle(0)
        robotObj.getServo("shoulder").moveToAngle(0)
        
def startCamera():
        fps = 5
        clientIP = "192.168.100.117"
        port = 5000
        height = 360
        width = 640
        time = 0
        start_command = "/opt/vc/bin/raspivid -vf -fps %s -o - -w %s -h %s -t %s | nc.traditional %s %s" % (fps, width, height, time, clientIP, port)
        subprocess.call(start_command, shell=True)

def stopCamera():
        os.system("killall -9 raspivid")
        os.system("killall -9 netcat")

def stopMoving(joint):
        robotObj.getServo(joint).stop()

class MyTCPHandler(SocketServer.BaseRequestHandler):
                
        def handler(self):
                listmouse = self.data.split()
                panPos = int(listmouse[1])
                tiltPos = int(listmouse[0])
                shoulderPos = int(listmouse[2])

                #there is probbly a better way of doing this using map or somthing
                #like that but hardcoding is the temp solution

                panPos += 90
                tiltPos += 90
                shoulderPos += 90
                
                #print("PanPos:", panPos, "tiltPos:", tiltPos, "shoulderPos:", shoulderPos)
                if panPos >= 100:
                        robotObj.getServo("pan").decreaseAngle(speed = abs(panPos-90)/90.0)
                elif panPos >= 80:
                        robotObj.getServo("pan").stop()
                elif panPos >= 0:
                        robotObj.getServo("pan").increaseAngle(speed = abs(panPos-90)/90.0)
                else:
                        print("ISSUE WITH PAN")
                        
                if tiltPos >= 100:
                        robotObj.getServo("tilt").increaseAngle(speed = abs(tiltPos-90)/90.0)
                elif tiltPos >= 80:
                        robotObj.getServo("tilt").stop()
                elif tiltPos >= 0:
                        robotObj.getServo("tilt").decreaseAngle(speed = abs(tiltPos-90)/90.0)
                else:
                        print("ISSUE WITH TILIT")

                if shoulderPos >= 100:
                        robotObj.getServo("shoulder").decreaseAngle(speed = abs(shoulderPos-90)/90.0)
                elif shoulderPos >= 80:
                        robotObj.getServo("shoulder").stop()
                elif shoulderPos >= 0:
                        robotObj.getServo("shoulder").increaseAngle(speed = abs(shoulderPos-90)/90.0)
                else:
                        print("ISSUE WITH SHOULDER")
                
                
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
                                resetCamPos()
                                #this is more of a reset button now
                                
                                #camera.close()
                                #window.destroy()
                                #window.quit()
                        elif x == "r":
                                robotObj.wheelMove("stop")
                        elif x == "t":
                                robotObj.resetJointPos()
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
                                robotObj.getServo("pan").decreaseAngle()
                        elif x == "z":
                                robotObj.getServo("tilt").increaseAngle()
                        elif x == "x":
                                robotObj.getServo("tilt").moveToAngle(0)
                        elif x == "c":
                                robotObj.getServo("tilt").decreaseAngle()
                        elif x == "j":
                                robotObj.getServo("shoulder").decreaseAngle()
                        elif x == "k":
                                robotObj.getServo("shoulder").moveToAngle(0)
                        elif x == "l":
                                robotObj.getServo("shoulder").increaseAngle()
                        elif x == "u":
                                startCamera()
                        elif x == "i":
                                stopCamera()
                        else:
                                print(x)
                                print("press another key please")
                elif len(x) == 2:
                        #keyup?
                        x = x[0]
                        if x == "q":
                                None
                        elif x == "r":
                                None
                        elif x == "t":
                                None
                        elif x == "w":
                                robotObj.wheelMove("stop")
                        elif x == "a":
                                robotObj.wheelMove("stop")
                        elif x == "d":
                                robotObj.wheelMove("stop")
                        elif x == "s":
                                robotObj.wheelMove("stop")
                        elif x == "1" or x == "3":
                                robotObj.getServo("pan").stop()
                        elif x in ["j", "l"]:
                                robotObj.getServo("shoulder").stop()
                        elif x in ["z", "c"]:
                                robotObj.getServo("tilt").stop()
                elif len(x) == 11:
                        #camera command
                        if x == "startCamera":
                                startCamera()
                                self.request.sendall("Camera Started")
                        elif x == "stoppCamera":
                                stopCamera()
                                self.request.sendall("Camera Stopped")
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


