import tkinter as tk
import matplotlib.pyplot as plt

window = tk.Tk()

def plt_plot():
    x = [1,3,5,7,9]
    y = [3,6,9,12,18]
    plt.scatter(x,y)
    plt.fill_between(x,y[2])
    plt.show()

Welcome = tk.Button(text="Python rocks!",
                   fg="black",
                   bg="white",
                   width = 50,
                   height = 20,
                   command = plt_plot
                   ).pack()

window.mainloop()