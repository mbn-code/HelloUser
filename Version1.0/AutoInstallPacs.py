# This is the main script for automatically installing all the pip3 packages and deb/pacman/dnf or yum packages.
import os

def script():
    distro_var = input("Which package manager are you using(apt,pacman,dnf,yum)?: ")
    
    if distro_var.lower() == "apt":
        # install the apt packages 
        os.system("sudo apt install base58 cutter file dig whois")
        # moduels that need to be installed
        os.system("pip3.10 install hashlib psutil")

    if distro_var.lower() == "pacman":
        os.system("sudo pacman -S base58 cutter file dig whois")

        os.system("pip3.10 install hashlib psutil")

    if distro_var.lower() == "dnf":
        os.system("sudo dnf install base58 cutter file dig whois")
        os.system("pip3.10 install hashlib psutil")

    if distro_var.lower() == "yum":
        os.system("sudo yum install base58 cutter file dig whois")
        os.system("pip3.10 install hashlib psutil")



if __name__ == "__main__":
    script()


