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

/*output values:
000 - forward
001 - left
002 - right
003 - back 
004 - stay still
005 - down
006 - go up
007 - forward left
008 - forward right
*/

int securityDistance = 70;
int loopDelay = 50;

long maximumRange = 300; // Maximum range needed
long minimumRange = 5; // Minimum range needed
/*
QueueArray <double> downMAArray;     QueueArray <double> upMAArray; 
QueueArray <double> frontMAArray;    QueueArray <double> frontLeftMAArray;   QueueArray <double> frontRightMAArray;
QueueArray <double> leftMAArray;     QueueArray <double> rightMAArray;
*/
double downDistance, upDistance, frontDistance, frontLeftDistance, frontRightDistance, leftDistance, rightDistance;
double multiplier; // used for counting moving average

int iteration =0;
void goForward()
{Serial1.print("000");
 Serial.print("000");}

void goLeft()
{Serial1.print("001");
 Serial.print("001");}

void goRight()
{Serial1.print("002");
 Serial.print("002");}

void goBack()
{Serial1.print("003");
 Serial.print("003");}

void stayStill()
{Serial1.print("004");
 Serial.print("004");}

void goDown()
{Serial1.print("005");
 Serial.print("005");}

void goUp()
{Serial1.print("006");
 Serial.print("006");}

void goForwardLeft()
{Serial1.print("007");
 Serial.print("007");}

void goForwardRight()
{Serial1.print("008");
 Serial.print("008");}


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
   //HC-SR04
   digitalWrite(trig, LOW); 
   delayMicroseconds(2); 
   digitalWrite(trig, HIGH);
   delayMicroseconds(10); 
   digitalWrite(trig, LOW);
   long distance = pulseIn(echo, HIGH, 10000)/58.2;
   if (distance >= maximumRange || distance ==0)
   {
     return maximumRange;
   }
   else if (distance < minimumRange)
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



void loop() {
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
 
   if (upDistance< securityDistance && downDistance > securityDistance)
   {  goDown();}
   else if (downDistance < securityDistance && upDistance > securityDistance)
   {  goUp();}
   else if (frontDistance== maximumRange)
   {
     if (leftDistance>rightDistance+ securityDistance)
      {  goLeft();}
     else if (rightDistance> leftDistance+ securityDistance)
      {  goRight();}
     else
      { goForward();} 
   }
   else if (frontDistance< maximumRange)
   {
      if (frontDistance < securityDistance)
      {  goBack();}
      else
      {
        if (frontLeftDistance > frontRightDistance && leftDistance> securityDistance)
        {  goForwardLeft();}
        else if (frontRightDistance > frontLeftDistance && rightDistance> securityDistance)
        {  goForwardRight();}
        else
        {  stayStill();}   
      }
   }

   delay(loopDelay);

}
