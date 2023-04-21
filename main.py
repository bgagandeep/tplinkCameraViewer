import cv2

# Replace the URL, username, and password below with your RTSP source URL, username, and password
url = 'rtsp://<username>:<password>@<rtsp_adress>'

# Create a VideoCapture object to read from the RTSP source
cap = cv2.VideoCapture(url)

# Loop over frames from the VideoCapture object
while True:
    ret, frame = cap.read()  # Read a frame from the VideoCapture object
    if ret:  # If the frame was read successfully
        cv2.imshow('RTSP Source', frame)  # Show the frame in a window named "RTSP Source"
        if cv2.waitKey(1) & 0xFF == ord('q'):  # If the 'q' key is pressed
            break  # Exit the loop
    else:  # If the frame could not be read
        break  # Exit the loop

# Release the VideoCapture object and destroy all windows
cap.release()
cv2.destroyAllWindows()
