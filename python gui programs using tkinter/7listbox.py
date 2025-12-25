import tkinter as tk

root = tk.Tk()
root.title("Listbox Example")
root.geometry("300x250")

# Label
label = tk.Label(root, text="Select a programming language:")
label.pack(pady=10)

# Listbox with single selection mode
listbox = tk.Listbox(root, height=5)
languages = ["Python", "Java", "C++", "JavaScript", "Ruby"]

# Add items to the listbox
for lang in languages:
    listbox.insert(tk.END, lang)

listbox.pack(pady=5)

# Function to show selected item
def show_selection():
    selected = listbox.curselection()  # Returns a tuple of selected indices
    if selected:
        choice = listbox.get(selected[0])  # Get item by index
        result_label.config(text=f"You selected: {choice}")
    else:
        result_label.config(text="No selection")

# Submit Button
btn = tk.Button(root, text="Submit", command=show_selection)
btn.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
