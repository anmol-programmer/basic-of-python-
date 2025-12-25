import datetime
import tkinter as tk

root = tk.Tk()
root.title("Alarm Clock")
root.geometry("300x250")
root.configure(bg="lightblue")


alarm_time = ""

tk.Label(root, text="Set Alarm Time (HH:MM:SS):", bg="lightblue").pack(pady=10)

entry = tk.Entry(root, font=("Helvetica", 14))
entry.pack()

status_label = tk.Label(root, text="", bg="lightblue", fg="blue", font=("Helvetica", 12))
status_label.pack(pady=20)

def check_alarm():
    current_time = datetime.datetime.now().strftime("%H:%M:%S")
    if current_time == alarm_time:
        status_label.config(text=" Wake up! It's time!")
        return
    root.after(1000, check_alarm)

def set_alarm():
    global alarm_time
    
    alarm_time = entry.get()
    datetime.datetime.strptime(alarm_time, "%H:%M:%S")
    status_label.config(text=f" Alarm is set for {alarm_time}")
    check_alarm()
    

tk.Button(root, text="Set Alarm", command=set_alarm).pack(pady=10)

root.mainloop()
