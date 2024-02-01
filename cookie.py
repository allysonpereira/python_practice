from pynput.mouse import Button, Controller
from pynput.keyboard import Key, Listener
import threading
import time
cps = 1000
click_interval = 1/cps  # Change this value to adjust the click interval (in seconds)
is_clicking = False
 
def on_press(key):
    global is_clicking
    if key == Key.f8:
        is_clicking = not is_clicking
        if is_clicking:
            print("Clicking started")
            threading.Thread(target=start_clicking).start()
        else:
            print("Clicking stopped")
 
def start_clicking():
    mouse = Controller()
    while is_clicking:
        mouse.click(Button.left, 1)
        time.sleep(click_interval)
 
def on_release(key):
    if key == Key.esc:
        return False
 
with Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()