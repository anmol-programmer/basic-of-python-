from tkinter import *
from tkinter import filedialog, messagebox
from tkinter.ttk import Combobox
from PIL import Image, ImageTk
import os

root = Tk()
root.title("Student Registration System")
root.geometry("1050x600")
root.config(bg="#06283D")

file_path = "students.txt"

# ---------------- Variables ----------------
full_name_var = StringVar()
student_phone_var = StringVar()  # New: Student Phone
dob_var = StringVar()
gender_var = StringVar(value="Male")
class_var = StringVar()
religion_var = StringVar()
skills_var = StringVar()
father_name_var = StringVar()
father_occ_var = StringVar()
father_phone_var = StringVar()  # New: Father Phone
mother_name_var = StringVar()
mother_occ_var = StringVar()
mother_phone_var = StringVar()  # New: Mother Phone
photo_path = None

# ---------------- Functions ----------------
def upload_image():
    global photo_path
    file_path_img = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    if file_path_img:
        photo_path = file_path_img
        img = Image.open(photo_path)
        img = img.resize((150, 150))
        photo = ImageTk.PhotoImage(img)
        img_label.config(image=photo)
        img_label.image = photo

def save_data():
    if full_name_var.get() == "":
        messagebox.showerror("Error", "Full Name is required!")
        return

    with open(file_path, "a") as f:
        f.write("|".join([
            full_name_var.get(),
            student_phone_var.get(),
            dob_var.get(),
            gender_var.get(),
            class_var.get(),
            religion_var.get(),
            skills_var.get(),
            father_name_var.get(),
            father_occ_var.get(),
            father_phone_var.get(),
            mother_name_var.get(),
            mother_occ_var.get(),
            mother_phone_var.get(),
            photo_path if photo_path else ""
        ]) + "\n")

    messagebox.showinfo("Success", "Data saved successfully!")
    reset_form()

def reset_form():
    full_name_var.set("")
    student_phone_var.set("")
    dob_var.set("")
    gender_var.set("Male")
    class_var.set("")
    religion_var.set("")
    skills_var.set("")
    father_name_var.set("")
    father_occ_var.set("")
    father_phone_var.set("")
    mother_name_var.set("")
    mother_occ_var.set("")
    mother_phone_var.set("")
    img_label.config(image="")
    img_label.image = None

def search_student():
    name_to_search = search_entry.get().strip()
    if name_to_search == "":
        messagebox.showerror("Error", "Enter a name to search!")
        return

    if not os.path.exists(file_path):
        messagebox.showinfo("Not Found", "No student records found.")
        return

    found = False
    with open(file_path, "r") as f:
        for line in f:
            data = line.strip().split("|")
            if data[0] == name_to_search:
                found = True
                full_name_var.set(data[0])
                student_phone_var.set(data[1])
                dob_var.set(data[2])
                gender_var.set(data[3])
                class_var.set(data[4])
                religion_var.set(data[5])
                skills_var.set(data[6])
                father_name_var.set(data[7])
                father_occ_var.set(data[8])
                father_phone_var.set(data[9])
                mother_name_var.set(data[10])
                mother_occ_var.set(data[11])
                mother_phone_var.set(data[12])
                global photo_path
                photo_path = data[13]
                if photo_path and os.path.exists(photo_path):
                    img = Image.open(photo_path)
                    img = img.resize((150, 150))
                    photo = ImageTk.PhotoImage(img)
                    img_label.config(image=photo)
                    img_label.image = photo
                else:
                    img_label.config(image="")
                break

    if not found:
        messagebox.showinfo("Not Found", "No student found with that name.")

def exit_app():
    root.destroy()


# Title Section
title_frame = Frame(root, bg="#53ED8E", height=70)
title_frame.pack(fill=X)

# Load and resize logo
logo_img = Image.open("image.png")  # Path to logo
logo_img = logo_img.resize((50, 50))  # Resize logo
logo = ImageTk.PhotoImage(logo_img)

# Logo in first column
logo_label = Label(title_frame, image=logo, bg="#53ED8E")
logo_label.grid(row=0, column=0, padx=10, pady=10)

# Title text in second column
title_label = Label(title_frame, text="STUDENT REGISTRATION", font=("Arial", 20, "bold"), bg="#53ED8E", fg="#06283D")
title_label.grid(row=0, column=1, sticky="w", padx=10)

Label(title_frame, text="Email: satyamcollegebuddy@gmail.com", font=("Arial", 10), bg="#53ED8E", fg="#06283D").place(x=1025, y=6,anchor="e")

search_entry = Entry(title_frame, font=("Arial", 12),  fg="black")
search_entry.place(x=950, y=33, width=300, anchor="e")
Button(title_frame, text="Search", bg="#53ED8E", fg="#06283D", font=("Arial", 12, "bold"), bd=2, command=search_student).place(x=1025, y=30, anchor="e")

# ---------------- Student Details ----------------
student_frame = LabelFrame(root, text="Student's Details", font=("Arial", 12, "bold"), bg="#53ED8E", padx=10, pady=10)
student_frame.place(x=20, y=100, width=600, height=230)

Label(student_frame, text="Full Name:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=0, column=0, sticky=W, pady=5)
Entry(student_frame, textvariable=full_name_var).grid(row=0, column=1, pady=5, sticky=W)

Label(student_frame, text="Phone:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=0, column=2, sticky=W, pady=5)
Entry(student_frame, textvariable=student_phone_var).grid(row=0, column=3, pady=5,sticky=W)

Label(student_frame, text="Class:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=1, column=0, sticky=W, pady=5)
Combobox(student_frame, textvariable=class_var, values=["BCA", "MCA", "BBA", "MBA"], state="readonly").grid(row=1, column=1, pady=5,sticky=W)

Label(student_frame, text="Date of Birth:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=1, column=2, sticky=W, pady=5)
Entry(student_frame, textvariable=dob_var).grid(row=1, column=3, pady=5, sticky=W)

Label(student_frame, text="Session:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=2, column=0, sticky=W, pady=5)
Entry(student_frame, textvariable=religion_var).grid(row=2, column=1, pady=5,sticky=W)

Label(student_frame, text="Gender:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=2, column=2, sticky=W, pady=5)
Radiobutton(student_frame, text="Male", font=("Arial", 10, "bold"), variable=gender_var, value="Male", bg="#53ED8E", fg="#06283D").grid(row=2, column=3, sticky=W)
Radiobutton(student_frame, text="Female", font=("Arial", 10, "bold"), variable=gender_var, value="Female", bg="#53ED8E", fg="#06283D").grid(row=2, column=3, padx=80)

Label(student_frame, text="Skills:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=3, column=0, sticky=W, pady=5)
Entry(student_frame, textvariable=skills_var).grid(row=3, column=1, pady=5,sticky=W)

# ---------------- Parent Details ----------------
parent_frame = LabelFrame(root, text="Parent's Details", font=("Arial", 12, "bold"), bg="#53ED8E", fg="#06283D", padx=10, pady=10)
parent_frame.place(x=20, y=350, width=600, height=180)

# Row 0
Label(parent_frame, text="Father's Name:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=0, column=0, sticky=W, pady=5, padx=5)
Entry(parent_frame, textvariable=father_name_var, width=25).grid(row=0, column=1, pady=5, padx=5)

Label(parent_frame, text="Phone:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=0, column=2, sticky=W, pady=5, padx=5)
Entry(parent_frame, textvariable=father_phone_var, width=25).grid(row=0, column=3, pady=5, padx=5)

# Row 1
Label(parent_frame, text="Occupation:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=1, column=0, sticky=W, pady=5, padx=5)
Entry(parent_frame, textvariable=father_occ_var, width=25).grid(row=1, column=1, pady=5, padx=5)

Label(parent_frame, text="Mother's Name:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=1, column=2, sticky=W, pady=5, padx=5)
Entry(parent_frame, textvariable=mother_name_var, width=25).grid(row=1, column=3, pady=5, padx=5)

# Row 2
Label(parent_frame, text="Phone:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=2, column=0, sticky=W, pady=5, padx=5)
Entry(parent_frame, textvariable=mother_phone_var, width=25).grid(row=2, column=1, pady=5, padx=5)

Label(parent_frame, text="Occupation:", font=("Arial", 10, "bold"), bg="#53ED8E", fg="#06283D").grid(row=2, column=2, sticky=W, pady=5, padx=5)
Entry(parent_frame, textvariable=mother_occ_var, width=25).grid(row=2, column=3, pady=5, padx=5)

# ---------------- Photo & Buttons ----------------
img = PhotoImage(file="image1.png")
img_label = Label(root, bg="lightgreen", image=img, width=50, height=150)
img_label.place(x=850, y=100, width=175)

Button(root, text="Upload", font=("Arial", 13, "bold"), bg="#53ED8E", fg="#06283D", command=upload_image).place(x=1025, y=290, width=150, anchor="e")
Button(root, text="Save", font=("Arial", 13, "bold"), bg="#53ED8E", fg="#06283D", command=save_data).place(x=1025, y=340, width=150, anchor="e")
Button(root, text="Reset", font=("Arial", 13, "bold"), bg="#53ED8E", fg="#06283D", command=reset_form).place(x=1025, y=390, width=150, anchor="e")
Button(root, text="Exit", font=("Arial", 13, "bold"), bg="#53ED8E", fg="#06283D", command=exit_app).place(x=1025, y=440, width=150, anchor="e")

root.mainloop()
