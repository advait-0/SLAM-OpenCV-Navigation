## Occupational Grid Maps
<font size=4><p>These maps basically tell you which part of the map is occupied and which is not. </p></font>
<!-- <font size=4><p></p></font> -->
<font size=4><p>For eg., the floorplan of a house has coloured rectangles showing the wall. And the empty white space, represents the free space ie. the rooms.</p></font> 
<font size=4><p>white pixels:free space</p></font> 
<font size=4><p>black pixels:occupied area</p></font> 

<font size=4><p>Aim: To derive such occupancy grid maps from real world sensor data.</p></font> 
---

## Volumetric v/s Feature occupancy grid map
![](volumetric_features.png)
<font size=4><p>Volumetric: The free space, in the form of paths, is visible on the map.</p></font>
<font size=4><p>Feature: Landmarks in the form of dots are seen on the occupancy grid map.</p></font>

---
## Mapping
<font size=4><p>We can get a map from:</p></font>
<font size=4><p>1. Sensor data</p></font>
<font size=4><p>2. Control commands</p></font>

---
## Mapping with pose information only
<font size=4><p>Occupancy grid cells are like floor tiles. Each cell can either be occupied or unoccupied.</p></font>
![](grid_cell.png)

### Probability : Binary variable (either occupied or not)
<font size=4><p>The probability of a grid cell being occupied is p(mi)</p></font>
![](occupancy_probability.png)
<font size=4><p>When p(mi)=0.8, it is considered to be 1.</p></font>
<font size=4><p>When p(mi) is not knonw or there are discrepancies, it is assigned the value of 0.5</p></font>
<font size=4><p>Since the probability is binary, P(occupied)=1-P(not occupied)</p></font>

### How do grid cells with different probability look
![](colour.png)

---

## Assumption 2
<font size=4><p>World doesn't move or change. Once a grid cell has a certain probability of occupation, it will remain same throughout.</p></font>

## Assumption 3
<font size=4><p>Probability of each grid cell is independant if its surrounding grid cells.</p></font>

---
## Overall occupancy probability as a function of each cell's probability
![](prob_func.png)

<font size=4><p>eg.</p></font>
![](example_of_probability_func.png)
![](eg2.png)

---
![](ouput.png)
<font size=4><p>The RHS is made up of binary variables.</p></font>
<font size=4><p>The LHS is a set of all the probability outputs.</p></font>

---
<font size=4><p>After doing all the calculations, we get</p></font>
![](final_equation.png)
<font size=4><p>LHS= new state of a cell 'i' at time 't'</p></font>
<font size=4><p>inv_sensor_model(...)= s=what the sensors are seeing at that instant</p></font>
<font size=4><p>l(t-1)(i)= Analogy with the LHS term: It is the old value the cell 'i' had</p></font>
<font size=4><p>lo= prior information</p></font>

![](wall.png)
<font size=4><p>Using a laser sensor, the initial part of the graph shows that there is free space and the probability is 0.</p></font>
<font size=4><p>When the rays of the laser encounter a wall, the rays are reflected back and hence the wall is detected. The probability of occupancy is thus said to be 1 there.</p></font>
<font size=4><p>The part of the graph beyond the wall cannot be detected due to obstruction by the wall. And, we dont know how thick the wall is. Hence, the probability of occupancy further cannot be known an dhnece is given the value of 0.5</p></font>

---
## Kalman Filters
<font size=4><p>Why to use?</p></font>
<font size=4><p>It helps us predict what the system will do next.</p></font>

<font size=4><p>Advantages of Kalman filters</p></font>
<font size=4><p>1. Fast computation.</p></font>
<font size=4><p>2. No need of history of data.</p></font>
<font size=4><p>3. Even with lots of noise/error, it will give good results.</p></font>

<font size=4><p>Step 1: Predict</p></font>
<font size=4><p>In this step, an estimation of the current state of the system is made using the previous value (not the ones before the last)</p></font>
<font size=4><p>Step 2: Update</p></font>
<font size=4><p>The 'actual values' from sensors like lidar are taken.</p></font>
<font size=4><p>Then, calculate the difference between the measured and the predicted values. Using the 'Kalman Gain', come to a conclusion on which value is more correct.</p></font>
<font size=4><p>This process is continued until the predicted and measured values become equivalent.</p></font>

## Problem with Kalman filters
<font size=4><p>They do not have any angle parameters. Hence, they do not work for non-linear systems.</p></font>

---
## Extended Kalman Filter
<font size=4><p>Extended Kalman Filter makes the non linear function into linear function using Taylor Series , it helps in getting the linear approximation of a non linear function.</p></font>
<font size=4><p>In extended Kalman filter the approximation was done based on a single point i.e means . This approximation may not be the best possible approximation and lead to poor performance.</p></font>

---
## Localization
<!-- <font size=4><p></p></font> -->
<font size=4><p>Process of estimating where the bot is in its environment.</p></font>

## Particle Filter
<font size=4><p>It is based upon the Monte Carlo method.</p></font>
<font size=4><p>What is the difference between EKF and particle filter?</p></font>
<font size=4><p>EKF can be used only for gaussian distributions. Whereas, the Monte Carlo method can be used generally.</p></font>

---
## How do particle-based filters work?
![](working_of_particle.png)
<font size=4><p>The places where partciles are dense, there is greater probability of the system being there.</p></font>
![](size_of_partcles.png)
<font size=4><p>The places where there is a higher probability of the system being present will have higher weights. (ie. the size of the particles present there would be largest)</p></font>

## Sampling Principle
![](sampling_principle.png)
<font size=4><p>The blue curve is the target curve f(x) which tells us exacly the probability of the system being present at that point.</p></font>
<font size=4><p>The red curve is the pi-curve/ proposal curve - pi(x)</p></font>
<font size=4><p>The weight is defined as f(x)/pi(x)</p></font>

---
## Prediction and update in particle filter
![](weighted_monte_carlo.png)
<font size=4><p>Step 1: Two empty containers, one for each function.</p></font>

# Monte Carlo Explanation
![](partcile_working.png)
<font size=4><p>Particles are assumed to be present on every spot of the map.</p></font>
<font size=4><p>Using the weights, the  particles which have higher probability are given more importance.</p></font>
![](weights.png)
<font size=4><p>The red readings are gotten by sensor values.</p></font>
<font size=4><p></p>The last readings mean: Higher weights are given to those parciles which occur at the peak of the graph.</font>

## AMCL 
<font size=4><p>amcl is a probabilistic localization system for a robot moving in 2D. It implements the adaptive (or KLD-sampling) Monte Carlo localization approach, which uses a particle filter to track the pose of a robot against a known map.</p></font>
