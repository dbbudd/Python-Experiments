#!/usr/bin/env python

import serial

class Ard():
    
    def __init__(self, path='/dev/tty.usbserial', baud=9600):
        self.arduino = serial.Serial(path, baud)
    
    def send(self, data):
        self.arduino.write(data)
        
        
    def read(self, bytes):
        while(1):
            if(self.arduino.inWaiting() > bytes-1):
                return self.arduino.read(bytes)
    
    def flush():
        self.arduino.flushInput()
    