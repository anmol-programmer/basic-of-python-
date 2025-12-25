import tkinter as tk

def on_enter(event):
    event.widget.config(bg="lightgreen")
    print("Mouse entered the widget")

root = tk.Tk()
root.title("Enter Event Example")

label = tk.Label(root, text="Hover over me", bg="lightgray", width=25, height=5)
label.pack(pady=20)

# Bind <Enter> event
label.bind("<Enter>", on_enter)

root.mainloop()
