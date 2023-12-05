# Driver-Drowsiness-Detection
## Overview
This repository hosts code for a Drowsiness Detection System, employing facial landmarks and eye aspect ratio analysis. The system aims to identify signs of drowsiness by monitoring changes in the eyes' aspect ratio and promptly triggers an alert mechanism, including an email notification with a snapshot and an audible alarm, when drowsiness is detected.

## Technologies Used
+ Python
+ OpenCV
+ NumPy
+ imutils
+ pygame
+ dlib
+ smtplib

## Setup

1. #### Install the required dependencies using the following command: <br>
        pip install opencv-python numpy imutils pygame dlib

2.  #### Download the required haarcascade and shape predictor files: <br>
      * Haarcascade file: [haarcascade_frontalface_default.xml](https://github.com/opencv/opencv/blob/master/data/haarcascades/haarcascade_frontalface_default.xml) <br>
      * Shape predictor file: [shape_predictor_68_face_landmarks.dat](http://dlib.net/files/shape_predictor_68_face_landmarks.dat.bz2)

3. Place the downloaded files in the appropriate paths in the code. <br>
4. Set up your Gmail account for email notifications: <br>
   +  Enable "Less secure app access" in your Google Account settings
   +  Generate an "App Password" for the script
5. Update the script with your email credentials and adjust any configuration parameters if needed


## How to Run
##### Run the script using the following command: <br>
      python drowsiness_detection.py

## Acknowledgments
  +  The dlib library for facial landmarks extraction <br>
  +  OpenCV and imutils for image processing and video capture <br>
  +  pygame for audio alert <br>

#### Feel free to contribute to the project and provide feedback!
