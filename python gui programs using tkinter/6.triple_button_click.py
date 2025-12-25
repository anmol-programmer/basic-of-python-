import tkinter as tk

def on_triple_click(event):
    print("Triple-click detected at:", event.x, event.y)

root = tk.Tk()
root.title("Triple Click Example")
root.geometry("300x200")
root.configure(bg="lightblue")

label = tk.Label(root, text="Triple-click me", font=("Arial", 14))
label.pack(pady=40)

# Bind triple left-click to the label
label.bind("<Triple-Button-1>", on_triple_click)

root.mainloop()
