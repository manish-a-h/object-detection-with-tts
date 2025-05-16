# object_detector.py
import torch
from config import CONFIDENCE_THRESHOLD

# Load YOLOv5 model
model = torch.hub.load('ultralytics/yolov5', 'yolov5s', pretrained=True)
model.conf = CONFIDENCE_THRESHOLD

def detect_objects(frame):
    results = model(frame)
    detections = results.pandas().xyxy[0]
    return detections
