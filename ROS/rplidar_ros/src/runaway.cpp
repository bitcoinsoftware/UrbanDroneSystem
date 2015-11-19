#include "turtle.h"
#include "turtle.cpp"

//----------------------declarations---------------

void moveTurtle(ros::Publisher *, float);
bool calculateDirection(const sensor_msgs::LaserScan::ConstPtr&, float&);

//----------------------definitions----------------
//scaning from rpLidar
void scanFromReader(const sensor_msgs::LaserScan::ConstPtr& scan, ros::Publisher& turtle_pub, Services& services) {

	float direction;

	ros::Rate loop_rate(FREQ);
	services.teleport_turtle();
	services.clear_turtle();

	if (calculateDirection(scan, direction)) {
		services.teleport_turtle(direction);
		moveTurtle(&turtle_pub, 0.0);
	}
	loop_rate.sleep();
}

//TODO: Override it from the base class
bool calculateDirection(const sensor_msgs::LaserScan::ConstPtr& scan, float& finalDirection) {
	float nearestDistance = MAX_DIST;
	float direction;
	
	int count = scan->scan_time / scan->time_increment;
	
	for(int i = 0; i < count; i++) {
		float distance = scan->ranges[i];
		if ((distance < nearestDistance) && (distance > MIN_DIST)) {
			nearestDistance = distance;
			direction = scan->angle_min + scan->angle_increment * i;
		}
	}
	
	if (nearestDistance < MAX_DIST) {
		//swap direction
		finalDirection = (direction < 0? direction + M_PI: direction - M_PI);
		ROS_INFO("move in direction %f, nearest point %f", RAD2DEG(finalDirection), nearestDistance);
		return true;
	}
	else {
		ROS_INFO("stable");
		return false;
	}
}

//moving a turtle
//pass a direction to move
void moveTurtle(ros::Publisher * pub, float direction) {
	//twist var
	geometry_msgs::Twist twist;
	//velocity
	twist.linear.x = 1.0;
	twist.linear.y = 0.0;
	twist.linear.z = 0.0;
	//angular
	twist.angular.x = 0.0;
	twist.angular.y = 0.0;
	twist.angular.z = direction;
	
	//publish twist to the trutle
	pub->publish(twist);
	

}

int main(int argc, char** argv) {
	ros::init(argc, argv, "runaway");
	
	//handle to Node
	ros::NodeHandle nh;
	
	//publish to the turtle
	ros::Publisher turtle_pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1);
	
	Services services(&nh);	
	
	//subscribe from the rp lidar scan
	//as arguments pass -> method which should be invoked and reference to the publisher, it is the turtle
	ros::Subscriber sub = nh.subscribe<sensor_msgs::LaserScan>("/scan", 1, boost::bind(scanFromReader, _1, boost::ref(turtle_pub), boost::ref(services)));
	
	ros::spin();
	
	return 0;
}

//test only
int mmain(int argc, char** argv) {
	ros::init(argc, argv, "runaway");
	
	ros::NodeHandle nh;

	//publish to turtle	
	ros::Publisher turtle_pub = nh.advertise<geometry_msgs::Twist>("/turtle1/cmd_vel", 1);
	
	Services services(&nh);
	
	while(ros::ok()){
		
		//define loop rate
		ros::Rate loop_rate(FREQ);		
		//teleport turtle
		services.teleport_turtle();
		//clear his path
		services.clear_turtle();
		//move him
		moveTurtle(&turtle_pub, 2.0);	

		loop_rate.sleep();
	}
}
