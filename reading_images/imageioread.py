import imageio
import visvis as vv
import matplotlib.pyplot as plt
# imageio is another  Python library that provides 
#an easy interface to read and write a wide range of image data, 
#including animated images, volumetric data, and scientific formats.

im = imageio.imread('thanos.jpg')
print(im.shape)
# their official documentation uses visvis library to visualise the data 
# in case it doesn't work on your system
# you can also use matplotlib

plt.imshow(im)
plt.show()
#vv.imshow(im)