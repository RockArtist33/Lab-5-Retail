# Import the required libraries
from tkinter import *
from tkinter import ttk

# Create an instance of tkinter frame
win=Tk()

# Set the size of the tkinter window
win.geometry("700x350")

# Create an instance of Style widget
style=ttk.Style()
style.theme_use('clam')

# Add a Treeview widget
tree=ttk.Treeview(win, column=("c1", "c2"), show='headings', height=8)
tree.column("# 1",anchor=CENTER, stretch=NO, width=100)
tree.heading("# 1", text="ID")
tree.column("# 2", anchor=CENTER, stretch=NO)
tree.heading("# 2", text="Programming Language")

# Insert the data in Treeview widget
tree.insert('', 'end',text="1",values=('1','C++'))
tree.insert('', 'end',text="2",values=('2', 'Java'))
tree.insert('', 'end',text="3",values=('3', 'Python'))
tree.insert('', 'end',text="4",values=('4', 'Golang'))
tree.insert('', 'end',text="5",values=('5', 'JavaScript'))
tree.insert('', 'end',text="6",values=('6', 'C# '))
tree.insert('', 'end',text="7",values=('6', 'Rust'))
tree.insert('', 'end',text="8",values=('6', 'SQL'))

tree.pack()
win.mainloop()