'''
Developer: M.Sc. Shiva Agrawal
Place: Germany
Version: 1.0
Date: 03.07.2019
Description:  Canny Edge detection for the input video stream

Canny edge detection
Steps:
1. Import image and convert to grayscale
2. Remove noise using gaussian filter
3. Get Gradient using Sobel (X and Y)
4. Non maximum suppression
5. Hysteresis Thresholding (low and high)

NOTE: all the above steps (2 to 5) are possible to do by using canny() function. No need to implement them separately.

Project steps:
1. read video from webcam or video file
2. extract one image at a time and convert it into grayscale
3. Apply canny edge detector
4. Out the image into video stream


'''

import cv2

#-----------------------------------------------------------------------------------------------------------------------
# canny edge detection function
#-----------------------------------------------------------------------------------------------------------------------
def cannyEdgeDetection(color_image):
    threshold_low = 50     # hyperparameter
    threshold_high = 120   # hyperparameter
    gray_image = cv2.cvtColor(color_image,cv2.COLOR_BGR2GRAY) # convert into grascale image
    canny = cv2.Canny(gray_image,threshold_low,threshold_high)
    return canny

#-----------------------------------------------------------------------------------------------------------------------
# Calling Script
#-----------------------------------------------------------------------------------------------------------------------

#create a video capture instance
# NOTE: in the parameter of cv2.VideoCapture()
# value = 0 : Means it connects to first camera or webcam of device
# value = 'filename' :  Means it reds the video file

# NOTE: Use of the below lines and comment the other as per application
# cap = cv2.VideoCapture(0)                         # for webcam
cap = cv2.VideoCapture('German_city_roads.mp4')      # for video file

while (cap.isOpened()):
    ret, frame = cap.read() # read camera
    if ret == True:
        cv2.imshow('Live Edge Detection',cannyEdgeDetection(frame))
        cv2.imshow('Live Video',frame)
        if cv2.waitKey(30) == 13: # for enter key
            break

cap.release() # release camera
out.release()
cv2.destroyAllWindows()







