import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Scrollbar Example")
root.geometry("400x300")

# Create a Text widget
text_box = tk.Text(root, wrap="word", height=10, width=40)
text_box.pack(side="left", fill="both", expand=True)

# Create a vertical Scrollbar and link it to the Text widget
scrollbar = tk.Scrollbar(root, command=text_box.yview)
scrollbar.pack(side="right", fill="y")

# Configure the Text widget to work with the scrollbar
text_box.config(yscrollcommand=scrollbar.set)

# Insert dummy content to make scrolling visible
for i in range(50):
    text_box.insert("end", f"This is line number {i + 1}\n")

# Start the main event loop
root.mainloop()
