#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from scipy.spatial import distance
from imutils import face_utils
import numpy as np
import pygame
import time
import dlib
import cv2
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.base import MIMEBase
from email import encoders
from email.mime.text import MIMEText

pygame.mixer.init()
pygame.mixer.music.load('audio/alarm.mp3')

EYE_ASPECT_RATIO_THRESHOLD = 0.25
EYE_ASPECT_RATIO_CONSEC_FRAMES = 50
COUNTER = 0

face_cascade = cv2.CascadeClassifier("sources/haarcascade_frontalface_default.xml")

def eye_aspect_ratio(eye):
    A = distance.euclidean(eye[1], eye[5])
    B = distance.euclidean(eye[2], eye[4])
    C = distance.euclidean(eye[0], eye[3])
    ear = (A + B) / (2 * C)
    return ear


def send_email_alert(sender_email,receiver_email,password,snapshot_filename):
    subject = "Drowsiness Alert!"
    body = "The person is drowsy. Please check."
    msg = MIMEMultipart()
    msg['From'] = sender_email
    msg['To'] = receiver_email
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))
    # Attach the snapshot to the email
    with open(snapshot_filename, 'rb') as attachment:
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            'Content-Disposition',
            f'attachment; filename= {snapshot_filename}',
        )
        msg.attach(part)
        try:
            server = smtplib.SMTP('smtp.gmail.com', 587)
            server.starttls()
            server.login(sender_email, password)
            server.sendmail(sender_email, receiver_email, msg.as_string())
            print("Email notification sent successfully!")
            server.quit()
        except Exception as e:
            print(f"Failed to send email notification: {e}")

            
detector = dlib.get_frontal_face_detector()
predictor = dlib.shape_predictor('shape_predictor_68_face_landmarks.dat')

(lStart, lEnd) = face_utils.FACIAL_LANDMARKS_IDXS['left_eye']
(rStart, rEnd) = face_utils.FACIAL_LANDMARKS_IDXS['right_eye']

video_capture = cv2.VideoCapture(0)
time.sleep(2)

# Email configurations
sender_email = 'from_mail@yourexample.com'  
receiver_email = 'receiver_mail@yourexample.com'  
password = 'your password'  

# Initialize variables for dynamic threshold 
dynamic_threshold = EYE_ASPECT_RATIO_THRESHOLD  # Initialize with default threshold

while True:
    ret, frame = video_capture.read()
    frame = cv2.flip(frame, 1)
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    faces = detector(gray, 0)
    face_rectangle = face_cascade.detectMultiScale(gray, 1.3, 5)

    for (x, y, w, h) in face_rectangle:
        cv2.rectangle(frame, (x, y), (x + w, y + h), (255, 0, 0), 2)

    for face in faces:
        shape = predictor(gray, face)
        shape = face_utils.shape_to_np(shape)

        leftEye = shape[lStart:lEnd]
        rightEye = shape[rStart:rEnd]

        leftEyeAspectRatio = eye_aspect_ratio(leftEye)
        rightEyeAspectRatio = eye_aspect_ratio(rightEye)
        eyeAspectRatio = (leftEyeAspectRatio + rightEyeAspectRatio) / 2

        leftEyeHull = cv2.convexHull(leftEye)
        rightEyeHull = cv2.convexHull(rightEye)

        cv2.drawContours(frame, [leftEyeHull], -1, (0, 255, 0), 1)
        cv2.drawContours(frame, [rightEyeHull], -1, (0, 255, 0), 1)

        if eyeAspectRatio < dynamic_threshold:
            COUNTER += 1
            if COUNTER >= EYE_ASPECT_RATIO_CONSEC_FRAMES:
                pygame.mixer.music.play()
                cv2.putText(frame, "Drowsy!!", (150, 200),
                            cv2.FONT_HERSHEY_SIMPLEX, 1.5, (0, 0, 255), 2)
                
                # Save a snapshot
                # Folder path to save the snapshots
                snapshot_folder = 'Drowsiness Snapshots/'
                snapshot_filename = f'{snapshot_folder}drowsy_snapshot_{time.strftime("%Y%m%d%H%M%S")}.png'
                cv2.imwrite(snapshot_filename, frame)
                print(f"Snapshot saved: {snapshot_filename}")
                
                # Send email notification
                send_email_alert(sender_email,receiver_email,password,snapshot_filename)
                
                pygame.mixer.music.stop()
                COUNTER = 0

    cv2.imshow('Video', frame)

    if cv2.waitKey(1) & 0xFF == ord('q'):
        break

video_capture.release()
cv2.destroyAllWindows()


# In[ ]:




