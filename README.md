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
- OpenCV
- Flask
- Requests
- Telegram Bot API

## Installation

1. Clone the repository:

   ```bash
   git clone https://github.com/malasiaa/intruder_detection.git
   cd intruder_detection
