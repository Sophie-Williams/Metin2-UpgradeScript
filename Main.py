import pyautogui
import time

while True:
    #selection = input()
    #if selection is "U" or selection is "u":
    pyautogui.moveTo(600,600)
    pyautogui.rightClick()
    for i in range(10):
        pyautogui.click(1640, 907)
        time.sleep(0.2)
        pyautogui.click(1516, 687)
        time.sleep(0.2)
        pyautogui.click(800, 750)
        time.sleep(0.2)
        pyautogui.click(800, 565)
        time.sleep(0.2)
    time.sleep(3)
