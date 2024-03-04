# Face and Eye Detection with OpenCV

## Overview
This repository contains Python code for real-time face and eye detection using OpenCV's Haar cascades. The code captures video from the default camera, converts each frame to grayscale, and utilizes pre-trained Haar cascade classifiers to detect faces and eyes. Detected regions are highlighted with rectangles in the video stream.

## Features
- Real-time face detection: Utilizes Haar cascade for frontal face detection.
- Real-time eye detection: Applies a separate Haar cascade for eye detection.
- Video streaming: Captures video from the default camera and displays the output with highlighted face and eye regions.

## Dependencies
- OpenCV: The code relies on the OpenCV library for computer vision tasks.

## Usage
1. **Clone the repository:**
    ```bash
    git clone https://github.com/tusharm03/facial_rec.git
    ```
2. **Navigate to the project directory:**
    ```bash
    cd facial_rec.py
    ```
3. **Run the face detection script:**
    ```bash

    comment out which one you wan to run
    python facial_rec.py
    ```
4. **Run the eye detection script:**
    ```bash
    comment out which one you wan to run
    python facial_rec.py
    ```
5. **Press 'q' to exit the video stream.**

## Notes
- The Haar cascade XML files for face and eye detection should be present in the project directory or can be specified with the correct file paths in the scripts.

## Credits
- The face and eye Haar cascade classifiers are part of the OpenCV library.

Feel free to contribute, report issues, or use this code as a foundation for your computer vision projects. Happy detecting!
