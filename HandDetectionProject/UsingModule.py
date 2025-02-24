import cv2
import mediapipe
import time
import HandDetectionModule as htm



pTime = 0
cTime = 0
source = cv2.VideoCapture(0)
detector = htm.handDetector()
while cv2.waitKey(1) != 27:
    success, img = source.read()
    img = detector.findHands(img)
    lmList = detector.findPosition(img)
    if len(lmList) != 0:
        print(lmList[4])

    cTime = time.time()
    fps = 1 / (cTime-pTime)
    pTime = cTime

    cv2.putText(img, str(int(fps)), (10,70), cv2.FONT_HERSHEY_COMPLEX, 3, (255, 0, 0), 3)
    cv2.imshow('Image', img)