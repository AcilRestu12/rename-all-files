from cgitb import text
import tkinter as tk
from turtle import width
import ttkbootstrap as ttk
from ttkbootstrap.constants import *



root = ttk.Window(themename="darkly")

btnBrowse = ttk.Button(root, text="Browse", bootstyle="default", width=12)
btnBrowse.grid(row=0, column=0, padx=(50,20), pady=(50,25))

folderName = tk.StringVar(value='None')

lblFolderName = ttk.Label(root, text=f'Folder name : {folderName.get()}', bootstyle="default", justify='left')
lblFolderName.grid(row=0, column=1, columnspan=2, padx=(20,50), pady=(50,25))


frmNewFln = ttk.Frame(root, bootstyle="default")
frmNewFln.grid(row=1, column=0, padx=(50,30), pady=25)

fln = tk.StringVar(value='File')

lblNewFln = ttk.Label(frmNewFln, text="Input new file name : ", bootstyle="default", justify='left')
lblNewFln.grid(row=0, column=0, padx=(20,5), pady=25)

inputNewFln = ttk.Entry(frmNewFln, bootstyle="default", width=18, textvariable=fln)
inputNewFln.grid(row=0, column=1, padx=(5,20), pady=25)

btnRename = ttk.Button(root, text="Rename", bootstyle="success", width=12)
btnRename.grid(row=1, column=1, padx=(30,50), pady=25)


btnMenuOrder = ttk.Menubutton(root, bootstyle="secondary", text='Position order', width=12)
btnMenuOrder.grid(row=2, column=0, padx=(50,30), pady=(0,25))

menuOrder = tk.Menu(btnMenuOrder, tearoff=0)
posOrders = ('No order', 'Prefix', 'Suffix')
choiceOrder = tk.StringVar()
for posOrder in posOrders:
    menuOrder.add_radiobutton(
        label=posOrder,
        value=posOrder,
        variable=choiceOrder)
btnMenuOrder["menu"] = menuOrder

frmEraseSymbol = ttk.Frame(root, bootstyle="default")
frmEraseSymbol.grid(row=2, column=1, padx=(30,50), pady=(0,25))

chkEraseSymbol = tk.StringVar()

chkbuttonEraseSymbol = ttk.Checkbutton(frmEraseSymbol, bootstyle="secondary", variable=chkEraseSymbol)
chkbuttonEraseSymbol.grid(row=0, column=0, padx=(20,5), pady=25)

lblEraseSymbol = ttk.Label(frmEraseSymbol, text="Erase symbol", bootstyle="default", justify='left')
lblEraseSymbol.grid(row=0, column=1, padx=(5,20), pady=25)


sumFiles = tk.StringVar(value=0)
lblReport = ttk.Label(root, text=f"{sumFiles.get()} file was successfully renamed", bootstyle="default", justify='left')
lblReport.grid(row=3, column=0, columnspan=4, padx=50, pady=(30,50))

if int(sumFiles.get()) < 0:
    sumFiles.set(0)

if int(sumFiles.get()) == 1 or int(sumFiles.get()) == 0:
    lblReport.configure(text=f"{sumFiles.get()} file was successfully renamed")
elif int(sumFiles.get()) > 1:
    lblReport.configure(text=f"{sumFiles.get()} files was successfully renamed")



root.title("Rename All Files")
# root.geometry("1280x720")
root.resizable(0, 0)


root.mainloop()