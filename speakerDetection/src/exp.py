import cv2

cap = cv2.VideoCapture("../videos/exapmle.webm")
while True:
    # print("herrerer")
    ret, img = cap.read()
    if not ret:
        break
    img = cv2.resize(img, (300, 500))
    cv2.imshow("fram", img)
    cv2.waitKey()