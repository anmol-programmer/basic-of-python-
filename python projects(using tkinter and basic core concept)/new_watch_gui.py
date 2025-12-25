import tkinter as tk
import math
import datetime

# Create main window
root = tk.Tk()
root.title("Satyam Digital Clock")
root.configure(bg="black")

canvas = tk.Canvas(root, width=400, height=400, bg="black", highlightthickness=3)
canvas.pack()

# Draw clock face
def draw_clock_face():
    canvas.create_oval(50, 50, 350, 350, outline="white", width=4)

    for i in range(12):
        angle = math.radians(i * 30 - 90)
        x_outer = 200 + 140 * math.cos(angle)
        y_outer = 200 + 140 * math.sin(angle)
        x_inner = 200 + 120 * math.cos(angle)
        y_inner = 200 + 120 * math.sin(angle)
        canvas.create_line(x_inner, y_inner, x_outer, y_outer, fill="white", width=3)

      
        num_x = 200 + 110 * math.cos(angle)
        num_y = 200 + 110 * math.sin(angle)
        canvas.create_text(num_x, num_y, text=str(i if i != 0 else 12),
                           fill="white", font=("Helvetica", 14, "bold"))

# Update hands every second
def update_clock():
    canvas.delete("hands")
    now = datetime.datetime.now()
    sec = now.second
    minute = now.minute
    hour = now.hour % 12

    center_x, center_y = 200, 200

    # Second hand
    sec_angle = math.radians(sec * 6 - 90)
    sec_x = center_x + 130 * math.cos(sec_angle)
    sec_y = center_y + 130 * math.sin(sec_angle)
    canvas.create_line(center_x, center_y, sec_x, sec_y, fill="red", width=1, tags="hands")

    # Minute hand
    min_angle = math.radians(minute * 6 - 90)
    min_x = center_x + 110 * math.cos(min_angle)
    min_y = center_y + 110 * math.sin(min_angle)
    canvas.create_line(center_x, center_y, min_x, min_y, fill="white", width=3, tags="hands")

    # Hour hand
    hour_angle = math.radians((hour * 30 + minute * 0.5) - 90)
    hour_x = center_x + 80 * math.cos(hour_angle)
    hour_y = center_y + 80 * math.sin(hour_angle)
    canvas.create_line(center_x, center_y, hour_x, hour_y, fill="white", width=5, tags="hands")

    root.after(1000, update_clock)

draw_clock_face()
update_clock()
root.mainloop()
