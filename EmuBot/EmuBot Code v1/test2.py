import serial
import sys
import Tkinter as tk
import time

#setup the camera
import picamera
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



def wheels(front_left, front_right, back_right, back_left):

        spinAtPcSpeed(1, front_left) #Front Left (100 fwd)
        spinAtPcSpeed(2, front_right) #Front Right (-100 fwd)
        
        spinAtPcSpeed(3, back_right) #Back Right (-100 fwd)
        spinAtPcSpeed(4, back_left) #Back Left (100 fwd)
        
        time.sleep(0.05)
        
def arm(tiltSpeed, panSpeed, shoulderSpeed):

        
        shoulderPos = max(-90, min(150, shoulderSpeed))

        tiltcmd = tiltPos + shoulderPos
        pancmd = panPos

        #Tilt is limited to 90 degrees, pan to 150.
        tiltcmd = max(-90, min(90, tiltcmd))
        pancmd = max(-150, min(150, pancmd))

        moveToDegAngle(5, shoulderPos, shoulderSpeed)
        moveToDegAngle(6, tiltcmd, max(10, tiltSpeed))
        moveToDegAngle(7, pancmd, max(10, panSpeed))

        time.sleep(0.05)
        

def pan(panPos, panSpeed):
        #Pan limited to 150 degrees 
        moveToDegAngle(7, panPos, panSpeed)
        time.sleep(0.05)
        
def startCamera(cam):
        #camera = picamera.PiCamera()
        
        cam.start_preview()

        cam.sharpness = 10
        cam.contrast = 30
        cam.vflip = True
        cam.hflip = True
        cam.exposure_mode = "auto"
        cam.brightness = 60

        sleep(5)

def stopCamera(cam):
        cam.stop_preview()
        cam.close()

def keypress(event):
        x = event.char
        if x == "q":
                wheels(0,0,0,0)
                pan(0, 100)
                root.destroy()
                #root.quit()
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
                pan(-90, 50)
                print("Pan to -90 Degrees")
        elif x == "2":
                pan(-45, 50)
                print("Pan to -45 Degrees")
        elif x == "3":
                pan(0, 50)
                print("Pan to 0 Degrees")
        elif x == "4":
                pan(45, 50)
                print("Pan to 45 Degrees")
        elif x == "5":
                pan(90, 50)
                print("Pan to 90 Degrees")
        elif x == "c":
                startCamera(camera)
                print("camera activiated")
        elif x == "v":
                stopCamera(camera)
                print("camera activiated")
        else:
                print(event.char)
                print("press another key please")

root = tk.Tk()
print("Press the <q> key to exit:")
root.bind_all('<Key>', keypress)

#don't show the tk window
#root.withdraw()

root.mainloop()

