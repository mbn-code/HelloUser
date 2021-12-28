import platform
import os
#import random
import hashlib
import psutil
#import ctypes

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
"inf, information, -if" - get hardware and network information 
"activate, ac" -> lock, camera, blackout - The activate function has paraments which can be activated with the activate command. 
"cd" - Change directory
"ls, ll, l" - list things in current directory
"neofetch" - display simple local computer specs
""")
        case ["hash" | "-hs"]:
            hashing()

        case ["neofetch"]:
            os.system("neofetch")

        case ["inf" | "information" | "-if"]:
            information()

        case ["ls" | "ll" | "l"]:
            os.system("ls")
        
        case ["cd", path]:
            if path == None:
                print(f"No directory {path}")
            else: 
                os.chdir(str(path))

        case ["exit", "quit", "stop"]:
            os.system("exit")

        case ["activate" | "ac", *rest]:
            if "lock" in rest:
                script_lock()
            elif "camera" in rest:
                # try to read the file if it's existing
                # If it's not, write a 0 to the file, to let the program know that cheese is not installed
                # Then if the file exists read the file and check if the file line is a 1 or 0
                # If 1, start cheese via terminal, if 0 try automatically installing cheese.
                

                path = "~bin/cheese"
                if os.path.isfile(path) == False:
                    with open("check_cheese.txt", "w") as write_1:
                        write_1.write("1")

                    print("Checking if cheese is installed to the system")

                    packman_ask = input("Are you running dnf, apt or pacman?: ")
                    if packman_ask.lower() == "apt":
                        os.system("sudo apt install cheese")

                    if packman_ask.lower() == "pacman":
                        os.system("sudo pacman -S cheese")

                    if packman_ask.lower() == "dnf":
                        ask_fandora_version = input("Are you running Fadora '22' or later, or '21' and older?")
                        if ask_fandora_version.lower() == "22":
                            os.system("sudo dnf install cheese")

                        elif ask_fandora_version.lower() == "21":
                            os.system("sudo yum install cheese")
                elif os.path.isfile(path):
                    os.system("cheese")

            elif "blackout" or "bl":
                print("Currently not able to use tkinter in python3.10")

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

