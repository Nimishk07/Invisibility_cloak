import cv2 as cv
import numpy as np
def nothing(x):
    pass
cap = cv.VideoCapture(0)
cap.set(3, 1200)
cap.set(4, 720)
cv.namedWindow("Tracker", cv.WINDOW_NORMAL)
cv.createTrackbar("L-H", "Tracker", 0, 179, nothing)
cv.createTrackbar("L-S", "Tracker", 0, 255, nothing)
cv.createTrackbar("L-V", "Tracker", 0, 255, nothing)
cv.createTrackbar("U-H", "Tracker", 179, 179, nothing)
cv.createTrackbar("U-S", "Tracker", 255, 255, nothing)
cv.createTrackbar("U-V", "Tracker", 255, 255, nothing)

while 1:
    ret, frame = cap.read()
    if not ret:
        break
    frame = cv.flip(frame, 1)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    l_h= cv.getTrackbarPos("L-H","Tracker")
    l_s= cv.getTrackbarPos("L-S", "Tracker")
    l_v= cv.getTrackbarPos("L-V", "Tracker")
    u_h= cv.getTrackbarPos("U-H", "Tracker")
    u_s= cv.getTrackbarPos("U-S", "Tracker")
    u_v= cv.getTrackbarPos("U-V", "Tracker")
    lower_limit = np.array([l_h,l_s,l_v])
    upper_limit = np.array([u_h, u_s, u_v])
    mask=cv.inRange(hsv,lower_limit,upper_limit)
    hsvres=cv.bitwise_and(frame,frame,mask=mask)
    maskgrey=cv.cvtColor(mask, cv.COLOR_GRAY2BGR)
    h_stack=np.hstack((maskgrey,frame,hsvres))
    cv.imshow("Tracker",cv.resize(h_stack, None, fx=0.4, fy=0.4))
    k=cv.waitKey(1)
    if k==27:
        break
    if k==ord('s'):
        s=[[l_h,l_s,l_v],[u_h,u_s,u_v]]
        np.save("hsv_value",s)
        print(s)
        break
cap.release()
cv.destroyAllWindows()



