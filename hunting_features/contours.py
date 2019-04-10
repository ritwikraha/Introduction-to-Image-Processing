import numpy as np
import cv2
 
im = cv2.imread('stark.jpg')
im1 =im
imgray = cv2.cvtColor(im,cv2.COLOR_BGR2GRAY)
ret,thresh = cv2.threshold(imgray,127,255,0)
contours= cv2.findContours(thresh,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
im_contours=cv2.drawContours(im1, contours, -1, (0,255,0), 3)


cv2.imshow('CHAIN_APPROX_NONE',im_contours )

cv2.waitKey(0)
cv2.destroyAllWindows()
