# import at top here
import platform
import os
import random
#import tkinter
import hashlib
import psutil
from pathlib import Path
import cv2
import numpy as np
from numpy.core.fromnumeric import resize
import pyautogui


version = "BETA-V1.1"
def information():
    print(f"""
ToolKit-Version: {version}
Computer name: {platform.node()}
OS Version: {platform.version()}
Release : {platform.release()}
Arch: {platform.machine()}
Py Compiler: {platform.python_compiler()}
Processor: {platform.processor()}
Ram: {str(round(psutil.virtual_memory().total / (1024 ** 3)))+ " GB"}
""")


def hashing():
    print("hashing types:")
    print("md5\nsha1\nsha256\nsha512")


    which_hash_type = input("Which hash type do you want to hash your string in?: ")

    hashinput = input("plain text: ")

def md5_hash(data):
    hash_object = hashlib.md5()
    hash_object.update(str(data).encode())
    print("hash ", hash_object.hexdigest())


def sha1_hash(data):
    hash_object = hashlib.sha1()
    hash_object.update(str(data).encode())
    print("hash ", hash_object.hexdigest())

def sha256(data):
    hash_object = hashlib.sha256()
    hash_object.update(str(data).encode())
    print("hash ", hash_object.hexdigest())


def sha512(data):
    hash_object = hashlib.sha512()
    hash_object.update(str(data).encode())
    print("hash ", hash_object.hexdigest())        

def script_lock():
    print("Activated lock feature")
    # This is a script and is meant to be run with the following cascades:
    # frontalFaceCloser
    # face_default
    def script():

        # here are all the haar cascades
        # https://github.com/opencv/opencv/tree/master/data/haarcascades

        # I --- Font and side haar cascades .xml files
        faceCascade = cv2.CascadeClassifier("face_default.xml")
        faceCascadeProfile = cv2.CascadeClassifier("faceProfile_extended.xml")

        frontalFaceCloser = cv2.CascadeClassifier("frontalFaceCloser.xml")

        # I -- Video capture device to use 
        video_capture = cv2.VideoCapture(0)

        import time

        time.sleep(5)

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
    if __name__ == "__main__":
        script()

def main_script(command: str) -> None:
    match command.split():

        case ["version" | "-V"]:
            print(f"{version}")


        case ["help" | "-h" | "--H"]:
            print("""
"help, -h, --H" - displays this menu of commands
"date, datetime, -D" - show the current date and time
"hash, -hs" - command for quickly being able to hash a string with just a command
"inf, information, -if"
""")
        case ["hash" | "-hs"]:
            hashing()

        case ["neofetch"]:
            os.system("neofetch")

        case ["inf" | "information" | "-if"]:
            information()

        case ["ls" | "ll"| "l"]:
            os.system("ls")
            
        case ["activate", *rest]:
            if "lock" in rest:
                script_lock()
            elif "-l" in rest:
                print("""
-l
lock - Uses face recognition to detect if someone is looking at your pc whilst your gone, and snaps a screenshot.
""")
            else:
                print("Do 'activate -l' for things to activate")

        case _:
            os.system(command)
            command_list = ["version","help","hash","neofetch","information"]
            for command_ in command_list:
                if command_ != command: 
                    if platform == "linux" or platform == "linux2":
                        print("Linux operating system detected:")
                        print("Try installing the command via 'apt', 'pacman' or 'dnf' depending on your distrobution")
                        break
                    elif platform == "darwin":
                        print("OS X detected:")
                        print("Try installing the command with brew")
                        break
                    elif platform == "win32":
                        print("Windows / linux detected:")
                        print("Try installing the command via 'apt' or 'pacman' depending on package manager")
                        break

def main():
    while 1:
        command = input(f"beta-V-{version}! ")
        main_script(command) 

if __name__ == "__main__":
    main()
    print(f"Hello {platform.node()} to the helloUser AI")

