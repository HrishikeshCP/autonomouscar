import cv2

def capture_from_multiple_cameras(cameras, window_titles, window_size=(640, 480)):
    # Create video capture objects for each camera
    cap_list = [cv2.VideoCapture(camera) for camera in cameras]

    if not all(cap.isOpened() for cap in cap_list):
        print("Error: One or more cameras could not be opened.")
        return

    # Create windows for each camera with a constant size
    for title in window_titles:
        cv2.namedWindow(title, cv2.WINDOW_NORMAL)
        cv2.resizeWindow(title, window_size[0], window_size[1])

    while True:
        frames = [cap.read()[1] for cap in cap_list]

        # Display frames from each camera
        for i, frame in enumerate(frames):
            cv2.imshow(window_titles[i], frame)

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # Release video capture objects and close windows
    for cap in cap_list:
        cap.release()

    cv2.destroyAllWindows()

# Camera indexes (you can change these according to your setup)
camera_indexes = [0, 3, 2]

# Window titles for each camera window
window_titles = ["Camera 1", "Camera 2", "Camera 3"]

# Set a constant window size
constant_window_size = (640, 480)

# Call the function to capture video from multiple cameras
capture_from_multiple_cameras(camera_indexes, window_titles, constant_window_size)
