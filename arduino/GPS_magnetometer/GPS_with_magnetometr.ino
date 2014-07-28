#include <Wire.h>
#include <Adafruit_Sensor.h>
#include <Adafruit_HMC5883_U.h>

Adafruit_HMC5883_Unified mag = Adafruit_HMC5883_Unified(12345);

int rxPin = 0; // RX pin
int txPin = 1; // TX pin
int byteGPS=-1;


void setup() {
  pinMode(rxPin, INPUT);
  pinMode(txPin, OUTPUT);
  Serial.begin(9600);
  if(!mag.begin())
  {
    /* There was a problem detecting the HMC5883 ... check your connections */
    Serial.println("Ooops, no HMC5883 detected ... Check your wiring!");
    while(1);
  }
}

char RMC_Sequence[7] = {'$', 'G', 'P', 'R', 'M', 'C', ','};
int RMC_Sequence_Counter;

int Time_Byte_Counter = 0;

int Print_Time()                          // format hhmmss.sss or hhmmss.ss
{
  
  if(Time_Byte_Counter == 0 && (char)byteGPS != ',')
    Serial.print("UTC time: ");
  
  else if(Time_Byte_Counter == 2)
     Serial.print("h ");
     
  else if(Time_Byte_Counter == 4)
    Serial.print("min ");

  else if(Time_Byte_Counter > 5 && (char)byteGPS == ','){
    Serial.print("s");
    Time_Byte_Counter = 0;
    return 1;}
    
  if((char)byteGPS == ','){
    Time_Byte_Counter = 0;
    return 1;}
  
  ++Time_Byte_Counter;
  Serial.print((char)byteGPS);
  
  return 0;
}

int Date_Byte_Counter = 0;

int Print_Date()
{
  
  if(Date_Byte_Counter == 0 && (char)byteGPS != ',')
    Serial.print("UTC date: ");
  
  else if(Date_Byte_Counter == 2)
     Serial.print("d ");
     
  else if(Date_Byte_Counter == 4)
    Serial.print("m ");

  else if(Date_Byte_Counter > 4 && (char)byteGPS == ','){
    Serial.print("y");
    Date_Byte_Counter = 0;
    return 1;}
    
  if((char)byteGPS == ','){
    Date_Byte_Counter == 0;
    return 1;}
  
  ++Date_Byte_Counter;
  Serial.print((char)byteGPS);
  
  return 0;
}


int Lat_Byte_Counter = 0;
long latitude = 2000000000;
long newlatitude;

void Save_Latitude()
{
  long c = byteGPS - 48;  //char to int
  for(int i = 0; i < 8 - Lat_Byte_Counter;++i)
    c=c*10;
  if(Lat_Byte_Counter>1)
    c=c*1.666666667;    //minutes to fraction of a degree
  newlatitude += c;
  
    if(Lat_Byte_Counter == 8)
    {
      if(latitude == 2000000000)           //check if this is first change to latitude
        latitude = newlatitude;
      else{
      latitude = latitude *0.25000;
      newlatitude = newlatitude *0.75000;
      latitude = latitude +newlatitude;}
      newlatitude = 0;
    }
    
    
    ++Lat_Byte_Counter;
    //Serial.print((char)byteGPS);
}


int Long_Byte_Counter = 0;
long longitude = 2000000000;
long newlongitude;

void Save_Longitude()
{
  long c = byteGPS - 48;  //char to int
  for(int i = 0; i < 9 - Long_Byte_Counter;++i)
    c=c*10;
  if(Long_Byte_Counter>2)
    c=c*1.666666667;    //minutes to fraction of a degree
  newlongitude += c;
    
    if(Long_Byte_Counter == 9)
    {
      if(longitude == 2000000000)          //check if this is first change to longitude
        longitude = newlongitude;
      else{
      longitude = longitude *0.25000;
      newlongitude = newlongitude *0.75000;
      longitude = longitude +newlongitude;}
      newlongitude = 0;
    }
    
    ++Long_Byte_Counter;
}


float headingDegrees;
float heading;

void Mag_Angle_Scan()
{
  sensors_event_t event; 
  mag.getEvent(&event);
  float headingnew = atan2(event.magnetic.y, event.magnetic.x);
  headingnew -= 0.30;
  
  if(headingnew < 0)
    headingnew += 2*PI;
  if(headingnew > 2*PI)
    headingnew -= 2*PI;
    
  if(heading - headingnew > PI) headingnew += 2*PI;
  else if(heading - headingnew < -PI) headingnew -= 2*PI;
    headingnew = headingnew*0.25000;
    heading = heading*0.75000;
    heading += headingnew;
    
  if(headingnew < 0)
    heading += 2*PI;
  if(heading > 2*PI)
    heading -= 2*PI;
    
  headingDegrees = heading * 180/M_PI;
}


long cm_latitude;               //convert data to cm
long cm_longitude;
long cm_oldlatitude;
long cm_oldlongitude;
long last_calc_velocity_time = millis();

void Calc_Velocity()
{
  cm_oldlatitude = cm_latitude;
  cm_oldlongitude = cm_longitude;
  cm_latitude = latitude *0.00001 *111132.9444444444; //111133m per 1 lat degree
  cm_longitude = longitude *0.00001*cos(latitude*0.0000001*0.0174532925)*111319.491666667; // 111319m per 1 long degree on equator
  
  float kierunek=0;
  float velocity_x= cm_longitude*0.01 -cm_oldlongitude*0.01;
  float velocity_y= cm_latitude*0.01 -cm_oldlatitude*0.01;
  Serial.print("vel: ");
  double vel = sqrt((velocity_y*velocity_y)+(velocity_x*velocity_x));
  vel = vel*0.001*(millis() -last_calc_velocity_time);
  last_calc_velocity_time = millis();
  Serial.print(vel, 5);
  Serial.print("m/s  dir: ");
  
  if(vel>0)
    if(velocity_y == 0 && velocity_x > 0) kierunek = 90;
    else if(velocity_y==0 && velocity_x<0) kierunek = 270;
    else if(velocity_y>0 && velocity_x == 0) kierunek = 0;
    else if(velocity_y<0 && velocity_x == 0) kierunek = 180;
    else
    {
      kierunek = atan(velocity_x/velocity_y);
      kierunek = kierunek*180/3.1415926535;
      if(velocity_y < 0)
        kierunek +=180;
      if(kierunek < 0)kierunek +=360;
    }
    Serial.print(kierunek);
}


void Calc_Coords_xCm_In_Front()
{
  long distance = 10000;
  long distance_x=distance; long distance_y=0;
  
 if(headingDegrees !=270 && headingDegrees !=90)
 {
  float ratiodist = tan(heading);
  if(ratiodist>=0){
    distance_y = distance*1/(ratiodist + 1);
    distance_x = distance*ratiodist/(ratiodist + 1);
  }
  else {
    distance_y = distance*1/(ratiodist - 1);
    distance_x = distance*ratiodist/(ratiodist - 1);
  }
 }
  long newpos_y;
  long newpos_x;
  if(headingDegrees>180){
    newpos_y = -distance_y*0.89982273492 + latitude; //convert into latitude and add into latitude
    newpos_x = -distance_x/cos(newpos_y*0.0000001*0.0174532925)*0.8983152770714713 +longitude; //convert into latitude and add into longitude
  }
  else{
    newpos_y = distance_y*0.89982273492 + latitude;  //convert into latitude and add into latitude
    newpos_x = distance_x/cos(newpos_y*0.0000001*0.0174532925)*0.8983152770714713 +longitude; //convert into latitude and add into longitude
  }
    
 
 Serial.print("  "); Serial.print(newpos_y);Serial.print("y "); Serial.print(newpos_x); Serial.print("x ");
}



int Curr_Decode = 0;
int Curr_RMC_Decode = -1;



void loop() {
  byteGPS=Serial.read();         // Read a byte of the serial port
  if (byteGPS == -1) {     // See if the port is empty yet
    delay(100);
    Mag_Angle_Scan();
  }
    else {
      
      if(Curr_Decode == 0)            // 0 is for $GPRMC
      {
        if(Curr_RMC_Decode == 0)       // 0 is for time
        {
          if(Print_Time()){
            ++ Curr_RMC_Decode;
            Serial.print("  |  ");
          }
        }
        
        else if(Curr_RMC_Decode == 1)  // 1 tell if latitude and longitude is valid
        {
          if((char)byteGPS == ',') ++ Curr_RMC_Decode;
          else if((char)byteGPS == 'V') Serial.print("data not valid  |  ");
        }
        
        else if(Curr_RMC_Decode == 2)  // 2 is for latitude
        {
          if((char)byteGPS != ','){
            if((char)byteGPS != '.') Save_Latitude();}
          else ++Curr_RMC_Decode;
        }
        
        else if(Curr_RMC_Decode == 3)  // 3 is for lat N or S
        {
          if((char)byteGPS != ','){
            if((char)byteGPS == 'S')latitude = -latitude;
              if(Lat_Byte_Counter>0){
                Serial.print("latitude: ");
                Lat_Byte_Counter=0;
                Serial.print(latitude);
                Serial.print((char)byteGPS);
                Serial.print("  |  ");
              }
          }
          else ++Curr_RMC_Decode;
        }
        
        else if(Curr_RMC_Decode == 4)  // 4 is for longitude
        {
          if((char)byteGPS != ','){
            if((char)byteGPS != '.') Save_Longitude();}
          else ++Curr_RMC_Decode;
        }
        
        else if(Curr_RMC_Decode == 5)  // 5 is for long E or W
        {
          if((char)byteGPS != ','){
            if((char)byteGPS =='W')longitude = -longitude;
              if(Long_Byte_Counter>0){
                Serial.print("longitude: ");
              Long_Byte_Counter=0;
              Serial.print(longitude*0.0000001, 8);
              Serial.print((char)byteGPS);
              Serial.print("  |  ");
              }
          }
          else{
            ++Curr_RMC_Decode;
             
            Mag_Angle_Scan();
            Serial.print("Heading: "); Serial.print(headingDegrees); Serial.print("  |  ");
            Calc_Velocity();
            Serial.print("  |  ");
            Calc_Coords_xCm_In_Front();
            Serial.print("  |  ");
          }
        }
        
        else if(Curr_RMC_Decode == 6) // 6 is for velocity in knots
        {
          if((char)byteGPS == ',')
            ++Curr_RMC_Decode;
        }
        
        else if(Curr_RMC_Decode == 7) // 7 is for course in degrees
        {
           if((char)byteGPS == ',')
             ++Curr_RMC_Decode;
        }
        
        else if(Curr_RMC_Decode == 8) // 8 is for date
        {
          if(Print_Date())
          {
            ++Curr_RMC_Decode;
          }
        }
        else
        {
          Curr_RMC_Decode = 0;
          Curr_Decode = -1;
          Serial.println("");
        }
      }
      else
      {
        if(RMC_Sequence[RMC_Sequence_Counter] == (char)byteGPS)
        {
          //Serial.print("rmccheck");
          if(RMC_Sequence_Counter == 6){
            Curr_Decode = 0;
            RMC_Sequence_Counter = 0;
          }
          else ++RMC_Sequence_Counter;
        }
      }
      
    }
}

















































