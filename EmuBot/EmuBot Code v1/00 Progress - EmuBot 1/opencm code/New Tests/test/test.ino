/* Minimum_Source*/


#define DXL_BUS_SERIAL1 1  //Dynamixel on Serial1(USART1)  <-OpenCM9.04
Dynamixel Dxl(DXL_BUS_SERIAL1);


void setup() {
  // put your setup code here, to run once:
  // Dynamixel 2.0 Baudrate -> 0: 9600, 1: 57600, 2: 115200, 3: 1Mbps 
  Dxl.begin(3);
  //Serial2.begin(1);
  Serial1.begin(9600);
  Dxl.writeWord(1, 8, 0); 
}

byte initialise(byte ID, boolean mode){
  
  //Wheel Mode - Rotates 360 degrees like a regular motor
  //Moves at a set angle with normal servo motors
  
  if (mode){
    Dxl.wheelMode(ID);
    //Dxl.goalSpeed(ID_NUM, 400) forward
    //Dxl.goalSpeed(ID_NUM, 400 | 0x400) reverse
  }
  else{
    Dxl.jointMode(ID);
    //Dxl.goalPosition(ID_NUM, 1) //forward
    //Dxl.goalPosition(ID_NUM, 1023) //reverse
  }
  return 1;
}

boolean dxRead(byte ID, byte inst){
  //Check if servo is moving (46 is moving control address)
  int status;
  status = Dxl.readWord(ID, inst);
  return status;
}

byte dxWrite(byte ID, byte inst, word speed){
  //32 = Moving Speed
  int status;
  status = Dxl.writeWord(ID, inst, speed);
  return status;
}






void loop() {
  int status;
  word speed = 400;
  // put your main code here, to run repeatedly: 
  status = initialise(1, 1);
  status = dxWrite(1, 32, speed);
  delay(3000);
  
  
  if (Serial.available()){
    word x = Serial.read();
    if (x == 43){
      speed = speed + 10;
    }
    else if (x == 45){
      speed = speed - 10;
    }
    Serial.println(x);
  }
  
  
}

