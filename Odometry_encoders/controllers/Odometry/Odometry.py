"""Odometery """

from controller import Robot
import math

def drive_robot(robot):

    timestep = 64
    max_speed = 6.28
    wheel_radius = 0.025
    wheel_base = 0.09
    
    #instances of motors
    lmotor = robot.getDevice('motor1')
    rmotor = robot.getDevice('motor2')
    
    lmotor.setPosition(float('inf'))
    rmotor.setPosition(float('inf'))
    
    lmotor.setVelocity(0.0)
    rmotor.setVelocity(0.0)    

    #instances of encoders
    lpos = robot.getDevice('pos1')
    lpos.enable(timestep)
    
    rpos = robot.getDevice('pos2')   
    rpos.enable(timestep)
    
    pos_values = [0,0]
    dist_values = [0,0]
    
    #Encoder conversions
    wheel_circ = 2 * 3.14 * wheel_radius
    unit_rad = wheel_circ/6.28
    
    #pose [x,y,theta]
    robot_pose = [0,0,0]
    last_pos_values = [0,0]
    
       
    
    
    while robot.step(timestep) != -1:
        pos_values[0] = lpos.getValue()
        pos_values[1] = rpos.getValue()
        
        print("lpos: ",pos_values[0],"rpos: ",pos_values[1])
        
        for i in range(2):
            diff = pos_values[i] - last_pos_values[i]
            dist_values[i] = diff * unit_rad
            
        
        v = (dist_values[0] + dist_values[1])/2 #linear velocity
        w = (dist_values[1] - dist_values[0])/wheel_base  #angular velocity
        
        dt = 1
        robot_pose[2] += (w * dt) #Theta
        
        v_x = v * math.cos(robot_pose[2]) #linear velocity x component
        v_y = v * math.sin(robot_pose[2]) #linear velocity y component
        
        robot_pose[0] += (v_x * dt)
        robot_pose[1] += (v_y * dt)
        
        print("Robot Pose: ",robot_pose)
        
        
        lmotor.setVelocity(max_speed)
        rmotor.setVelocity(max_speed)  
        
        for i in range(2):
            last_pos_values[i] = pos_values[i]   

if __name__ == "__main__":

    robot = Robot()
    drive_robot(robot)
     