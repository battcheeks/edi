# import pyautogui
from pynput.keyboard import Key, Controller
# Holds down the alt key
# pyautogui.keyDown("key.cmd")

# # Presses the tab key once
# pyautogui.press("tab")
# pyautogui.press("tab")

# # Lets go of the alt key
# pyautogui.keyUp("key.cmd")
keyboard = Controller()
keyboard.press('a')
keyboard.press('Key.cmd')
keyboard.release('a')
keyboard.release('Key.cmd')