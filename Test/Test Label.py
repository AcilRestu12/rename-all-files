import tkinter
from tkinter import *
 
window = Tk()
 
var = StringVar()
label = Label( window, textvariable=var, relief=RAISED )
 
# set label value
var.set("Selamat Datang Di RIffamedia.com")
 
label.pack()
window.mainloop()