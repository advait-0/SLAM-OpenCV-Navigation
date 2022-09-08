## What is SLAM
<font size=4><p>SLAM is concerned with the problem of building a map of an unknown environment
by a mobile robot while at the same time navigating the environment using the map.</p></font>

---
## EKF (Extended Kalman Filter)
<font size=4><p>In estimation theory, the extended Kalman filter (EKF) is the nonlinear version of the Kalman filter</p></font>

<font size=4><p>What is a Kalman Filter?</p></font>
<font size=4><p>Algorithm that uses a series of measurements observed over time, including statistical noise and other inaccuracies, and produces estimates of unknown variables</p></font>

---
## Odometry performance
<font size=4><p>The odometry performance measures how well the robot can estimate its own
position, just from the rotation of the wheels.</p></font>

<font size=4><p>In simple terms, odometry is the use of motion sensors to determine the robot's change in position relative to some known position. For example, if a robot is traveling in a straight line and if it knows the diameter of its wheels, then by counting the number of wheel revolutions it can determine how far it has traveled.</p></font>

---
## Types of sensors
<font size=4><p>1. Laser</p></font>
<font size=3><p>Drawbacks: Give faulty readings when looked across glass and underwater.</p></font>
<font size=4><p>2. Sonar</p></font>
<font size=3><p>Drawbacks: Not as accurate as laser but, best choice underwater.</p></font>
<font size=4><p>3. Camers</p></font>
<font size=3><p>Drawbacks: Gives the best results since it is similar to way humans look at surroundings. Lot of information can be captured.</p></font>

---
## 
<font size=4><p>The odometry reults are often not very accurate.</p></font>
<font size=4><p>Hence, sensors are used to scan the environment and the bot's surroundings are updated accordingly.</p></font>

## How does the EKF help in updating the environments?
<font size=4><p>EKF takes into account the landmarks in the surroundings of the robot. </p></font>
<font size=4><p>As the bot moves, its wheels rotate. Hence, odometry shows a change in position of the bot.</p></font>

![](EKF_Algorithm.png)


<font size=4><p>Laser scan and landmark extraction:Then, using sensors (as odometry is not very accurate), landmarks from the surroundings are observed. </p></font>

<font size=4><p>Data association: The robot then compares the new landmarks to the previous ones which it has already seen (at previous locations).</p></font>

<!-- <font size=4><p></p></font> -->
<font size=4><p>Re-observed landmarks: The landmarks which were also observed at previous locations are already present in the EKF.</p></font>
<font size=4><p>Newly observed landmarks: The landmarks which have appeared for the first time at the current location are updated to the EKF as new observations.</p></font>
<font size=4><p>Odometry change: After taking into account all the sensor results, the odometry results (which were less accuarte) are then updated to make more correct.</p></font>

## Laser Outputs
<font size=4><p>The output from the laser scanner tells the ranges from right to left</p></font>
<font size=4><p></p></font>

## Odometry and Sensors parallel
<font size=4><p>The difficult part about the odometry data and the laser data is to get the timing
right.(ie. the odometry of bot and resluts given by sensors 'at the same istant' should be compared.</p></font>
<font size=4><p>To overcome this, the odometry results are extrapolated. (The sensor ones are not because it is difficult to predict their results by simple extrapolation)</p></font>
<font size=4><p></p></font>

## Landmarks
<font size=4><p>They are used by the robot to recognize its position in the surroundings.</p></font>
<font size=4><p>Landmarks should be:</p></font>
<font size=3><p>re-observable</p></font>
<font size=3><p>unique</p></font>
<font size=3><p>stationary</p></font>
