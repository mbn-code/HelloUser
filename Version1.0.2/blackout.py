from time import sleep
from tkinter import *

def show_features():
    feature1 = Label(root, text="feature01").grid(row=2,column=2, padx=20)
    feature2 = Label(root, text=f"feature02").grid(row=2,column=3, padx=20)
    feature3 = Label(root, text=f"feature03").grid(row=2,column=4, padx=20)

    feature1_button = Button(root, text="feature1").grid(row=3, column=2, padx=20)
    feature2_button = Button(root, text="feature2").grid(row=3, column=3, padx=20)
    feature3_button = Button(root, text="feature3").grid(row=3, column=4, padx=20)

root = Tk()
root.title("blackout")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(height=False, width=False)
root.overrideredirect(True)
root.config(bg="black")

space_padding = Label(root, text="", bg="black").grid(padx=50, pady=50)
welcome_label = Label(root, text="Blackout feature enabled.", fg="white", bg="black", font="italic, 20").grid(padx=30, pady=30, column=1, row=1)

show_features = Button(root, text="Show blackout features", borderwidth=0, command=show_features).grid(column=1, row=2)


root.mainloop()