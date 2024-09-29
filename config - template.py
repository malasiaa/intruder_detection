#-----flask script

# IPs allowed to send requests to flask server
# These are template IPs
ALLOWED_IPS = ['192.168.69.69', '192.168.69.70']  # change to "None" if any IP can send a request 


#-----model function python

# telegram setup
TELEGRAM_bot_token = 'TELEGRAM:TOKEN'
TELEGRA_chat_id = 'CHATID12342'

# Replace with your IP camera's stream URL
IP_CAMERA_URL = 'http://192.168.69.71:80/stream'

# insert the path to the directory where images will be stored, classified with humans or not
OUTPUT_IMAGES_PATH = "output_images"
