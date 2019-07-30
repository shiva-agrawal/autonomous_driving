# Multi camera Interfacing

This module is divided into three sub tasks:

1. Development of web cam image acquision ROS node which takes image from web cam, convert into ROS image. This node dows the following

 1. Subscribes the camera image from usb_cam node using image_transport subscriber
 2. Convert the ROS Image message into CV image using cv_bridge
 2. Do image processing. (here I have just increase the brightness for demo purpose)
 3. Convert back the processed CV image into ROS image message
 4. Assign the ROS msg to image_tranport publisher
 5. Publish the processed image to  topic /processedImage/image (topic defined by me)
For the part, ROS node is developed using C++ and openCV 3 in Ubuntu 16.04. 

2. Interface 4 camera with raspberry pi using multi camera adapter and then develop a test script to get images from all the 4 camera. 
This task is also complete and a test file is available in the repository. 

Below figure shows the results:

![Results](https://github.com/shiva-agrawal/autonomous_driving/blob/master/01_Sensors%20and%20Actuators/Camera/results.png)

3. Combining Task 1 and 2 i.e. developing ROS node, but to aquire images from all 4 camera and publish them as ROS topic.
This part will be available soon and updated here.

## Folder details:

* ROS node for web cam image - ROS node with all the files
* Multicamera Interfacing.jpg - Hardware interfacing
* multiCameraTest.py - Python script for tesing multi camera system with raspberry pi
* results.png - all results in one figure

## Reference:

* https://www.arducam.com/multi-camera-adapter-module-raspberry-pi/
