# key_press.py

import pyautogui
import random
from custom_delay import custom_delay

def random_key_press():
    """Simulate random key presses with a more complex pattern."""
    sequence_length = random.choice([1, 2, 3])
    keys = ['shift', 'ctrl', 'alt', 'space', 'enter', 'tab']
    
    for _ in range(sequence_length):
        pyautogui.press(random.choice(keys))
        custom_delay(0.1, 0.4)
