import cv2
import mediapipe as mp
import time

cap = cv2.VideoCapture(0)
mpFaceDetection = mp.solutions.face_detection
faceDetection = mpFaceDetection.FaceDetection(0.75)
mpDraw = mp.solutions.drawing_utils

pTime = 0

while cv2.waitKey(1) != 27:
    success, img = cap.read()
    imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
    results = faceDetection.process(imgRGB)
    # print(results.detections)
    if results.detections:
        # mpDraw.draw_landmarks(img, results.detections, mpFaceDetection.FACE_CONNECTIONS)
        for id, detection in enumerate(results.detections):
            # mpDraw.draw_detection(img, detection)
            # print(id, detection)
            # print(detection.score)
            # print(detection.location_data.relative_bounding_box)
            bboxC = detection.location_data.relative_bounding_box
            ih, iw, ic = img.shape
            bbox = int(bboxC.xmin*iw), int(bboxC.ymin*ih), int(bboxC.width*iw), int(bboxC.height*ih)
            cv2.rectangle(img, bbox, (255, 0, 150), 2)
            cv2.putText(img, f'{int(detection.score[0]*100)}%', (bbox[0], bbox[1]-20), cv2.FONT_HERSHEY_PLAIN, 3, (255, 150, 0), 3)

    cTime = time.time()
    fps = 1/(cTime - pTime)
    pTime = cTime
    cv2.putText(img, str(int(fps)), (70, 50), cv2.FONT_HERSHEY_PLAIN, 3, (255, 150, 0), 3)

    cv2.imshow("Image", img) 