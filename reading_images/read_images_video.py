import cv2

## Video input from cameras connected with the system.
## 0 -> Webcam, Use 1,2 etc depending on which USB port your camera is connected
cap = cv2.VideoCapture(0)

while(True):
    ret, frame = cap.read()

    cv2.imshow('frames', frame)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# When everything done, release the capture
cap.release()
cv2.destroyAllWindows()
