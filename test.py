import cv2

ip_camera_url = 'http://192.168.1.70'  # Example URL


try:
    cap = cv2.VideoCapture(ip_camera_url)
    cap.set(cv2.CAP_PROP_BUFFERSIZE, 1)  # Buffer size of 1 to reduce latency

    
    if not cap.isOpened():
        raise IOError("Cannot open camera")

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
