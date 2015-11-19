#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "geometry_msgs/Twist.h"
#include "limits"

#define RAD2DEG(x) ((x)*180./M_PI)

#define MAX_DIST 5.0F
#define MIN_DIST 0.5F
#define FREQ 0.5F

void moveTurtle(ros::Publisher* );
void calculateDirection(const sensor_msgs::LaserScan::ConstPtr &);

void scanTurtleReader(const sensor_msgs::LaserScan::ConstPtr & scan, ros::Publisher & turtle_pub) {
  
  calculateDirection(scan);

  ros::Rate loop_rate(FREQ);
  moveTurtle(&turtle_pub);
  loop_rate.sleep();
}

void calculateDirection(const sensor_msgs::LaserScan::ConstPtr & scan) {

  //  float nearest = std::numeric_limits<float>::infinity();
  float nearest = MAX_DIST;
  float direction;

  // nr of iterations
  int count = scan->scan_time / scan->time_increment;

  // search for best
  for(int i = 0; i < count; i++) {
    float distance = scan->ranges[i];
    if ((distance < nearest) && (distance > MIN_DIST)) {
      nearest = distance;
      direction  = RAD2DEG(scan->angle_min + scan->angle_increment * i);
    }
  }

  //  if (nearest != std::numeric_limits<float>::infinity()) {
  if (nearest < MAX_DIST) {
    float oppositeDirection = (direction < 0? direction + 180 : direction - 180);
    ROS_INFO("move in direction %f, nearest point %f", oppositeDirection, nearest);
  } 
  else {
    ROS_INFO("stable");
  }
}



void moveTurtle(ros::Publisher *pub) {
  //create twist variable
  geometry_msgs::Twist twist;

  twist.linear.x = 1.0;
  twist.linear.y = 0.0;
  twist.linear.z = 0.0;
  twist.angular.x = 0.0;
  twist.angular.y = 0.0;
  twist.angular.z = 0.8;
  //place for calculating turtle move???

  pub->publish(twist);
}



int main(int argc, char **argv) {
  ros::init(argc, argv, "turtle_reader");
  ros::NodeHandle nh;

  // make publisher to the turtle
  ros::Publisher turtle_pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1);

  ros::Subscriber sub = nh.subscribe<sensor_msgs::LaserScan>("/scan", 1, boost::bind(scanTurtleReader, _1, boost::ref(turtle_pub)));


  ros::spin();

  return 0;
}
