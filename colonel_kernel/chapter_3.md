# Chapter 3
- - - -
## Colonel Kernel
- - - -
So you have read all about reading images. We have extracted all sorts of channels and colors from them.
The real question is whether you can put those puppy eyes and snapchat filters on your images
Well, that is a bit more complicated but we can learn how to create our custom filters.

So let's dive in.
- - - -
In image processing, a kernel, convolution matrix, or mask is a small matrix. It is used for blurring, sharpening, embossing, edge detection, and more. This is accomplished by doing a convolution between a kernel and an image.
Convolution is the process of adding each element of the image to its local neighbors, weighted by the kernel.

- - - -
`code()`

for each image row in input image:
   for each pixel in image row:

      set accumulator to zero

      for each kernel row in kernel:
         for each element in kernel row:

            if element position  corresponding* to pixel position then
               multiply element value  corresponding* to pixel value
               add result to accumulator
            endif

      set output image pixel to accumulator

- - - -
1. Let us first explore the code from basic_convolutional.py to understand how kernels work.
2. We don't need to know define custom kernels everytime let's  go through opencv_filters.py to learn more
3. There are even more custom filters from ImageFilter module, I've demonstrated one of them in PIL_FILTERS.py
- - - - 
Still Confused?

You can check out these links to learn more about kernel.
1. [Image Kernels](http://setosa.io/ev/image-kernels/)
2. [New Convolutional Kernels](https://arxiv.org/ftp/arxiv/papers/1806/1806.07996.pdf)
3. [Convolutions](https://www.tutorialspoint.com/dip/concept_of_convolution.htm)