import tkinter as tk

def on_scroll(event):
    direction = "Up" if event.delta > 0 else "Down"
    print(f"Scrolled {direction}")

root = tk.Tk()
root.title("Mouse Wheel Scroll Example")

label = tk.Label(root, text="Scroll your mouse here", width=30, height=10, bg="lightblue")
label.pack(pady=20)

# Bind MouseWheel (for Windows/macOS)
label.bind("<MouseWheel>", on_scroll)

root.mainloop()
