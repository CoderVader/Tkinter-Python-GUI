import tkinter as tk
from tkinter import *
import webbrowser


win = tk.Tk()
win.title("Personal Web Browser")
win.geometry("500x300")


def google():
    webbrowser.open("www.google.com")

def amazon():
    webbrowser.open("www.amazon.com")


igoogle = PhotoImage(file="")
google = tk.Button(win,image=igoogle,command=google())
google.grid(row=0,column=0)

iamazon = PhotoImage(file="")
amazon = tk.Button(win,image=iamazon, command=amazon())
amazon.grid(row=0, column=0)


win.mainloop()