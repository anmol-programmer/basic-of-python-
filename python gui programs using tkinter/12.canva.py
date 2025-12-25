import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Canvas Drawing Example")
root.geometry("500x500")

# Create a Canvas widget
canvas = tk.Canvas(root, width=500, height=500, bg="white")
canvas.pack(pady=20)

# Draw a line (x1, y1, x2, y2)
canvas.create_line(10, 10, 200, 10, fill="blue", width=2)
canvas.pack(pady=20)
# Draw a rectangle (x1, y1, x2, y2)
canvas.create_rectangle(50, 40, 150, 100, outline="green", fill="yellow", width=2)
canvas.pack(pady=20)
# Draw an oval (x1, y1, x2, y2) — fits within bounding box
canvas.create_oval(170, 40, 270, 100, outline="red", fill="pink", width=2)
canvas.pack(pady=20)
# Draw text at (x, y)
canvas.create_text(150, 150, text="Hello Canvas!", font=("Arial", 14), fill="purple")

# Run the application
root.mainloop()
