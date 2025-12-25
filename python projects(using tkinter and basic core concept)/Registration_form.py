import tkinter as tk

root = tk.Tk()
root.title("Registration Form")
root.geometry("400x400")
root.configure(bg="lightblue")  


form_frame = tk.Frame(root, bg="white", padx=20, pady=20)
form_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)

title = tk.Label(form_frame, text="Registration Form", font=("Arial", 16, "bold"), bg="white")
title.grid(row=0, column=0, columnspan=2, pady=(0, 20))

def add_row(label_text, row_num):
    label = tk.Label(form_frame, text=label_text, bg="white")
    label.grid(row=row_num, column=0, sticky="w", pady=5)
    entry = tk.Entry(form_frame, width=30, bd=1, relief="solid", bg="#e6e6e6")
    entry.grid(row=row_num, column=1, pady=5)

add_row("Name*", 1)
add_row("Email*", 2)
add_row("Phone*", 3)
add_row("Subject*", 4)

# Message box
label_msg = tk.Label(form_frame, text="Message*", bg="white")
label_msg.grid(row=5, column=0, sticky="w", pady=5)
text_msg = tk.Text(form_frame, width=28, height=4, bd=1, relief="solid", bg="#e6e6e6")
text_msg.grid(row=5, column=1, pady=5)

submit_btn = tk.Button(form_frame, text="Submit", bg="#005b8f", fg="white", font=("Arial", 10))
submit_btn.grid(row=6, column=0, columnspan=2, pady=15)

# Start GUI
root.mainloop()
