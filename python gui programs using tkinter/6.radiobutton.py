import tkinter as tk

root = tk.Tk()
root.title("Radiobutton Example")
root.geometry("300x250")

# Variable to store selected value
selected_option = tk.StringVar()
selected_option.set(None)  # Default: no selection

# Radiobuttons
rb1 = tk.Radiobutton(root, text="Male", variable=selected_option, value="Male")
rb2 = tk.Radiobutton(root, text="Female", variable=selected_option, value="Female")
rb3 = tk.Radiobutton(root, text="Other", variable=selected_option, value="Other")

rb1.pack(anchor='w', pady=5)
rb2.pack(anchor='w', pady=5)
rb3.pack(anchor='w', pady=5)

# Function to show selected value
def show_selection():
    choice = selected_option.get()
    result_label.config(text=f"You selected: {choice}")

# Submit Button
btn = tk.Button(root, text="Submit", command=show_selection)
btn.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
