#import pygame
from time import sleep
import ServoInterface as bot

import socket

robot_port = 3000  # Change to applicable

# Create a socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# "Bind" it to all ip-addresses on the local host, and a specific port
s.bind(("", robot_port))

# Tell the socket to listen for connections
s.listen(5)

while True:
    # Wait for a new connection
    print "Waiting for connection..."
    (c, c_addr) = s.accept()

    print "New connection from: ", c_addr

    while True:
        try:
            command = c.recv(1)
        except socket.error, e:
            print "Error: %r" % e
            break;

        if command == 'F':
            # Move Forwards for the 'F' command
            print "Rolling Forwards"
            bot.spinAtPcSpeed(1, speed[1])
            bot.spinAtPcSpeed(2, -speed[1])
            bot.spinAtPcSpeed(3, -speed[1])
            bot.spinAtPcSpeed(4, speed[1])
            print "Received command 'F'"
        elif command == 'B':
            print "Rolling Backwards"
            bot.spinAtPcSpeed(1, -speed[1])
            bot.spinAtPcSpeed(2, speed[1])
            bot.spinAtPcSpeed(3, speed[1])
            bot.spinAtPcSpeed(4, -speed[1])
        elif command == 'L';
            print "Turning Left"
            speed = bot.throttleSteeringToLeftRight(Bot_FB, Bot_LR)
            bot.spinAtPcSpeed(1, speed[0])
            bot.spinAtPcSpeed(2, -speed[1])
            bot.spinAtPcSpeed(3, -speed[1])
            bot.spinAtPcSpeed(4, speed[0])
        elif command == 'R';
            print "Turning Right"
            speed = bot.throttleSteeringToLeftRight(Bot_FB, -Bot_LR)
            bot.spinAtPcSpeed(1, speed[0])
            bot.spinAtPcSpeed(2, -speed[1])
            bot.spinAtPcSpeed(3, -speed[1])
            bot.spinAtPcSpeed(4, speed[0])
        else:
            print "Unknown command, closing connection"
            break

    c.close()