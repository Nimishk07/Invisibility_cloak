import cv2 as cv
import numpy as np
cap=cv.VideoCapture(0)
cap.set(3,1200)
cap.set(4,720)
cv.namedWindow("capture background",cv.WINDOW_NORMAL)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv.flip(frame,1)
    cv.imshow("capture background",frame)
    k=cv.waitKey(1)
    if k==27:       # the order of escape is 27 to exit without saving anything
        break
    if k==ord('s'):   #it is to save the image
        cv.imwrite("background.png",frame)
        break
cap.release()
cv.destroyAllWindows()

