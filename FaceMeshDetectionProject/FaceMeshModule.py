import cv2
import mediapipe as mp
import time

class faceMeshDetector():
    def __init__(self, staticMode = False, maxFaces = 2, refine_landmarks = False, minDetectionCon = 0.5, minTrackingCon = 0.5):

        self.staticMode = staticMode
        self.maxFaces =  maxFaces
        self.minDetectionCon = minDetectionCon
        self.minTrackingCon =  minTrackingCon
        self.refine_landmarks = refine_landmarks

        self.mpDraw = mp.solutions.drawing_utils
        self.mpFaceMesh = mp.solutions.face_mesh
        self.faceMesh = self.mpFaceMesh.FaceMesh(self.staticMode, self.maxFaces, self.refine_landmarks, self.minDetectionCon, self.minTrackingCon)
        self.draw_spec = self.mpDraw.DrawingSpec(thickness=1, circle_radius=1)

    def findFaceMesh(self, img, draw=True):
        self.imgRGB = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        self.results = self.faceMesh.process(self.imgRGB)
        faces = []
        if self.results.multi_face_landmarks:
            for faceLms in self.results.multi_face_landmarks:
                if draw:
                    self.mpDraw.draw_landmarks(img, faceLms, self.mpFaceMesh.FACEMESH_CONTOURS, self.draw_spec, self.draw_spec)
                face = []
                for id, lm in enumerate(faceLms.landmark):
                    # print(lm)
                    ih, iw, ic = img.shape
                    x, y = int(lm.x*iw), int(lm.y*ih)
                    cv2.putText(img, str(id), (x, y), cv2.FONT_HERSHEY_PLAIN, 1, (0, 255, 0), 1)
                    # print(id, x, y)
                    face.append([x,y])
                faces.append([])
        return img, faces

def main():
    cap = cv2.VideoCapture(0)
    pTime = 0
    detector = faceMeshDetector()

    while cv2.waitKey(1) != 27:
        success, img = cap.read()
        img, faces = detector.findFaceMesh(img)
        if len(faces) != 0:
            print(len(faces))

        cTime = time.time()
        fps = 1/(cTime-pTime)
        pTime = cTime
        cv2.putText(img, f"FPS: {int(fps)}", (20, 70), cv2.FONT_HERSHEY_PLAIN, 3, (0, 255, 0), 3)

        cv2.imshow("Image", img)


if __name__ == "__main__":
    main()