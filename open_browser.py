# open_browser.py

import webbrowser
import random
from custom_delay import custom_delay
import pyautogui

def open_browser():
    """Simulate opening a browser and performing random actions."""
    webbrowser.register('chrome', None, webbrowser.BackgroundBrowser("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"))
    webbrowser.get('chrome')
    websites = ['https://stackoverflow.com/', 'https://github.com/', 'https://redline-d.redbull.com/', 'https://redline-q.redbull.com/', 'https://engineer.joinbrix.com']
    webbrowser.open(random.choice(websites))
    custom_delay(5, 10)  # Wait for the page to load

    if random.random() > 0.5:
        pyautogui.scroll(random.randint(-500, 500))  # Scroll up or down
    pyautogui.press('esc')  # Close the tab
