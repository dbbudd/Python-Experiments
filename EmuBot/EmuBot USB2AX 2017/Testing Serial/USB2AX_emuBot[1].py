from pyax12.connection import Connection
sc = Connection(port=”/dev/ttyACM0″, baudrate=1000000)


def jointMode(ID):
        sc.set_ccw_angle_limit(id,0,True)
        sc.set_cw_angle_limit(id,0,True)

def wheelMode(ID):
        sc.set_ccw_angle_limit(id,0,False)
        sc.set_cw_angle_limit(id,0,False)

def readDxl(id):
        sc.pretty_print_control_table(id)

def moveJoint(ID, position, speed):
        sc.goto(id, position, speed, True)
        
def moveWheel(ID, speed):
        sc.goto(id, 0, speed=512, degrees=False)
