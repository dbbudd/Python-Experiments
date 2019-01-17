#!/usr/bin/env python

import serial

#setup the serial connection speed
ser = serial.Serial('/dev/ttyAMA0', 9600)

#main loop
while 1:
    c = raw_input("Enter a char: ")
    if len(c) == 1:
        #end data to Arduino
        ser.write(c.encode())
        
        #receive data from Arduino
        response = ser.readline()
        
        print(response.decode().strip())