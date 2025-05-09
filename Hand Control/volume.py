import cv2
import numpy as np
from cvzone.HandTrackingModule import HandDetector
from ctypes import cast, POINTER
from comtypes import CLSCTX_ALL
from pycaw.pycaw import AudioUtilities, IAudioEndpointVolume
import math
import time

# Initialize video capture
video = cv2.VideoCapture(0)
detector = HandDetector(detectionCon=0.8, maxHands=1)

# Volume control setup
devices = AudioUtilities.GetSpeakers()
interface = devices.Activate(IAudioEndpointVolume._iid_, CLSCTX_ALL, None)
volume = cast(interface, POINTER(IAudioEndpointVolume))
volMin, volMax = volume.GetVolumeRange()[:2]

# Variables for swipe detection
prev_center_x = None
swipe_threshold = 80  # How far the hand must move to be considered a swipe
swipe_cooldown = 1.0  # seconds
last_swipe_time = 0

while True:
    success, img = video.read()
    hands, img = detector.findHands(img)

    if hands:
        lmList = hands[0]["lmList"]
        bbox = hands[0]["bbox"]
        center = hands[0]["center"]

        if lmList:
            # Volume control using thumb and index finger
            x1, y1 = lmList[4][:2]
            x2, y2 = lmList[8][:2]
            cx, cy = (x1 + x2) // 2, (y1 + y2) // 2

            length = math.hypot(x2 - x1, y2 - y1)
            vol = np.interp(length, [30, 200], [volMin, volMax])
            volume.SetMasterVolumeLevel(vol, None)

            # Volume bar
            volBar = np.interp(length, [30, 200], [400, 150])
            volPercent = np.interp(length, [30, 200], [0, 100])
            cv2.rectangle(img, (50, 150), (85, 400), (0, 0, 0), 2)
            cv2.rectangle(img, (50, int(volBar)), (85, 400), (0, 255, 0), cv2.FILLED)
            cv2.putText(img, f'{int(volPercent)} %', (40, 430), cv2.FONT_HERSHEY_PLAIN,
                        2, (0, 255, 0), 2)

            # Swipe Detection
            current_time = time.time()
            if prev_center_x is not None:
                diff = center[0] - prev_center_x
                if diff > swipe_threshold and (current_time - last_swipe_time) > swipe_cooldown:
                    print(" Next Swipe Detected")
                    last_swipe_time = current_time
                    # You can trigger your action here, like changing slides or tracks

            prev_center_x = center[0]

    cv2.imshow("Hand Gesture Control", img)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video.release()
cv2.destroyAllWindows()
