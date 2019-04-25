import cv2

outdoor = cv2.imread('cube_outdoor.jpeg')
indoor = cv2.imread('cube_indoor.jpeg')

##outdoor = cv2.cvtColor(outdoor, cv2.COLOR_BGR2RGB)
##indoor = cv2.cvtColor(indoor, cv2.COLOR_BGR2RGB)

##B, G, R = cv2.split(outdoor)
##B_, G_, R_ = cv2.split(indoor)

##outdoorHSV = cv2.cvtColor(outdoor, cv2.COLOR_BGR2HSV)
##indoorHSV = cv2.cvtColor(indoor, cv2.COLOR_BGR2HSV)

##H, S, V = cv2.split(outdoorHSV)
##H_, S_, V_ = cv2.split(indoorHSV)

outdoorLAB = cv2.cvtColor(outdoor, cv2.COLOR_BGR2LAB)
indoorLAB = cv2.cvtColor(indoor, cv2.COLOR_BGR2LAB)

L, A, B = cv2.split(outdoorLAB)
L_, A_, B_ = cv2.split(indoorLAB)

cv2.imshow('outdoor', outdoor)
cv2.imshow('L', L)
cv2.imshow('A', A)
cv2.imshow('B', B)
cv2.imshow('indoor', indoor)
cv2.imshow('L_', L_)
cv2.imshow('A_', A_)
cv2.imshow('B_', B_)

cv2.imwrite('L.jpeg', L)
cv2.imwrite('A.jpeg', A)
cv2.imwrite('B.jpeg', B)
cv2.imwrite('L_.jpeg', L_)
cv2.imwrite('A_.jpeg', A_)
cv2.imwrite('B_.jpeg', B_)
