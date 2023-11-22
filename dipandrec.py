import cv2

# Initialize the camera
cap = cv2.VideoCapture(1)  # 0 for the default camera, you can change it to the camera's index if you have multiple cameras

# Check if the camera opened successfully
if not cap.isOpened():
    print("Error: Could not open camera.")
    exit()

# Create a VideoWriter object to record the video (you can customize the codec and filename)
fourcc = cv2.VideoWriter_fourcc(*'XVID')  # Video codec, use XVID for AVI format
out = cv2.VideoWriter('output.avi', fourcc, 20.0, (640, 480))  # 'output.avi' is the output video file

while True:
    # Read a frame from the camera
    ret, frame = cap.read()

    if not ret:
        print("Error: Failed to grab a frame.")
        break

    # Write the frame to the output file
    out.write(frame)

    # Display the frame
    cv2.imshow('Camera Feed', frame)

    # Break the loop if 'q' is pressed
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

# Release the camera and output file
cap.release()
#out.release()

# Close all OpenCV windows
cv2.destroyAllWindows()
