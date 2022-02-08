from tkinter import *

root = Tk()

parent = Menu(root)
root.config(menu=parent)

#fungsi sederhana ( print )
def perintah():
    print('OK work !')

#menu utama, diberi nama 'file'
file = Menu(parent)
parent.add_cascade(label='File', menu=file)
file.add_command(label='Open', command=perintah)
file.add_command(label='Save', command=perintah)
file.add_separator()
file.add_command(label='Save', command=perintah)

edit = Menu(parent)
parent.add_cascade(label='Edit', menu=file)
edit.add_command(label='Copy', command=perintah)
edit.add_command(label='Paste', command=perintah)

root.mainloop()
