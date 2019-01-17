#!/usr/bin/env python

import serial
import time

DXL_REG_CCW_Angle_Limit = 8
DXL_REG_Moving_Speed = 32

s = serial.Serial()                        # create a serial port object
s.baudrate = 57600                        # baud rate, in bits/second
s.port = "/dev/ttyAMA0"            # this is whatever port your are using
s.timeout = 3.0
s.open()

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





writeWord(1, DXL_REG_CCW_Angle_Limit, 0)
jointMode(5)

moveToDegAngle(5, 0, 10)
time.sleep(2)
moveToDegAngle(5, 45, 10)
time.sleep(2)
moveToDegAngle(5, 0, 10)
time.sleep(2)
spinAtPcSpeed(1, 30)
time.sleep(2)
spinAtPcSpeed(1, 0)
