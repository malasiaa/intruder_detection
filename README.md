# Intruder Detection System

The **Intruder Detection System** is a Python-based project that uses computer vision to detect intruders from a video stream, such as an IP camera. The system is designed to notify the user through a Telegram Bot when an intruder is detected. It captures and saves images if motion is detected. Supports real-time notifications when a human is detected.

<p align="center" width="100%">
    <img width="32%" src="https://github.com/user-attachments/assets/5e410775-80b7-4b94-811d-9602282ffe89">
</p>


## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [Requirements](#requirements)
- [Installation](#installation)

## Features

- **Real-time Intruder Detection**: Detects intruders or motion in a video stream.
- **Telegram Notifications**: Sends an alert to a Telegram bot when an intruder is detected.
- **Image Capture**: Captures images of the intruder and saves them locally.
- **Customizable**: Easy to set up with your own IP camera and Telegram bot.

## Architecture

This project is a fork of my repository [wifi_camera_esp32](https://github.com/malasiaa/wifi_camera_esp32), but on steroids :laughing:. The ESP32 CAM, combined with a PIR sensor is placed in the desired place. You should run the Flask server script. The ESP32 board will connect to your WiFi, and if the PIR sensor detects a motion, it will send a get request to the flask server. This on another hand will retrieve an image from the camera, and classify if there are any humans in it, by using the lightweight YOLOV8s model, which can easily be run on today's average CPU. If there is any, it will send a Telegram message to your cellphone.

<p align="center" width="100%">
    <img width="32%" src="https://github.com/user-attachments/assets/76a85c85-d25d-4e98-82d2-01d780b02871">
</p>

## Requirements

- Python 3.8 or above
- PlatformIO (or Arduino IDE)
- Telegram Bot API
- ESP32 board with a camera module (AI Thinker Model) ([ESP32-CAM and ESP32-CAM-MB](https://pt.aliexpress.com/item/1005006938892262.html?src=google&src=google&albch=shopping&acnt=272-267-0231&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&isSmbAutoCall=false&needSmbHouyi=false&src=google&albch=shopping&acnt=272-267-0231&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005006938892262&ds_e_product_merchant_id=5346350603&ds_e_product_country=PT&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=20695431540&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=Cj0KCQjw4MSzBhC8ARIsAPFOuyUrv-3EmW35uy8ZSv-_7S-G1Faw_W5M5DSnsyVQwbEPoaeKBJvvBDEaAjWfEALw_wcB&aff_fcid=cf0879a328a44c42afd7b636f587dfdb-1718749467693-00217-UneMJZVf&aff_fsk=UneMJZVf&aff_platform=aaf&sk=UneMJZVf&aff_trace_key=cf0879a328a44c42afd7b636f587dfdb-1718749467693-00217-UneMJZVf&terminal_id=bec40578c234405895a1646236025a60&afSmartRedirect=y))
- [PIR sensor](https://pt.aliexpress.com/item/1005007104651468.html?src=google&src=google&albch=shopping&acnt=298-731-3000&isdl=y&slnk=&plac=&mtctp=&albbt=Google_7_shopping&aff_platform=google&aff_short_key=UneMJZVf&gclsrc=aw.ds&&albagn=888888&&ds_e_adid=&ds_e_matchtype=&ds_e_device=m&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005007104651468&ds_e_product_merchant_id=109246662&ds_e_product_country=PT&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=20857248473&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1)
  
## Installation

1. **Clone the repository**
   
   ```bash
   git clone https://github.com/malasiaa/intruder_detection.git
   cd intruder_detection

2. **#ESP32 CAM setup**
   1) Open the Arduino IDE, or PlatformIO
   2) Select the main.cpp file
   3) Connect the ESP board to your computer
   4) Select the appropriate board and port under Tools > Board and Tools > Port, or if using PlatformIO, upload the config.ini file
   5) Specify your WiFi SSID, password, and the Flask Server IP, in the main.cpp sketch
   6) If using PlatformIO, add the header file camera_stream.h path in "includePath" list at the .vscode/c_cpp_properties.json file
   7) Upload the code to the board

3. **Python Setup**

   1) Create a virtual environment and install dependencies

        ```bash
        python3 -m venv venv
        source venv/bin/activate
  
          #Or using conda:
     
        conda create --name intruder_detection_env
        conda activate intruder_detection_env
  
     
        pip install -r requirements.txt

   2) Update variables in [config.py](https://github.com/malasiaa/intruder_detection/blob/main/config.py), used by the flask and model scripts
      - IPs allowed to send a request to flask server
      - Telegram token and chat id
      - The camera IP, where it is streaming
      - Create a directory where you want to save the images classified
     
   3) Run [flask_server.py](https://github.com/malasiaa/intruder_detection/blob/main/flask_server.py) and be safe!
