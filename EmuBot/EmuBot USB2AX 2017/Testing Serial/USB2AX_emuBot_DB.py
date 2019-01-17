"""
This code requires first installing the pyax12 Python package.
- http://pyax-12.readthedocs.io/en/latest/index.html

Pyax12 is a Python 3 package which can be installed on a Linux/OSX machine like so:

sudo pip3 install pyax12

Servos must already have an ID set before the below functions can be used.
You'll need to use something like Dynamixel Manager to set the ID on each
servo - https://github.com/Interbotix/dynaManager/releases

# OTHER METHODS TO PLAY WITH
#def read_data(self, dynamixel_id, address, length)
#def write_data(self, dynamixel_id, address, data)
#def ping(self, dynamixel_id)
# Sync_Write = 0x83

PACKET STRUCTURE
    +----+----+--+------+-----+----------+---+-----------+---------+
    |0XFF|0XFF|ID|LENGTH|ERROR|PARAMETER1|...|PARAMETER N|CHECK SUM|
    +----+----+--+------+-----+----------+---+-----------+---------+

"""

import time
from pyax12.connection import Connection
from pyax12.packet import *
#sc = Connection(port=”/dev/ttyACM0″, baudrate=1000000)
sc = Connection(port="/dev/tty.usbmodem1461", baudrate="1000000")



# Set up a dynamixel so that it behaves like joint
def jointMode(ID):
        sc.flush()
        sc.set_ccw_angle_limit(ID,0,True)
        sc.set_cw_angle_limit(ID,0,True)

# Set up a dynamixel so that it behaves like wheel
def wheelMode(ID):
        sc.set_ccw_angle_limit(ID,0,False)
        sc.set_cw_angle_limit(ID,0,False)

# Print useful information about an individual dynamixel servo
def readDxl(ID):
        sc.flush()
        sc.pretty_print_control_table(ID)

# Move a dynamixel that has been set up as a joint
def moveJoint(ID, position, speed):
        sc.flush()
        sc.goto(ID, position, speed, True)

# Move a dynamixel that has been set up as a joint       
def moveWheel(ID, speed):
        sc.flush()
        sc.goto(ID, 0, speed, degrees=False)

def checkAvailableDxl():
        sc.flush()
        lst = sc.scan()
        new_list = []
        for dxl in lst:
              new_list.append("ID " + str(dxl))

        return new_list

def reset(ID):
        AX_HEADER = 0xFF
        PK_LENGTH = 0x02
        AX_WRITE = 0x06
        AX_PARAM1 = 0x00
        AX_PARAM2 = 0x00
        CHECKSUM = compute_checksum(bytes((ID, PK_LENGTH, AX_WRITE))) 

        sc.flush()
        sc.send(bytes((AX_HEADER, AX_HEADER, ID, PK_LENGTH, AX_WRITE, CHECKSUM)))
        print("instruction packet sent... wait 5 seconds")
        time.sleep(5)
        print("Dynamixel has been reset and ID is set to '1'")
        
def reboot(ID):
        AX_HEADER = 0xFF
        #ID = 0xFD
        PK_LENGTH = 0x05
        ERROR = 0x01
        AX_WRITE = 0x03
        AX_PARAM1 = 0x00
        AX_PARAM2 = 0x08
        AX_PARAM3 = 0x2F
        CHECKSUM = compute_checksum(bytes((ID, PK_LENGTH, AX_WRITE, AX_PARAM1, AX_PARAM2, AX_PARAM3)))
        
        sc.flush()
        sc.send(bytes((AX_HEADER, AX_HEADER, ID, PK_LENGTH, AX_WRITE, AX_PARAM1, AX_PARAM2, AX_PARAM3, CHECKSUM)))
        print("instruction packet sent... wait 5 seconds")
        time.sleep(5)
        print("available Dxl are")
        print(checkAvailableDxl())


def setID(CURRENT_ID, NEW_ID):
    AX_HEADER = 0xFF
    ID = CURRENT_ID #254 will send to all dynamixels plugged in
    PK_LENGTH = 0x04
    AX_WRITE = 0x03
    AX_PARAM1 = 0x03
    AX_PARAM2 = NEW_ID 
    CHECKSUM = compute_checksum(bytes((ID, PK_LENGTH, AX_WRITE, AX_PARAM1, AX_PARAM2))) 
    
    sc.flush()
    sc.send(bytes((AX_HEADER, AX_HEADER, ID, PK_LENGTH, AX_WRITE, AX_PARAM1, AX_PARAM2, CHECKSUM)))
    print("instruction packet sent...")
    time.sleep(1)
    print("available Dxl are ...")
    print(checkAvailableDxl())


def sync_write(indexes, reg, values):
	'''
	Synchronized write for multiple servos
	STILL NEEDS WORK
	'''
	sc.flush()
	length = (len(values[0]) + 1) * len(indexes) + 4
	indexSum = sum(indexes)	
	valuesSum = 0
	for i in range(0, len(values)) :
		valuesSum += sum(values[i])		
		
	checksum = 255-((indexSum+length+AX_SYNC_WRITE+reg+valuesSum)%256)    # calculate checksum, same as ~(sum(data))  
	sc.send((chr(0xFF)+chr(0xFF)+chr(BROADCASTID)+chr(length)+chr(AX_REG_WRITE)+chr(reg) + chr(len(values[0]))))

	for i in range(0, len(indexes)):	
		sc.send(chr(indexes[i]))
		for val in values[i] :
			sc.send(chr(val))
			
	sc.send(chr(checksum))
	sc.flush()

    

try:       
        moveWheel(7, 200)
        time.sleep(3)
        moveWheel(7, 0)
        
except:
        print("fail")

