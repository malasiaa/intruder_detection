import torch
import cv2
import datetime, time
from ultralytics import YOLO

try:

    # Create an instance of YOLOv5
    model = YOLO('yolov8s.pt')
    
    # Move the model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    exit(1)


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
    
    current_time = datetime.datetime.today()
    # Run the YOLOv5 model on the frame
    results = model(frame)  # Pass the image to YOLOv5 model

    # Parse the detection results
    detected_humans = False

    for result in results:
        for box in result.boxes:  # Iterate over each detected box
            class_id = int(box.cls)  # Get the class ID
            print(f"Class ID: {class_id}")
            if class_id == 0:  # Class '0' corresponds to 'person'
                detected_humans = True
            
            # Extract the bounding box coordinates (x1, y1, x2, y2)
            x1, y1, x2, y2 = map(int, box.xyxy[0])
            
            # Draw the rectangle around the detected object
            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 0), 2)
            
            # Add label to the box
            label = f'{model.names[class_id]}'
            cv2.putText(frame, label, (x1, y1 - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 0), 2)

    current_time = datetime.datetime.today()
    current_time = current_time.strftime("%m.%d.%Y_%H:%M:%S")

    # Save the image with bounding boxes
    cv2.imwrite(f"/output_images/output_with_boxes_{current_time}.jpg", frame)
    
    # Release the video capture object
    cap.release()

    if detected_humans:
        print("Human detected!")
    else:
        print("No human detected.")

# Call the function
run_script()
