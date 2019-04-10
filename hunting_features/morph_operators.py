import cv2
import numpy as np
from matplotlib import pyplot as plt

img = cv2.imread('stark_dark.jpg',0)
kernel = np.ones((5,5),np.uint8)

#So the thickness or size of the foreground object decreases
# or simply white region decreases in the image.
# It is useful for removing small white noises


erosion = cv2.erode(img,kernel,iterations = 1)


# dilation increases the white region in the image or size of foreground object increases.

dilation = cv2.dilate(img,kernel,iterations = 1)

# opening -where erosion is followed by dilation
# useful in removing noise

opening = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)

# closing-where dilation is followed by erosion
# useful in refining the object

closing = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)

# gradient- difference between dilation and erosion of an object
# useful in finding edges
gradient = cv2.morphologyEx(img, cv2.MORPH_GRADIENT, kernel)



titles = ['Original Image','EROSION','DILATION','OPENING','CLOSING','GRADIENT']
images = [img, erosion, dilation, opening, closing, gradient]

for i in range(6):
    plt.subplot(2,3,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])

plt.show()