from tkinter import *

page = Tk()

text = Text(page, height=10, width=50)
text.insert(END, "Hello, world!\n")
text.pack()

page.mainloop()
