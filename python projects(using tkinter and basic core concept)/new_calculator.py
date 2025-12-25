from tkinter import *

root = Tk()
root.title("Simple Calculator")
root.geometry("570x590+100+100")
root.resizable(False, False)
root.configure(background="#f5f5f5")  # Light gray background

equation = ""

def show(value):
    global equation
    equation += value
    label_output.config(text=equation)

def clear():
    global equation
    equation = ""
    label_output.config(text=equation)

def calculate():
    global equation
    result = ""
    if equation != "":
        try:
            result = eval(equation)
        except:
            result = "error"
            equation = ""
    label_output.config(text=result)

# Output label
label_output = Label(root, width=30, height=2, text="", font=("arial", 24),bg="white", fg="#333333")  # White display with dark gray text
label_output.pack()

# Row 1 - Operators
button_c = Button(root, text="C", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="white", bg="#007acc", command=lambda: clear())
button_c.place(x=10, y=100)

button_m = Button(root, text="/", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="white", bg="#007acc", command=lambda: show("/"))
button_m.place(x=150, y=100)

button_d = Button(root, text="%", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="white", bg="#007acc", command=lambda: show("%"))
button_d.place(x=290, y=100)

button_mu = Button(root, text="X", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="white", bg="#007acc", command=lambda: show("*"))
button_mu.place(x=430, y=100)

# Row 2
button_7 = Button(root, text="7", width=5, height=1, font=("arial", 30, "bold"), bd=2, fg="#333333", bg="white", command=lambda: show("7"))
button_7.place(x=10, y=200)

button_8 = Button(root, text="8", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("8"))
button_8.place(x=150, y=200)

button_9 = Button(root, text="9", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("9"))
button_9.place(x=290, y=200)

button_mi = Button(root, text="-", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="white", bg="#007acc", command=lambda: show("-"))
button_mi.place(x=430, y=200)

# Row 3
button_4 = Button(root, text="4", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("4"))
button_4.place(x=10, y=300)

button_5 = Button(root, text="5", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("5"))
button_5.place(x=150, y=300)

button_6 = Button(root, text="6", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("6"))
button_6.place(x=290, y=300)

button_p = Button(root, text="+", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="white", bg="#007acc", command=lambda: show("+"))
button_p.place(x=430, y=300)

# Row 4
button_1 = Button(root, text="1", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("1"))
button_1.place(x=10, y=400)

button_2 = Button(root, text="2", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("2"))
button_2.place(x=150, y=400)

button_3 = Button(root, text="3", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("3"))
button_3.place(x=290, y=400)

button_eq = Button(root, text="=", width=5, height=3, font=("arial", 30, "bold"),bd=2, fg="white", bg="#007acc", command=lambda: calculate())
button_eq.place(x=430, y=400)

# Row 5
button_0 = Button(root, text="0", width=11, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("0"))
button_0.place(x=10, y=500)

button_dot = Button(root, text=".", width=5, height=1, font=("arial", 30, "bold"),bd=2, fg="#333333", bg="white", command=lambda: show("."))
button_dot.place(x=290, y=500)

root.mainloop()
