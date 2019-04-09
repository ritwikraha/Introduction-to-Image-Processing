import cv2

b=cv2.imread('batman.jpg')

blue=b.copy()
print(b.shape)

# look at the dimensions getting printed
# it should be something like this (579, 387, 3)

# here the first two dimensions represent the size of the matrix
#the third dimension represents the channels in the image

#0=BLUE
#1=GREEN
#2=RED

#for a grayscale image the third dimension will be just 1

#first we set the green and red channels to zero
blue[:,:,1]=0
blue[:,:,2]=0
# next we make anothe copy of batman (again not literally)
green=b.copy()
#set blue and red channels to zero
# a green batman, joker would be happy
green[:,:,0]=0
green[:,:,2]=0
#finally we make another copy and turn him red
red=b.copy()
red[:,:,0]=0
red[:,:,1]=0
# please note here that all your workspaces uses RGB mode
# however OpenCV uses BGR mode of indexing

cv2.imshow('Blue Knight',blue)
cv2.imshow('Green Knight',green)
cv2.imshow('Red Knight',red)

cv2.waitKey(0)
cv2.destroyAllWindows()