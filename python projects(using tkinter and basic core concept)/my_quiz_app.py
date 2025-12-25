import tkinter as tk

root = tk.Tk()
root.title("Quiz Application")
root.geometry("600x500")
root.configure(bg="lightblue")


status_label = tk.Label(root, text="", fg="blue", bg="lightgreen")
status_label.pack(side="right", fill=tk.Y)

user_name = ""
roll_number = ""
class_name = ""

def setup_user_info():
    clear_window()
    tk.Label(root, text="Enter Your Details", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

    tk.Label(root, text="Name:", bg="lightblue").pack()
    name_entry = tk.Entry(root)
    name_entry.pack()

    tk.Label(root, text="Roll Number:", bg="lightblue").pack()
    roll_entry = tk.Entry(root)
    roll_entry.pack()

    tk.Label(root, text="Class:", bg="lightblue").pack()
    class_entry = tk.Entry(root)
    class_entry.pack()

    def save_user_info():
        nonlocal name_entry, roll_entry, class_entry
        global user_name, roll_number, class_name

        user_name = name_entry.get().strip()
        roll_number = roll_entry.get().strip()
        class_name = class_entry.get().strip()

        if not user_name or not roll_number or not class_name:
            status_label.config(text="Please fill all fields!", fg="red")
            return

        status_label.config(text=f"Welcome {user_name}!", fg="green")
        main_menu()

    tk.Button(root, text="Submit", command=save_user_info).pack(pady=10)

def main_menu():
    clear_window()
    tk.Label(root, text="Quiz Application Menu", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=20)

    tk.Button(root, text="1. Add New Question", width=30, command=add_question).pack(pady=5)
    tk.Button(root, text="2. Start Quiz", width=30, command=start_quiz).pack(pady=5)
    tk.Button(root, text="3. View Quiz Results", width=30, command=view_results).pack(pady=5)
    tk.Button(root, text="4. Clear All Data", width=30, command=clear_files).pack(pady=5)
    tk.Button(root, text="5. Exit", width=30, command=root.quit).pack(pady=5)

def clear_window():
    for widget in root.winfo_children():
        if widget != status_label:
            widget.destroy()

def add_question():
    clear_window()
    tk.Label(root, text="Add New Question", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)

    labels = ["Question", "Option a", "Option b", "Option c", "Option d", "Correct option (a/b/c/d)"]
    entries = {}

    for label in labels:
        tk.Label(root, text=label, bg="lightblue").pack()
        entry = tk.Entry(root, width=50)
        entry.pack()
        entries[label] = entry

    def save_question():
        q = entries["Question"].get().strip()
        a = entries["Option a"].get().strip()
        b = entries["Option b"].get().strip()
        c = entries["Option c"].get().strip()
        d = entries["Option d"].get().strip()
        correct = entries["Correct option (a/b/c/d)"].get().strip().lower()

        if not q or not a or not b or not c or not d or correct not in ['a', 'b', 'c', 'd']:
            status_label.config(text="Please fill all fields correctly!", fg="red")
            return

        with open("questions.txt", "a") as f:
            f.write(f"{q}\n")
            f.write(f"a) {a}\n")
            f.write(f"b) {b}\n")
            f.write(f"c) {c}\n")
            f.write(f"d) {d}\n")
            f.write(f"Answer) {correct}\n\n")

        status_label.config(text="Question saved successfully!", fg="green")
        main_menu()

    tk.Button(root, text="Save Question", command=save_question).pack(pady=10)

def start_quiz():
    clear_window()
    questions = []
    with open("questions.txt", "r") as f:
            lines = [line.strip() for line in f if line.strip()]

    i = 0
    while i < len(lines):
        if i + 5 >= len(lines):
            break  
        question = lines[i]
        options = [lines[i+1][3:], lines[i+2][3:], lines[i+3][3:], lines[i+4][3:]]  
        correct = lines[i+5].split(") ")[1] 
        questions.append((question, options, correct))
        i += 6

    if not questions:
        status_label.config(text="No questions available!", fg="red")
        return

    current_index = [0]  # using list for mutability in inner function
    selected_option = tk.StringVar()
    score = [0]

    def display_question():
        clear_window()
        q, opts, _ = questions[current_index[0]]
        tk.Label(root, text=f"Q{current_index[0]+1}. {q}", font=("Arial", 14, "bold"), bg="lightblue", wraplength=550).pack(pady=10)

        selected_option.set(None) 

        for i, opt in zip("abcd", opts):
            tk.Radiobutton(root, text=opt, variable=selected_option, value=i, bg="lightblue").pack(anchor="w", padx=20)

        tk.Button(root, text="Next", command=next_question).pack(pady=10)

    def next_question():
        if not selected_option.get():
            status_label.config(text="Please select an option!", fg="red")
            return

        _, _, correct = questions[current_index[0]]
        if selected_option.get() == correct:
            score[0] += 1

        current_index[0] += 1
        if current_index[0] < len(questions):
            display_question()
        else:
            show_result()

    def show_result():
        clear_window()
        total = len(questions)
        tk.Label(root, text=f"Quiz Completed!", font=("Arial", 16, "bold"), bg="lightblue").pack(pady=10)
        tk.Label(root, text=f"Name: {user_name}\nRoll No: {roll_number}\nClass: {class_name}", bg="lightblue").pack(pady=5)
        tk.Label(root, text=f"Score: {score[0]} / {total}", font=("Arial", 14), bg="lightblue").pack(pady=10)
        
        with open("quiz_results.txt", "a") as f:
            f.write(f"{user_name}, Roll: {roll_number}, Class: {class_name}, Score: {score[0]}/{total}\n")

        tk.Button(root, text="Back to Menu", command=main_menu).pack(pady=10)
        status_label.config(text="Quiz Completed!", fg="green")

    display_question()


def view_results():
    clear_window()
    with open("quiz_results.txt", "r") as f:
            results = f.read()

    tk.Label(root, text="Quiz Results", font=("Arial", 14), bg="lightblue").pack(pady=10)
    result_text = tk.Text(root, wrap=tk.WORD, height=15)
    result_text.insert(tk.END, results)
    result_text.config(state=tk.DISABLED)
    result_text.pack(padx=10, pady=10)
    tk.Button(root, text="Back to Menu", command=main_menu).pack(pady=10)

def clear_files():
    open("questions.txt", "w").close()
    open("quiz_results.txt", "w").close()
    status_label.config(text="All data has been cleared.", fg="green")
    main_menu()

# Start the app
setup_user_info()
root.mainloop()
