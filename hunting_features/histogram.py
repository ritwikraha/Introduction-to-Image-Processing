# Import the necesssary module
import scipy.ndimage as ndi
import matplotlib.pyplot as plt
import numpy as nd
import imageio
import numpy as np

#import the image
im=imageio.imread('stark_dark.jpg')

# Create a histogram, binned at each possible value
hist = ndi.histogram(im,min=0,max=255,bins=256)

# Create a cumulative distribution function
cdf = hist.cumsum() / hist.sum()

# Plot the histogram and CDF
fig, axes = plt.subplots(2, 1, sharex=True)
axes[0].plot(hist, label='Histogram')
axes[1].plot(cdf, label='CDF')
plt.show()