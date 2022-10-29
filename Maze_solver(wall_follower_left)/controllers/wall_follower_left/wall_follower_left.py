"""wall_follower_left controller."""

# You may need to import some classes of the controller module. Ex:
#  from controller import Robot, Motor, DistanceSensor
from controller import Robot

   
def run_robot(robot):

    
    # get the time step of the current world.
    timestep = int(robot.getBasicTimeStep())
    max_speed = 6.28
    
    # You should insert a getDevice-like function in order to get the
    # instance of a device of the robot. Something like:
    #  motor = robot.getDevice('motorname')
    #  ds = robot.getDevice('dsname')
    #  ds.enable(timestep)
    #creating motor instances
    l_motor = robot.getDevice('left wheel motor')
    r_motor = robot.getDevice('right wheel motor')
    
    l_motor.setPosition(float('inf'))
    l_motor.setVelocity(0.0)
    
    
    r_motor.setPosition(float('inf'))
    r_motor.setVelocity(0.0)
    
    #position sensor(0-7) instances
    prox = []
    for i in range(8):
        name = "ps" + str(i)
        prox.append(robot.getDevice(name))
        prox[i].enable(timestep)
        
       
    # Main loop:
    # - perform simulation steps until Webots is stopping the controller
    while robot.step(timestep) != -1:
    
        for i in range(8):
            print("ps num: ",i,"value: ",prox[i].getValue())
            
        left = prox[5].getValue() > 77
        left_corner = prox[6].getValue() > 77
        front = prox[7].getValue() > 77
        
        if front:
            print("Turn right")
            l_motor.setVelocity(max_speed)
            r_motor.setVelocity(-max_speed)
            
        else:
        
            if left:
            
                print("Forward")
                l_motor.setVelocity(0.6*max_speed)
                r_motor.setVelocity(0.6*max_speed)

            else:
                print("Turn left")
                l_motor.setVelocity(0.1*max_speed)
                r_motor.setVelocity(max_speed)   
                                
            if left_corner:
                print("Too close")
                l_motor.setVelocity(max_speed)
                r_motor.setVelocity(0.1*max_speed)    

 
                     
                
            
           

if __name__ == "__main__":
    
    # create the Robot instance.
    robot = Robot()
    run_robot(robot) 




