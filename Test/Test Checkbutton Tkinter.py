import tkinter as tk
 
app = tk.Tk() 
app.geometry('250x200')

chkValue = tk.StringVar() 
 
chkExample = tk.Checkbutton(app,
                            text='Check Box', 
                            bg = 'gray',
                            fg = 'blue',
                            var=chkValue,
                            onvalue="RGB", 
                            offvalue="YCbCr") 
chkExample.grid(column=0, row=0)

chkExample.select()
print("The checkbutton value when selected is {}".format(chkValue.get()))
chkExample.deselect()
print("The checkbutton value when deselected is {}".format(chkValue.get()))

app.mainloop()