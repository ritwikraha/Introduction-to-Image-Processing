import cv2
import numpy as np

image = cv2.imread('monalisa.jpg')

#cv2.imshow('image', image)

## Create a numpy array of zeros 
mask = np.zeros(image.shape, dtype=np.uint8)

## Define region to be not masked 
##roi_corners = np.array([[(10,10), (300,300), (10,300)]], dtype=np.int32)
roi_corners = np.array([[(120,50),(200,190),(40,190),(50,50)]], dtype=np.int32)


channel_count = image.shape[2] 
ignore_mask_color = (255,)*channel_count
## Fill the region except ROI 
cv2.fillPoly(mask, roi_corners, ignore_mask_color)
## Perform bitwise_and to black out the region except ROI
masked_image = cv2.bitwise_and(image, mask)

cv2.imshow('masked_image',masked_image)

