import easygui
import os
import tkinter as tk
import tkinter.ttk as ttk
import pandas as pd

window = tk.Tk()
window.resizable(False, False)
window.columnconfigure(0, weight=1)
window.columnconfigure(1, weight=1)
entry_name = tk.StringVar()
entry_name1 = tk.StringVar()
entry_name2 = tk.StringVar()

window.title("table: ")

x = 0

x1 = 0
y1 = 0
x2 = 0
y2 = 0


def button_make(windowvar, text, command, x, y):
    button_temp = tk.Button(
        windowvar,
        text=text,
        command=command
    )
    button_temp.place(x=x, y=y)
    return button_temp


def Entry_make(windowvar, input_var, x, y):
    Entry_temp = tk.Entry(
        windowvar,
        textvariable=input_var
    )
    Entry_temp.place(x=x, y=y)
    return Entry_temp


def Label_make(windowvar, text, x, y):
    Label_Temp = tk.Label(
        windowvar,
        text=text
    )
    Label_Temp.place(x=x, y=y)
    return Label_Temp


def show_table():
    global tree, scroll1, scrollbar
    columns = list(testdf2.columns)
    tree = ttk.Treeview(window, height=10, selectmode="browse")
    tree.configure(columns=columns)
    tree.column("# 0", anchor="w", width=40)
    for index in columns:
        tree.column(index, anchor="w", width=100)
        tree.heading(index, text=index, anchor="w")

    for ind, rows in testdf2.iterrows():
        tree.insert("", 0, text=ind, values=list(rows))

    scroll1 = ttk.Scrollbar(
        window,
        orient="vertical",
        command=tree.yview
    )
    tree.configure(yscrollcommand=scroll1.set)

    # tree.grid(column=2, row=0, rowspan=10)
    tree.place(x=100, y=0)
    scroll1.place(x=100 + 42 + (100 * len(testdf.columns)), y=0, height=window.winfo_height() + 26)
    scrollbar = tk.Scrollbar(window, orient="horizontal", command=tree.xview)
    tree.configure(xscrollcommand=scrollbar.set)
    scrollbar.place(x=(150 + 40), y=window.winfo_height() + 30, width=((100 * len(testdf.columns)) - 150))

    print(str(300 + (100 * len(testdf.columns))) + "x" + str(window.winfo_height() + 100))
    window.geometry(str(200 + (100 * len(testdf.columns))) + "x" + str(250))


def hide_table():
    # os.system('python main2.py')
    tree.destroy()
    scroll1.destroy()
    scrollbar.destroy()


def new_window():
    def top2():
        def update():
            global testdf2
            testdf.iloc[index_n.get(), col_name.get()] = textvars.get()
            testdf2 = testdf.iloc[::-1]
            tree.destroy()
            scroll1.destroy()
            scrollbar.destroy()
            show_table()
            popup2.destroy()

        textvars = tk.StringVar()
        top.destroy()

        popup2 = tk.Toplevel(window)
        popup2.resizable(False, False)
        popup2.geometry = ("350x100")
        current_val = "current cell value = {}".format(testdf.iloc[index_n.get(), col_name.get()])

        Label_make(popup2, current_val, 10, 10)
        Entry_make(popup2, textvars, 10, 40)
        button_make(popup2, "Update", update, 10, 70)

    top = tk.Toplevel(window)
    top.resizable(False, False)
    top.geometry("335x100")
    top.title("Change Data")
    index_n = tk.IntVar()
    col_name = tk.IntVar()

    Label_make(top, "Enter the index number of the row:", 10, 10)
    Entry_make(top, index_n, 200, 10)
    Label_make(top, "Enter the column number:", 10, 40)
    Entry_make(top, col_name, 160, 40)
    button_make(top, "Press to view Cell", top2, 10, 70)


def check_exists(label11):
    x = label11.winfo_exists()
    return x


def add_table():
    global testdf, testdf2, entry_name
    x = pd.Series([entry_name.get(), entry_name1.get(), entry_name2.get()], index=testdf.columns)
    testdf.loc[len(testdf)] = x
    testdf2 = testdf.iloc[::-1]

    tree.destroy()
    scroll1.destroy()
    scrollbar.destroy()
    show_table()


def Table_manipulate():
    top = tk.Toplevel()
    top.title("Change the Table")
    top.geometry("200x200")
    top.resizable(False, False)

    button_make(top, "Add column", col_add, 10, 10)
    button_make(top, "Remove column", col_rmv, 90, 10)
    button_make(top, "Add row", row_add, 10, 50)
    button_make(top, "Remove row", row_rmv, 69, 50)
    button_make(top, "Change column", col_change, 10, 90)


def row_add():
    global testdf2
    testdf.loc[len(testdf.index)] = " "
    testdf2 = testdf.iloc[::-1]
    tree.destroy()
    scroll1.destroy()
    scrollbar.destroy()
    show_table()


def row_rmv():
    def rem():
        global testdf, testdf2, tree
        testdf.drop(index=var.get(), inplace=True)
        testdf.reset_index(drop=True, inplace=True)
        testdf2 = testdf.iloc[::-1]
        tree.destroy()
        scroll1.destroy()
        scrollbar.destroy()
        show_table()

    var = tk.IntVar()
    top = tk.Toplevel()
    top.title("Row removal")
    top.geometry("250x100")
    top.resizable(False, False)
    Label_make(top, "Enter Row Num:", 10, 10)
    Entry_make(top, var, 100, 10)
    button_make(top, "Delete", rem, 10, 40)


def col_rmv():
    def rem():
        global testdf, testdf2, tree
        testdf.drop(testdf.columns[var.get()], inplace=True, axis=1)
        testdf.reset_index(drop=True, inplace=True)
        testdf2 = testdf.iloc[::-1]
        tree.destroy()
        scroll1.destroy()
        scrollbar.destroy()
        show_table()

    var = tk.IntVar()
    top = tk.Toplevel()
    top.title("Column removal")
    top.geometry("250x100")
    top.resizable(False, False)
    Label_make(top, "Enter Column Num:", 10, 10)
    Entry_make(top, var, 130, 10)
    button_make(top, "Delete", rem, 10, 40)


def col_add():
    def add_complete():
        global testdf2
        testdf[entryvar.get()] = " "
        testdf2 = testdf.iloc[::-1]
        tree.destroy()
        scroll1.destroy()
        scrollbar.destroy()
        show_table()

    new_window = tk.Toplevel()
    new_window.title("Add Column")
    new_window.geometry("220x100")
    new_window.resizable(False, False)
    entryvar = tk.StringVar()

    Label_make(new_window, "Add column", 10, 10)
    Entry_make(new_window, entryvar, 90, 10)
    button_make(new_window, "Update", add_complete, 10, 40)


def col_change():
    def add_complete():
        def change_column():
            global testdf, testdf2

            x = entryvar2.get()
            print(testdf.columns[x])
            testdf.columns[x] = entryvar.get()
            testdf2 = testdf.iloc[::-1]
            tree.destroy()
            scroll1.destroy()
            scrollbar.destroy()
            show_table()

        new_window = tk.Toplevel()
        new_window.title("Add Column")
        new_window.geometry("300x100")
        new_window.resizable(False, False)
        Label_make(new_window, "Change column name", 10, 10)
        Entry_make(new_window, entryvar, 140, 10)
        button_make(new_window, "Update", change_column, 10, 40)

    new_window = tk.Toplevel()
    new_window.title("Add Column")
    new_window.geometry("300x100")
    new_window.resizable(False, False)
    entryvar = tk.StringVar()
    entryvar2 = tk.IntVar()
    Label_make(new_window, "Enter column num:", 10, 10)
    Entry_make(new_window, entryvar2, 120, 10)
    button_make(new_window, "Enter", add_complete, 10, 40)


def save():
    try:
        file = easygui.filesavebox(msg="Save to the intended file", title="Save File",filetypes=['*.csv', "All files", "*"],
                                   default="*.csv")
        file_ext = os.path.splitext(file)
        if file_ext[1] == ".csv":
            testdf.to_csv(file, index=False)
        else:
            testdf.to_csv(file + ".csv", index=False)
    except TypeError:
        raise TypeError("The file has not been saved, perhaps you cancelled?")


def load1():
    global testdf, testdf2
    try:
        file = easygui.fileopenbox(msg="Open the intended file", title="Load File", filetypes=['*.csv'],
                                   default="*.csv")
        window.title("table: " + file)
        testdf = pd.read_csv(file)
        testdf2 = testdf.iloc[::-1]
    except TypeError:
        raise TypeError("The the program stopped, perhaps you cancelled loading?")

def load():
    global tree, testdf, testdf2
    try:
        file = easygui.fileopenbox(msg="Open the intended file", title="Load File", filetypes=['*.csv'],
                                   default="*.csv")
        window.title("table: " + file)
        testdf = pd.read_csv(file)
        testdf2 = testdf.iloc[::-1]
        tree.destroy()
        scroll1.destroy()
        scrollbar.destroy()
        show_table()
    except TypeError:
        raise TypeError("The file has not been loaded, perhaps you cancelled?")


load1()
button_make(window, "Edit Table", Table_manipulate, 20, 10)
button_make(window, "Edit Data", new_window, 20, 50)
button_make(window, "Load file", load, 20, 90)
button_make(window, "Save to file", save, 20, 130)
show_table()

window.mainloop()
