#Hey Johnathan, if your reading this, your prob wondering how the code works
#its based off ducky script (the worlds easiet code) which injects keystrokes.

import time
import pyautogui
from pyautogui import press,typewrite, hotkey, alert
alert(text='So gullible...', title='Never click on exes', button='Yes sir')
pyautogui.hotkey('win', "r")
time.sleep(0.05)
pyautogui.write("https://youtu.be/fC7oUOUEEi4")
time.sleep(0.05)
pyautogui.press("enter")
