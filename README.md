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

## Features
### The Drowsiness Detection System incorporates a set of key features to ensure accurate and timely identification of drowsiness, bolstering overall safety. 
+ Leveraging a webcam feed and the dlib library, the system conducts real-time drowsiness detection by calculating the eye aspect ratio. 
+ With facial landmarks extraction capabilities, utilizing the dlib library's 68-point landmark model, the system ensures precise spatial data, contributing to robust drowsiness detection. 
+ The alert mechanism is multi-faceted, triggering an immediate audible alarm through the pygame library upon detecting drowsiness. 
+ Simultaneously, the system sends an email notification with a snapshot of the drowsy moment to a designated recipient, facilitating detailed post-analysis. 
+ Configurability is a key aspect, allowing users to dynamically adjust parameters such as the eye aspect ratio threshold and the number of consecutive frames for detection, adapting the system to varying preferences and environmental conditions. 
+ Additionally, the system maintains a detailed log of each drowsiness detection instance, including timestamps and relevant details, while saving snapshots for comprehensive post-analysis and reporting. 
+ These features collectively position the system as a reliable tool for real-time monitoring, prompt alerting, and proactive prevention of potential risks associated with drowsy behavior.







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
## Results 
The Drowsiness Detection System has been successfully implemented and demonstrates robust performance in identifying signs of drowsiness in real-time. 
##### The key outcomes and results of the project include: <br>
+ The system effectively monitors facial landmarks and calculates the eye aspect ratio to determine the level of drowsiness and is accurately identified based on predefined thresholds for eye aspect ratio.
  Demo - <br>
  
  
    

  https://github.com/MonicaDasari/Driver-Drowsiness-Detection/assets/145815156/848c0335-d615-44b1-bd6c-0ab7bdb90938



+ The system provides real-time alerts when drowsiness is detected. An audible alarm is triggered simultaneously with the alert, ensuring immediate attention.
+ snapshot - <br>
  ![Drowsy Alert](https://github.com/MonicaDasari/Driver-Drowsiness-Detection/assets/145815156/328efb83-762d-4921-95a6-f6dedb3f9eb1)
  ![Email_Sent_Snapshot](https://github.com/MonicaDasari/Driver-Drowsiness-Detection/assets/145815156/fde4d4ff-a79d-4c81-ac3b-4ae9d3180f95) 
  ![Snapshots](https://github.com/MonicaDasari/Driver-Drowsiness-Detection/assets/145815156/b0335b00-3677-4f39-8d78-65c68ddfb4d3)

+ Upon detecting drowsiness, the system sends an email notification to a designated recipient.
+ The email notification includes a snapshot of the drowsy moment, aiding in further analysis <br> 
  ![Email_snapshot](https://github.com/MonicaDasari/Driver-Drowsiness-Detection/assets/145815156/75bfa348-2526-46fa-bc5b-1900278ac5f8)
  ![Email_snapshot_1](https://github.com/MonicaDasari/Driver-Drowsiness-Detection/assets/145815156/b49de64b-164c-41ce-a169-858bc1fb1ff3)

These results collectively showcase the effectiveness, reliability, and practicality of the Drowsiness Detection System in enhancing safety and preventing potential risks associated with drowsy behavior. Users can rely on the system as a valuable tool for real-time monitoring and timely intervention.



#### Feel free to contribute to the project and provide feedback!
