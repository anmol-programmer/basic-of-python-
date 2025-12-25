import tkinter as tk

def key_pressed(event):
    print(f"Key pressed: {event.char} (keycode: {event.keycode})")

root = tk.Tk()
root.title("Key Press Event")

entry = tk.Entry(root, width=30)
entry.pack(pady=20)

# Bind the <Key> event
entry.bind("<Key>", key_pressed)

root.mainloop()
