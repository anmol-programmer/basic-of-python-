import tkinter as tk

root = tk.Tk()
root.title("Student Registration Form")
root.geometry("600x750")
root.configure(bg="pink")

# Heading
tk.Label(root, text="Student Registration Form", font=("Arial", 20, "bold"), bg="pink").grid(row=0, column=0, columnspan=3, pady=20)

# Roll no
tk.Label(root, text="Roll no. :", bg="pink").grid(row=1, column=0, sticky="e", padx=10, pady=5)
tk.Entry(root, width=30).grid(row=1, column=1, columnspan=2, sticky="w")

# Student name
tk.Label(root, text="Student name :", bg="pink").grid(row=2, column=0, sticky="e", padx=10, pady=5)
tk.Entry(root, width=14).grid(row=2, column=1, sticky="w")
tk.Entry(root, width=14).grid(row=2, column=2, sticky="w")

# Father's name
tk.Label(root, text="Father's name :", bg="pink").grid(row=3, column=0, sticky="e", padx=10, pady=5)
tk.Entry(root, width=30).grid(row=3, column=1, columnspan=2, sticky="w")

# DOB
tk.Label(root, text="Date of birth :", bg="pink").grid(row=4, column=0, sticky="e", padx=10, pady=5)
days = [str(i) for i in range(1, 32)]
months = [str(i) for i in range(1, 13)]
years = [str(i) for i in range(1980, 2026)]
day_var = tk.StringVar(value="Day")
month_var = tk.StringVar(value="Month")
year_var = tk.StringVar(value="Year")
tk.OptionMenu(root, day_var, *days).grid(row=4, column=1, sticky="w")
tk.OptionMenu(root, month_var, *months).grid(row=4, column=1)
tk.OptionMenu(root, year_var, *years).grid(row=4, column=1, sticky="e")
tk.Label(root, text="(DD-MM-YYYY)", bg="pink").grid(row=4, column=2, sticky="w")

# Mobile no
tk.Label(root, text="Mobile no. :", bg="pink").grid(row=5, column=0, sticky="e", padx=10, pady=5)
tk.Label(root, text="+91", bg="pink").grid(row=5, column=1, sticky="w")
tk.Entry(root, width=25).grid(row=5, column=1, padx=25, sticky="w")

# Email
tk.Label(root, text="Email id :", bg="pink").grid(row=6, column=0, sticky="e", padx=10, pady=5)
tk.Entry(root, width=30).grid(row=6, column=1, columnspan=2, sticky="w")

# Password
tk.Label(root, text="Password :", bg="pink").grid(row=7, column=0, sticky="e", padx=10, pady=5)
tk.Entry(root, width=30, show="*").grid(row=7, column=1, columnspan=2, sticky="w")

# Gender
tk.Label(root, text="Gender :", bg="pink").grid(row=8, column=0, sticky="e", padx=10, pady=5)
tk.Radiobutton(root, text="Male", value="Male", bg="pink").grid(row=8, column=1, sticky="w")
tk.Radiobutton(root, text="Female", value="Female", bg="pink").grid(row=8, column=2, sticky="w")

# Department
tk.Label(root, text="Department :", bg="pink").grid(row=9, column=0, sticky="e", padx=10, pady=5)
departments = ["CSE", "IT", "ECE", "Civil", "Mech"]
for i, dept in enumerate(departments):
    tk.Checkbutton(root, text=dept, bg="pink").grid(row=9+i//3, column=1+i%3, sticky="w")

# Course
tk.Label(root, text="Course :", bg="pink").grid(row=11, column=0, sticky="e", padx=10, pady=5)
course_var = tk.StringVar(value="Select Current Course")
tk.OptionMenu(root, course_var, "B.Tech", "M.Tech", "Diploma", "MCA", "BCA").grid(row=11, column=1, columnspan=2, sticky="w")

# Photo
tk.Label(root, text="Student photo :", bg="pink").grid(row=12, column=0, sticky="e", padx=10, pady=5)
tk.Button(root, text="Choose File").grid(row=12, column=1, columnspan=2, sticky="w")

# City
tk.Label(root, text="City :", bg="pink").grid(row=13, column=0, sticky="e", padx=10, pady=5)
tk.Entry(root, width=30).grid(row=13, column=1, columnspan=2, sticky="w")

# Address
tk.Label(root, text="Address :", bg="pink").grid(row=14, column=0, sticky="ne", padx=10, pady=5)
tk.Text(root, height=4, width=30).grid(row=14, column=1, columnspan=2, sticky="w")

# Submit Button
tk.Button(root, text="Register", width=15).grid(row=15, column=1, pady=20, sticky="w")

root.mainloop()
