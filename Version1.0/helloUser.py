import platform
import os
#import random
import hashlib
from types import TracebackType
import psutil
#import ctypes
import time
# Getting the screen resolution for the monitor
#user32 = ctypes.windll.user32
#sc1 = user32.GetSystemMetrics(0)
#sc2 = user32.GetSystemMetrics(1)

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


def FibNums():
    global amount
    amount = input("Fibonacci numbers to print: ")
    
    print(f"Printing the first {amount} fibonacci numbers")
    def printFibonacciNumbers(n: int) -> None:
        # Check for n == 1 and + 1 if true
        n==1;n+=1                      
        f1 = 0
        f2 = 1
        if (n < 1):
            return
        print(f1)
        for x in range(1, n):
            print(f2)
            next = f1 + f2
            f1 = f2
            f2 = next
            print("-"*50 + f" num: {x}")
    printFibonacciNumbers(int(amount))

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

    def choose():
        if hashinput == None:
            print("Enter valid hashtype")
        elif which_hash_type.lower() == "md5":
            md5_hash(data=hashinput)
        elif which_hash_type.lower() == "sha1":
            sha1_hash(data=hashinput)
        elif which_hash_type.lower() == "sha256":
            sha256(data=hashinput)
        elif which_hash_type.lower() == "sha512":
            sha512(data=hashinput)

    if __name__ == "__main__":
        choose()

def script_lock():
    print("Activated lock feature")
    os.system(f"python3 /home/{platform.node()}/Documents/helloUser/HelloUser/Version1.0/lockF.py")

def main_script(command: str) -> None:
    match command.split():

        case ["version" | "-V"]:
            print(f"{version}")


        case ["help" | "-h" | "--H"]:
            print("""
"help, -h, --H" - displays this menu of commands
"date, datetime, -D" - show the current date and time
"hash, -hs" - command for quickly being able to hash a string with just a command
"inf, information, -if" - get hardware and network information 
"activate, ac" -> lock, camera, blackout - The activate function has paraments which can be activated with the activate command. 
"cd" - Change directory
"ls, ll, l" - list things in current directory
"neofetch" - display simple local computer specs
"base64, bs"- Encodes whatever text is in a file into base64, and outputs to terminal
"fib, fibonacci" - Print amount of fibonacci numbers from a given value 
""")
        case ["hash" | "-hs"]:
            hashing()

        case ["base64", "bs", path]:
            if path == None:
                print(f"No file or directory {path}")
            else:
                os.system(f"base64 {path}")

        case ["fib" | "fibonacci"]:
            FibNums()

        case ["neofetch"]:
            os.system("neofetch")

        case ["inf" | "information" | "-if"]:
            information()

        case ["ls" | "ll" | "l"]:
            os.system("ls")
        
        case ["time"]:
            current_time = time.strftime("%Y-%m-%d %H:%M:%S", time.localtime(time.time()))
            print(f"Current date and time {current_time}")
        
        case ["cd", path]:
            if path == None:
                print(f"No directory {path}")
            else: 
                os.chdir(str(path))

        case ["exit" | "quit" | "stop"]:
            quit()

        case ["activate" | "ac", *rest]:
            if "lock" in rest:
                script_lock()
            elif "camera" in rest:
                import cv2

                cap = cv2.VideoCapture(0)

                if not cap.isOpened():
                    raise IOError("Cannot open webcam")

                while True:
                    ret, frame = cap.read()
                    frame = cv2.resize(frame, None, fx=0.5, fy=0.5, interpolation=cv2.INTER_AREA)
                    cv2.imshow('Input', frame)

                    c = cv2.waitKey(1)
                    if c == 27:
                        break

                cap.release()
                cv2.destroyAllWindows()

            #elif "blackout" or "bl" in rest:
            #    print("Currently not able to use tkinter in python3.10")

            elif "-l" in rest:
                print("""
-l
lock - Uses face recognition to detect if someone is looking at your pc whilst your gone, and snaps a screenshot
camera - Opens the camera
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
    for i in range(20):
        command = input(f"beta-V-{version}§ ")
        main_script(command) 

if __name__ == "__main__":
    print(f"Hello {platform.node()} to the helloUser AI : -h for help")
    main()

