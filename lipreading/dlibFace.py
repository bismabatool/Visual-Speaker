import cv2
import numpy as np
import dlib
import imutils
from imutils import face_utils
from scipy.spatial import distance as dist
vid_list = ["./datase/06/WhatsApp Video 2020-01-13 at 1.45.24 AM.mp4","./datase/06/20200112_205430_Trim.mp4",
            "./datase/06/WhatsApp Video 2020-01-13 at 1.44.32 AM.mp4", "./datase/06/20200112_172453_Trim.mp4",
            "./datase/06/VID-20200112-WA0053.mp4", "./datase/06/20200112_205328_Trim.mp4", "./datase/06/20200112_205216_Trim.mp4",
            "./datase/06/VID-20200112-WA0194.mp4", "./datase/06/20200112_205216_Trim.mp4","./datase/06/VID-20200112-WA0098.mp4",
            "./datase/06/VID-20200112-WA0229.mp4"]
cap = cv2.VideoCapture(vid_list[-1]) #VID-20200112-WA0148.mp4

detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

while True:
    _, frame = cap.read()
    if not _:
        break;
    # frame = cv2.resize(frame, (400,400))
    frame = imutils.rotate(frame, 270)
    # frame = frame[0:300, 0:400]

    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)

    faces = detector(gray)

    for face in faces:
        x1 = face.left()
        y1 = face.top()
        x2 = face.right()
        y2 = face.bottom()
        # cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 3)

        (rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS["mouth"]
        landmarks = predictor(gray, face)
        # pts = [49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68]
        a = []
        for n in range(rStart, rEnd):
            x = landmarks.part(n).x
            y = landmarks.part(n).y
            cv2.putText(frame, str(n), (x, y), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 0, 255), 1, cv2.LINE_AA, False)
        shape = face_utils.shape_to_np(landmarks)
        mouth = shape[rStart:rEnd]

    cv2.imshow("Frame", frame)

    key = cv2.waitKey(1)
    if key == 27:
        break