import cv2
import numpy as np
import pyrealsense2 as rs

# Configure depth and color streams
pipeline = rs.pipeline()
config = rs.config()

# Enable the depth stream with the desired format and resolution
config.enable_stream(rs.stream.depth, 640, 480, rs.format.z16, 15)

# Start streaming
pipeline.start(config)

# # Create filters
spatial = rs.spatial_filter()
temporal = rs.temporal_filter()
threshold = rs.threshold_filter(min_dist=0.2, max_dist=5)  # Set your desired minimum and maximum depth values here

try:
    while True:
        # Wait for a coherent pair of frames: depth and color
        frames = pipeline.wait_for_frames()
        depth_frame = frames.get_depth_frame()
        filtered_frame=depth_frame
        # Apply filters
        filtered_frame = threshold.process(filtered_frame)
        filtered_frame = spatial.process(filtered_frame)
        filtered_frame = temporal.process(filtered_frame)

        # Get metadata
        metadata = filtered_frame.get_frame_metadata(rs.frame_metadata_value.frame_timestamp)

        # Convert the filtered depth frame to a numpy array
        depth_image = np.asanyarray(filtered_frame.get_data())

        # Apply colormap to the depth image
        depth_colormap = cv2.applyColorMap(cv2.convertScaleAbs(depth_image, alpha=0.03), cv2.COLORMAP_JET)

        # Display the depth image
        cv2.imshow('Depth Image', depth_colormap)

        # Print metadata
        print("Frame Timestamp:", metadata)
        # Add more print statements for other metadata as needed

        # Break the loop if 'q' key is pressed
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

finally:
    # Stop streaming
    pipeline.stop()
    cv2.destroyAllWindows()
