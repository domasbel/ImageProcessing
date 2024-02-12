# -*- coding: utf-8 -*-
"""
Created on Fri Dec 21 13:56:33 2018

@author: Andrius
"""

import cv2
from brisque import BRISQUE

print(cv2.__version__)
print(cv2.__file__)

# # Read image
image = cv2.imread('pic.png')
# # Show image
cv2.imshow('Color image',image)
# # Write image
cv2.imwrite('pic.jpg', image)

# Display information about image
print (image.shape)
print (image.size)
print (image.dtype)

# # Read image as grayscale
# image2 = cv2.imread('pic.png', 0)
# # image2 = cv2.imread('pic.png', cv2.IMREAD_GRAYSCALE )
# # cv2.IMREAD_COLOR or 1 (default value) – reads color image, but values of transparency are ignored.
# # cv2.IMREAD_GRAYSCALE or 0 – reads grayscale image.
# # cv2.IMREAD_UNCHANGED or -1 – reads color image and alpha channel.
# cv2.imshow('Grayscale image',image2)
# cv2.imwrite('pic2.jpg', image2)

# # Convert image to grayscale
# gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
# cv2.imshow('Grayscale',gray)
# print(gray.shape)
# # Convert image back to BGR
# bgr = cv2.cvtColor(gray, cv2.COLOR_GRAY2BGR)
# cv2.imshow('BGR',bgr)
# print(bgr.shape)

# # Change top left pixel to red
# # y, x, channel
# img = image.copy();
# img[0, 0, 0] = 0;
# img[0, 0, 1] = 0;
# img[0, 0, 2] = 255;
# # or
# img[0,0] = [0, 0, 255]
# cv2.imshow('Changed',img)

# # Change other pixel to blue
# # y, x, channel
# img = image.copy();
# print( img.item(100, 120, 1))
# img.itemset( (100, 120, 1), 255)
# print( img.item(100, 120, 1) )
# cv2.imshow('Changed',img)

# # Change whole channel (red)
# img = image.copy();
# img[:, :, 0] = 0
# img[:, :, 1] = 0
# cv2.imshow('Changed',img)

# # Change group of pixels
# # y, x, channel
# img = image.copy();
# img[100:120, 120:130, 0] = 0;
# img[100:120, 120:130, 1] = 0;
# img[100:120, 120:130, 2] = 255;
# # or
# img[100,120] = [0, 0, 255]
# cv2.imshow('Changed',img)

# # Move pixel region
# img = image.copy();
# my_roi = img[0:300, 0:300]
# img[500:800, 500:800] = my_roi
# cv2.imshow('Changed',img)

# Calculate image quality
# https://pypi.org/project/brisque/
# Image Quality Assessment (IQA)
# less is better
# https://learnopencv.com/image-quality-assessment-brisque/
image3 = cv2.imread('pic.png')
obj = BRISQUE(url=False)
print("Quality score: " + str(obj.score(image3)))

# # Close the windows
k = cv2.waitKey(0)
if k == 27:         # wait for ESC key to exit
    cv2.destroyAllWindows()
elif k & 0xFF == ord('q'):
    cv2.destroyAllWindows()
