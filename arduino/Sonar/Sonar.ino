  #include <QueueArray.h>

//////SONARY//////
#define trigPinUp A2 
#define echoPinUp A3 
#define trigPinFront 6
#define echoPinFront 7
#define trigPinFleft 4
#define echoPinFleft 5
#define trigPinFright 8
#define echoPinFright 9
#define trigPinLeft 10
#define echoPinLeft 11
#define trigPinRight 12
#define echoPinRight 13
#define mb1240PinDown A0
#define movingAveragePeriod 2

///////PPM SEND//////
#define chanel_number 8  
#define default_servo_value 1500 
#define PPM_FrLen 22500  
#define PPM_PulseLen 300  
#define onState 1 
#define sigPin A4

//////PPM READ//////
#define PPM_Pin 2  //this must be 2 or 3

///////CH PPM//////
#define THROTTLE 2
#define ROLL 0
#define PITCH 1
#define YAW 3
#define MODE 4
#define RC6 5
#define RC7 6
#define RC8 7

///////MODES//////
#define Stabilize 1100
#define AltHold 1400
#define Loiter 1700

//PPM
//0  CH1 - ROLL < 1500 >
//1  CH2 - PITCH /\ 1500- \/ 1500+
//2  CH3 - THROTTLE
//3  CH4 - YAW < 1500 >
//4  CH5 - MODE SET

//VALUE
//Command = "5555"
//Command[0] - Yaw (Left < 5 < Right)
//Command[1] - Pitch (Back < 5 < Forward)
//Command[2] - Roll (Left < 5 < Right)
//Command[3] - Throttle (Down < 5 < Up)

/////SONARY////
int securityDistance = 70;
int distanceMargin = 10;
int distanceMarginYaw = 100;
int loopDelay = 50;

long maximumRangeHCSR04 = 300; // Maximum range needed
long minimumRangeHCSR04 = 5; // Minimum range needed
long startDistance = 150;
double downDistance, upDistance, frontDistance, frontLeftDistance, frontRightDistance, leftDistance, rightDistance;
double multiplier = 0.7; // used for counting moving average

int iteration =0;

int MODE_AUTO;
int SerialCommand[5];

//////PPM/////
int PpmWrite[chanel_number];
int PpmRead[16];  //array for storing up to 16 servo signals
int SecurityPPM = 20;


//////SETUP//////
void setup() {
  Serial1.begin(9600);
  Serial.begin(9600);
  pinMode(trigPinUp, OUTPUT);       pinMode(echoPinUp, INPUT) ;
  pinMode(trigPinFront, OUTPUT);    pinMode(echoPinFront, INPUT);
  pinMode(trigPinFleft, OUTPUT);    pinMode(echoPinFleft, INPUT);
  pinMode(trigPinFright, OUTPUT);   pinMode(echoPinFright, INPUT);
  pinMode(trigPinLeft, OUTPUT);     pinMode(echoPinLeft, INPUT);
  pinMode(trigPinRight, OUTPUT);    pinMode(echoPinRight, INPUT);
  pinMode(mb1240PinDown, INPUT);
  
  for(int i=0; i<chanel_number; i++){
    PpmWrite[i]= default_servo_value;
  }
////////////PPM OUT///////////
  pinMode(sigPin, OUTPUT);
  digitalWrite(sigPin, !onState);  
  
  cli();
  TCCR3A = 0; 
  TCCR3B = 0;
  
  OCR3A = 100;  
  TCCR3B |= (1 << WGM32); 
  TCCR3B |= (1 << CS31); 
  TIMSK3 |= (1 << OCIE3A); 
  sei();
  
///////PPM IN/////////////
 
  pinMode(PPM_Pin, INPUT);
  attachInterrupt(PPM_Pin - 2, read_ppm, CHANGE);

  TCCR1A = 0;  //reset timer1
  TCCR1B = 0;
  TCCR1B |= (1 << CS11);  //set timer1 to increment every 0,5 us
  
}


//#######################LOOP###########################################################

void loop() 
{
  if(PpmRead[RC6] > 1500)
  {
  MODE_AUTO = 1; 
  }
  else
  {
  PpmWrite[THROTTLE]=PpmRead[THROTTLE];
  PpmWrite[ROLL]=PpmRead[ROLL];
  PpmWrite[PITCH]=PpmRead[PITCH];
  PpmWrite[YAW]=PpmRead[YAW];
  PpmWrite[MODE]=PpmRead[MODE];
  PpmWrite[RC6]=PpmRead[RC6];
  PpmWrite[RC7]=PpmRead[RC7];
  PpmWrite[RC8]=PpmRead[RC8];
  MODE_AUTO = 0; 
  
  } 
  
    int c=0;
    int SerialReadCommand[4];

    
    if (Serial.available() > 0) 
  {             
       while (Serial.available() > 0) {
         SerialReadCommand[c]=Serial.read(); //read data  
         c++;      
       }
       SerialCommand[0] = SerialReadCommand[0]-48;
       SerialCommand[1] = SerialReadCommand[1]-48;
       SerialCommand[2] = SerialReadCommand[2]-48;
       SerialCommand[3] = SerialReadCommand[3]-48;
       SerialCommand[4] = SerialReadCommand[4]-48;
      // Serial1.print(SerialCommand[0]);
      // Serial1.print(SerialCommand[1]);
      // Serial1.print(SerialCommand[2]);
      // Serial1.print(SerialCommand[3]);
      // Serial1.println(SerialCommand[4]);
       
  }
  else
  {
       SerialCommand[0] = 5;
       SerialCommand[1] = 5;
       SerialCommand[2] = 5;
       SerialCommand[3] = 5;
       SerialCommand[4] = 5;
  }
  
  if (MODE_AUTO == 1)
  {
  if (iteration<movingAveragePeriod) 
  {
     downDistance = getMB1240Distance(mb1240PinDown);
     upDistance =getHCSRdistance(trigPinUp, echoPinUp, startDistance);
     frontDistance = getHCSRdistance(trigPinFront, echoPinFront, startDistance);
     frontLeftDistance = getHCSRdistance(trigPinFleft, echoPinFleft, startDistance);
     frontRightDistance = getHCSRdistance(trigPinFright, echoPinFright, startDistance);
     leftDistance = getHCSRdistance(trigPinLeft, echoPinLeft, startDistance);
     rightDistance = getHCSRdistance(trigPinRight, echoPinRight, startDistance);
     iteration=iteration+1;
  }
  else
  {
     downDistance = downDistance*multiplier + getMB1240Distance(mb1240PinDown)*(1-multiplier);
     upDistance = upDistance*multiplier + getHCSRdistance(trigPinUp, echoPinUp, upDistance)*(1-multiplier);
     frontDistance = frontDistance*multiplier + getHCSRdistance(trigPinFront, echoPinFront, frontDistance)*(1-multiplier);
     frontLeftDistance = frontLeftDistance*multiplier + getHCSRdistance(trigPinFleft, echoPinFleft, frontLeftDistance)*(1-multiplier);
     frontRightDistance = frontRightDistance*multiplier + getHCSRdistance(trigPinFright, echoPinFright, frontRightDistance)*(1-multiplier);
     leftDistance = leftDistance*multiplier + getHCSRdistance(trigPinLeft, echoPinLeft, leftDistance)*(1-multiplier);
     rightDistance = rightDistance*multiplier + getHCSRdistance(trigPinRight, echoPinRight, rightDistance)*(1-multiplier);
     Serial1.println(multiplier);
  }

   printDistances( upDistance, frontDistance, frontLeftDistance, frontRightDistance, leftDistance, rightDistance, downDistance);
   makeMove(upDistance, frontDistance, frontLeftDistance, frontRightDistance, leftDistance, rightDistance, downDistance);
   
   
 
  }
   
   
      int count;
  //Serial1.print("\n");
  while(PpmRead[count] != 0){  //print out the servo values
    //Serial1.print(PpmRead[count]);
    //Serial1.print("  ");
    count++;
  }
  //Serial1.print("\n");
  delay(loopDelay);
}




/////SONAR MB1240/////
double getMB1240Distance( int analogPin)
{
    double sum =0; 
   
   int probesNumber = 10;
   for(int i=0; i<probesNumber;i++)
   {
     sum = sum + analogRead(analogPin)/2;
     delay(10);
   }
   return sum/probesNumber*2.54; 
}

/////SONARY HCS////////
double getHCSRdistance(int trig, int echo, int prevResult)
{
   digitalWrite(trig, LOW); 
   delayMicroseconds(2); 
   digitalWrite(trig, HIGH);
   delayMicroseconds(10); 
   digitalWrite(trig, LOW);
   long distance = pulseIn(echo, HIGH, 10000)/58.2;
   if (distance >= maximumRangeHCSR04)
   {
     return maximumRangeHCSR04;
   }
   else if (distance < minimumRangeHCSR04 )
   {
    return prevResult; 
   }
   return distance; 
}

/////PRINT DISTANCE/////
void printDistances(int upDistance, int frontDistance, int frontLeftDistance, int frontRightDistance, int leftDistance, int rightDistance, int downDistance)
{
   Serial1.print("DOWN ");Serial1.print(downDistance); Serial1.print(" UP ");Serial1.print(upDistance); Serial1.print(" FRONT ");Serial1.print(frontDistance);
   Serial1.print(" FR LEFT ");Serial1.print(frontLeftDistance); Serial1.print(" FR RIGHT ");Serial1.print(frontRightDistance); Serial1.print(" LEFT ");Serial1.print(leftDistance);
   Serial1.print(" RIGHT "); Serial1.println(rightDistance);
}

//#######################MOVE###########################################################

void makeMove(int upDistance, int frontDistance, int frontLeftDistance, int frontRightDistance, int leftDistance, int rightDistance, int downDistance)
{
  char result[] ="5555";
  
  // <-- ROTATION LEFT / ROTATION RIGHT -->
  if (frontLeftDistance> frontRightDistance + distanceMarginYaw)      {result[0]='4';} // rotate left
  else if (frontRightDistance > frontLeftDistance + distanceMarginYaw){result[0]='6';} //rotate right

  // <-- FRONT / BACK -->
  if (frontDistance< securityDistance)     {result[1]='6';}  //than go back
  
  // <-- LEFT / RIGHT MOVE -->
  if(leftDistance<securityDistance && rightDistance> securityDistance)  // if it's to low
  { result[2]='6'; }//than go up
  else if (leftDistance<securityDistance && rightDistance<=securityDistance) // if it's to low and to close to the ceiling
  {
     if (leftDistance > rightDistance + distanceMargin) {result[2]='4';}   //if there is more place down  -> go down
     else if (leftDistance+ distanceMargin <rightDistance) {result[2]='6';} // if there is more place up -> go up
     else {result[2]='5';}  // else stay still
  }
  else if(rightDistance < securityDistance) // if it is high and there is small distance to the ceiling
      {result[2]='4';}  //than go up
  
  // <-- UP / DOWN MOVE -->
  if(downDistance<securityDistance && upDistance> securityDistance)  // if it's to low
  {  result[3]='6'; }//than go up
  else if (downDistance<securityDistance && upDistance<=securityDistance) // if it's to low and to close to the ceiling
  {
     if (downDistance > upDistance + distanceMargin) {result[3]='4';}   //if there is more place down  -> go down
     else if (downDistance+ distanceMargin <upDistance) {result[3]='6';} // if there is more place up -> go up
     else {result[3]='5';}  // else stay still
  }
  else if (upDistance < securityDistance) // if it is high and there is small distance to the ceiling
  {result[3]='4';}  //than go up
  //Serial1.print(result); 
  //Serial1.print("\n");  
 
 
  
    int Command[4];
  int i=0; 
  //PpmWrite[MODE] = AltHold;
  PpmWrite[MODE]=PpmRead[MODE];
  PpmWrite[RC6]=PpmRead[RC6];
  PpmWrite[RC7]=PpmRead[RC7];
  PpmWrite[RC8]=PpmRead[RC8];
  
//MOVES
  Command[0] = result[0]-48;
  Command[1] = result[1]-48;
  Command[2] = result[2]-48;
  Command[3] = result[3]-48;
  
  //YAW//
  if(Command[0]==5)
  {
    Yaw(SerialCommand[0]);
  }
  else
  {
  Yaw(Command[0]);
  }
  
  //PITCH//
   if(Command[1]==5)
  {
    Pitch(SerialCommand[1]);
  }
  else
  {
    Pitch(Command[1]);
  }
  
 //ROLL//
   if(Command[2]==5)
  {
    Roll(SerialCommand[2]);
  }
  else
  {
    Roll(Command[2]);
  }
  
 //THROTTLE//
   if(Command[3]==5)
  {
    Throttle(SerialCommand[3]);
  }
  else
  {
    Throttle(Command[3]);
  }  
  
}






//////MOVES//////
void Yaw(int signal)
  {
  int value;
  value=signal*100;
  value=value+1000;
  if(PpmRead[YAW] > 1500+SecurityPPM | PpmRead[YAW] < 1500-SecurityPPM)
  {
    PpmWrite[YAW]=PpmRead[YAW];
  }
  else
{  
  PpmWrite[YAW] = value;
}
  //Serial1.print("Yaw: ");
 // Serial1.println(value);
  }
  
void Pitch(int signal)
  {
  int value;
  value=signal*100;
  value=value+1000;
  if(PpmRead[PITCH] > 1500+SecurityPPM | PpmRead[PITCH] < 1500-SecurityPPM)
  {
    PpmWrite[PITCH]=PpmRead[PITCH];
  }
  else
{   
  PpmWrite[PITCH] = value;
}
  //Serial1.print("Pitch: ");
  //Serial1.println(value);
  }
  
void Roll(int signal)
  {
  int value;
  value=signal*100;
  value=value+1000;
if(PpmRead[ROLL] > 1500+SecurityPPM | PpmRead[ROLL] < 1500-SecurityPPM)
  {
    PpmWrite[ROLL]=PpmRead[ROLL];
  }
  else
{     
  PpmWrite[ROLL] = value;
}
  //Serial1.print("Roll: ");
  //Serial1.println(value);
  }
  
void Throttle(int signal)
  {
  int value;
  value=signal*100;
  value=value+1000;
if(PpmRead[THROTTLE] > 1500+SecurityPPM | PpmRead[THROTTLE] < 1500-SecurityPPM)
  {
    PpmWrite[THROTTLE]=PpmRead[THROTTLE];
  }
  else
{  
  PpmWrite[THROTTLE] = value;
}
  //Serial1.print("Throttle: ");
  //Serial1.println(value);
  }
  
void read_ppm(){  //leave this alone
  static unsigned int pulse;
  static unsigned long counter;
  static byte channel;

  counter = TCNT1;
  TCNT1 = 0;

  if(counter < 1020){  //must be a pulse if less than 510us
    pulse = counter;
  }
  else if(counter > 3820){  //sync pulses over 1910us
    channel = 0;
  }
  else{  //servo values between 510us and 2420us will end up here
    PpmRead[channel] = (counter + pulse)/2;
    channel++;
  }
}


ISR(TIMER3_COMPA_vect){  //leave this alone
  static boolean state = true;
  
  TCNT3 = 0;
  
  if(state) {  //start pulse
    digitalWrite(sigPin, onState);
    OCR3A = PPM_PulseLen * 2;
    state = false;
  }
  else{  //end pulse and calculate when to start the next pulse
    static byte cur_chan_numb;
    static unsigned int calc_rest;
  
    digitalWrite(sigPin, !onState);
    state = true;

    if(cur_chan_numb >= chanel_number){
      cur_chan_numb = 0;
      calc_rest = calc_rest + PPM_PulseLen;// 
      OCR3A = (PPM_FrLen - calc_rest) * 2;
      calc_rest = 0;
    }
    else{
      OCR3A = (PpmWrite[cur_chan_numb] - PPM_PulseLen) * 2;
      calc_rest = calc_rest + PpmWrite[cur_chan_numb];
      cur_chan_numb++;
    }     
  }
}
