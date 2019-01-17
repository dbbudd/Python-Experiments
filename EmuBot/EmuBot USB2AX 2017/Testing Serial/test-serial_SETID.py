import serial
import time

ser = serial.Serial()
ser.port = "/dev/tty.usbmodem1461"
ser.baudrate = 10000

try:
    ser.open()
    print("serial open...")
except:
    print("serial connection failed")

def setID():
    AX_HEADER = 0xFF
    ID = 0xFE #ALL SERVOS
    PK_LENGTH = 0x04
    AX_WRITE = 0x03
    AX_PARAM1 = 0x03
    AX_PARAM2 = 0x01
    CHECKSUM = 255-((ID+PK_LENGTH+AX_WRITE)%256) #Calculate checksum, same as ~(sum(data)) 0xF6

    ser.flush()
    ser.write(bytes((AX_HEADER, AX_HEADER, ID, PK_LENGTH, AX_WRITE, AX_PARAM1, AX_PARAM2, CHECKSUM)))
    print("ID changed from " + str(current) + " to " + str(newID))
    print(CHECKSUM)
    print(str(CHECKSUM))
    print(str(bytes(CHECKSUM)))
    time.sleep(3)
            

def reset(ID=0xFE):
    ser.flush()

    #prepare packet
    PK_LENGTH = 0x02
    AX_RESET = 0x06
    AX_HEADER = 0xFF
    CHECKSUM = 255-((ID+PK_LENGTH+AX_RESET)%256)    # calculate checksum, same as ~(sum(data))  0xF7
    ser.write(bytes((AX_HEADER, AX_HEADER, ID, PK_LENGTH, AX_RESET, CHECKSUM)))
    
    time.sleep(3)
    print("ID " + str(ID) + " was reset")

def reboot():
    ser.flush()
    ser.write(bytes((0xFF, 0xFF, 0xFD, 0x00, 0x01, 0x03, 0x00, 0x08, 0x2F, 0x4E)))

    time.sleep(3)
    print(" Dxl was rebooted")

def write(ID):
    '''
    AX_ACTION = 0x03 #3
    length = 2			# configure length
    checksum = 255-((index+length+AX_ACTION)%256)    # calculate checksum, same as ~(sum(data))  
    port.write(chr(0xFF)+chr(0xFF)+chr(index)+chr(length)+chr(AX_ACTION))	# Write the first part of the protocol	
    port.write(chr(checksum))	# write the checksum
    '''
    time.sleep(3)
    print("write")


setID()

ser.close()
print("serial closed...")
