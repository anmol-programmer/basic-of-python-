import tkinter as tk

# Create the main window
root = tk.Tk()
root.title("Spinbox Example")
root.geometry("300x200")
root.configure(bg="lightyellow")

# Label
label = tk.Label(root, text="Select a number:", bg="lightyellow")
label.pack(pady=10)

# Spinbox: from 1 to 10
spin = tk.Spinbox(root, from_=1, to=100)
spin.pack(pady=10)

# Function to get selected value
def show_value():
    value = spin.get()
    result_label.config(text=f"You selected: {value}")

# Button to display result
btn = tk.Button(root, text="Submit", command=show_value)
btn.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="", bg="lightyellow")
result_label.pack()

# Run the application
root.mainloop()
