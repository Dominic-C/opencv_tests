import numpy as np
import imutils
import cv2

cap = cv2.VideoCapture("raw_videos/walking.mp4")

width = 800
def aspect_ratio_height(x):
    return int((x/16)*9)

while (cap.isOpened()):
    ret, frame = cap.read()

    frame = cv2.flip(frame,0)
    frame = cv2.flip(frame,1)
    frame = cv2.resize(frame, (width,aspect_ratio_height(width)),interpolation=cv2.INTER_AREA)

    # convert to grayscale   
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    # apply gaussian blur
    gray = cv2.GaussianBlur(gray, (21,21), 0)

    cv2.imshow("frame", frame)
    cv2.imshow("gaussian", gray)
    if cv2.waitKey(15) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()