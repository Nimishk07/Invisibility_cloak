import cv2 as cv
import numpy as np
load_from_disk=True
cap=cv.VideoCapture(0)
cap.set(3,1200)
cap.set(4,720)
bg=cv.imread("background.png")
# cv.imshow("kj",bg)
noiseth=400
cv.namedWindow("Harry potter",cv.WINDOW_NORMAL)
if load_from_disk:
    savedhsv = np.load("hsv_value.npy")
    lower = savedhsv[0]
    upper = savedhsv[1]
else:
    lower = list(map(int, input().split()))
    upper = list(map(int, input().split()))
kernel = np.ones((5, 5), np.uint8)
while True:
    ret,frame=cap.read()
    if not ret:
        break
    frame=cv.flip(frame,1)
    hsv=cv.cvtColor(frame,cv.COLOR_BGR2HSV)
    mask=cv.inRange(hsv,lower,upper)
    mask = cv.erode(mask, kernel, iterations=3)
    mask = cv.dilate(mask, kernel, iterations=5)
    contours, hierarchy = cv.findContours(mask, cv.RETR_EXTERNAL,cv.CHAIN_APPROX_SIMPLE)
    x=0
    y=0
    h=0
    w=0
    if contours and cv.contourArea(max(contours, key=cv.contourArea)) > noiseth:
        c = max(contours, key=cv.contourArea)
        x, y, w, h = cv.boundingRect(c)
        #\ cv.rectangle(frame, (x, y), (x + w, y + h), (0, 25, 255), 2)

    black_matrix = np.full((540, 960), 0, dtype=np.uint8)
    black_matrix[y:y+h+20, x:x+w+20] = 255
    mask = black_matrix


    cloak=cv.bitwise_and(bg,bg,mask=mask)
    mask=cv.bitwise_not(mask)
    rest=cv.bitwise_and(frame,frame,mask=mask)
    result=rest+cloak
    cv.imshow("Harry potter",result)
    if cv.waitKey(1)==27:
        break
cap.release()
cv.destroyAllWindows()
print(lower)
print(upper)
print(mask.shape)