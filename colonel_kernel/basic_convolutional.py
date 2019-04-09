from PIL import Image, ImageDraw

# Load image:
input_image = Image.open("aquaman.jpg")

# The PixelAccess class provides read and write access to PIL.Image data at a pixel level.

input_pixels = input_image.load()

# Box Blur kernel
# the very basic low pass filter there is
blurr_kernel = [[1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9],
              [1 / 9, 1 / 9, 1 / 9]]

# a high pass filter that is meant to boost the pixel,
# if the neighbour pixels are different
sharpen_kernel = [[  0  , -.5 ,    0 ],
                   [-.5 ,   3  , -.5 ],
                   [  0  , -.5 ,    0 ]]


# Select kernel here:
kernel = blurr_kernel

# Middle of the kernel
offset = len(kernel) // 2

# Create output image
output_image = Image.new("RGB", input_image.size)
draw = ImageDraw.Draw(output_image)

# Compute convolution between intensity and kernels
for i in range(offset, input_image.width - offset):
    for j in range(offset, input_image.height - offset):
        conv = [0, 0, 0]
        # conv is created to store the value of convolution
        for a in range(len(kernel)):
            for b in range(len(kernel)):
                xn = i + a - offset
                yn = j + b - offset
                pixel = input_pixels[xn, yn]
                conv[0] += pixel[0] * kernel[a][b]
                conv[1] += pixel[1] * kernel[a][b]
                conv[2] += pixel[2] * kernel[a][b]

        draw.point((i, j), (int(conv[0]), int(conv[1]), int(conv[2])))
    
output_image.save("finalman.jpg")