#!/usr/bin/env python

import serial
import time

s = serial.Serial()                        # create a serial port object
s.baudrate = 57600                        # baud rate, in bits/second
s.port = "/dev/ttyAMA0"            # this is whatever port your are using
s.timeout = 3.0
s.open()



def jointMode(ID):
        s.write('W'+'j'+chr(ID))


def wheelMode(ID, addr=8, val=0):
        s.write('W'+'w'+chr(ID))
        
        s.write(chr(int(addr)%256))
        s.write(chr(int(addr)>>8))
        
        s.write(chr(int(val)%256))
        s.write(chr(int(val)>>8))


def moveJoint(ID, degPosition, pcSpeed):
        #WRITE ID
        s.write('W'+'p'+chr(ID))
        
        #WRITE POSITION
        #check constraints
        while degPosition > 180:
                degPosition = degPosition - 360
        while degPosition < -180:
                degPosition = degPosition + 360
        if (degPosition < -150):
                degPosition = -150
        if (degPosition > 150):
                degPosition = 150
                
        position = int(float(degPosition)*3.41+511.5)
        s.write(chr(int(position)%256))
        s.write(chr(int(int(float(degPosition)*3.41+511.5))>>8))
        
        #WRITE SPEED
        velocity = int(float(pcSpeed)*10.23)
        s.write(chr(int(velocity)%256))
        s.write(chr(int(velocity)>>8))

def moveWheel(ID, pcSpeed):
        
        s.write('W'+'w'+chr(ID))
        
        #WRITE ADDRESS
        addr = 32
        s.write(chr(int(addr)%256))
        s.write(chr(int(addr)>>8))
        
        #WRITE SPEED        
        if pcSpeed >= 0:
                #Wrapper for forward speed
                speed = int(float(pcSpeed)*10.23)
        else:
                #Wrapper for backward speed
                speed = int(1024+int(float(-pcSpeed)*10.23))
                
        s.write(chr(int(speed)%256))
        s.write(chr(int(speed)>>8))        





jointMode(5) #Joints are 5,6,7
wheelMode(1) #Wheels are 1,2,3,4

moveJoint(5, 0, 10)
time.sleep(2)
moveJoint(5, 45, 10)
time.sleep(2)
moveJoint(5, 0, 10)
time.sleep(2)
moveWheel(1, 30)
time.sleep(2)
moveWheel(1, 0)
