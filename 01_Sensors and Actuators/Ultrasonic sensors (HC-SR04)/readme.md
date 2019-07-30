# Ultrasonic Sensors - Driver development and Hardware Interfacing
* 10 Ultrasonic sensors (HC-SR04) are coonected to Arduino ATmega2560. 
* Arduino driver is written in C where it scans all the sensors one by one and stores the mesured values in cm.
* After accumulation of all the values in each cycle, complete data is transmitted serially.
* Arduino board is connected to Raspberry pi via USB cable. 
* This allows direct data transmission between boards via serial communication.
* A data read function is written (using Python) in raspberry pi, which reads the serial port, decodes the data and display all 
values from all the sensors.

## Hardware

![hardware](https://github.com/shiva-agrawal/autonomous_driving/blob/master/01_Sensors%20and%20Actuators/Ultrasonic%20sensors%20(HC-SR04)/hardware.jpg)

## Live demo of measurement acquisition from all 10 sensors
![Live demo](https://github.com/shiva-agrawal/autonomous_driving/blob/master/01_Sensors%20and%20Actuators/Ultrasonic%20sensors%20(HC-SR04)/Ultrasonic_sensors_demo.gif)

## Folder details:
* arduino_main.ino - arduino driver 
* arduino_serial_test.py - function at raspberry pi to read the serial data
* pin connections.txt - details of pin connections of sensors with arduino ATMega560 board
* Ultrasonic_sensors_demo.gif - live demo of 10 sensor values at arduino serial monitor
* hardware.jpg - hardware interfacing 



