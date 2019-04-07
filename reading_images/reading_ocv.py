import numpy as np
import cv2

#Use the function cv2.imread() to read an image. The image should be in the working directory or a full path of image should be given.

#Second argument is a flag which specifies the way image should be read.

#cv2.IMREAD_COLOR : Loads a color image. Any transparency of image will be neglected. It is the default flag.
#cv2.IMREAD_GRAYSCALE : Loads image in grayscale mode
#cv2.IMREAD_UNCHANGED : Loads image as such including alpha channel

# Instead of these three flags, you can simply pass integers 1, 0 or -1 respectively.

img = cv2.imread('thanos.jpg',1)

cv2.imshow('Perfectly balanced',img)
# now use the different flags to see for yourself
cv2.waitKey(0)
cv2.destroyAllWindows()