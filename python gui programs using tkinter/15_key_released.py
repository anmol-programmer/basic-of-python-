import tkinter as tk

def on_key(event):
    print(f"Key pressed: {event.char}, keysym: {event.keysym}, keycode: {event.keycode}")

root = tk.Tk()
entry = tk.Entry(root)
entry.pack(pady=20)

# You can use either of these:
entry.bind("<Key>", on_key)         # or
# entry.bind("<KeyPress>", on_key)

root.mainloop()
