import pygame
import time
import serial

pygame.init()
gamepad=pygame.joystick.Joystick(0)

gamepad.init()
print(gamepad.get_id())
print(gamepad.get_init())
print(gamepad.get_numaxes())
print(gamepad.get_numbuttons())

ser = serial.Serial()
ser.setPort("/dev/ttyUSB0")
ser.baudrate = 9600
ser.open()
time.sleep(1)

while True:
    pygame.event.pump()
    if gamepad.get_button(8) !=0:
        break
    else:
        for i in range(8):
            if gamepad.get_button(i)!=0:
                print("button ", i + 1)
                ser.write(chr(i+1))
                print("sending ", i + 1)
                time.sleep(0.1)
gamepad.quit()
ser.close()