import tkinter as tk

def on_drag(event):
    print(f"Dragging at ({event.x}, {event.y})")

root = tk.Tk()
root.title("Drag with Left Button")

label = tk.Label(root, text="Drag the mouse here", width=30, height=5, bg="lightblue")
label.pack(pady=40)

# Bind dragging with left mouse button
label.bind("<B1-Motion>", on_drag)

root.mainloop()
