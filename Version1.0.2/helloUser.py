import platform
import os
import hashlib
import psutil
import time
import sys
from time import sleep
# Can't use pyautogui because python3.10 doesn't support tk yet I think
# import pyautogui


version = "BETA-V1.2"
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

# This is a part of the math commands listed in the README.md file
def FibNums():
    global amount
    amount = input("Fibonacci numbers to print: ")
    
    print(f"Printing the first {amount} of fibonacci numbers")
    def printFibonacciNumbers(n: int) -> None:
        # +1 if n == 1
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

# This is a part of the security commands as listed in the README.md
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
        
        case ["cutter", file_path]:
            print(f"Starting {file_path} in {command}")
            os.system(f"sudo cutter {file_path}")

        case ["msfconsole"]:
            char_var = "Please wait for msfconsole to start.. \n"
            for char in char_var:
                sleep(0.015)
                sys.stdout.write(char)
                sys.stdout.flush()
            os.system("msfconsole")

        case ["ip" | "ipinfo", ip]:
            os.system(f"curl ipinfo.io/{ip}")
            print("\n")

        case ["open"]:
            if platform == "win32":
                pass
            if platform == "linux" or "linux2":
                pass
            if platform == "darwin":
                pass


        case ["hash" | "-hs"]:
            hashing()

        case ["base58", path]:
            if path == None:
                print(f"No file {path}")
            else:
                os.system(f"base58 {path}")

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
        
        case ["file" | "-fl", file_path]:
            os.system(f"file {file_path}")

        case ["cd", path]:
            if path == None:
                print(f"No directory {path}")
            else: 
                os.chdir(str(path))


        # Using built in tool into parrot os, this allows for subdomain to ip and domain to ip 
        case ["d2ip", domain, *rest]:
            if "-d" in rest:
                os.system(f"ping {domain} -c 1")
            elif "-s" in rest:
                os.system(f"dnsmap {domain} -d 200")
            else:
                d2ip = input("Enter domain to ping: ")
                os.system(f"ping {d2ip} -c 1")

        # Because this is a system command don't need to add a lot of if "rest" 
        # Because it will just add whatever you put at the end to the input
        case ["dig" | "-dg", domain_ip, *rest]:
            if "-v" in rest:
                print("Version tag enabled")
                os.system(f"dig {domain_ip} -v")            
            else: 
                os.system(f"dig {domain_ip}")
        
        case ["-ws", domain_ip]:
            os.system(f"whois {domain_ip}")

        case ["activate" | "ac", *rest]:
            if "lock" in rest:
                script_lock()

            if "blackout" in rest:
                print("Blackout mode enabled")
                os.system("python3 blackout.py")
            
            if "bl" in rest:
                print("Blackout mode enabled")
                os.system("python3 blackout.py")

            if "lockdown" in rest:
                print("Activating lockdown mode")
                os.system("python3 lockdown.py")

            if "ld" in rest:
                print("Activating lockdown mode")
                os.system("python3 lockdown.py")


            elif "-l" in rest:
                print("""
-l
lock - Uses face recognition to detect if someone is looking at your pc whilst your gone, and snaps a screenshot
camera - Opens the camera
blackout - Open a window that covers the whole screen (Keybin: Ctrl + c + move mouse after to close blackout feature) 
lockdown - Closes all windows ()
""")
            else:
                do_var = "Do 'activate -l' to see the list of things to activate\n"
                for char in do_var:
                    sleep(0.020)
                    sys.stdout.write(char)
                    sys.stdout.flush()

        case ["exit" | "quit" | "stop"]:
            exit_ask = input("Are you sure you want to quit?: ")
            if exit_ask.lower() == "y" or "yes":
                word_quit = "Quitting"
                for char in word_quit:
                    sleep(0.030)
                    sys.stdout.write(char)
                    sys.stdout.flush()
                word_dot = ".."
                for char2 in word_dot:
                    sleep(0.2)
                    sys.stdout.write(char2)
                    sys.stdout.flush()
                quit()
            elif exit_ask.lower() == "n" or "no":
                print(f"Returning to CLI-{version}...")
                pass

        case _:
            os.system(command)

def main():
    while 1:
        command = input(f"{platform.node()} {CRED} helloUser-V-{version}§ ")
        main_script(command) 
        
if __name__ == "__main__":
    global CRED
    CRED = "\030"
    welcome_string = f"Hello {platform.node()} to the helloUser AI : -h for help\n" 
    for char in welcome_string:
        sleep(0.020)
        sys.stdout.write(char)
        sys.stdout.flush()
    main()