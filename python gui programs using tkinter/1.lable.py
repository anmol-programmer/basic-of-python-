import tkinter as tk
root=tk.Tk()
root.title("New GUI Application")
root.geometry("400x300")
lable = tk.Label(root, text="Welcome to the New GUI Application!")
lable.place(x=19,y=40)
root.mainloop()