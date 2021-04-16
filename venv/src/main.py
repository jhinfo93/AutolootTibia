
from src import controller

while True:
    if keyboard.is_pressed('p'):
        try:
            keyboard.press("shift")
            time.sleep(0.1)
            testeLoot()
            time.sleep(0.1)
            keyboard.release("shift")
        except Exception as e:
            print(e)
