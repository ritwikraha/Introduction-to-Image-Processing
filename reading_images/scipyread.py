from scipy import misc

#imread is deprecated! imread is deprecated in SciPy 1.0.0, and will be removed in 1.2.0. 
#Use imageio.imread instead.
#Read an image from a file as an array.
#This function is only available if Python Imaging Library (PIL) is installed.
f=misc.imread('Thanos.jpg')

import matplotlib.pyplot as plt
plt.imshow(f)
plt.show()