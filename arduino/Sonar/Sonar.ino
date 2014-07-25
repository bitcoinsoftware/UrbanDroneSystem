#include <QueueArray.h>

#define trigPinUp 2 
#define echoPinUp 3 
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
#define movingAveragePeriod 8

int securityDistance = 70;
int distanceMargin =10;
int loopDelay = 50;

long maximumRangeHCSR04 = 300; // Maximum range needed
long minimumRangeHCSR04 = 5; // Minimum range needed

double downDistance, upDistance, frontDistance, frontLeftDistance, frontRightDistance, leftDistance, rightDistance;
double multiplier; // used for counting moving average

int iteration =0;

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

double getHCSRdistance(int trig, int echo)
{
   digitalWrite(trig, LOW); 
   delayMicroseconds(2); 
   digitalWrite(trig, HIGH);
   delayMicroseconds(10); 
   digitalWrite(trig, LOW);
   long distance = pulseIn(echo, HIGH, 10000)/58.2;
   if (distance >= maximumRangeHCSR04 || distance ==0)
   {
     return maximumRangeHCSR04;
   }
   else if (distance < minimumRangeHCSR04)
   {
     return 0;
   } 
   return distance; 
}
void printDistances(int upDistance, int frontDistance, int frontLeftDistance, int frontRightDistance, int leftDistance, int rightDistance, int downDistance)
{
   Serial.print("DOWN ");Serial.print(downDistance); Serial.print(" UP ");Serial.print(upDistance); Serial.print(" FRONT ");Serial.print(frontDistance);
   Serial.print(" FR LEFT ");Serial.print(frontLeftDistance); Serial.print(" FR RIGHT ");Serial.print(frontRightDistance); Serial.print(" LEFT ");Serial.print(leftDistance);
   Serial.print(" RIGHT "); Serial.println(rightDistance);
}

void makeMove(int upDistance, int frontDistance, int frontLeftDistance, int frontRightDistance, int leftDistance, int rightDistance, int downDistance)
{
  char result[] ="5555";
  
  // <-- ROTATION LEFT / ROTATION RIGHT -->
  if (frontLeftDistance> frontRightDistance + distanceMargin)      {result[0]='4';} // rotate left
  else if (frontRightDistance > frontLeftDistance + distanceMargin){result[0]='6';} //rotate right

  // <-- FRONT / BACK -->
  if (frontDistance< securityDistance)     {result[1]='4';}  //than go back
  
  // <-- LEFT / RIGHT MOVE -->
  if(leftDistance<securityDistance && rightDistance> securityDistance)  // if it's to low
  { result[2]='6'; }//than go up
  if else (leftDistance<securityDistance && rightDistance<=securityDistance) // if it's to low and to close to the ceiling
  {
     if (leftDistance > rightDistance + distanceMargin) {result[2]='4';}   //if there is more place down  -> go down
     else if (leftDistance+ distanceMargin <rightDistance) {result[2]='6';} // if there is more place up -> go up
     else {result[2]='5';}  // else stay still
  }
  if else(rightDistance < securityDistance) // if it is high and there is small distance to the ceiling
      {result[2]='4';}  //than go up
  
  // <-- UP / DOWN MOVE -->
  if(downDistance<securityDistance && upDistance> securityDistance)  // if it's to low
  {  result[3]='6'; }//than go up
  if else (downDistance<securityDistance && upDistance<=securityDistance) // if it's to low and to close to the ceiling
  {
     if (downDistance > upDistance + distanceMargin) {result[3]='4';}   //if there is more place down  -> go down
     else if (downDistance+ distanceMargin <upDistance) {result[3]='6';} // if there is more place up -> go up
     else {result[3]='5';}  // else stay still
  }
  if else(upDistance < securityDistance) // if it is high and there is small distance to the ceiling
  {result[3]='4';}  //than go up
  
  Serial1.print(result);
  Serial.print(result);  
}

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
  multiplier = (movingAveragePeriod-1)/movingAveragePeriod;
}

void loop() 
{
  if (iteration<movingAveragePeriod) 
  {
     downDistance = getMB1240Distance(mb1240PinDown);
     upDistance =getHCSRdistance(trigPinUp, echoPinUp);
     frontDistance = getHCSRdistance(trigPinFront, echoPinFront);
     frontLeftDistance = getHCSRdistance(trigPinFleft, echoPinFleft);
     frontRightDistance = getHCSRdistance(trigPinFright, echoPinFright);
     leftDistance = getHCSRdistance(trigPinLeft, echoPinLeft);
     rightDistance = getHCSRdistance(trigPinRight, echoPinRight);
     iteration=iteration+1;
  }
  else
  {
     downDistance = downDistance*multiplier + getMB1240Distance(mb1240PinDown)*(1-multiplier);
     upDistance = upDistance*multiplier + getHCSRdistance(trigPinUp, echoPinUp)*(1-multiplier);
     frontDistance = frontDistance*multiplier + getHCSRdistance(trigPinFront, echoPinFront)*(1-multiplier);
     frontLeftDistance = frontLeftDistance*multiplier + getHCSRdistance(trigPinFleft, echoPinFleft)*(1-multiplier);
     frontRightDistance = frontRightDistance*multiplier + getHCSRdistance(trigPinFright, echoPinFright)*(1-multiplier);
     leftDistance = leftDistance*multiplier + getHCSRdistance(trigPinLeft, echoPinLeft)*(1-multiplier);
     rightDistance = rightDistance*multiplier + getHCSRdistance(trigPinRight, echoPinRight)*(1-multiplier);
  }

   printDistances( upDistance, frontDistance, frontLeftDistance, frontRightDistance, leftDistance, rightDistance, downDistance);
   makeMove(upDistance, frontDistance, frontLeftDistance, frontRightDistance, leftDistance, rightDistance, downDistance);
   delay(loopDelay);
}
