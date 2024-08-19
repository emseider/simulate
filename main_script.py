# main_script.py

import random

from mouse_movement import random_mouse_movement
from key_press import random_key_press
from open_browser import open_browser
from switch_applications import switch_applications
from simulate_inactivity import simulate_inactivity
from custom_delay import custom_delay

actions = [
    random_mouse_movement,
    random_key_press,
    open_browser,
    switch_applications,
    simulate_inactivity
]

while True:
    action = random.choices(actions, weights=[0.2, 0.2, 0.2, 0.2, 0.2], k=1)[0]
    # action = random.choice(actions)
    print(f"Performing action: {action.__name__}")
    action()

    # Introduce a human-like delay between actions
    custom_delay(60, 300)  # Between 1 and 5 minutes
