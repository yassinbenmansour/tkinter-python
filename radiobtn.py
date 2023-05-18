import text
from tkinter import *
def show_selection():
    selected_option = radio_var.get()
    text.config(text=f"Resultat: {selected_option}")

page = Tk()

# Create a variable to hold the selected option
radio_var = StringVar()
radio_var.set("Option 1")

# Create Radiobuttons
radio_button1 = Radiobutton(page, text="Option 1", variable=radio_var, value="Option 1")
radio_button2 = Radiobutton(page, text="Option 2", variable=radio_var, value="Option 2")
radio_button3 = Radiobutton(page, text="Option 3", variable=radio_var, value="Option 3")

# Pack the Radiobuttons
radio_button1.pack()
radio_button2.pack()
radio_button3.pack()

# Create a button to show the selected option
button = Button(page, text="Show Selection", command=show_selection)
button.pack()

text = Label(page, text="")
text.pack()

# Start the main event loop
page.mainloop()