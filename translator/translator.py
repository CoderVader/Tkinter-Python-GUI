import tkinter as tk
from googletrans import Translator

win = tk.Tk()
win.title("Translator")
win.geometry("400x160")

def translation():
    word = entry.get()
    translator = Translator(service_urls=['translate.google.com'])
    translation1 = translator.translate(word, dest = "es")

    label1 = tk.Label(win,text=f"Translated in Spanish : {translation1.text}",bg="yellow")
    label1.grid(row=2,column=0)

# Title
label = tk.Label(win,text = "Enter a word: ")
label.grid(row=0, column=0, sticky="W")cd

#Input Field
entry = tk.Entry(win)
entry.grid(row=1, column=0)

# button
button = tk.Button(win,text="Translate", command=translation)
button.grid(row=1, column=2)

win.mainloop()
