import tkinter as tk

def middle_click(event):
    print(f"Middle button clicked at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Middle Click Example")

btn = tk.Button(root, text="Click Me (Middle)")
btn.pack(pady=20)

# Bind middle mouse button
btn.bind("<Button-2>", middle_click)

root.mainloop()
