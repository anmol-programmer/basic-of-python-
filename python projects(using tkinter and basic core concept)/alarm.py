import datetime
import time


def alarm_clock(alarm_time):
    print(f"Alarm is set for {alarm_time}...")
    while True:
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        if current_time == alarm_time:
            print("Wake up! It's time!")
            break
        time.sleep(1)


alarm_time = input("Enter alarm time (HH:MM:SS): ")
alarm_clock(alarm_time, )
