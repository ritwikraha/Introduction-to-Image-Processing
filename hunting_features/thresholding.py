import cv2
import numpy as np
from matplotlib import pyplot as plt


# opencv has some pre-built methods of thresholding
#  If pixel value is greater than a threshold value,
# it is assigned one value (may be white), else it is assigned another value (may be black). 

img = cv2.imread('stark.jpg',0)
ret,thresh1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
ret,thresh2 = cv2.threshold(img,127,255,cv2.THRESH_BINARY_INV)
ret,thresh3 = cv2.threshold(img,127,255,cv2.THRESH_TRUNC)
ret,thresh4 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO)
ret,thresh5 = cv2.threshold(img,127,255,cv2.THRESH_TOZERO_INV)


# some adaptive thresholding functions that allows us to find edges and contours
# apart from adaptive mean, and adaptive gaussian there is also otsu's binarization

thresh6 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
thresh7 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)


cv2.imwrite('stark_dark.jpg',thresh1)

titles = ['Original Image','BINARY','BINARY_INV','TRUNC','TOZERO','TOZERO_INV','A_MEAN','A_GAUSSIAN']
images = [img, thresh1, thresh2, thresh3, thresh4, thresh5,thresh6,thresh7]

for i in range(8):
    plt.subplot(2,4,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()