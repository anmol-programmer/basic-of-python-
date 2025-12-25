import tkinter as tk

def on_mouse_click(event):
    print(f"Mouse clicked at ({event.x}, {event.y}) with Button-{event.num}")

root = tk.Tk()
root.title("Mouse Click Example")

btn = tk.Button(root, text="Click Me")
btn.pack(pady=20)

# Bind any mouse button click
btn.bind("<Button>", on_mouse_click)

root.mainloop()
