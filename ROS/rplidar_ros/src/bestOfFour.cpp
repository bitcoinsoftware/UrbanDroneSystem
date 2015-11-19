#include "turtle.h"
#include "turtle.cpp"
#define SAFE_MOVE 0.5F 

//maybe this include is incorrect

void moveTurtle(ros::Publisher *, float);
bool calculateDirection(const sensor_msgs::LaserScan::ConstPtr&, float&);


//scaning from rpLidar
void scanFromReader(const sensor_msgs::LaserScan::ConstPtr& scan, ros::Publisher& turtle_pub, Services& services) {

	float direction;
	
	//move turtle with certain frequency
	ros::Rate loop_rate(FREQ);
	services.teleport_turtle();
	services.clear_turtle();
	
	if(calculateDirection(scan, direction)) {
		services.teleport_turtle(direction);
		moveTurtle(&turtle_pub, direction);
	}
	loop_rate.sleep();
}

//TODO: Override it from the base class
bool calculateDirection(const sensor_msgs::LaserScan::ConstPtr& scan, float& finalDirection) {
	float nearestDistance = MAX_DIST;

	//zapamiętaj pozycję w tabeli, do której odnosi się najlepszy pomiar
	int nearestPosition;
	
	float direction;
	
	//liczba pomiarów
	int count = scan->scan_time / scan->time_increment;

	
	//calculate nearest direction
	for(int i = 0; i < count; i++) {
		float distance = scan->ranges[i];
		if ((distance < nearestDistance) && (distance > MIN_DIST)) {
			nearestDistance = distance;
			direction = scan->angle_min + scan->angle_increment * i;
			nearestPosition = i;
		}
	}
	
	int pi_8 = count / 8;  // 1/8 pełnego kąta - 45 stopni
	
	//calculating direction for avoiding an obstacle
	if (nearestDistance < MAX_DIST) {
		float distanceLeft;
		float distanceRight;
		
		//jeżeli żadna wartość nie przekroczy SAFE MOVE to wybierz best Position
		float bestDirection;
		
		// if any direction is better it will move in that direction
		float bestDistance = nearestDistance;
		
		//all directions except +/- 180 degrees 
		for (int i = 1; i < 4; i++) { 
			int positionLeft = nearestPosition - i * pi_8;
			if(positionLeft < 0) 
				positionLeft = nearestPosition + (8-i)*pi_8;
			
			distanceLeft = scan->ranges[positionLeft];
			
			int positionRight = nearestPosition + i * pi_8;
			if(positionRight >= count)
				positionRight = nearestPosition - (8-i)*pi_8;
				
			distanceRight = scan->ranges[positionRight];
			
			//this is the best choice and return from loop
			// if distance in this direction is greater than safe move
			if (distanceLeft >= nearestDistance + SAFE_MOVE || distanceRight >= nearestDistance + SAFE_MOVE) {
				if (distanceLeft > distanceRight) {
					finalDirection = scan->angle_min + scan->angle_increment * positionLeft;
				}
				else {
					finalDirection = scan->angle_min + scan->angle_increment * positionRight;
				}
				ROS_INFO("move in direction %f, nearest point %f", RAD2DEG(finalDirection), nearestDistance);
				return true;
			}
			else {
				if (distanceLeft > bestDistance) {
					bestDistance = distanceLeft;
					bestDirection =  scan->angle_min + scan->angle_increment * positionLeft;
				}
				if (distanceRight > bestDistance) {
					bestDistance = distanceRight;
					bestDirection = scan->angle_min + scan->angle_increment * positionRight;
				}
			} 
		}
		
		float distance;
		float position;
		position = nearestPosition - 4 * pi_8;
		if(position < 0)
			position = nearestPosition + 4 * pi_8;
			
		distance = scan->ranges[position];
		if (distance > bestDistance) {
			bestDistance = distance;
			bestDirection = scan->angle_min + scan->angle_increment * position;
		}
		
		finalDirection = bestDirection;
		
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
