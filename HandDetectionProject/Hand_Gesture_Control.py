import cv2
import time
import numpy as np
import HandDetectionModule as htm
import math
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume

###############################################
wCam, hCam = 640, 480
###############################################

cap = cv2.VideoCapture(0)
cap.set(3, wCam)
cap.set(4, hCam)
pTime = 0

detector = htm.handDetector(maxHands=1, detectionCon=0.7) #This step imports hand detector function from the module

devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(
    IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = interface.QueryInterface(IAudioEndpointVolume)
# volume.GetMute()
# volume.GetMasterVolumeLevel()
volRange = volume.GetVolumeRange()

minVol = volRange[0]
maxVol = volRange[1]
vol = 0
volBar = 300
volPer = 0
while cv2.waitKey(1) != 27:
    success, img = cap.read()
    img = detector.findHands(img)
    lmlist = detector.findPosition(img, draw=False)
    if len(lmlist) != 0:   
        # print(lmlist[4], lmlist[8])

        x1, y1 = lmlist[4][1], lmlist[4][2]
        x2, y2 = lmlist[8][1], lmlist[8][2]
        cx, cy = (x1+x2)//2, (y1+y2)//2

        cv2.circle(img, (x1, y1), 8, (255, 8, 255), cv2.FILLED)
        cv2.circle(img, (x2, y2), 8, (255, 8, 255), cv2.FILLED)
        cv2.circle(img, (cx, cy), 8, (255, 8, 255), cv2.FILLED)
        cv2.line(img, (x1, y1), (x2, y2), (255, 8, 255), 3)

        length = math.hypot(x2-x1, y2-y1)
        # print(length)

        # Hand range 20 - 200
        # Volumne range -37 - 0
        vol = np.interp(length, [20, 200], [minVol, maxVol])
        volBar = np.interp(length, [20, 200], [300, 150])
        volPer = np.interp(length, [20, 200], [0,100])
        print(int(length), vol)
        volume.SetMasterVolumeLevel(vol, None)

        if  length<20:
            cv2.circle(img, (cx, cy), 8, (0, 255, 0), cv2.FILLED)

    cv2.rectangle(img, (50, 150), (70, 300), (255, 0, 0), 3)
    cv2.rectangle(img, (50, int(volBar)), (70, 300), (255, 0, 0), cv2.FILLED)
    cv2.putText(img, f'{int(volPer)} %', (48, 400), cv2.FONT_HERSHEY_COMPLEX,
                1, (255, 0, 0), 3)

    cTime = time.time()
    fps = 1/(cTime-pTime)
    pTime = cTime

    cv2.putText(img, f'FPS: {int(fps)}', (48, 50), cv2.FONT_HERSHEY_COMPLEX,
                1, (0, 0, 0), 3)

    cv2.imshow("Img", img)
    