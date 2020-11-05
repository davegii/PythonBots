import pyautogui
import time
import keyboard
import win32api, win32con

#Locations for each column in the piano tiles:
#Tile 1: X:  778 Y:  684
#Tile 2: X:  895 Y:  791
#Tile 3: X: 1010 Y:  807
#Tile 4: X: 1161 Y:  816

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

#if the pixel color at each row is black, click on it
while not keyboard.is_pressed('q'):
    if pyautogui.pixel(778,300)[0] == 0:
        click(778,300)
    if pyautogui.pixel(895,300)[0] == 0:
        click(895,300)
    if pyautogui.pixel(1010,300)[0] == 0:
        click(1010,300)
    if pyautogui.pixel(1161,300)[0] == 0:
        click(1161,300)
