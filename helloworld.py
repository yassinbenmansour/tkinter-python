from tkinter import *

page = Tk()

txt = Label(page,text="HELLO YASSINE", bg="red", fg="black", font=("Helvetica", 24), justify="center", padx=10, pady=10, relief="raised")
txt.pack()
page.mainloop()


"""
text: The text to be displayed in the Label.

bg: The background color of the Label.

fg: The foreground (text) color of the Label.

font: The font used for the text in the Label.

justify: The justification of the text (left, center, or right).

padx: The padding (in pixels) on the left and right sides of the Label.

pady: The padding (in pixels) on the top and bottom sides of the Label.

relief: The border style of the Label (flat, raised, sunken, etc.).

image: An image to be displayed in the Label (instead of text).

"""
