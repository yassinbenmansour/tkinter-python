from tkinter import *

page = Tk()
opt1 = IntVar()
opt2 = IntVar()
opt3 = IntVar()
def check():
    data1 = opt1.get()
    data2 = opt2.get()

    if (data1 == 1):
        resultop.config(text="false")
    elif(data2 == 1):
        resultop.config(text="true bravo")
    else:
        resultop.config(text="false")





Q1 = Label(page,text="What does HTML stand for?" , justify="left")
Q1.pack()

chekbtn1 = Checkbutton(page,text="a. Hyper Text Marking Language",variable=opt1,command=check)
chekbtn2 = Checkbutton(page,text="b. Hyper Text Markup Language",variable=opt2 ,command=check)
chekbtn3 = Checkbutton(page,text="c. Hyper Text Mailing Language",variable=opt3,command=check)

resultop = Label(page, text="Resultat:")

chekbtn1.pack()
chekbtn2.pack()
chekbtn3.pack()

resultop.pack()

page.mainloop()
