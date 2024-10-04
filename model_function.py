import torch
import cv2
import datetime
from ultralytics import YOLO
from aiogram import Bot
from aiogram import Dispatcher
from aiogram.types import FSInputFile
import config
import asyncio

# Set up Telegram bot
bot_token = config.TELEGRAM_bot_token
chat_id = config.TELEGRAM_chat_id

bot = Bot(token=bot_token)

dp = Dispatcher()

try:
    # Create an instance of YOLOv8
    model = YOLO('yolov8s.pt')
    
    # Move the model to GPU if available
    device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
    model.to(device)
    
except Exception as e:
    print(f"An error occurred while loading the model: {e}")
    exit(1)

# Define an async function to send the photo
async def send_telegram_message(chat_id, image_path, text="Human detected!"):
    
    try:
        # Use InputFile to wrap the image path
        photo = FSInputFile(image_path)
        await bot.send_photo(chat_id=chat_id, photo=photo, caption=text)
    except PermissionError as e:
        print(f"PermissionError: {e}")
    finally:
        await bot.session.close()  # Close the bot session properly

async def main():
    # Replace with your IP camera's stream URL
    ip_camera_url = config.IP_CAMERA_URL

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
    cv2.imwrite(f"{config.OUTPUT_IMAGES_PATH}/output_with_boxes_{current_time}.jpg", frame)

    # Release the video capture object
    cap.release()

    if detected_humans:
        # Saving the image with human
        image_path = f"{config.OUTPUT_IMAGES_PATH}/human_output_with_boxes_{current_time}.jpg"
        cv2.imwrite(image_path, frame)
        print("Human detected!")

        # Send Telegram message
        await send_telegram_message(chat_id=chat_id, image_path=image_path)
    else:
        # Saving the image with human
        image_path = f"output_images/output_with_boxes_{current_time}.jpg"
        cv2.imwrite(image_path, frame)
        print("No human detected.")

