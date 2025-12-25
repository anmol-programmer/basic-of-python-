import tkinter as tk

root = tk.Tk()
root.title("Scale (Slider) Example")
root.geometry("300x250")
root.configure(bg="lightblue")

# Label
label = tk.Label(root, text="Select a value:")
label.pack(pady=10)

# Create Scale widget (from 0 to 100)
slider = tk.Scale(root, from_=0, to=100, orient=tk.HORIZONTAL)
slider.pack(pady=10)

# Function to show selected value
def show_value():
    value = slider.get()  # Get current slider value
    result_label.config(text=f"Selected Value: {value}")

# Button
btn = tk.Button(root, text="Submit", command=show_value)
btn.pack(pady=10)

# Label to show result
result_label = tk.Label(root, text="")
result_label.pack()

root.mainloop()
