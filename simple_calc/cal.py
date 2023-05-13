from tkinter  import *

page = Tk()

nbr1 = StringVar
nbr2 = StringVar
def sum():
    nb1 = nbr1.get()
    nb2 = nbr2.get()
    result = Label(page , text=f"Votre Nom complete est : {nb1}+{nb2} = {int(nb1)+int(nb2)} ")
    result.pack()
def sous():
    nb1 = nbr1.get()
    nb2 = nbr2.get()
    result = Label(page, text=f"Votre Nom complete est : {nb1}-{nb2} = {int(nb1) - int(nb2)} ")
    result.pack()
def multi():
    nb1 = nbr1.get()
    nb2 = nbr2.get()
    result = Label(page, text=f"Votre Nom complete est : {nb1}*{nb2} = {int(nb1) * int(nb2)} ")
    result.pack()
def div():
    nb1 = nbr1.get()
    nb2 = nbr2.get()
    result = Label(page, text=f"Votre Nom complete est : {nb1}/{nb2} = {int(nb1) / int(nb2)} ")
    result.pack()

titre = Label(page , text="CALCULATRICE", font=("Helvetica", 24), justify="center")
titre.pack()

label1 = Label(page, text="nbr 1 : ")
label1.pack()
nbr1 = Entry(page,textvariable=nbr1, width=50 )
nbr1.pack()
label = Label(page, text="nbr 2: ")
label.pack()
nbr2 = Entry(page,textvariable=nbr2, width=50 )
nbr2.pack()


btnsm = Button(page, text="somme!", command=sum)
btns = Button(page, text="soustation!", command=sous)
btnm = Button(page, text="multiplication!", command=multi)
btnd = Button(page, text="division!", command=div)
btnq = Button(page, text="quit!", command=quit)




btnd.pack()
btns.pack()
btnsm.pack()
btnm.pack()

btnq.pack()





page.mainloop()