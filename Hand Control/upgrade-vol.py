import cv2
import mediapipe as mp
import pyautogui
import time

# Initialize MediaPipe Hands
mp_hands = mp.solutions.hands
hands = mp_hands.Hands(min_detection_confidence=0.8, min_tracking_confidence=0.8)

# Initialize OpenCV
cap = cv2.VideoCapture(0)

def control_music(gesture):
    if gesture == "pinch":
        # Volume up or down (depending on direction)
        pyautogui.press("volumeup")  # Simulate volume up
    elif gesture == "swipe_right":
        # Next song
        pyautogui.press("nexttrack")
    elif gesture == "swipe_left":
        # Previous song
        pyautogui.press("prevtrack")
    elif gesture == "two_fingers_up":
        # Play/Pause
        pyautogui.press("playpause")

while True:
    ret, frame = cap.read()
    if not ret:
        break

    # Flip the frame horizontally for a later mirror view
    frame = cv2.flip(frame, 1)
    # Convert the frame to RGB
    rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
    
    # Process the frame with MediaPipe
    results = hands.process(rgb_frame)
    
    if results.multi_hand_landmarks:
        for hand_landmarks in results.multi_hand_landmarks:
            # Detect pinch gesture by distance between index and thumb
            thumb_tip = hand_landmarks.landmark[mp_hands.HandLandmark.THUMB_TIP]
            index_tip = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
            distance = ((thumb_tip.x - index_tip.x)**2 + (thumb_tip.y - index_tip.y)**2)**0.5
            
            if distance < 0.05:  # Pinch gesture
                control_music("pinch")
            
            # Detect swipe gestures
            # Swipe right or left detection logic (based on movement direction)
            if len(hand_landmarks.landmark) >= 20:
                wrist = hand_landmarks.landmark[mp_hands.HandLandmark.WRIST]
                index = hand_landmarks.landmark[mp_hands.HandLandmark.INDEX_FINGER_TIP]
                
                if index.x > wrist.x:  # Swipe right
                    control_music("swipe_right")
                elif index.x < wrist.x:  # Swipe left
                    control_music("swipe_left")
                
                # Detect two fingers up for play/pause
                if thumb_tip.y < index_tip.y:  # Two fingers up gesture
                    control_music("two_fingers_up")

    # Display the frame
    cv2.imshow("Gesture-Controlled Music Player", frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

cap.release()
cv2.destroyAllWindows()
