import tkinter as tk

def double_left_click(event):
    print(f"Double left-click at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Double Click Example")

btn = tk.Button(root, text="Double Left-Click Me")
btn.pack(pady=20)

# Bind double-click with left mouse button
btn.bind("<Double-Button-1>", double_left_click)

root.mainloop()
