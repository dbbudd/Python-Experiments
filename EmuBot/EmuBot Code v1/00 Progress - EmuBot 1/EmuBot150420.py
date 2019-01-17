import serial
import sys
import Tkinter as tk
import picamera
import math

import os


import time

MOVE_SPEED = 20

#math.degrees()

class joint(object):        
        def __init__(self, servoID, minLimit, maxLimit, moveSpeed = 20):
                self.servoID = servoID
                self.minLimit = minLimit
                self.maxLimit = maxLimit
                self.currAngle = 0
                self.moveSpeed = moveSpeed
                #getting servo object
                self.moveToAngle(0)

        def moveToAngle(self, angle):
                if angle <= self.maxLimit and angle >= self.minLimit:
                        moveToDegAngle(self.servoID, angle, self.moveSpeed)
                        self.currAngle = angle
                        time.sleep(0.05)

        def increaseAngle(self, dist = 1):
                self.moveToAngle(self.currAngle+dist)
                self.currAngle += dist
        
                

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

s = serial.Serial()			   # create a serial port object
s.baudrate = 57600			  # baud rate, in bits/second
s.port = "/dev/ttyAMA0"		   # this is whatever port your are using
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


shoulderObj = joint(5, -90, 150)
panObj = joint(7, -90, 90, moveSpeed = 50)

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

def wheels(front_left, front_right, back_right, back_left):

        spinAtPcSpeed(1, front_left) #Front Left (100 fwd)
        spinAtPcSpeed(2, front_right) #Front Right (-100 fwd)
        
        spinAtPcSpeed(3, back_right) #Back Right (-100 fwd)
        spinAtPcSpeed(4, back_left) #Back Left (100 fwd)
        
        time.sleep(0.05)
        
def tilt(tiltPos, tiltSpeed):
        #Pan limited to 90 and -90 degrees 
        moveToDegAngle(6, tiltPos, tiltSpeed)
        time.sleep(0.05)

def shoulder(tiltPos, tiltSpeed):
        # Shoulder is limited to -90 and 150. Note that this will hit the ground (which could be desired).
        moveToDegAngle(5, tiltPos, tiltSpeed)
        time.sleep(0.05)

def pan(panPos, panSpeed):
        #Pan limited to 90 and -90 degrees 
        moveToDegAngle(7, panPos, panSpeed)
        time.sleep(0.05)
        
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

def keypress(event):
        x = event.char
        if x == "q":
                wheels(0,0,0,0)
                resetCamPos()
                camera.close()
                window.destroy()
                #window.quit()
        elif x == "w":
                print ("forward")
                wheels(100,-100,-100,100)
        elif x == "a":
                print("left")
                wheels(100, 100, 100, 100)
        elif x == "d":
                print("right")
                wheels (-100, -100, -100, -100)
        elif x == "s":
                print("back")
                wheels(-100,100,100,-100)
        elif x == "1":
                #pan will go to 90 and -90
                panObj.increaseAngle()
        elif x == "2":
                panObj.moveToAngle(0)
        elif x == "3":
                pan(45, 50)
        elif x == "z":
                tilt(-90,MOVE_SPEED)
        elif x == "x":
                tilt(0,MOVE_SPEED)
        elif x == "c":
                tilt(90,MOVE_SPEED)
        elif x == "i":
                shoulderObj.moveToAngle(0)
        elif x == "k":
                shoulderObj.moveToAngle(90)
        else:
                print(event.char)
                print("press another key please")
        
def keyunpress(event):
        x = event.char
        print(x)
        if x == "w":
                print ("forward")
                wheels(0,0,0,0)
        elif x == "a":
                print("left")
                wheels(0,0,0,0)
        elif x == "d":
                print("right")
                wheels(0,0,0,0)
        elif x == "s":
                print("back")
                wheels(0,0,0,0)
        else:
                print(event.char)
                print("Stop press another key please")

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

window.bind_all('<KeyPress>', keypress)
window.bind("<KeyRelease>", keyunpress)

#don't show the tk window
#root.withdraw()

window.mainloop()

#config to fix repeating press error
os.system("xset r off")
