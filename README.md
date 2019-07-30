# Project Title: Autonomous Driving
#### Author and Developer: MSc. Shiva Agrawal
#### Place: Germany
#### Email id: agrawalshivaa@gmail.com
#### Memeber of IEEE-RAS (IEEE Robotics and Automation Society)

#
“If You Are Working On Something That You Really Care About, You Don’t Have To Be Pushed. The Vision Pulls You.” – Steve Jobs
#

This is long term project aimed to develop various algorithms in the field of autonomous driving and autonomous mobile robot. There are dedicated processing blocks like sensor interfacing, perception, localization and mapping, path planning and obstacle avoidance, control system, actuator interfacing, etc. in the development of the complete autonomous vehicle (refer architecture below) and so each algorithm after development and testing, will be included under the corresponding sub-topic with detail information and source code.

The project include both software and Hardware development and interfacing. In order to develop cost effective project, low cost controller boards, sensors and actuators are used.

NOTE: This repository contains only the information and source code of the current completed work under each module. Hence as further work is develop, it will be updated. 

# Table of Content
  * [Software and Tools](#software-and-tools)
  * [Hardware and Sensors](#Hardware-and-sensors)
  * [System Archtecture](#system-architecture)
  * [Sensors and Actuators](#Sensors-and-actuators)
    * [Ultrasonic sensors](#ultrasonic-sensors)
    * [360 degree LIDAR](#360-degree-LIDAR)
    * [Camera Module](#camera-module)
  * [Perception](#Perception)
    * [Canny Edge detector](#Canny-edge-detector)
    * [Road Lane detection using Hough Transformation](#Road-lane-detection-using-hough-transformation)
    * [Vehicle Detection using HOG and SVC](#vehicle-detection-using-HOG-and-SVC)
    * [Trafiic sign classifier using CNN and Keras](#trafiic-sign-classifier-using-CNN-and-keras)
    * [Self driving Sensors Simulation with ROS and Gazebo](#self-driving-sensors-simulation-with-ros-and-gazebo)
  * [Robot/Vehicle Modeling and Control](#robot-vehicle-modeling-and-control)
    * [3D modelling and Visualization of Robots using ROS and Gazebo](#3d-modelling-and-visualization-of-robots-using-ros-and-Gazebo)

# Softwares and Tools

Name | Purpose
-----|--------
ROS (Robot Operating System)-Kinetic | For development of communication between I/O and other processing blocks
Ubuntu 16.04 | Base Operating system used to run ROS and other software
C++ | Programming language
Python | Programming language
scipy, numpy, pandas|Python scientific computing and datastructure library
Matplotlib|Python library for generating plots and statistical results
Tensorflow, keras|Python Deep learning library
Scikit-learn|Python Machine mearning library
openCV| computer vision library supports both C++ and Python
Pycharm| IDE for Python development

# Hardware and sensors

Name | Purpose
-----|------------
Raspberry pi 3 Model B|SoC controller board which supports ROS and camera interfacing
Arduino ATmega2560|Interfacing of some sensors and then communicate with raspberry pi 
Ultrasonic sensors|Total 10 sensors for all sides of vehicle
Pi-camera|4 modules to cover 360 degree FoV of the vehicle for machine vision
RPLIDAR A1| 360 degree rotating lidar to collect point cloud data for perception
IMU| for measuring acceleration, roatation of the vehicle for Localization
GPS| for Localization
wheel encoder| for Localization
DC motor|rear wheel motion actuator - for longitudinal control of vehcile
Servo| front wheel steer actuator - for lateral control of vehicle

# System architecture

![Project Block diagram](https://github.com/shiva-agrawal/autonomous_driving/blob/master/00_Overview/System%20Srchitecture.JPG)

# Sensors and Actuators

This module contains informationa for interfacing each sensor and actuator with Raspberry pi 3 and/or Arduino ATmega2560 board. The development of driver for each sensor and actuator is in the form of ROS publisher or Subscriber node.

Sensor Drivers - Publisher nodes - Collect the measurement data and publish to other nodes at specific sample rate.
Actuator Drivers - Subscriber nodes - take motion control information and then actuate the motor accordingly.

Complete Hardware Interfacing block diagram is shown below.

<img src="https://github.com/shiva-agrawal/autonomous_driving/blob/master/00_Overview/Hardware%20Interface%20Block%20Diagram.jpg" width="550" height = 450/>


## Ultrasonic sensors
* As shown in the above block diagram, 10 sensors are interface with Arduino ATmega2560 development board. 
* Measurement from each sensor is taken one at a time in circular manner and the result for one cycle including all the sensors is send to raspberry pi serially. This driver is developed in C++ using Arduino Sketch.
* Python script is developed and tested in raspberry pi to get the sensor measurement data. ROS node is planned in future for this. 

Hardware Interfacing | Distance measurement 
-----|------------
<imag src = "https://github.com/shiva-agrawal/autonomous_driving/blob/master/01_Sensors%20and%20Actuators/Ultrasonic%20sensors%20(HC-SR04)/hardware.jpg" width = 300 height = 250> | ![Live Distance measurement](https://github.com/shiva-agrawal/autonomous_driving/blob/master/01_Sensors%20and%20Actuators/Ultrasonic%20sensors%20(HC-SR04)/Ultrasonic_sensors_demo.gif)

## 360 degree LIDAR 
* As shown in above block diagram, RPLIDAR A1 is interfaced with raspberry pi directly using of the USB ports. 
* It can measure and send the data in form of angle and range for 360 degree in one scan serially.
* The ROS publisher node for this sensor is already developed by ROS community and hence it is downloaded and used here directly.

[Block Diagram] + [video or animation]

## Camera Module
* As shown in the block diagram, the camera are first connected to a camera adapter board for raspberry pi.
* This adapter board helps to interface multiple camera using one CSI port of rspebrry pi
* The normal testing script is developed at first using Python and picamera library
* Then ROS publisher node is developed and tested which takes the image from each camera one by one and send it to other nodes at specific sampling rate.

[Block Diagram] + [video or animation]

# Perception

After getting the sensor raw data or processed data, this module works to extract useful information out of the data. To extract the useful information, either one or more sensors are used toegther. The process of combining data frommultiple sensors together to get accurate information is known as **"Sensor Data Fusion"**. This also includes huge use of computer vision, deep learning like Neural netwroks, Machine learning algorithms, etc. and hence also require high computing power.

## Canny Edge detector
* This algorithm is one of the best among edge detection algorithms use in computer vision and it has wide applications in AD. It comprised of multiple steps shown in block diagram below.
* It is developed in Python with openCV and well tested on multiple images and also on road video stream.
* Below is the block diagram for the complete process of canny edge detector algorithm and also the animation of the video result.

![Canny Edge Detection steps](https://github.com/shiva-agrawal/Autonomous_Driving_Project/blob/master/02_Perception/01%20Canny%20Edge%20Detector/block_diagram.JPG)
![Edge detection video](https://github.com/shiva-agrawal/Autonomous_Driving_Project/blob/master/02_Perception/01%20Canny%20Edge%20Detector/result.gif)

## Road Lane detection using Hough Transformation
* It uses canny edge detector described above as base for lane detection. 
* Further Hough transform (a mathematical form to represent the lines using slope and intercept in hough space) finds the lines in the Region of interest and provides the coordinates of all the lines.
* This lines are then superimposed on the original image / stream of images to detect lanes continuously during driving.
* This algorithm is use in the front mounted camera and is very important application for Autonomous driving.
![process flow diagram with result](https://github.com/shiva-agrawal/Autonomous_Driving_Project/blob/master/02_Perception/02%20Lane%20Detection%20using%20Hough%20Transformation/lane_detection_process_flow_diagram.JPG)

## Vehicle Detection using HOG and SVC
* HOG - Histogram of Oriented Gradient (a feature extracion algorithm in computer vision)
* SVM - Support Vector Classifier (a Machine Learning technique for classification) 
* A large dataset (images) of car and non car are taken as input. 
* Pahse 1 - HOG is used to extract features from each image and stored
* Phase 2 - These features are then given to SVC to train the model for vehicle detection.
![Block diagram](https://github.com/shiva-agrawal/Autonomous_Driving_Project/blob/master/02_Perception/03%20Car%20Detection%20using%20HOG%20and%20SVC/processs_flow_diagram.JPG)

## Trafiic sign classifier using CNN and Keras
* Morethan 30,000 color images of different traffic signs are taken for the input.
* A Deep neural network is build which consist of convulational later, pooling layer and Fully connected layer.
* Python library - keras is used to develop and train the Neural network.
* Then confusion matrix is calculated for the accuracy of the model

## Sensors simulation with ROS and Gazebo
* Simulation of following sensors in ROS kinetic and Gazebo
  * Velodyne
  * Mono and stereo camera
  * GPS
  * IMU
  * Ultrasonic sensor
* Use of sensor models in form of xacro files for simulation
* Testing and documentation

[Block Diagram] + [video or animation]

# Robot/Vehicle Modeling and Control 
For Autonomous robot or autonomous vehicle, smooth control (longitudinal and lateral) is final part in the complete process. The design of control system requires deep information about the system, here. vehicle/robot and hence modeling of the robot is also included here. Then design of various control systems and generation of final actuator signal which drives DC motor and/or servo motor for navagation is also part of this module.

## 3D modelling and Visualization of Robots using ROS and Gazebo
* Development of 3D models of differential mobile Robots (used here as example only). 
* NOTE: In future ackermann drive model will also be developed and simulated for the work.
* Understanding and Developement of URDF and XACRO files for robots
* Implementation of launch files 
* Visualization of 3D robots in Gazebo Simulation environment

[Block Diagram] + [video or animation]












