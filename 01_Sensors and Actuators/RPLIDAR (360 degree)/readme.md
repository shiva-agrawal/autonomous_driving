# RP LIDAR A1 - (360 degree) rotating sensor - Driver Development and Interfacing
* The sensor comes with USB connector which is directly connected with raspberry pi board.
* Data is send serially to the board.
* ROS publisher node is already available in the ROS community and hence it is downloaded, a ROS package is created and tested.
* This node publishes the complete scan data in form of range values for each degree angle for complete 360 degree.

## Hardware Interfacing
<img src = "https://github.com/shiva-agrawal/autonomous_driving/blob/master/01_Sensors%20and%20Actuators/RPLIDAR%20(360%20degree)/hardware%20interfacing.JPG" width = 500 height = 250/>

## Point cloud data from LIDAR
<img src = "https://github.com/shiva-agrawal/autonomous_driving/blob/master/01_Sensors%20and%20Actuators/RPLIDAR%20(360%20degree)/LIDAR_demo.gif">

## Folder Details:
* rplidar_ws - ROS package
* LIDAR_demo.gif - test results
* Hardware Interfacing. jpg - hardware connections of LIDAR with Raspberry-pi

