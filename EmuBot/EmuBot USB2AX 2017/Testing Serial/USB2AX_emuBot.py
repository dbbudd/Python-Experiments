"""
This code requires first installing the pyax12 Python package.
- http://pyax-12.readthedocs.io/en/latest/index.html

Pyax12 is a Python 3 package which can be installed on a Linux/OSX machine like so:

sudo pip3 install pyax12

Servos must already have an ID set before the below functions can be used.
You'll need to use something like Dynamixel Manager to set the ID on each
servo - https://github.com/Interbotix/dynaManager/releases
"""


from pyax12.connection import Connection
sc = Connection(port=”/dev/ttyACM0″, baudrate=1000000)

# Set up a dynamixel so that it behaves like joint
def jointMode(ID):
        sc.set_ccw_angle_limit(id,0,True)
        sc.set_cw_angle_limit(id,0,True)

# Set up a dynamixel so that it behaves like wheel
def wheelMode(ID):
        sc.set_ccw_angle_limit(id,0,False)
        sc.set_cw_angle_limit(id,0,False)

# Print useful information about an individual dynamixel servo
def readDxl(id):
        sc.pretty_print_control_table(id)

# Move a dynamixel that has been set up as a joint
def moveJoint(ID, position, speed):
        sc.goto(id, position, speed, True)

# Move a dynamixel that has been set up as a joint       
def moveWheel(ID, speed):
        sc.goto(id, 0, speed=512, degrees=False)
