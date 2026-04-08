import os
import time

def clear():
    os.system("cls" if os.name == "nt" else "clear")

def delay(speed):
    if speed == 1:
        time.sleep(0.5)
    elif speed == 2:
        time.sleep(0.2)
    else:
        time.sleep(0.05)