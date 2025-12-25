import tkinter as tk

# Create main window
root = tk.Tk()
root.title("Traffic Signal Simulation")
root.geometry("500x500")
root.configure(bg="lightgray")

# Create canvas
canvas = tk.Canvas(root, width=500, height=500, bg="lightgray")
canvas.pack()

# Draw traffic light box
canvas.create_rectangle(200, 50, 300, 200, fill="black", outline="white")

# Create red, yellow, and green lights
red_light = canvas.create_oval(220, 60, 280, 100, fill="gray")
yellow_light = canvas.create_oval(220, 100, 280, 140, fill="gray")
green_light = canvas.create_oval(220, 140, 280, 180, fill="gray")

# Draw road
canvas.create_rectangle(0, 365, 500, 400, fill="brown")

# Draw car (rectangle with wheels)
car_body = canvas.create_rectangle(50, 310, 150, 350, fill="blue")
wheel1 = canvas.create_oval(60, 345, 80, 365, fill="black")
wheel2 = canvas.create_oval(120, 345, 140, 365, fill="black")

# Function to update signal
def update_signal(state):
    if state == "move":
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="green")
    elif state == "stop":
        canvas.itemconfig(red_light, fill="red")
        canvas.itemconfig(yellow_light, fill="gray")
        canvas.itemconfig(green_light, fill="gray")
    elif state == "wait":
        canvas.itemconfig(red_light, fill="gray")
        canvas.itemconfig(yellow_light, fill="yellow")
        canvas.itemconfig(green_light, fill="gray")

# Function to move car
def move_car():
    update_signal("wait")
    canvas.update()
    canvas.after(1000)  # wait for yellow signal
    update_signal("move")
    for _ in range(50):
        canvas.move(car_body, 4, 0)
        canvas.move(wheel1, 4, 0)
        canvas.move(wheel2, 4, 0)
        canvas.update()
        
        canvas.after(50)
    update_signal("stop")

# Stop car and signal red
def stop_car():
    update_signal("stop")

# Wait state and signal yellow
def wait_car():
    update_signal("wait")

# Buttons
tk.Button(root, text="Move Car", command=move_car, bg="green", fg="white", width=15).place(x=50, y=430)
tk.Button(root, text="Stop Car", command=stop_car, bg="red", fg="white", width=15).place(x=200, y=430)
tk.Button(root, text="Wait to Start", command=wait_car, bg="yellow", fg="black", width=15).place(x=350, y=430)

root.mainloop()
