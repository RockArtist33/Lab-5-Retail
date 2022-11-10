import tkinter as tk
import time
import matplotlib.pyplot as plt

window = tk.Tk()
window.geometry("600x400")
window.columnconfigure(0,weight = 1)
window.columnconfigure(1,weight = 1)
entry_name = tk.StringVar()
text1 = entry_name

def update():
    entry_name = entry.get()
    string_shown.config(text=entry_name)
    print(string_shown["text"])
    string_shown.grid(column = 1,row = 1)


string_shown = tk.Label(
    window,
    text= "",
    fg = "white",
    bg= "black",
    height = 2,
    font = ("fff forward", 20)
    )



entry = tk.Entry(
    textvariable= entry_name,
    width = 20
)

entry.grid(column = 0,row = 1)


Welcome = tk.Button(text="Python rocks!",
                   fg="black",
                   bg="white",
                   width = 20,
                   height = 2,
                   command =lambda: update()
                   )

Welcome.grid(column=0, row = 2)

window.mainloop()