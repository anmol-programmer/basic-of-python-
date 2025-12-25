import tkinter as tk

def left_click(event):
    print(f"Left button clicked at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Left Click Example")

btn = tk.Button(root, text="Click Me (Left)")
btn.pack(pady=20)

# Bind only left mouse button click
btn.bind("<Button-1>", left_click)

root.mainloop()
