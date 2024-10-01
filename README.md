# Intruder Detection System

The **Intruder Detection System** is a Python-based project that uses computer vision to detect intruders from a video stream, such as an IP camera. The system is designed to notify the user through Telegram when motion or an intruder is detected. It supports real-time notifications and captures images of the detected intruders.

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
- ESP32 board with a camera module (AI Thinker Model) ([ESP32-CAM and ESP32-CAM-MB](https://pt.aliexpress.com/item/1005006938892262.html?src=google&src=google&albch=shopping&acnt=272-267-0231&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&isSmbAutoCall=false&needSmbHouyi=false&src=google&albch=shopping&acnt=272-267-0231&slnk=&plac=&mtctp=&albbt=Google_7_shopping&gclsrc=aw.ds&albagn=888888&ds_e_adid=&ds_e_matchtype=&ds_e_device=c&ds_e_network=x&ds_e_product_group_id=&ds_e_product_id=pt1005006938892262&ds_e_product_merchant_id=5346350603&ds_e_product_country=PT&ds_e_product_language=pt&ds_e_product_channel=online&ds_e_product_store_id=&ds_url_v=2&albcp=20695431540&albag=&isSmbAutoCall=false&needSmbHouyi=false&gad_source=1&gclid=Cj0KCQjw4MSzBhC8ARIsAPFOuyUrv-3EmW35uy8ZSv-_7S-G1Faw_W5M5DSnsyVQwbEPoaeKBJvvBDEaAjWfEALw_wcB&aff_fcid=cf0879a328a44c42afd7b636f587dfdb-1718749467693-00217-UneMJZVf&aff_fsk=UneMJZVf&aff_platform=aaf&sk=UneMJZVf&aff_trace_key=cf0879a328a44c42afd7b636f587dfdb-1718749467693-00217-UneMJZVf&terminal_id=bec40578c234405895a1646236025a60&afSmartRedirect=y)).
## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/malasiaa/intruder_detection.git
   cd intruder_detection
