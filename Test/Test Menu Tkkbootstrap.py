from cgitb import text
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *

def printSelected():
    print(f'chice : {choice.get()}\n')


root = ttk.Window(themename="darkly")

menuBtn = ttk.Menubutton(bootstyle="success", text='Menu')
# menu.add_command(label='Open', command=perintah)
# menu.add_command(label='Save', command=perintah)

menuBtn.grid(row=0, column=0, padx=50, pady=50)

menu = tk.Menu(menuBtn, tearoff=0)
colors = ('Red', 'Green', 'Blue')
choice = tk.StringVar()

for color in colors:
    menu.add_radiobutton(
        label=color,
        value=color,
        variable=choice)

menuBtn["menu"] = menu

btnPrint = ttk.Button(root, text="Print", bootstyle="success", width=12, command=printSelected)
btnPrint.grid(row=0, column=1, padx=50, pady=50)

# choice = menu.entrycget(index=1, option='value')

root.title("Rename All Files")
# root.geometry("1280x720")
root.resizable(0, 0)


root.mainloop()
