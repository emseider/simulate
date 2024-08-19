# custom_delay.py

import time
import random

def custom_delay(min_time=0.5, max_time=2.0):
    """Simulate a human-like delay with random intervals."""
    time.sleep(random.uniform(min_time, max_time))
