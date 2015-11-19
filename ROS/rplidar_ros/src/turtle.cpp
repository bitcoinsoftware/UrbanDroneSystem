#include "turtle.h"

/*
 * Base class for connecting rplidar with turtle
 */
 
class RplidarTurtleConnector {


};






/*
 *	Class for calling services
 */
class Services {
	private:
 	ros::NodeHandle* nh;
	ros::ServiceClient teleport;
	ros::ServiceClient clear;
	turtlesim::TeleportAbsolute start_pos;
	std_srvs::Empty empty;	
	 
 	public:
 	// Node handle is required to create instance of this class
 	Services(ros::NodeHandle* nh){
 		this->nh = nh;
 		init_values();
 		init_services();
 	}
 	
 	// Teleport turtle to the start position
 	bool teleport_turtle() {
		if(teleport.call(start_pos))
			return true;
		else
			return false;
 	}
 	
 	// Teleport turtle in the given direction
 	bool teleport_turtle(float turn) {
 		turtlesim::TeleportAbsolute pos;
 		pos.request.x = 5.5;
 		pos.request.y = 5.5;
 		pos.request.theta = turn;
 		if (teleport.call(pos))
 			return true;
 		else
 			return false;
 	}
 	
 	// Clear path made by turtle
 	bool clear_turtle() {
 		if(clear.call(empty))
 			return true;
		else
			return false;
 	}
 	
 	private:
 	void init_services(){
		this->teleport = nh->serviceClient<turtlesim::TeleportAbsolute>("/turtle1/teleport_absolute");
		this->clear = nh->serviceClient<std_srvs::Empty>("/clear");
 	}
 	
 	void init_values() {
 		start_pos.request.x = 5.5;
 		start_pos.request.y = 5.5;
 		start_pos.request.theta = 1.57;  // M_PI/2
	}
};

