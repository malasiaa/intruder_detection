# Intruder Detection System

The **Intruder Detection System** is a Python-based project that uses a computer vision to detect intruders from a video stream, such as an IP camera. The system is designed to notify the user through a Telegram Bot when an intruder is detected. It supports real-time notifications, captures and saves images if motion is detected.

**Architecture**

This project is a fork of my repository [wifi_camera_esp32](https://github.com/malasiaa/wifi_camera_esp32), but with steroids :laughing:. The ESP32 CAM, combined with a PIR sensor is placed in the desired place. You should run the Flask server script. The ESP32 board will connect to your WiFi, and if a motion is detected by the PIR sensor, it will send a get request to flask server. This on another hand will retrieve an image from the camera, classify if there's any humans in it, by using the lightweight YOLOV8s model, which can easily be runned on today's average cpu. If there is any, it will send a Telegram message to your cellphone.

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
- [Acknowledgements](#acknowledgements)
- [License](#license)

## Features

- **Real-time Intruder Detection**: Detects intruders or motion in a video stream.
- **Telegram Notifications**: Sends an alert to a Telegram bot when an intruder is detected.
- **Image Capture**: Captures images of the intruder and saves them locally.
- **Customizable**: Easy to set up with your own IP camera and Telegram bot.

## Requirements

- Python 3.8 or above
- Telegram Bot API
- ESP32 board with a camera module (AI Thinker Model) ([ESP32-CAM and ESP32-CAM-MB](https://pt.aliexpress.com/item/1005006938892262.html?src=google&src=google&albch=shopping&acnt=272-267-0231&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&isSmbAutoCall=false&needSmbHouyi=false&src=google&albch=shopping&acnt=272-267-0231&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005006938892262&ds_e_product_merchant_id=5346350603&ds_e_product_country=PT&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=20695431540&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=Cj0KCQjw4MSzBhC8ARIsAPFOuyUrv-3EmW35uy8ZSv-_7S-G1Faw_W5M5DSnsyVQwbEPoaeKBJvvBDEaAjWfEALw_wcB&aff_fcid=cf0879a328a44c42afd7b636f587dfdb-1718749467693-00217-UneMJZVf&aff_fsk=UneMJZVf&aff_platform=aaf&sk=UneMJZVf&aff_trace_key=cf0879a328a44c42afd7b636f587dfdb-1718749467693-00217-UneMJZVf&terminal_id=bec40578c234405895a1646236025a60&afSmartRedirect=y))
- PlatformIO (or Arduino IDE)
- 
## Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/malasiaa/intruder_detection.git
   cd intruder_detection

2. **ESP32 CAM setup**
 - Open the Arduino IDE, or PlatformIO.
 - Select the main.cpp file.
 - Connect the ESP board to your computer.
 - Select the appropriate board and port under Tools > Board and Tools > Port, or if using PlatformIO, upload the config.ini file.
 - Specify your WiFi SSID, password, and the Flask Server IP, in the main.cpp sketch.
 - If using PlatformIO, make sure to add the header file camera_stream.h path in "includePath" list at the .vscode/c_cpp_properties.json file.
 - Upload the code to the board.

3. **Python setup**
 - Create a virtual environment
   ```bash
   python -m venv venv
   source venv/bin/activate

 - Install the required dependencies
   ```bash
   pip install -r requirements.txt

 - In [config.py](https://github.com/malasiaa/intruder_detection/blob/main/config.py) update the fields used by the flask and model scripts.
   1) IPS allowed to send a request to flask server; 2) telegram token and chat id; 3) The camera IP, where it is streaming; 4) directory where you want to save the images classified.
