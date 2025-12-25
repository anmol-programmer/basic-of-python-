import tkinter as tk

def on_enter(event):
    event.widget.config(bg="lightgreen")
    print("Mouse entered the widget")

def on_leave(event):
    event.widget.config(bg="lightgray")
    print("Mouse left the widget")

root = tk.Tk()
root.title("Enter and Leave Events")

label = tk.Label(root, text="Hover over me", bg="lightgray", width=25, height=5)
label.pack(pady=20)

label.bind("<Enter>", on_enter)
label.bind("<Leave>", on_leave)

root.mainloop()
