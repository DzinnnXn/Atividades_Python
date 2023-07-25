import pyautogui as py
import time
import os

py.press('win')
time.sleep(1)
py.write("google")
time.sleep(2)
py.press("enter")
time.sleep(1)
py.write("google.com")
time.sleep(1)
py.press("enter")
time.sleep(1)
py.write("youtube")
time.sleep(1)
py.press("down")
time.sleep(1)
py.press("enter")
time.sleep(1)
py.press("tab", presses=21)
time.sleep(1)
py.press("enter")
os.system("pause")