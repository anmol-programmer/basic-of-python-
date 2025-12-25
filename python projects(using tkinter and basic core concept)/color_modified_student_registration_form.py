import tkinter as tk

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("400x500")
root.configure(bg="green")  # Background color for the main window

# Heading
heading_label = tk.Label(root, text="Student Registration Form", font=("Arial", 16, "bold"), fg="blue", bg="green")
heading_label.grid(row=0, column=0, columnspan=2, pady=10)

subheading_label = tk.Label(root, text="Fill in this form to register", font=("Arial", 10), fg="blue", bg="green")
subheading_label.grid(row=1, column=0, columnspan=2, pady=5)

# First Name
first_name_label = tk.Label(root, text="First Name", fg="blue", bg="green")
first_name_label.grid(row=2, column=0, sticky="w", padx=10, pady=5)

first_name_entry = tk.Entry(root, fg="blue", bg="green")
first_name_entry.grid(row=2, column=1, padx=10, pady=5)

# Last Name
last_name_label = tk.Label(root, text="Last Name", fg="blue", bg="green")
last_name_label.grid(row=3, column=0, sticky="w", padx=10, pady=5)

last_name_entry = tk.Entry(root, fg="blue", bg="green")
last_name_entry.grid(row=3, column=1, padx=10, pady=5)

# Email
email_label = tk.Label(root, text="E-mail", fg="blue", bg="green")
email_label.grid(row=4, column=0, sticky="w", padx=10, pady=5)

email_entry = tk.Entry(root, fg="blue", bg="green")
email_entry.grid(row=4, column=1, padx=10, pady=5)

# Date of Birth
dob_label = tk.Label(root, text="Date of Birth", fg="blue", bg="green")
dob_label.grid(row=5, column=0, sticky="w", padx=10, pady=5)

dob_entry = tk.Entry(root, fg="blue", bg="green")
dob_entry.grid(row=5, column=1, padx=10, pady=5)

# Username
username_label = tk.Label(root, text="Set Username", fg="blue", bg="green")
username_label.grid(row=6, column=0, sticky="w", padx=10, pady=5)

username_entry = tk.Entry(root, fg="blue", bg="green")
username_entry.grid(row=6, column=1, padx=10, pady=5)

# Password
password_label = tk.Label(root, text="Set Password", fg="blue", bg="green")
password_label.grid(row=7, column=0, sticky="w", padx=10, pady=5)

password_entry = tk.Entry(root, show="*", fg="blue", bg="green")
password_entry.grid(row=7, column=1, padx=10, pady=5)

# Gender
gender_label = tk.Label(root, text="Gender", fg="blue", bg="green")
gender_label.grid(row=8, column=0, sticky="w", padx=10, pady=5)

male_radio = tk.Radiobutton(root, text="Male", value="Male", fg="blue", bg="green", selectcolor="green")
male_radio.grid(row=8, column=1, sticky="w")

female_radio = tk.Radiobutton(root, text="Female", value="Female", fg="blue", bg="green", selectcolor="green")
female_radio.grid(row=9, column=1, sticky="w")

others_radio = tk.Radiobutton(root, text="Others", value="Others", fg="blue", bg="green", selectcolor="green")
others_radio.grid(row=10, column=1, sticky="w")

# Course
course_label = tk.Label(root, text="Course", fg="blue", bg="green")
course_label.grid(row=11, column=0, sticky="w", padx=10, pady=10)

course_entry = tk.Entry(root, fg="blue", bg="green")
course_entry.grid(row=11, column=1, padx=10, pady=10)

root.mainloop()
