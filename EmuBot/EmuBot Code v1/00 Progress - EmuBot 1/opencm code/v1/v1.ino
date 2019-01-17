/*
 
A thin shim translating Dynamixel commands from Serial 2 to Dynamixel. 
Very much a work-in-progress. For example, we can't read from the servos yet. 
 
Note that all values in <> are ASCII decimal integers. 
<pos> is a value from 0 to 1023. 
<vel> is a velocity, 0 to 1023 is forward, 1024-2047 is negative. 
 
Possible commands: 
 
"Wj<ID>" to make motor <ID> enter joint mode. 
"Wp<ID>,<pos>,<vel>" to make motor <ID> move to position <pos> with velocity <vel>. 
"Ww<ID>,<add>,<val>" to write <val> to register <add> of motor <ID>. 
 
*/
 
Dynamixel Dxl(1); 
 
void setup() 
{
  Serial2.begin(57600); 
  Dxl.begin(3); 
}
 
byte blockingRead()
{
  while (!Serial2.available()) delay(10); 
  return Serial2.read(); 
}
 
void processWrite(byte cmd, byte id)
{
          switch (cmd)
        {
          case 'j':
          {
            Dxl.jointMode(id); 
            break;
          } 
          case 'p':
          {
            int pos, vel; 
            if (!(readInt(&pos) && readInt(&vel))) break; 
            Dxl.setPosition(id, pos, vel); 
            break;
          }
          case 'w':
          {
            int add, val; 
            if (!(readInt(&add) && readInt(&val))) break; 
            Dxl.writeWord(id, add, val); 
            break; 
          }
        }
}

void processCommand(byte cmd, byte id)
{
  /* Gets sent some 'complex' command in the cmd byte and then executes */
  switch (cmd)
  {
    case 's':
    {
      /* attempts to stop servo in its current postion */
      int currPos = Dxl.readWord(id, 36);
      Dxl.setPosition(id, currPos, 0); //Tries to move to currPos as fast a possible
      break;
    }
  }
}
 
void loop() 
{
  while (Serial2.available())
  {
    // Wait for a start byte, "W" for write or "R" for read. 
    byte inByte = blockingRead();
    switch (inByte) 
    {
      case 'W':
      {
        byte cmd = blockingRead();
        byte id = blockingRead();
        //processWrite(cmd, id); 
        break;
      }
      /*case 'R':
      {
        byte cmd = blockingRead();
        byte id = blockingRead();
        processRead(cmd, id);
        break;
      }*/
      case 'C':
      {
        byte cmd = blockingRead();
        byte id = blockingRead();
        processCommand(cmd, id);
        break;
      }
    }    
  }
}
 
boolean readInt(int * outVal)
{
  byte inBuffer[sizeof(short)]; 
  int i; 
  for (i = 0; i < sizeof(short); i ++)
  {
    inBuffer[i] = blockingRead();
  }
  *outVal = *((short*)inBuffer); 
  return true; 
}
