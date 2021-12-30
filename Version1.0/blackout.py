from tkinter import * 

root = Tk()
root.title("blackout")

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()
root.geometry(f"{screen_width}x{screen_height}")
root.resizable(height=False, width=False)
root.overrideredirect(True)


root.mainloop()