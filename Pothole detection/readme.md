# Pothole Detection System using YOLOv4 Tiny

This repository contains a Python-based system for detecting potholes in a video stream using YOLOv4 Tiny object detection.

## Overview

The pothole detection system is designed to:

- Process a video stream or file input.
- Detect potholes in the video frames using YOLOv4 Tiny.
- Draw bounding boxes around detected potholes.
- Save images of detected potholes along with their coordinates.
- Display the frames per second (FPS) processed.

## Requirements

The system requires the following libraries and components:

- OpenCV (`cv2`)
- Geocoder
- Operating System (OS) module
- DateTime module

## Usage

1. Ensure that the necessary libraries are installed.
2. Configure the paths to the YOLOv4 Tiny weights, configurations, and label names (`obj.names`) in the Python script.
3. Set the input video source (file path or camera) in the script.
4. Run the Python script `pothole_detection.py`.
5. Press 'q' to stop the video stream and terminate the detection process.

## Files and Directory Structure

- `pothole_detection.py`: Main Python script for pothole detection.
- `obj.names`: Text file containing label names for the YOLOv4 Tiny model.
- `yolov4_tiny.weights`: YOLOv4 Tiny pre-trained weights file.
- `yolov4_tiny.cfg`: YOLOv4 Tiny configuration file.
- `result.avi`: Output video file with detected potholes.

## Parameters and Customization

- Adjust confidence and NMS thresholds for detection accuracy (`Conf_threshold`, `NMS_threshold`).
- Modify the output directory (`result_path`) for saving detected pothole images and coordinates.

## Notes

- Ensure CUDA and GPU support for faster processing if using GPU-enabled OpenCV.
- Fine-tune detection parameters for better accuracy based on specific scenarios and video quality.

## Contribution

Contributions to optimize, improve accuracy, or add new functionalities are welcome. Feel free to open issues or pull requests.

## License

This project is licensed under the [MIT License](LICENSE).
