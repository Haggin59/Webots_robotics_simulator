"""diff_drv controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

# create the Robot instance.
robot = Robot()

# get the time step of the current world.
timestep = 64
max_speed = 6.28 #angular speed



#motor instances
lmotor = robot.getDevice('motor1')
rmotor = robot.getDevice('motor2')

lmotor.setPosition(float('inf'))
rmotor.setPosition(float('inf'))

lmotor.setVelocity(0.0)
rmotor.setVelocity(0.0)

num_sides = 4
length_side = 0.25

wheel_radius = 0.025
linear_velocity = wheel_radius * max_speed

duration_side = length_side/linear_velocity

start_time = robot.getTime()

angle_of_rotation = 6.28/num_sides
distance_bw_wheels = 0.090
rate_of_rotation = (2*linear_velocity)/distance_bw_wheels
duration_turn = angle_of_rotation/rate_of_rotation


# Main loop:
# - perform simulation steps until Webots is stopping the controller
while robot.step(timestep) != -1:
    
    current_time = robot.getTime()
    
    #if current time is within duration_side, the robot moves forward
    if current_time < start_time + duration_side:
    
        lspeed = max_speed
        rspeed = max_speed 
    
    #if current time exceeds the duration_side, the robot turns for duration_side
    elif current_time > start_time + duration_side and current_time < start_time + duration_side + duration_turn:
        lspeed =  -max_speed
        rspeed =   max_speed
        
    
    
    else:
        lspeed =  0
        rspeed =  0
        #at each turn the start time is updated
        start_time = robot.getTime()    
     
    #control speeds  are feed to the motors        
    lmotor.setVelocity(lspeed)
    rmotor.setVelocity(rspeed)

