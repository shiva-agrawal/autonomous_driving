'''
Developer: MSc. Shiva Agrawal
Description:

This is the multi camera test code. It is used to acquire images from 4 pi camera connected together with board
using arducam multicamera adapter,

the image resolution is set to 640 x 480.
WIth this adapter, only one camera can be accessed at a time and hence, each camera (A, B, C, D) are accessed and image is grabed in round robbin manner. 

'''


import RPi.GPIO as gp
from picamera import PiCamera
from time import sleep


camera = PiCamera()
camera.resolution = (640,480)
 

gp.setwarnings(False)
gp.setmode(gp.BOARD)

# setup the stack layer 1 board
# for details of pin, refer Arducam multicamera adapter document online
gp.setup(7,gp.OUT)
gp.setup(11,gp.OUT)
gp.setup(12,gp.OUT)

# grab from camera A
gp.output(7, False)
gp.output(11,False)
gp.output(12,True)

camera.capture('/home/crazytech/Shiva/imageA.jpg')
sleep(0.25)


# grab from camera B
gp.output(7, True)
gp.output(11,False)
gp.output(12,True)

camera.capture('/home/crazytech/Shiva/imageC.jpg')
sleep(0.25)

# grab from camera C
gp.output(7, False)
gp.output(11,True)
gp.output(12,False)

camera.capture('/home/crazytech/Shiva/imageB.jpg')
sleep(0.25)

# grab from camera D
gp.output(7, True)
gp.output(11,True)
gp.output(12,False)

camera.capture('/home/crazytech/Shiva/imageD.jpg')
sleep(0.25)
