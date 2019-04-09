from PIL import ImageFilter, Image

im = Image.open("aquaman.jpg")

# custom image enhancement filters
# available at ImageFilter module 

image = im.filter(ImageFilter.BLUR)

image2 = im.filter(ImageFilter.MinFilter(3))
image3 = im.filter(ImageFilter.EDGE_ENHANCE_MORE)


# more documentation here:
# --------
#
# pillow.readthedocs.io/en/5.1.x/reference/ImageFilter.html
#
# --------

image.save('PIL BLUR.jpg')
image2.save('PIL MIN FILTER.jpg')
image3.save('PIL EDGE.jpg')

