import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('stark.jpg',0)

# edges read from the  image  through canny edge detection algorithm
edges = cv2.Canny(img,100,200)

# It calculates the Laplacian of the image
# each derivative used is a sobel derivative

laplacian = cv2.Laplacian(img,cv2.CV_64F)

#Sobel operators is a joint Gausssian smoothing plus differentiation operation,
# so it is more resistant to noise.
# we can specify the direction of the derivatives to be taken

#sobelx is derivative w.r.t x axis

sobelx = cv2.Sobel(img,cv2.CV_64F,1,0,ksize=5)

#sobely is is the derivative w.r.t y axis
sobely = cv2.Sobel(img,cv2.CV_64F,0,1,ksize=5)
scharr = cv2.Scharr(img,cv2.CV_64F,0,1)

titles = ['Original Image','canny','laplacian','sobelx','sobely','scharr']
images = [img, edges, laplacian, sobelx, sobely, scharr]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()