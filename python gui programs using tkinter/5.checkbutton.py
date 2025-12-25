import tkinter as tk

root = tk.Tk()
root.title("Checkbutton Example")
root.geometry("300x250")

# Variables to store checkbutton state (1 for checked, 0 for unchecked)
option1 = tk.IntVar()
option2 = tk.IntVar()
option3 = tk.IntVar()

# Checkbuttons
cb1 = tk.Checkbutton(root, text="Python", variable=option1)
cb2 = tk.Checkbutton(root, text="Java", variable=option2)
cb3 = tk.Checkbutton(root, text="C++", variable=option3)

cb1.pack(anchor='w', pady=5)
cb2.pack(anchor='w', pady=5)
cb3.pack(anchor='w', pady=5)

# Function to show selected options
def show_selection():
    result = "Selected:\n"
    if option1.get() == 1:
        result += "- Python\n"
    if option2.get() == 1:
        result += "- Java\n"
    if option3.get() == 1:
        result += "- C++\n"
    result_label.config(text=result)

# Submit Button
btn = tk.Button(root, text="Submit", command=show_selection)
btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
