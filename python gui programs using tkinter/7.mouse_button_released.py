import tkinter as tk

def on_release(event):
    print(f"Mouse button {event.num} released at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Button Release Example")
root.geometry("300x200")


btn = tk.Button(root, text="Click and Release")
btn.pack(pady=20)

# Bind mouse button release
btn.bind("<ButtonRelease>", on_release)

root.mainloop()
