import tkinter as tk

# Function to be called when button is clicked
def on_button_click():
    label.config(text="Button was clicked!")


root = tk.Tk()
root.title("Button Example")
root.geometry("400x300")


label = tk.Label(root, text="Click the button below")
label.place(x=50,y=50)


button = tk.Button(root, text="Click Me", command=on_button_click)
button.place(x=75, y=100)


root.mainloop()
