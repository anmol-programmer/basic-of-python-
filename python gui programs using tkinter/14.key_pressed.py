import tkinter as tk

def key_event(event):
    print(f"You pressed: {event.char} (keysym: {event.keysym})")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack(pady=20)

entry.bind("<KeyPress>", key_event)  # Same as <Key>

root.mainloop()
