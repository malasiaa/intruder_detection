import torch
import cv2
import datetime
from ultralytics import YOLO
import telegram

# Set up Telegram bot
bot_token = '7558765085:AAHA9j4WIlNfpkWXGoaErnowFFFRKaMtsk0'
chat_id = '6731228814'

bot = telegram.Bot(token=bot_token)

try:
    # Create an instance of YOLOv8
    model = YOLO('yolov8s.pt')
    
    # Move the model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    exit(1)

def send_telegram_message(text, image_path=None):
    """Send a message with an optional image to the Telegram bot."""
    bot.send_message(chat_id=chat_id, text=text)
    if image_path:
        # Send the image if provided
        bot.send_photo(chat_id=chat_id, photo=open(image_path, 'rb'))

def run_script():
    # Replace with your IP camera's stream URL
    ip_camera_url = 'http://192.168.1.71:81/stream'  # Example URL

    # Open the video stream
    cap = cv2.VideoCapture(ip_camera_url)

    if not cap.isOpened():
        print("Error: Cannot access the camera stream.")
        return
    # Workaround to deal with delay and avoid getting the n-1 frame
    # Clear the buffer by reading multiple frames
    for i in range(5):  # Read 5 frames to clear the buffer
        ret, frame = cap.read()

    if not ret:
        print("Error: Unable to read frame from the camera.")
        cap.release()  # Always release the video capture object when done
        return

    # Run the YOLOv8 model on the latest frame
    results = model(frame)

    detected_humans = False

    # Parse the detection results
    for result in results:
        for box in result.boxes:
            class_id = int(box.cls)
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

    # Get the current time to include in the filename
    current_time = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')

    # Save the image with bounding boxes and timestamp in the filename
    cv2.imwrite(f"output_images/output_with_boxes_{current_time}.jpg", frame)

    # Release the video capture object
    cap.release()

    if detected_humans:
        # Saving the image with human
        image_path = f"output_images/human_output_with_boxes_{current_time}.jpg"
        cv2.imwrite(image_path, frame)
        print("Human detected!")

        # Send Telegram message
        send_telegram_message("Alert: Human detected on your camera feed!", image_path=image_path)
    else:
        # Saving the image with human
        image_path = f"output_images/output_with_boxes_{current_time}.jpg"
        cv2.imwrite(image_path, frame)
        print("No human detected.")

