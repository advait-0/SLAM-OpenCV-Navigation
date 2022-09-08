# Table of contents
1. [What is SLAM](## Introduction to SLAM)
    1. [The Prerequisites](## The Prerequisites)
    2. [Process](#Process)
    3. 












# Introduction to SLAM
Acronym for Simultaneous Localization and Mapping, SLAM is a more of a method than an algorithm used to build a map of the environment. The Extended Kalman Filter ([EKF](##EKF)) plays an important role in this implementation.

## The Prerequisites
They consist of the bot along with a measurement device, which can measure parameters including but not limited to odometry.
The odometry performance measures how well the robot can estimate its own position, just from the rotation of the wheels.
We shall use laser scanners for our data collection (a SICK scanner),
stereoscopic, triclops system and SONAR can also be taken into consideration.

# Process

![](https://i.imgur.com/TH3AzI0.png)

Neither sensors alone give us the optimal output, it is after combining the readings from the IMU, odometer and lidar do we get a close to real life location estimation
![](https://i.imgur.com/N0xjptP.png)

### Landmarks
Landmarks are points which can be easily distinguished and can be recognized again when seen from a different position and angle