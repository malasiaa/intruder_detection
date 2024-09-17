import cv2

ip_camera_url = 'http://192.168.1.70'  # Example URL

# Open the video stream
cap = cv2.VideoCapture(0)

#cap = cv2.VideoCapture(0)
while cap.isOpened():
    ret, frame = cap.read()

    # show image 'Webcam' is the name atributed in the window
    cv2.imshow('Webcam', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Releases camera
#cap.release()
# Closes the frame
cv2.destroyAllWindows()


