import cv2
import numpy as np
from numpy.core.fromnumeric import resize
import pyautogui
import random
import platform
import os
import time

# here are all the haar cascades
# https://github.com/opencv/opencv/tree/master/data/haarcascades

# I --- Font and side haar cascades .xml files
faceCascade = cv2.CascadeClassifier("face_default.xml")
faceCascadeProfile = cv2.CascadeClassifier("faceProfile_extended.xml")
frontalFaceCloser = cv2.CascadeClassifier("frontalFaceCloser.xml")

# I -- Video capture device to use 
video_capture = cv2.VideoCapture(0)

time.sleep(3)

# It's in a while loop to keep the program running, so it's able to capture a face.
while True:
    # Capture frame-by-frame
    ret, frame = video_capture.read()
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    
    retval2,thresh1 = cv2.threshold(gray,70,255,cv2.THRESH_BINARY_INV+cv2.THRESH_OTSU)
    mask = np.zeros(thresh1.shape, dtype = "uint8") 
    img2 = cv2.bitwise_and(thresh1, mask)

    # I ----- Detect faces using the haar cascades .xml files
    faces = faceCascadeProfile.detectMultiScale(gray,
                                            scaleFactor=1.1,
                                            minNeighbors=10,
                                            minSize=(60, 60),
                                            flags=cv2.CASCADE_SCALE_IMAGE)

    faces_profile = faceCascade.detectMultiScale(gray,
                                            scaleFactor=1.1,
                                            minNeighbors=11,
                                            minSize=(30, 35),
                                            flags=cv2.CASCADE_SCALE_IMAGE)


    frontalFaceCloser_detect = frontalFaceCloser.detectMultiScale(gray,
                                            scaleFactor=1.1,
                                            minNeighbors=2,
                                            minSize=(40, 45),
                                            )

    
    

    # I ----- draw rectangles around front and profile face --- I

    for (x,y,w,h) in faces:
        cv2.rectangle(frame, (x, y), (x + w, y + h),(0,255,255), 2)
        # Display the resulting frame
    
    for (x,y,h,w) in faces_profile:
        cv2.rectangle(frame, (x, y), (x + w, y + h),(255,255,0), 1)

    
    for (x,y,h,w) in frontalFaceCloser_detect:
        cv2.rectangle(frame, (x, y), (x + w, y + h),(0,200,0), 1)


    # I -- Function for if the face is detected -- I


    # I -------- Check for face detected ---------- I
    if len(faces) or len(faces_profile) > 0:

        
        # take screenshot using pyautogui
        image = pyautogui.screenshot()
        
        # since the pyautogui takes as a 
        # PIL(pillow) and in RGB we need to 
        # convert it to numpy array and BGR 
        # so we can write it to the disk
        image = cv2.cvtColor(np.array(image),cv2.COLOR_RGB2BGR)
        try:
            os.mkdir(f"/home/{platform.node()}/Pictures/lockF")
        except:
            if FileExistsError:
                cv2.imwrite(f"/home/{platform.node()}/Pictures/lockF/screenS"+ str(random.randint(1,99)) + ".png", image)
            

    # -------------- Show the image ----------------
    width = 1110
    height = 900
    dim = (width, height)
    
    resized = cv2.resize(frame, dim, interpolation = cv2.INTER_AREA)
        
    cv2.imshow("Face tracking", resized)

    width = 400
    height = 320
    dim = (width, height)
    
    resized = cv2.resize(thresh1, dim, interpolation = cv2.INTER_AREA)

    cv2.imshow('BGR2GRAY', resized)


    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
video_capture.release()
cv2.destroyAllWindows()
