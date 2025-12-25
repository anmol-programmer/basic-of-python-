import tkinter as tk
import datetime

root = tk.Tk()
root.title("Digital Clock")
root.geometry("300x100")
root.configure(bg="black")

time_label = tk.Label(root, font=("Helvetica", 40), fg="lime", bg="black")
time_label.pack()

def update_clock():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    time_label.config(text=current_time)
    root.after(1000, update_clock)

update_clock()
root.mainloop()
