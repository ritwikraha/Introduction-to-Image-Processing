import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('aquaman.jpg')

# an averaging filter kernel
kernel = np.ones((5,5),np.float32)/25

blur = cv2.blur(img,(5,5))
gblur = cv2.GaussianBlur(img,(5,5),0)
medianblur = cv2.medianBlur(img,5)

dst = cv2.filter2D(img,-1,kernel)

cv2.imwrite('lowpass.jpg',blur)
cv2.imwrite('gaussian.jpg',gblur)
cv2.imwrite('median blur.jpg',medianblur)
cv2.imwrite('averaging filter.jpg',blur)

