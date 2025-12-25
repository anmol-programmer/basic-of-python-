import tkinter as tk

def right_click(event):
    print(f"Right button clicked at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Right Click Example")

btn = tk.Button(root, text="Right-Click Me")
btn.pack(pady=20)

# Bind right mouse button
btn.bind("<Button-3>", right_click)

root.mainloop()
