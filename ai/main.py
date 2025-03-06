import os
try:
    import ultralytics
    import fastapi
except ImportError:
    os.system('pip install ultralytics')
    os.system('pip install fastapi[standard]')

from fastapi import FastAPI, UploadFile, File
from ultralytics import YOLO
import cv2
import numpy as np
from io import BytesIO
from PIL import Image

# FastAPI app
app = FastAPI()

# YOLOv8m model
model_path = "ai/yolov8m_7_segment.pt"
model = YOLO(model_path)


def read_imagefile(file) -> np.ndarray:
    """Convert uploaded file into an OpenCV image."""
    image = Image.open(BytesIO(file))
    return np.array(image)

@app.post("/predict/")
async def predict(file: UploadFile = File(...)):
    """Endpoint to accept an image and return model predictions."""
    contents = await file.read()
    image = read_imagefile(contents)

    # correct color format for YOLO model
    image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

    # Run YOLO inference
    results = model(image)

    # convert results into JSON format
    predictions = []
    for result in results:
        for box in result.boxes:
            predictions.append({
                "x1": float(box.xyxy[0][0]), "y1": float(box.xyxy[0][1]),
                "x2": float(box.xyxy[0][2]), "y2": float(box.xyxy[0][3]),
                "confidence": float(box.conf[0]),
                "class": int(box.cls[0])
            })
    predictions.sort(key = lambda x: x["x1"])
    return {"predictions\n": 
            predictions}

# to run the server use this command: fastapi dev ai/main.py