# import voice recognition - Imports the voice recognition module

import os
import datetime
# import the voice recognition module 
import voice_recognition as vr

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

def script_lock():
    print("Locking")
    os.system("python3 lock.py")

# voice recognition 
def voice_rec():
    # Voice recognition
    # Recognizes the voice input
    # Returns the voice input
    voice_rec = vr.Recognizer()
    # Listens for the voice input
    with vr.Microphone() as source:
        print("Listening...")
        audio = voice_rec.listen(source)
    # Converts the voice input to text
    voice_input = voice_rec.recognize_google(audio)
    print(f"You said: {voice_input}")
    
    if voice_input == "lock":
        script_lock()
    elif voice_input == "fibonacci":
        FibNums()
    elif voice_input == "date":
        print(datetime.datetime.now())
    elif voice_input == "time":
        print(datetime.datetime.now())
    elif voice_input == "hello":
        print("Hello")
    elif voice_input == "bye":
        print("Bye")
    elif voice_input == "exit":
        print("Exiting")
        exit()
    else:
        print("Command not recognized")
        voice_rec()
    


if __name__ == "__main__":
    voice_rec()