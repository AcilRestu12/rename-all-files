from ast import Pass
from cgitb import text
from distutils.log import error
from importlib.resources import path
from re import I
import tkinter as tk
from turtle import width
import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import os
from tkinter import filedialog
from tkinter import messagebox



def btnBrowseClicked():
    global pathFolder
    
    pathFolder = filedialog.askdirectory(initialdir=os.getcwd(), title="Select Folder")
    print(f'pathFolder : {pathFolder}\n')
    
    folderName.set(pathFolder.split('/')[-1])
    if pathFolder == '':
        folderName.set('None')
    else: 
        folderName.set(pathFolder.split('/')[-1])
        
    lblFolderName.configure(text=f'Folder name : {folderName.get()}')
    print(f'folderName : {folderName.get()}\n')

        
def btnRenameClicked():
    global pathFolder
    
    pathFolder += '/'
    num = 1
    sumFiles.set(0)
    
    for i, filename in enumerate(os.listdir(pathFolder)):
        # print(f'filename : {filename}')
        listFile = (filename.split('.'))
        oldName = listFile[0]
        extensionFile = listFile[1]
        
        # print(f'listFile : {listFile}')
        # print(f'Nama file : {listFile[0]}')
        # print(f'Ekstensi file : {listFile[1]}\n---------')

        if inputNewFln.get() == '/oldname':
            fln.set(oldName)

        if num > 1 and fln.get() == '':
            fln.set('/oldname')
            
        if fln.get() == '/oldname':
            fln.set(oldName)
                        
        if chkEraseSymbol.get() == '1':
            if choiceOrder.get() == 'Prefix':
                newName = f'{num} {inputNewFln.get()}'
            elif choiceOrder.get() == 'Suffix':
                newName = f'{inputNewFln.get()} {num}'
            elif choiceOrder.get() == 'No order':
                # newName = f'{inputNewFln.get()}'
                messagebox.showerror('Error', f'Please select position order!')
        else:
            if choiceOrder.get() == 'Prefix':
                newName = f'{num}-{inputNewFln.get()}'
            elif choiceOrder.get() == 'Suffix':
                newName = f'{inputNewFln.get()}-{num}'
            elif choiceOrder.get() == 'No order':
                messagebox.showerror('Error', f'Please select position order!')
            
        newFilename = newName + '.' + extensionFile
        
        try:
            os.rename(pathFolder + filename, pathFolder + newFilename)
            print(f'newFilename : {newFilename}\n')
            sumFiles.set(int(sumFiles.get())+1)
            if inputNewFln.get() == '/oldname':
                fln.set('')
        except error:
            messagebox.showerror('Error', f'{oldName} was unsuccessfully renamed!')
            print(error +'\n')
        
        if int(sumFiles.get()) < 0:
            sumFiles.set(0)
        
        if int(sumFiles.get()) == 1 or int(sumFiles.get()) == 0:
            report.set(f"{sumFiles.get()} file was successfully renamed")
        elif int(sumFiles.get()) > 1:
            report.set(f"{sumFiles.get()} files was successfully renamed")    
                    
        num += 1



if __name__ == '__main__':
    
    pathFolder = None
    
    root = ttk.Window(themename="darkly")

    btnBrowse = ttk.Button(root, text="Browse", bootstyle="default", width=12, command=btnBrowseClicked)
    btnBrowse.grid(row=0, column=0, padx=(50,20), pady=(50,25))

    folderName = tk.StringVar(value='None')

    lblFolderName = ttk.Label(root, text=f'Folder name : {folderName.get()}', bootstyle="default", justify='left')
    lblFolderName.grid(row=0, column=1, columnspan=2, padx=(20,50), pady=(50,25))


    frmNewFln = ttk.Frame(root, bootstyle="default")
    frmNewFln.grid(row=1, column=0, padx=(50,30), pady=25)

    fln = tk.StringVar()

    lblNewFln = ttk.Label(frmNewFln, text="Input new file name : ", bootstyle="default", justify='left')
    lblNewFln.grid(row=0, column=0, padx=(20,5), pady=25)

    inputNewFln = ttk.Entry(frmNewFln, bootstyle="default", width=18, textvariable=fln)
    inputNewFln.grid(row=0, column=1, padx=(5,20), pady=25)

    btnRename = ttk.Button(root, text="Rename", bootstyle="success", width=12, command=btnRenameClicked)
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
    report = tk.StringVar(value='0 file')
    lblReport = ttk.Label(root, textvariable=report, bootstyle="default", justify='left')
    lblReport.grid(row=3, column=0, columnspan=4, padx=50, pady=(30,50))


    root.title("Rename All Files")
    # root.geometry("1280x720")
    root.resizable(0, 0)


    root.mainloop()
