import numpy as np
import cv2
cap = cv2.VideoCapture("/Users/admin/startup/Splash-Bootanimation.mp4")
if not cap.isOpened():
    print("Cannot open camera")
    exit()
while True:
    ret, frame = cap.read()
    cv2.imshow('', frame)
    cv2.waitKey(1)
# cap.release()
cv2.destroyAllWindows()
print(5)
