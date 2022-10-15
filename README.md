<p>
<h1 align = "center" > <strong>🚙 SLAM-OpenCV-Navigation 🚗</strong> <br>

<h3 align = "center">
 
</p>

A simulation of a Bot in Gazebo and RViz which creates a map of it's environment and navigates through it while avoiding obstacles.


## Table of Contents

* [About](#about)

   * [Tech Stack and Tools](#tech-stack-and-tools)

   * [File Structure](#file-structure)
* [Getting Started](#getting-started)

  * [Prerequisites](#prerequisites)

  * [Installation](#installation)

  * [Usage](#usage)

* [Project Methodology](#project-methodology)

* [Results and Demo](#results-and-demo)

* [Future Work](#future-work)

* [Troubleshooting](#troubleshooting)

* [Contributors](#contributors)

* [Acknowledgements and Resources](#acknowledgements)

* [License](#license)

  

## About

* The aim of the project is to design a bot that could map and navigate in the environment provided to it and simultaneously follow an object while avoiding obstacles.

* ROS was used to make the model of the bot functional, Gazebo and RViz were used for simulation and python for scripting.

  

### Tech Stack and Tools

 <img src="https://i.imgur.com/VWH6TKY.png" width="50" height="13" />&nbsp; &nbsp; &nbsp; &nbsp;ROS Noetic

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/OpenCV_Logo_with_text.png/487px-OpenCV_Logo_with_text.png" width="30" height="40" />&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;OpenCV

<img src="https://seeklogo.com/images/G/gazebo-logo-51C46471CA-seeklogo.com.png" width="40" height="50" />&nbsp; &nbsp; &nbsp; &nbsp;&nbsp;&nbsp;&nbsp;Gazebo

<img src="https://raw.githubusercontent.com/ros-visualization/rviz/noetic-devel/images/splash.png" width="60" height="50" />&nbsp; &nbsp; &nbsp; &nbsp;RViz

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="60" height="50" />&nbsp; &nbsp; &nbsp; &nbsp;Python



### File Structure
```  
|--📁urdf
|    |--   📄differential_bot.xacro            # xacro file containing all necessary inofrmation to define 
|    |--   📄differential_bot.gazebo           # gazebo file with all necessary sensor plugins                                                        
|
|--📁meshes
|    |--📄hokuyo.dae                           # mesh for hokuyo lidar
|    |--📄kinect.dae                           # mesh for kinect sensor
|
|--📁rviz
|    |--📄differential_bot.rviz                # rviz config file for bot launch
|  
|--📁world
|    |--📄iscas_museum.sdf                      # bot environment file
|
|--📁launch
|    |--📄world.launch                          # world launch file to launch bot with environment
|    |--📄amcl.launch                           # launch file used for mapping the environment
|    |--📄robot_description.launch              # launches the bot xacro along with necessary nodes
|    |--📄navigation_stack.launch               # launch file for autonomous navigation of the bot
|
|--📁Maps
|    |--📄iscas_museum.pgm                      # map portable grey map file
|    |--📄iscas_museum.yaml                     # environment map yaml
|
|--📁config
|    |--📄global_costmap_params.yaml            # global and local costmap parameter files 
|    |--📄local_costmap_params.yaml
|    |--📄base_local_planner_params.yaml
|    |--📄costmap_common_params.yaml
|
|--📁Assets
|    |--Slam-CV-Navigation.pdf
|
|--📄CMakeLists.txt
|--📗package.xml
```  

![Flowchart(3)](https://user-images.githubusercontent.com/99654265/195963699-33a9d91a-39a0-4441-aa32-d6bc314098af.png)

## Getting Started
### Prerequisites
1. [ROS Noetic](http://wiki.ros.org/noetic/Installation)

2. [Gazebo Version: 11.0.0](https://classic.gazebosim.org/download)

3. [RViz](http://wiki.ros.org/rviz/UserGuide)

4. [Ubuntu or it's flavours Versioned 20.04](https://ubuntu.com/)
  
### Installation

1. Clone the repo  
    <code>
    git clone --recursive https://github.com/notad22/SLAM-OpenCV-Navigation.git
    </code>

2. Install the dependencies  
   <code>
   sudo apt-get install ros-noetic-cv-bridge
   </code>  
   <code>
   sudo apt-get install ros-noetic-navfn
   </code>  
   <code>
   sudo apt-get install ros-noetic-amcl
   </code>  
   <code>
   sudo apt-get install ros-noetic-gmapping
   </code>  
   <code>
   sudo apt-get install ros-noetic-map-server
   </code>  
   <code>
   sudo apt-get install ros-noetic-move-base
   </code>  
   <code>
   sudo apt-get install ros-noetic-tf
   </code>  





## Usage

1. After cloning the repo, source the following    

     <code>
     source /opt/ros/noetic/setup.bash   
     </code>
     <p></p>
     <code>
     source ~/catkin_ws/devel/setup.bash
     </code>

(Alternative: You can add these commands to your bashrc.)

2. For launching the bot navigate to the launch folder   

   <code>
    cd ~/catkin_ws/src/slam_simulations/launch
   </code>  

3. Launch the world.launch file at first to get the bot with it's sensors and it's environment  

4. Open a new terminal tab or window and source the above mentioned commands

5. Launch the launchfile based on your use-case:  

   <code>
   roslaunch slam_simulations file_name.launch
   </code>

 - gmapping.launch - uses laser readings and pose data to create a 2D occupancy grid map
                     of the robot's surroundings. 

 - amcl.launch   - used to create a map of the environment using monte carlo 
                                 localization techniques.   
                              (suitable controller can be used here)
 
 - navigation_stack.launch - used to autonomously navigate the bot in the environment.
 
 6. darknet_ros.launch - Darknet is an open source neural network which implements the YOLO algorithm.
                       This launch file will detect objects in the surroundings of the robot and identify them.
                       <p>You can visit the repo below and follow the given steps for implementation of YOLO.</p>
                       [darknet_ros](https://github.com/leggedrobotics/darknet_ros.git)
                       <p>You can clone the above repo using:</p>
                       <code>
                       git clone --recursive https://github.com/leggedrobotics/darknet_ros.git
                       </code>  
                       Make sure to clone it recursively.   
                       After cloning it navigate to the package directory.   
                       <code>
                        cd ~/catkin_ws/src/darknet_ros/darknet_ros/launch
                       </code>   
                       Launch the launchfile.   
                       <code>
                        roslaunch darknet_ros darknet_ros.launch
                       </code> 
                       
                       
  7. To run the object followimg script  
     <code>
       rosrun slam_simulations obj_following.py
      </code>
   
    
   
   
                       
   
 
  
 
      
   
          
    
   
   
     
   


## Project Methodology
- The project started off by learning ROS commands and it's file structures and learning how to create a launch file.
- A model bot was then used to which links, joints and sensors were added for it's usage in gazebo.
- We then used the sensor readings from our hokuyo lidar to create a map of our surroundings using the gmapping package in ROS.
- Various deep learning modules for object detection, and filters to localize the bot in it's environment using 
  adaptive monte carlo localization were studied.
- YOLO was then used to detect objects in the environment of the bot, darknet opensource framework was used for this.
  
## Results and Demo

![Gmapping](https://user-images.githubusercontent.com/99654265/193448722-8218e642-e7e7-486b-b22e-1eeab0678895.gif)

https://user-images.githubusercontent.com/99654265/193328844-fdec88a9-9343-4de8-a604-f91be27b35bb.mp4









## Future Work

- [ ] To improve the bot's object following capabilities
- [ ] To merge tracking with SLAM for a more lucrative output.
- [ ] To implement the bot on real hardware.
  

## Troubleshooting
- Clone the darknet ROS repository recursively to avoid possible CMake errors.
- To achieve better navigation yaml parameters in the config can be tuned. 

## Contributors

* [Advait Dhamorikar](https://github.com/notad22)- advaitdhamorikar@gmail.com

* [Dishie Vinchhi](https://github.com/dishie2498) - vdishie@gmail.com

  

## Acknowledgements 
- [SRA Vjti](https://www.sravjti.in/) Eklavya 2022

A special thanks to our mentors for this project:
- [Aryaman Shardul](https://github.com/Aryaman22102002)
- [Rishabh Bali](https://github.com/Ris-Bali)
- [Sagar Chotalia](https://github.com/sagarchotalia) 
  <br/>

## Resources

- [Linear Algebra](https://youtube.com/playlist?list=PL0-GT3co4r2y2YErbmuJw2L5tW4Ew2O5B)
- [Deep Learning Specialisation](https://www.coursera.org/specializations/deep-learning)
- [Notes of Linear Algebra and DL](https://github.com/notad22/SLAM-OpenCV-Navigation/tree/dishie_notes)
- [Object Detection in ROS](https://github.com/leggedrobotics/darknet_ros) 
- [Playlist for localisation](https://www.youtube.com/playlist?list=PLgnQpQtFTOGSeTU35ojkOdsscnenP2Cqx)


## License

The [license](https://github.com/notad22/SLAM-OpenCV-Navigation/blob/main/LICENSE) used for this project.
