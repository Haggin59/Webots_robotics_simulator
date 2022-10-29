# Webots_robotics_simulator
Robotics simulations using Webots

This repo consist of robotics simulations created in the opensource simulator Webots.
I'm currently on a learning path, I'll update the repo with the new projects as I progress

# 1 Differential drive robot:
  It is the simulation of a custom made differential drive robot
  The current controller code makes the robot to follow the path of a polygon with the user desired number of sides
  The code is written in Python
  The robot is in an open loop control, therby it is susceptible to errors in motion.
   ![diff_drive](https://user-images.githubusercontent.com/72227384/198847227-b301a42a-f52a-48d6-a2f8-697166bba661.png)

# 2 Odometry and pose estimation
  In this project encoders are attached to the diff drive robot for measuring the wheel rotations
  The wheel rotations can be used to determine the distance covered by the robot
  calculations can be done to estimate the pose of the robot
  Pose: [x_coordinate, y_coordinate, theta_orientation] can be calculated  using kinematic equations  
  
# 3 Maze solver: Left wall following algorithm
  The best-known rule for traversing mazes is the wall follower, also known as either the 
  left-hand rule or the right-hand rule. If the maze is simply connected, that is, all its 
  walls are connected together or to the maze's outer boundary.
  Here the robot E-puck is made to follow the wall on its left until it reaches the end.![wall_follower1](https://user-images.githubusercontent.com/72227384/198847048-ec7a3473-3c95-4053-a53d-e7f57bf08d0b.png)
![wall_follower2 png](https://user-images.githubusercontent.com/72227384/198847057-84495127-ffa3-46ad-a16e-4f2bb4ce27a1.png)
