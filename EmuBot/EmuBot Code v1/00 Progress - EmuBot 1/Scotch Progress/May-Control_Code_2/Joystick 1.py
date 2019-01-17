"""
Constructed using the pygame.joystick library: https://www.pygame.org/docs/ref/joystick.html
'map' function from: https://mail.python.org/pipermail/tutor/2013-August/097291.html

Game Controller Button Map
0 - Square
1 - Cross/X
2 - Circle/O
3 - Triangle
4 - L1
5 - R1
6 - L2
7 - R2
8 - SELECT
9 - START
10 - L Joystick Press
11 - R Joystick Press
12 - Home/PS
"""

import pygame
import socket
from time import sleep
import ServoInterface as bot

def stop():
    pygame.quit()
    exit()
    
buttonNames = {0 : "Square",
             1 : "Cross/X",
             2 : "Circle/O",
             3 : "Triangle",
             4 : "L1",
             5 : "R1",
             6 : "L2",
             7 : "R2",
             8 : "Select",
             9 : "Start",
             10 : "R Joystick",
             11 : "L Joystick",
             12 : "Home/PS"
             }

#Map functions to the corresponding indices here
buttonMap = ["", #Square
             "", #Cross/X
             "", #Circle/O
             "", #Triangle
             "", #L1
             "", #R1
             "", #L2
             "", #R2
             "", #Select
             "", #Start
             "", #Right Joystick
             "", #Left Joystick
             stop  #Home/PS
             ]

servoPos = {"Wheel 1" : 0, "Wheel 2" : 0, "Wheel 3" : 0, "Wheel 4" : 0, "Shoulder" : 0, "Tilt" : 0, "Pan" : 0}
pygame.init()
pygame.joystick.init()
joystick = pygame.joystick.Joystick(0)

joystick.init() #Initialize joystick for use

#Map inputs in order to gain a better comparison and control scheme
def map(x, in_min, in_max, out_min, out_max):
    return (x - in_min) * (out_max - out_min) // (in_max - in_min) + out_min

def checkButtons():
    for button in range(joystick.get_numbuttons()):
        buttonState = joystick.get_button(button)
        if buttonState == 1 :
            print str(buttonNames[button]) + " has been pressed"
            try:
                buttonMap[button]() #Call any functions listed with the button in buttonMap
            except:
                pass #Button is not assigned
    
while True:
    for event in pygame.event.get(): #Update controller positions
        if event.type == pygame.JOYBUTTONDOWN:
            #print "Button Press detected"
            checkButtons()
        
    #Movement Controls
    Bot_LR = map(joystick.get_axis(2), -1, 1, -100, 100)
    Bot_FB = map(joystick.get_axis(3), -1, 1, -100, 100)

    #print "Bot_LR: " + str(Bot_LR)
    #print "Bot_FB: " + str(Bot_FB)

    if abs(Bot_LR) > abs(Bot_FB):
        if Bot_LR < 0:
            print "Turning Left at " + str(abs(Bot_LR)) + "%"
            speed = bot.throttleSteeringToLeftRight(Bot_FB, Bot_LR)
            bot.spinAtPcSpeed(1, speed[0])
            bot.spinAtPcSpeed(2, -speed[1])
            bot.spinAtPcSpeed(3, -speed[1])
            bot.spinAtPcSpeed(4, speed[0])
            
        else:
            print "Turning Right at " + str(abs(Bot_LR)) + "%"
            speed = bot.throttleSteeringToLeftRight(Bot_FB, -Bot_LR)
            bot.spinAtPcSpeed(1, speed[0])
            bot.spinAtPcSpeed(2, -speed[1])
            bot.spinAtPcSpeed(3, -speed[1])
            bot.spinAtPcSpeed(4, speed[0])
            
    elif abs(Bot_LR) < abs(Bot_FB):
        if Bot_FB < 0:
            print "Rolling Forwards at " + str(abs(Bot_FB)) + "%"
            bot.spinAtPcSpeed(1, bot_FB)
            bot.spinAtPcSpeed(2, -bot_FB)
            bot.spinAtPcSpeed(3, -bot_FB)
            bot.spinAtPcSpeed(4, bot_FB)
            
        else:
            print "Rolling Backwards at " + str(abs(Bot_FB)) + "%"
            bot.spinAtPcSpeed(1, -bot_FB)
            bot.spinAtPcSpeed(2, bot_FB)
            bot.spinAtPcSpeed(3, bot_FB)
            bot.spinAtPcSpeed(4, -bot_FB)


    #Camera Controls
    Cam_LR = map(joystick.get_axis(0), -1, 1, -100, 100) #Horiz. axis of R Joystick
    Cam_DU = map(joystick.get_axis(1), -1, 1, -100, 100) #Vertical axis of R Joystick
    Cam_H = map(joystick.get_hat(0)[1], -1, 1, -100, 100) #Vertical axis of 4-way pointer
    
    #print "Cam_LR: " + str(Cam_LR)
    #print "Cam_DU: " + str(Cam_DU)
    #print "Cam_H: " + str(Cam_H)
    
    if abs(Cam_LR) > abs(Cam_DU):
        if Cam_LR < 0:
            print "Camera yawing left at " + str(abs(Cam_LR)) + "%"
            bot.moveToDegAngle(7, servoPos["Pan"] - 1, 100)
            
        else:
            print "Camera yawing right at " + str(abs(Cam_LR)) + "%"
            bot.moveToDegAngle(7, servoPos["Pan"] + 1, 100)
            
    elif abs(Cam_LR) < abs(Cam_DU):
        if Cam_DU < 0:
            print "Camera pitching forwards at " + str(abs(Cam_DU)) + "%"
            bot.moveToDegAngle(6, servoPos["Tilt"] + 1, 100)
            
        else:
            print "Camera pitching backwards at " + str(abs(Cam_DU)) + "%"
            bot.moveToDegAngle(6, servoPos["Tilt"] - 1, 100)

    if Cam_H < 0:
        print "Camera traveling down"
        
    elif Cam_H > 0:
        print "Camera traveling up"

    
    sleep(0.1) #Debounce controls
