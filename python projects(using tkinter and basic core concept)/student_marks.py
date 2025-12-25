import tkinter as tk
import tkinter.font as tkFont

root = tk.Tk()
root.title("Student Report System")
root.geometry("800x900")
root.configure(bg="light green")

# Heading font
font_style = tkFont.Font(family="Arial", size=20, weight="bold", underline=1)

# Heading
label_s = tk.Label(root, text="RESULT CARD", font=font_style, fg="red", bg="light green")
label_s.grid(row=0, column=0, columnspan=2, pady=20)

# Student name label and entry
label_se = tk.Label(root, text="Student Name:", bg="light green", font=("Arial", 14))
label_se.grid(row=1, column=0, padx=10, pady=10, sticky="e")

entry_box = tk.Entry(root, width=50, font=("Arial", 14))
entry_box.grid(row=1, column=1, padx=10, pady=10, sticky="w")

root.mainloop()
