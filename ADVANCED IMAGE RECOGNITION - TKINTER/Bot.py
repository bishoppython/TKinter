from pyautogui import *
import pyautogui
import time
import keyboard
import random
import win32api, win32con


#X:  553 Y:  686 RGB: (155, 162, 230)
#X:  623 Y:  680 RGB: (253,  18,   1)
#X:  721 Y:  672 RGB: (157, 163, 231)
#X:  832 Y:  666 RGB: (169, 173, 232)

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0,0)
    time.sleep(0.01) #Pausa o script por 0.01 segundos
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0,0)

while keyboard.is_pressed('q') == False:

    if pyautogui.pixel(553, 400)[0] == 0:
        click(553, 400)
    if pyautogui.pixel(623, 400)[0] == 0:
        click(623, 400)
    if pyautogui.pixel(721, 400)[0] == 0:
        click(721, 400)
    if pyautogui.pixel(832, 400)[0] == 0:
        click(832, 400)
