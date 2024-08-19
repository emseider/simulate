# switch_applications.py

import subprocess
import random
from custom_delay import custom_delay
import pyautogui

def switch_applications():
    """Switch between applications and perform actions based on current state."""
    subprocess.call(["osascript", "-e", 'tell application "Finder" to activate'])
    custom_delay(1, 2)
    
    if random.random() > 0.5:
        subprocess.call(["osascript", "-e", 'tell application "Slack" to activate'])
    elif random.random() > 0.4:
        subprocess.call(["osascript", "-e", 'tell application "Microsoft Outlook" to activate'])
    elif random.random() > 0.3:
        subprocess.call(["osascript", "-e", 'tell application "Microsoft Teams" to activate'])
    else:
        subprocess.call(["osascript", "-e", 'tell application "Visual Studio Code" to activate'])
    
    custom_delay(1, 3)
    
    if random.random() > 0.5:
        pyautogui.press('space')
    elif random.random() > 0.3:
        pyautogui.write("Taking notes", interval=0.2)
