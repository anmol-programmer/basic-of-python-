import tkinter as tk

root = tk.Tk()
root.title("Entry Example")
root.geometry("300x200")

# Label
label = tk.Label(root, text="Enter your name:")
label.pack(pady=10)

# Entry (Single-line input)
entry = tk.Entry(root)
entry.pack(pady=5)

# Function to handle button click
def show_input():
    name = entry.get()  # Get the text from Entry
    result_label.config(text=f"Hello, {name}!")

# Button to submit input
button = tk.Button(root, text="Submit", command=show_input)
button.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack(pady=10)

root.mainloop()
