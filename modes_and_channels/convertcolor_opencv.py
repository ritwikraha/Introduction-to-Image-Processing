import cv2


#For color conversion, we use cv2.cvtColor(input_image, flag) where flag determines the type of conversion.

#For BGR (Blue Green Red) to Gray conversion we use the flags cv2.COLOR_BGR2GRAY. 

#Similarly for BGR rightarrow HSV(Hue Saturation Lightness), we use the flag cv2.COLOR_BGR2HSV

b=cv2.imread('batman.jpg')

#first we read batman,
# no, not literally, that's impossible

b_bw= cv2.cvtColor(b,cv2.COLOR_BGR2GRAY)

cv2.imshow('Dark Knight',b_bw)
# now use the different flags to see for yourself
cv2.waitKey(0)
cv2.destroyAllWindows()