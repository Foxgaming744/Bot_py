import pyautogui
import time

sellLoop = 1
actionLoop = 1

sellWait = 45
actionWait = 300

while sellLoop == 1:
    print("Waiting to perform actions...")
    time.sleep(sellWait)
    print("Executing actions...")

    pyautogui.typewrite(";sell")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.typewrite(";hunt")
    pyautogui.press("enter")
    time.sleep(1)
    pyautogui.typewrite(";fish")
    pyautogui.press("enter")

    print("Done! Looping...")
