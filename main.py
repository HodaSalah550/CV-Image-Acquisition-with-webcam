import cv2
import time

#Zero for the webcam
video = cv2.VideoCapture(0)

#a variable
a = 0

while True:
    a = a + 1
    #create a frame object
    check, frame = video.read()

    print(check)
    print(frame) #representating image

    #converting to grayscale
    gray = cv2.cvtColor (frame, cv2.COLOR_BGR2GRAY)

    #to show the frame
    cv2.imshow('Capturing', gray)

    #to wait.... press anykey to out (miliseconds)
    #cv2.waitKey (0)

    #for playing
    key = cv2.waitKey(1)

    if key == ord('q'):
        break

#printing how miliseconds the streaming will take
print(a)

#shutdown the camera
video.release()

cv2.destroyAllWindows