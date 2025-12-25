import datetime
import time
import os


def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')
while True:
    while True:
        time.sleep(1)
        clear_terminal()
        current_time = datetime.datetime.now().strftime("%H:%M:%S")
        print(f"Current time is {current_time}")
        break
        