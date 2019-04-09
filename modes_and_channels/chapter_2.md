# Chapter 2
- - - -
## Modes and Channels
- - - -
Have you ever wondered why black and white images look so different than color images. How are color images actually formed?

Do you actually need 7 colors to represent color images?

How does a computer differentiate between such images?

- - - - 
Okay first things first,

We can't represnt colors by fruits and flowers anymore. That ship has sailed a long time ago.

The color mode or image mode determines how colors combine based on the number of channels in a color model. Different color modes result in different levels of color detail and file size.

So hold on.

What are these channels?

The concept of channels is extended beyond the visible spectrum in multispectral and hyperspectral imaging. In that context, each channel corresponds to a range of wavelengths and contains spectroscopic information. The channels can have multiple widths and ranges.

- - - -
### RGB Channels

In a common 24 bit RGB image file, images are essentially made of three smaller 8 bit files. These smaller files are the image’s channels, and they have a range of 256 values, ranging from 0 – 255

- - - -
### Alpha Channels

Some image files (notably, like PNG) contain more image information in an extra channel. This channel is essentially no different than an RGB or CMYK channel, with 256 shades of gray representing the image areas. However, Alpha channels have on crucial difference: they denote transparency, not color information.

- - - -

If you are still confused, check out these four videos:

[How jpeg works -Computerphile](https://www.youtube.com/watch?v=LFXN9PiOGtY&list=PLzH6n4zXuckoAod3z31QEST1ZaizBuNHh&index=1)

