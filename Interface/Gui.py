from cgitb import text
import tkinter as tk
import ttkbootstrap as ttk
from ttkbootstrap.constants import *


root = ttk.Window(themename="darkly")

# frmBrowse = ttk.Frame(root, style='info', width=150, height=100)
# frmBrowse.grid(row=0, column=0, padx=50, pady=50)
# frmFln = ttk.Frame(root, bootstyle="light", width=150, height=35)

btnBrowse = ttk.Button(root, text="Browse", bootstyle="default", width=12)
btnBrowse.grid(row=0, column=0, padx=50, pady=25)

lblFln = ttk.Label(root, text="Folder name", bootstyle="default", width=12, justify='left')
lblFln.grid(row=0, column=1, columnspan=2, padx=20, pady=25)

lblNewFln = ttk.Label(root, text="Input new file name : ", bootstyle="default", justify='left')
lblNewFln.grid(row=1, column=0, padx=(50,0), pady=25)

inputNewFln = ttk.Entry(root, bootstyle="default", width=20)
inputNewFln.grid(row=1, column=1, padx=(0,50), pady=25)

btnRename = ttk.Button(root, text="Rename", bootstyle="success", width=12)
btnRename.grid(row=1, column=2, padx=20, pady=25)

checkbuttonOrder = ttk.Checkbutton(bootstyle="success")
checkbuttonOrder.grid(row=2, column=0, padx=(50,0), pady=25)

lblOrder = ttk.Label(root, text="Add prefix order number", bootstyle="default", justify='left')
lblOrder.grid(row=2, column=1, padx=(0,50), pady=25)

lblReport = ttk.Label(root, text="1 file was successfully renamed", bootstyle="default", justify='left')
lblReport.grid(row=3, column=0, columnspan=3, padx=50, pady=30)



root.title("Rename All Files")
# root.geometry("1280x720")
root.resizable(0, 0)


root.mainloop()
