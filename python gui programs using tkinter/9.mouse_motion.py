import tkinter as tk

def on_mouse_move(event):
    print(f"Mouse moved to ({event.x}, {event.y})")

root = tk.Tk()
label = tk.Label(root, text="Move your mouse over me", width=30, height=5, bg="lightblue")
label.pack(pady=20)

label.bind("<Motion>", on_mouse_move)

root.mainloop()
