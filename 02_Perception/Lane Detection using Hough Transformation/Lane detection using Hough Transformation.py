'''
Developer: M.Sc. Shiva Agrawal
Place: Germany
Version: 1.0
Date: 04.07.2019
Description:  This is the lane detection algorithm developed using opencv and python.

Steps:
1. Import the image
2. Convertimage into grascale
3. Apply gusssian filter to blur the image
4. find edges using canny edge detector algorithm
5. Extract the region of Interest (ROI)
6. Apply Hough Transoformation and find all the lanes
7. Super imposed the lanes on the original color image to highlight it wiith specific color

NOTE:
1. There are many hyper parameters which needs to tune as per the input image and/or video stream.
I have used the values which are suitable for the image used here as input.

2. the same algorithm can be exteded to use with video stream by tuning the hyper parameters appropriately.
'''

import cv2 as cv
import numpy as np

## import color image and convert to grayscale
image_color = cv.imread('input_image.jpg',cv.IMREAD_COLOR)
cv.imshow('original_image',image_color)

image_gray = cv.cvtColor(image_color,cv.COLOR_BGR2GRAY)
cv.imshow('gray scale image',image_gray)


## apply guassian blur on grayscale image
image_blur = cv.GaussianBlur(image_gray,(7,7),1) # guassian kernel of 7 x 7 is used here
cv.imshow('blur image',image_blur)

## apply canny edge detection to find the edges from blur image
threshold_01 = 50  # hyperparameter
threshold_02 = 180 # hyperparameter

canny = cv.Canny(image_blur,threshold_01,threshold_02)
cv.imshow('canny edge detection',canny)

## select the ROI for the vehicle lane on grayscale image and then apply the final mask on canny image
blank_image = np.zeros_like(image_gray)
height,width = image_gray.shape
print(height,width)
ROI = np.array([[(70,height),(400,340),(500,340),(width-70,height)]], dtype=np.int32) # region is selected manually
mask = cv.fillPoly(blank_image,ROI,255)

masked_image = cv.bitwise_and(canny,mask)
cv.imshow('mask image',masked_image)

## apply Hough transformation to detect lanes
# hyperparameters for hough
rho = 2
theta = np.pi/180
threshold = 70
min_line_len = 70
max_line_gap = 100

lines = cv.HoughLinesP(masked_image,rho,theta,threshold,np.array([]),min_line_len,max_line_gap)
print(lines) # it contains all the lines along each row as [x1 y1 x2 y2] points

## show the detected lanes on original image
# 1. create a blank 3 channel image of same size with all 0
line_image = np.zeros((masked_image.shape[0],masked_image.shape[1],3), dtype=np.uint8)

# 2. draw lines on this blank image
for eachLine in lines:
    for x1,y1,x2,y2 in eachLine:
        cv.line(line_image,(x1,y1),(x2,y2),[0,0,255], 10)

cv.imshow('line',line_image)
cv.imwrite('Hough_Transformed_lines.jpg', line_image)

# 3. superimpose the lines on original image
lane_detected_image = cv.addWeighted(image_color,1,line_image,1,0) # out = src1*alpha + src2*beta + gamma
cv.imshow('lane detection - Hough Transformation',lane_detected_image)
cv.waitKey(0)
cv.destroyAllWindows()