import tkinter as tk

root = tk.Tk()
root.title("Text Widget Example")
root.geometry("400x300")

# Label
label = tk.Label(root, text="Enter your feedback:")
label.pack(pady=10)


text_box = tk.Text(root, height=8, width=40)
text_box.pack(pady=5)

# Function to handle button click
def show_feedback():
    feedback = text_box.get("1.0", tk.END)  # Get text from line 1, char 0 to end
    result_label.config(text="Feedback received!")

# Button
submit_btn = tk.Button(root, text="Submit", command=show_feedback)
submit_btn.pack(pady=10)

# Result label
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
