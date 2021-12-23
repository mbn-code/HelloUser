import random
import platform
import speech_recognition as sr


sr_version = sr.__version__

User_name = platform.node()

def script() -> None:
    print(f"Voice recognition version {sr_version}")
    print(f"Welcome {User_name} to the HelloUser script")



if __name__ == "__main__":
    script()