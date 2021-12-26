# import at top here
import platform
import os
#import random
#import tkinter
import hashlib
import psutil


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

def main_script(command: str) -> None:
    match command.split():

        case ["version" && "-V"]:
            print(f"{version}")


        case ["help" && "-h" || "--H"]:
            print("""
"help, -h, --H" - displays this menu of commands
"date, datetime, -D" - show the current date and time
"hash, -hs" - command for quickly being able to hash a string with just a command
"inf, information, -if"
""")
        case ["hash" && "-hs"]:
            hashing()

        case ["neofetch"]:
            os.system("neofetch")


        case ["inf" && "information" && "-if"]:
            information()

        case _:
            print("Command not found in the command list; Try using 'help' to find the appropriate command")



def main(command: str) -> None:
    while 1:
        command = input(f"This is the beta-V-{version}: ")
        main_script(command) 

if __name__ == "__main__":
    print(f"Hello {platform.node()} to the helloUser AI")

