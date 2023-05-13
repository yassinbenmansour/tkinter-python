import tkinter as tk
from tkinter import *

page = Tk()

def aff():
    nom = name.get()
    pr = prenom.get()

    affiche = Label(page , text=f"Votre Nom complete est : {nom} {pr} ")
    affiche.pack()


name = tk.StringVar()
prenom = tk.StringVar()

label1 = Label(page, text="Nom : ")
label1.pack()

nameEntry = tk.Entry(page, textvariable=name, width=50)
nameEntry.pack()

label2 = Label(page, text="prenom : ")
label2.pack()

prenomEntry = tk.Entry(page, textvariable=prenom, width=50)
prenomEntry.pack()


submit = tk.Button(page, text="affiche!", command=aff)
submit.pack()

page.mainloop()
