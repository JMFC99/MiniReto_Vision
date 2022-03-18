import cv2
from cvzone.HandTrackingModule import HandDetector
import numpy as np

cap = cv2.VideoCapture(0)

cap.set(3, 1280)
cap.set(4, 720)

if not cap.isOpened():
    print("Camera couldn't access")
    exit()

detector = HandDetector(detectionCon=0.7)

x, y = 150, 230
w, h = 200, 200
col  = (255, 0, 255)

while cap.isOpened():
    success, img = cap.read()
    # print((x-w //2>= 0) and ( y-h // 2>=800) and (x+w // 2<=500) and (y+h // 2<=500))
    # print(img)
    # print(success)
    img = detector.findHands(img)
    lmList, bboxInfo = detector.findPosition(img)

   
    if lmList:
        dist,_,_ = detector.findDistance(8, 12, img, draw = False)
        
        fingers = detector.fingersUp()
        if fingers[1] == 1 and fingers[2] == 1:
            cursor = lmList[8]
            if dist < 50:
                if x-w // 2 < cursor[0] < x+w-120 // 2 and y-h // 2 < cursor[1] < y+h-120 // 2:
                    col = (0, 180, 20)
                    x, y = cursor
                cv2.circle(img, cursor, 50, (0, 160, 0), cv2.FILLED)
                cv2.putText(img, "Sujetado", (cursor[0]-40, cursor[1]), cv2.FONT_HERSHEY_COMPLEX_SMALL,1,(0,0,0), 2)

            else:
                col = (10, 5, 255)


    touched = (20,0,220)

    cv2.rectangle(img, (x-w // 2, y-h // 2), (x+w // 2, y+h // 2), col, cv2.FILLED)
    cv2.putText(img, f'({str(x)}, {str(y)})', (x-90, y), cv2.FONT_HERSHEY_COMPLEX_SMALL, 1, (0, 0, 0), 2)
    
    if ((y-h//2>=500 or y+h//2>=500)):
        # if  (not((x-w // 2>=800) )) or (not((x-w // 2<=1400))):
            touched = (0,255,0)
            
    cv2.rectangle (img,(0,800),(2000,500),touched,cv2.FILLED)
    # cv2.rectangle(img,(0,2000),(2000,2000),touched,cv2.FILLED)
    cv2.imshow("Image", img)
    cv2.waitKey(1)



