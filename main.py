# main.py
import cv2
from object_detector import detect_objects
from speech_engine import speak
from helper_utils import get_direction
from config import PRIORITY_OBJECTS

def main():
    cap = cv2.VideoCapture(0)
    
    while cap.isOpened():
        ret, frame = cap.read()
        if not ret:
            break

        detections = detect_objects(frame)
        frame_width = frame.shape[1]

        for _, row in detections.iterrows():
            label = row['name']
            x_center = (row['xmin'] + row['xmax']) / 2
            direction = get_direction(x_center, frame_width)

            # ✅ Print detection info
            print(f"Detected: {label} at x_center: {x_center:.2f}, direction: {direction}")

            if label in PRIORITY_OBJECTS:
                speak(f"{label} on your {direction}")

        # Optional: Show live frame
        cv2.imshow('YOLOv5 Live Detection', frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    cap.release()
    cv2.destroyAllWindows()

if __name__ == "__main__":
    main()
