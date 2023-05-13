import tkinter
from tkinter import *

page = Tk()
def btn_sayhello():
    txt = Label(page , text="hello" , font=("Helvetica", 16))
    txt.pack()


btn = tkinter.Button(page, text="Click me!", command=btn_sayhello , bg="green", fg="blue", font=("Helvetica", 16), width=10, height=2)
btn.pack()
page.mainloop()
