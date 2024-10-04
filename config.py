#-----flask script

# IPs allowed to send requests to flask server
# (Template IPs, replace with your IP camera's stream URL, and with you pc's IP if you desire)
ALLOWED_IPS = ['192.168.1.2', '192.168.1.3']  # change to "None" if any IP can send a request to flask server


#-----model function python

# telegram setup
TELEGRAM_bot_token = 'TELEGRAM:TOKEN'
TELEGRAM_chat_id = 'CHATID12342'

# Template IPs, replace with your IP camera's stream URL
IP_CAMERA_URL = 'http://192.168.1.2:80/stream'

# insert the path to the directory where images will be stored, classified with humans or not
OUTPUT_IMAGES_PATH = "output_images"
