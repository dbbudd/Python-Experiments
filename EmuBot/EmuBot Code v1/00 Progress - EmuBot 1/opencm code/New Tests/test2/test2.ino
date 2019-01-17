
#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04
Dynamixel Dxl(DXL_BUS_SERIAL1);

void setup() {
  // put your setup code here, to run once:
  // Dynamixel 2.0 Baudrate -> 0: 9600, 1: 57600, 2: 115200, 3: 1Mbps 
  Dxl.begin(3);
  Dxl.wheelMode(1); //wheelMode() is to use wheel mode
  
  //configure the Dynamixels
  Dxl.writeWord(1, 8, 0);
  
  //Serial2.begin(1);
  //Serial1.begin(9600);
}

byte blockingRead(){
  while (!SerialUSB.available()){
    delay(3);
  }
  
  return SerialUSB.read();
}

//setup an array to store values
byte cmd[8];

void loop(){
  while (SerialUSB.available()){
    //example write input is 'w132+999'
    //example read input is 'r146+040'
    cmd[0] = blockingRead(); //command
    
    //5 is the char '5' and the equiv numeric value is 53 and a 'O' is 48
    //ASCII codes for the digits 0 through 9 is 48 through 57. When the character '0'
    cmd[1] = int(blockingRead() - '0'); //ID
    cmd[2] = int(blockingRead() - '0'); //CMD1
    cmd[3] = int(blockingRead() - '0'); //CMD2
    cmd[4] = blockingRead(); // plus or minus
    cmd[5] = int(blockingRead() - '0'); //Val1
    cmd[6] = int(blockingRead() - '0'); //Val1
    cmd[7] = int(blockingRead() - '0'); //Val1
    
    
    int ID, CMD, VAL;
    ID = cmd[1];
    
    //first number times 10 + second number
    CMD = int((cmd[2] * 10) + cmd[3]);
    VAL = int((cmd[5] * 100) + (cmd[6] * 10) + cmd[7]);
      
    if (cmd[0] == 'w'){
      if (cmd[4] == '-'){
        Dxl.writeWord(ID, CMD, VAL | 0x400); //reverse
        //Dxl.goalSpeed(ID, VAL | 0x400);
      }
      else{
        Dxl.writeWord(ID, CMD, VAL);
        //Dxl.goalSpeed(ID, VAL);
      }
      
      SerialUSB.print("ID:");
      SerialUSB.print(ID);
      SerialUSB.print("\n");
      
      SerialUSB.print("CMD:");
      SerialUSB.print(CMD);
      SerialUSB.print("\n");
      
      SerialUSB.print("VAL:");
      SerialUSB.print(VAL);
      SerialUSB.print("\n");
      
    }
    else if (cmd[0] == 'r') {
      word status = Dxl.readWord(ID, CMD);
      SerialUSB.write(status);
      //SerialUSB.println(Dxl.readWord(ID, 36));
    }
  }
}
