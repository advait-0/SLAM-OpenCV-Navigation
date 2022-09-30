<p>
<h1 align = "center" > <strong>🚙 SLAM-OpenCV-Navigation 🚗</strong> <br>

<h3 align = "center">
 
</p>

A simulation of a Bot in Gazebo and RViz which creates a map of it's environment and navigates through it while avoiding obstacles.


## Table of Contents

* [About](#about)

* [Tech Stack and Tools](#tech-stack-and-tools)

* [File Structure](#file-structure)

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

* The aim of the project was to design a bot that could map and navigate in the environment provided to it and simultaneously follow an object while avoiding obstacles.

* ROS was used to make the model of the bot functional, Gazebo and RViz was used for simulational and python for scripting.

  

### Tech Stack and Tools

<img src="https://i.imgur.com/VWH6TKY.png" width="50" height="13" />         ROS Noetic

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/5/53/OpenCV_Logo_with_text.png/487px-OpenCV_Logo_with_text.png" width="30" height="40" />         OpenCV

<img src="https://seeklogo.com/images/G/gazebo-logo-51C46471CA-seeklogo.com.png" width="40" height="50" />         Gazebo

<img src="https://raw.githubusercontent.com/ros-visualization/rviz/noetic-devel/images/splash.png" width="60" height="50" />         RViz

<img src="https://upload.wikimedia.org/wikipedia/commons/thumb/c/c3/Python-logo-notext.svg/1869px-Python-logo-notext.svg.png" width="60" height="50" />         Python



### File Structure

![](https://user-images.githubusercontent.com/99654265/193124139-23f87a70-1c6a-484e-b7fb-cc17b8e1329c.png)


### Prerequisites
 1. [ROS Noetic](http://wiki.ros.org/noetic/Installation)

2. [Gazebo Version: 11.11](https://classic.gazebosim.org/download)

3. [RViz](http://wiki.ros.org/rviz/UserGuide)

4. [Ubuntu or it's flavours Versioned 20.04](https://ubuntu.com/)
  
### Installation

1. Clone the repo

<code>
git clone https://github.com/notad22/SLAM-OpenCV-Navigation.git
</code>

2. Install the dependencies

<code>
sudo apt-get install ros-noetic-cv-bridge
</code>
<br/>

<code>
sudo apt-get install ros-noetic-navfn
</code>  
<br />
<code>
sudo apt-get install ros-noetic-amcl
</code>  
<br />

<code>
sudo apt-get install ros-noetic-gmapping
</code>  
<br />
<code>
sudo apt-get install ros-noetic-map-server
</code>  
<br />
<code>
sudo apt-get install ros-noetic-move-base
</code>  
<br />
<code>
sudo apt-get install ros-noetic-tf
</code>  



## Usage

1. After cloning the repo, source the following
   <code>
   source /opt/ros/noetic/setup.bash   
   </code>
   <code>
   source ~/catkin_ws/devel/setup.bash
   </code>

(Alternative: You can add these commands to your bashrc.)

2. You can launch a specific launch file based upon your usage
    - world.launch - just launches the bot in the world 
    - amcl.launch   - used to create a map of the environment using monte carlo 
                                 localization techniques
    - navigation_stack.launch - used to autonomously navigate the bot in the environment

  
3. For launching the bot navigate to the launch folder 
<code>
cd ~/catkin_ws/src/slam_simulations/launch
</code>

 
4. Launch the launchfile based on your usage:
<code>
roslaunch slam_simulations file_name.launch
</code>

## Project Methodology
- The project started off by learning ROS commands and it's file structures and learning how to create a launch file.
- A model bot was then used to which links, joints and sensors were added for it's usage in gazebo.
- We then used the sensor readings from our hokuyo lidar and kinect sensor to create a map of our surroundings using the gmapping package in ROS.
- Various deep learning modules and filters were then studied so as to understand and implement the techniques to localize the bot in it's environment using adaptive monte carlo localization.
- YOLO was then used to detect objects in the environment of the bot, darknet opensource framework was used for this.
  
## Results and Demo


<video src="https://user-images.githubusercontent.com/99654265/193127103-8e45a508-9055-4779-ad68-afbe58d7d497.mp4" controls="controls" style="max-width: 730px;">
</video>


## Future Work

 
- [ ] To merge tracking with SLAM for a more lucrative output.
- [ ] To implement the bot on real hardware.
  

## Troubleshooting
- Clone the darknet ROS repository recursively to avoid possible CMake errors
- To achieve better navigation yaml parameters in the config can be tuned 

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


## License

The [license](https://github.com/notad22/SLAM-OpenCV-Navigation/blob/main/LICENSE) used for this project.
