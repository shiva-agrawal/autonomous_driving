'''
Developer: M.Sc. Shiva Agrawal
Place: Germany
Version: 1.0
Date: 15.06.2019
Description: This is the serial data read code written to get 10 Ultrasonic sensor data values from arduino ATmega2560 
via serial communication.

NOTE:
if the serial port permission are denied then open terminal and type
sudo usermod -a -G dialout username

then run it and then reboot the pi. It will start working permanantly.

'''

import serial
import numpy as np
# port name where arduino board is connedted for serial transmission
ser = serial.Serial("/dev/ttyACM0", 9600) 


# it reads the data in byte format and convert into float
# Output datastruture is an array with 20 values in each scan cycle.
# sensorID followed by value from UL sensor for all 10 sensors
while 1:
	if(ser.in_waiting >0):
		line = ser.readline().strip()  # removes the last new line byte from the data
		values = line.decode('utf-8').split(':') # convert byte into string and then split using :
		f = [float(i) for i in values[0:-1]]  # convert the 20 values (pair of sensorid and value of 10 UL sensors) into float from string
		print(f) # simply print
		
		
		
			
		
		
		
		
		
		


