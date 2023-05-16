import tkinter as tk
import time


class Clock:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Clock")

        self.label = tk.Label(self.root, text="", font=("Helvetica", 34))
        self.label.pack(padx=10, pady=10)

        self.update_clock()

        self.root.mainloop()

    def update_clock(self):
        current_time = time.strftime("%H:%M:%S")
        self.label.configure(text=current_time)
        self.root.after(1000, self.update_clock)


clock = Clock()
