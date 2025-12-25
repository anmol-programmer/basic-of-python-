import tkinter as tk

root = tk.Tk()
root.title("Message Widget Example")
root.geometry("400x200")

# Multi-line message text
msg_text = "Welcome to the Tkinter GUI tutorial!\n" \
           "This Message widget automatically wraps text and adjusts its size."

# Message widget
message = tk.Message(root, text=msg_text, width=350, bg="lightyellow",fg="green", font=("Arial", 12))
message.pack(pady=20)

root.mainloop()
