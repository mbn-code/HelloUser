import platform
import os
import hashlib
import psutil
import time
import sys
import speech_recognition as sr
from time import sleep

version = "BETA-V1.2"

def recognize_speech():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        print("Listening...")
        audio = r.listen(source)
    try:
        text = r.recognize_google(audio)
        print("You said:", text)
        return text.lower()
    except sr.UnknownValueError:
        print("Could not understand audio.")
    except sr.RequestError as e:
        print("Could not request results from Google Speech Recognition service; {0}".format(e))
    return ""

def information():
    print(f"""
ToolKit-Version: {version}
Computer name: {platform.node()}
OS Version: {platform.version()}
Release : {platform.release()}
Arch: {platform.machine()}
Py Compiler: {platform.python_compiler()}
Processor: {platform.processor()}
Ram: {str(round(psutil.virtual_memory().total / (1024 ** 3))) + " GB"}
""")

def FibNums():
    global amount
    amount = input("Fibonacci numbers to print: ")

    print(f"Printing the first {amount} of fibonacci numbers")

    def printFibonacciNumbers(n: int) -> None:
        n += 1
        f1 = 0
        f2 = 1
        if n < 1:
            return
        print(f1)
        for x in range(1, n):
            print(f2)
            next = f1 + f2
            f1 = f2
            f2 = next
            print("-" * 50 + f" num: {x}")

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
"dig, -dg" - Use the network tool dig in the hello Terminal
"whois, -ws" - Use the whois command to get information about a domain or ip
"File" - Determine file type
"msfconsole" - starts the popular metasploit-framework console
"base58" - Encodes a file path in base58
"Open" - Not finished - Executes a program
"ip, ipinfo" - Get detailed information on an ip address (only ip address)
"d2ip" - Convert domain to ip, both for TLD, and Subdomains
""")

        # Rest of the code...

def main():
    while True:
        command = recognize_speech()  # Use voice recognition to get the command
        print(f"Recognized command: {command}")
        if command:
            main_script(command)
        else:
            print("No command recognized.")

if __name__ == "__main__":
    global CRED
    CRED = "\030"
    welcome_string = f"Hello {platform.node()} to the helloUser AI : -h for help\n"
    for char in welcome_string:
        sleep(0.020)
        sys.stdout.write(char)
        sys.stdout.flush()
    main()
