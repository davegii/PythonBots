import pyautogui
import time
import keyboard
import win32api, win32con

def click(x,y):
    win32api.SetCursorPos((x,y))
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.01)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0)

# Region for the aimbooster: region=(580,430,750,520)

while keyboard.is_pressed('q') == False:
    pic = pyautogui.screenshot(region=(580,430,750,520))
    width,height = pic.size

    for x in range(0, width, 5):
        for y in range(0, height, 5):
            r,g,b = pic.getpixel((x,y))
            if b == 195 and r == 255:
                click(x+580,y+430)
                time.sleep(.05)
                break
        if b == 195 and r == 255:
            break