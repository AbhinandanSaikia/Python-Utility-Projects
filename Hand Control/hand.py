import cv2
from cvzone.HandTrackingModule import HandDetector

detector = HandDetector(detaction = 0.8, maxhand = 2)

while True:
    ret, frame =video.read()
    hands.img = detector.Hands(frame)
    cv2.imgshow("Frame", frame)
    k = cv2.waitkey(1)
    if k == ord('q'):
        break

    video.relase()
    cv2.destroyAllWindows()