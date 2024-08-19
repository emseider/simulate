# mouse_movement.py

import pyautogui
import random
from custom_delay import custom_delay

def random_mouse_movement():
    """Move mouse to a random location with human-like pauses and unpredictability."""
    width, height = pyautogui.size()
    target_x = random.randint(0, width)
    target_y = random.randint(0, height)
    duration = random.uniform(0.5, 3.0)
    
    # Add some jitter to the mouse movement
    steps = random.randint(5, 15)
    for _ in range(steps):
        jitter_x = random.randint(-5, 5)
        jitter_y = random.randint(-5, 5)
        pyautogui.moveTo(target_x + jitter_x, target_y + jitter_y, duration / steps)
        custom_delay(0.1, 0.3)

    if random.random() > 0.7:
        pyautogui.click()
