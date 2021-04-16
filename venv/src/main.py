import keyboard
import time
from src import controller as c

while True:
    if keyboard.is_pressed('p'):
        try:
            keyboard.press("shift")
            time.sleep(0.1)
            c.testeLoot()
            time.sleep(0.1)
            keyboard.release("shift")
        except Exception as e:
            print(e)
