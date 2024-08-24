import subprocess as sb_p
import tkinter as tk
from tkinter import *
from Admin import AdmLogin
from voter import voterLogin

def center_window(window):
    window.update_idletasks()
    width = window.winfo_width()
    height = window.winfo_height()
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width - width) // 2
    y = (screen_height - height) // 2
    window.geometry('{}x{}+{}+{}'.format(width, height, x, y))

def Home(root, frame1, frame2):
    for frame in root.winfo_children():
        for widget in frame.winfo_children():
            widget.destroy()

    frame2.configure(background="black")  # Set background color of frame2 to black

    Button(frame2, text="Home", command=lambda: Home(root, frame1, frame2), bg="blue", fg="white").pack(pady=10)
    Label(frame2, text="         ", bg="black").pack(side=LEFT)
    Label(frame2, text="         ", bg="black").pack(side=RIGHT)
    Label(frame2, text="").pack()

    root.title("Home")
    Label(frame1, text="Home", font=('Helvetica', 25, 'bold')).pack(pady=20)
    Label(frame1, text="").pack()

    admin = Button(frame1, text="Admin Login", width=15, command=lambda: AdmLogin(root, frame1), bg="green", fg="white")
    voter = Button(frame1, text="Voter Login", width=15, command=lambda: voterLogin(root, frame1), bg="orange", fg="white")
    newTab = Button(frame1, text="New Window", width=15, command=lambda: sb_p.call('start python homePage.py', shell=True), bg="red", fg="white")

    Label(frame1, text="").pack()
    admin.pack(pady=10)
    voter.pack(pady=10)
    newTab.pack(pady=10)

    frame1.pack(expand=True)
    frame2.pack()
    center_window(root)
    root.mainloop()

def new_home():
    root = Tk()
    root.geometry('500x500')
    root.configure(background="black")  # Set background color of root window to black
    frame1 = Frame(root, bg="black")  # Set background color of frame1 to black
    frame2 = Frame(root, bg="black")  # Set background color of frame2 to black
    Home(root, frame1, frame2)

if __name__ == "__main__":
    new_home()
