#include "ros/ros.h"
#include "sensor_msgs/LaserScan.h"
#include "geometry_msgs/Twist.h"
#include "limits"
#include "turtlesim/TeleportAbsolute.h"
#include "std_srvs/Empty.h"

#define RAD2DEG(x) ((x) * 180./M_PI)

#define MAX_DIST 3.0F
#define MIN_DIST 0.5F
#define FREQ 0.66F
