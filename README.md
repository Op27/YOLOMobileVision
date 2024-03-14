# YOLOMobileVision

## Overview
YOLOMobileVision leverages the YOLOv8 model to bring object detection and distance measurement capabilities directly to your mobile device. By simply using your mobile phone camera, you can detect objects in real-time and estimate their distance from the camera. This application is built on Ultralytics's YOLOv8 model and customized to make advanced computer vision techniques accessible and user-friendly for mobile users.

## Demo 
https://github.com/Op27/YOLOMobileVision/assets/39921621/8108ae75-d37b-4995-bf54-b99bd23aa1f5



## Features
- **Object Detection**: Detect various objects in the camera's field of view with high accuracy.
- **Distance Measurement**: Estimate the distance of detected objects from the camera.
- **Mobile Compatibility**: Designed specifically for use with mobile phone cameras.

## Getting Started
### Prerequisites
- A mobile phone with a camera.
- A mobile camera streaming app to stream your mobile camera feed a specific IP address to your computer. One option is to use 'DroidCam', which is widely available and user-friendly, free of charge. Please follow the instructions carefully to set up DroidCam on your device and ensure you protect your IP address from being exposed.


### Installation
1. Clone the repository to your local machine:
   ```bash
   git clone https://github.com/Op27/YOLOMobileVision.git
   ```
2. Install the required Python dependencies:
   ```bash
   pip install cv2-python
   pip install ultralytics
   pip install matplotlib
   ```
Make sure you have Python and pip installed on your system before running the above command.

### Setting Up Your Mobile Camera Stream
1. Install DroidCam on your mobile device and follow the setup instructions to start streaming your camera feed.
2. Ensure your mobile device and the computer running YOLOMobileVision are connected to the same network.
3. Upon setting up DroidCam, you will be provided with an IP address and port number. Enter this information into the 'camera_url' variable in the application code to connect the stream.
4. Handle your IP address with care to avoid unauthorized access to your device. Only use secure, trusted networks while streaming your camera feed.


### Usage
1. Set up your mobile phone to stream its camera feed to your computer.
2. Update the camera_url in the code to match your stream's IP address and port.
3. Run the application:
    ```bash
    python app.py
    ```
4. Point your mobile phone camera at objects to detect them and measure their real-time distance.

### Acknowledgements
Sincere gratitude to the YOLO team and Ultralytics for developing and maintaining the YOLOv8 model, which serves as the backbone of this YOLOMobileVision application. Their pioneering work in the field of computer vision has enabled me to create an application that brings object detection and distance measurement capabilities to mobile devices.

### Contributing
Your contributions to YOLOMobileVision are always welcome! 

### License
This project is licensed under the MIT License - see the LICENSE file for details.




