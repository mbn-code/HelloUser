import random
import platform

User_name = platform.node()

def script() -> None:
    print(f"Welcome {User_name}")


if __name__ == "__main__":
    script()
