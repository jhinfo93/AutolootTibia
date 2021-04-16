import mouse
import time
import keyboard


def testeLoot():
    mouse.move(546, 299)
    print("1")
    mouse.move(546, 255)
    print("2")
    mouse.move(591, 255)
    print("3")
    mouse.move(593, 346)
    print("4")
    mouse.move(637, 256)
    print("5")
    mouse.move(637, 298)
    print("6")
    mouse.move(635, 344)
    print("7")
    mouse.move(543, 345)
    print("8")


def pegarLoot():
    mouse.right_click(546, 299)
    mouse.right_click(546, 255)
    mouse.right_click(591, 255)
    mouse.right_click(593, 346)
    mouse.right_click(637, 256)
    mouse.right_click(637, 298)
    mouse.right_click(635, 344)
    mouse.right_click(543, 345)
