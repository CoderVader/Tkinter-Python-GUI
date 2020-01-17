import tkinter as tk
from tkinter import *
import webbrowser


win = tk.Tk()
win.title("My Web Browser")
win.geometry("500x300")


def google():
    webbrowser.open("www.google.com")cd

def youtube():
    webbrowser.open("www.youtube.com")

def instagram():
    webbrowser.open("www.amazon.in")

igoogle = PhotoImage(file = "")
google = tk.Button(win,image=igoogle, command=google)
google.grid(row=0,column=0)



win.mainloop()