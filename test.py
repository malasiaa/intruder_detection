import cv2

ip_camera_url = 'http://192.168.1.70/'  # Example URL

try:
    cap = cv2.VideoCapture(ip_camera_url, apiPreference=cv2.CAP_MSMF)
    
    if not cap.isOpened():
        raise IOError("Cannot open camera")

    cap.set(cv2.CAP_PROP_TIMEOUT_MS, 30000)

    while cap.isOpened():
        ret, frame = cap.read()

        if not ret:
            print("Cannot read frame")
            break

        cv2.imshow('Webcam', frame)

        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

except Exception as e:
    print(f"An error occurred: {str(e)}")

finally:
    cap.release()
    cv2.destroyAllWindows()
