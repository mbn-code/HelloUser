import platform
import os
import random
import hashlib
import psutil
from pathlib import Path



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
    os.system("python3 lockF.py")


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

