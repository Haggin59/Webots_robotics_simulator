#include <webots/Robot.hpp>
#include <webots/Motor.hpp>
#include <webots/DistanceSensor.hpp>
#include <webots/PositionSensor.hpp>

#define TIME_STEP 64

// All the webots classes are defined in the "webots" namespace
using namespace webots;

// create the Robot instance.
Robot *robot = new Robot();

// Function for time delay
void delay(float x);

int main(int argc, char **argv) {
  
  
  
  //Gripper motor instances
  Motor *finger1 = robot->getMotor("finger_1_joint_1");
  Motor *finger2 = robot->getMotor("finger_2_joint_1");
  Motor *finger3 = robot->getMotor("finger_middle_joint_1");
  
  //Arm motor instances
  Motor *Shoulder_lift = robot->getMotor("shoulder_lift_joint");
  Motor *elbow = robot->getMotor("elbow_joint");
  Motor *wrist1 = robot->getMotor("wrist_1_joint");
  Motor *wrist2 = robot->getMotor("wrist_2_joint");
  
  //setting initial position -> infinity
  finger1->setPosition(INFINITY);
  finger2->setPosition(INFINITY);
  finger3->setPosition(INFINITY);
  
  Shoulder_lift->setPosition(INFINITY);
  elbow->setPosition(INFINITY);
  wrist1->setPosition(INFINITY);
  wrist2->setPosition(INFINITY);
  
  //setting initial velocity -> 0.0
  finger1->setVelocity(0.0);
  finger2->setVelocity(0.0);
  finger3->setVelocity(0.0);
  
  Shoulder_lift->setVelocity(0.0);
  elbow->setVelocity(0.0);
  wrist1->setVelocity(0.0);
  wrist2->setVelocity(0.0);
  
  // get the time step of the current world.
  int timeStep = (int)robot->getBasicTimeStep();

  // Instance of distance sensor
  DistanceSensor *ds = robot->getDistanceSensor("distance sensor");
  ds->enable(TIME_STEP);
  
  // Variable used to indicate operational state of the robot
  int state = 0;
 
  // Main loop:
  // - perform simulation steps until Webots is stopping the controller
  while (robot->step(timeStep) != -1) {
    
    //Reading input from distancesensor 
    double val = ds->getValue();
    
    //std::cout<<"Distance: "<<val<<" Count: "<<count<<std::endl
   
    /*
      Operational stages of the robotic arm:
      
      0)Waiting until a can is within the proximity of the gripper, Home position
      1)Grasping the can using the gripper
      2)Rotating the arm to the desired goal location
      3)Releasing the can at the desired goal
      4)Rotating back to home position
       
    
    */
    
    // 0)Waiting
    if (state == 0) 
    {
      std::cout<<"Waiting"<<std::endl;   
      if(val<600)
      {
        std::cout<<"Can in range"<<std::endl;
        state = 1;  // Can in range ready for gripping
      }
    }
    
    // 1)Gripping
    if (state == 1) 
    {
        
        std::cout<<"Gripping"<<std::endl;
        
        finger1->setVelocity(3.14);
        finger1->setPosition(1);

        finger2->setVelocity(3.14);
        finger2->setPosition(1);
        
        finger3->setVelocity(3.14);
        finger3->setPosition(1); 
        
        delay(0.5);
        
        std::cout<<"Gripping done,Ready for rotation"<<std::endl;  
        state = 2; // can gripped, ready to rotate 
    }
    
    // 2)Rotating to goal
    if (state == 2)  
    {
        std::cout<<"Rotating"<<std::endl;
        
        Shoulder_lift->setVelocity(2);
        Shoulder_lift->setPosition(-1.88);
        
        elbow->setVelocity(2);
        elbow->setPosition(-2.14);
        
        wrist1->setVelocity(2);
        wrist1->setPosition(-2.38);
        
        wrist2->setVelocity(2);
        wrist2->setPosition(-1.51);
        
        delay(1);
        std::cout<<"Rotation done,Ready for release"<<std::endl;
        state  = 3; //Ready for release
           
    }
    
    //3)Releasing at goal
    if(state == 3)   
    {
        std::cout<<"Releasing"<<std::endl;
        
        finger1->setVelocity(3.14);
        finger1->setPosition(0.05);

        finger2->setVelocity(3.14);
        finger2->setPosition(0.05);
        
        finger3->setVelocity(3.14);
        finger3->setPosition(0.05);  
        
        delay(0.5);
        std::cout<<"Can Released,Return Home"<<std::endl;  
        state = 4; // can released, return home   
        
    }
    
    // 4)Returning back to Home
    if(state == 4) 
    {   
    
        std::cout<<"Returning Home"<<std::endl;
        
        Shoulder_lift->setVelocity(2);
        Shoulder_lift->setPosition(0);
        
        elbow->setVelocity(2);
        elbow->setPosition(0);
        
        wrist1->setVelocity(2);
        wrist1->setPosition(0);
        
        wrist2->setVelocity(2);
        wrist2->setPosition(0);
        
        delay(1);
        std::cout<<"At Home"<<std::endl;
        state = 0;
        
    }
    
    
    
  };

  // Enter here exit cleanup code.

  delete robot;
  return 0;
}

//user defined delay function
void delay(float x)
{
  float t1 = float(robot->getTime());
  float t2 = float(robot->getTime());
  
  do
  {
    t2 = float(robot->getTime());
    robot->step(1);
  }while(t2< (t1+x));
}

