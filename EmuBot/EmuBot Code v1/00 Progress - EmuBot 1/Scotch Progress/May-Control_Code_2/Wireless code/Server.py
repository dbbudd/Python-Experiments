import pygame
import socket
from time import sleep
import ServoInterface as bot

# Each address on the Internet is identified by an ip-address
# and a port number.
robot_ip_address = raw_input('Robot IP address')  # Change to applicable
robot_port       = 3000            # Change to applicable

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to somewhere...
s.connect((robot_ip_address, robot_port))

# Send one character to the socket
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
            print "Turning Left"
            s.send('L')
            
        else:
            print "Turning Right"
            s.send('R')
            
    elif abs(Bot_LR) < abs(Bot_FB):
        if Bot_FB < 0:
            print "Rolling Forwards"
            s.send('F')
            
        else:
            print "Rolling Backwards"
            s.send('B')
    
    sleep(0.1) #Debounce controls

# Close the socket after use
s.close()

