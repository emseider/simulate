# simulate_inactivity.py
import random
import time

def simulate_inactivity():
    # Simulates a pause in activity
    print("Taking a break...")
    time.sleep(random.uniform(60, 600))  # wait between 1 and 10 minutes
