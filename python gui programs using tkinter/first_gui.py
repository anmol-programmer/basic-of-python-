import tkinter as tk

# Function to update the label with the user's input
def show_message():
    user_input = entry.get()
    output_label.config(text="You typed: " + user_input)

# Create the main window
window = tk.Tk()
window.title("Simple GUI App")
window.geometry("300x150")

# Create a label
label = tk.Label(window, text="Enter something:")
label.pack(pady=5)

# Create an entry box
entry = tk.Entry(window, width=30)
entry.pack(pady=5)

# Create a button
button = tk.Button(window, text="Show", command=show_message)
button.pack(pady=5)

# Create a label to display output
output_label = tk.Label(window, text="")
output_label.pack(pady=5)

# Run the GUI loop
window.mainloop()
