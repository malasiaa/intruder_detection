import torch
import cv2

# Load the pre-trained YOLOv5 model (e.g., yolov5s for a small model)
model = torch.hub.load('yolov5', 'yolov5s')  # yolov5s is a lightweight model


def run_script():
    # Replace with your IP camera's stream URL
    ip_camera_url = 'http://192.168.1.70:81/stream'  # Example URL

    # Open the video stream
    cap = cv2.VideoCapture(ip_camera_url)

    if not cap.isOpened():
        print("Error: Cannot access the camera stream.")
        return

    ret, frame = cap.read()  # Read one frame
    if not ret:
        print("Error: Unable to read frame from the camera.")
        return
    
    # Run the YOLOv5 model on the frame
    results = model(frame)  # Pass the image to YOLOv5 model
    
    # Parse the detection results
    detected_humans = False
    for pred in results.pred[0]:  # results.pred[0] contains the detected objects
        # pred[5] is the class label, 0 corresponds to 'person' in the COCO dataset
        print(pred[5])
        if int(pred[5]) == 0:  # If the detected class is 'person'
            detected_humans = True
            break
    
    # Release the video capture object
    cap.release()

    if detected_humans:
        print("Human detected!")
    else:
        print("No human detected.")