# Webots_robotics_simulator
Robotics simulations using Webots

This repo consist of robotics simulations created in the opensource simulator Webots.
I'm currently on a learning path, I'll update the repo with the new projects as I progress

#1 Differential drive robot:
  It is the simulation of a custom made differential drive robot
  The current controller code makes the robot to follow the path of a polygon with the user desired number of sides
  The code is written in Python
  The robot is in an open loop control, therby it is susceptible to errors in motion.

#2 Odometry and pose estimation
  In this project encoders are attached to the diff drive robot for measuring the wheel rotations
  The wheel rotations can be used to determine the distance covered by the robot
  calculations can be done to estimate the pose of the robot
  Pose: [x_coordinate, y_coordinate, theta_orientation] can be calculated  using kinematic equations
