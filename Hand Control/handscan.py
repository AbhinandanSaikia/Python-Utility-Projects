import cv2
from cvzone.HandTrackingModule import HandDetector

# Initialize video capture
video = cv2.VideoCapture(0)

# Correct parameter names
detector = HandDetector(detectionCon=0.8, maxHands=2)

while True:
    ret, frame = video.read()
    if not ret:
        break

    # Detect hands
    hands, img = detector.findHands(frame)

    # Display the image
    cv2.imshow("Frame", img)

    # Exit on 'q' key
    k = cv2.waitKey(1)
    if k == ord('q'):
        break

# Release resources
video.release()
cv2.destroyAllWindows()
