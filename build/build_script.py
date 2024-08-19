import webbrowser as wb
import random as rd
import pyautogui as pg
import time as tm
import subprocess as sp

def cd(min_t=0.5, max_t=2.0):
    tm.sleep(rd.uniform(min_t, max_t))

def ob():
    wb.register('ch', None, wb.BackgroundBrowser("/Applications/Google\ Chrome.app/Contents/MacOS/Google\ Chrome"))
    wb.get('ch')
    sites = ['https://stackoverflow.com/', 'https://github.com/', 'https://redline-d.redbull.com/', 'https://redline-q.redbull.com/', 'https://engineer.joinbrix.com']
    wb.open(rd.choice(sites))
    cd(5, 10)
    if rd.random() > 0.5:
        pg.scroll(rd.randint(-500, 500))
    pg.press('esc')

def kp():
    seq_len = rd.choice([1, 2, 3])
    keys = ['shift', 'ctrl', 'alt', 'space', 'enter', 'tab']
    for _ in range(seq_len):
        pg.press(rd.choice(keys))
        cd(0.1, 0.4)

def mm():
    w, h = pg.size()
    tx, ty = rd.randint(0, w), rd.randint(0, h)
    dur = rd.uniform(0.5, 3.0)
    steps = rd.randint(5, 15)
    for _ in range(steps):
        jx, jy = rd.randint(-5, 5), rd.randint(-5, 5)
        pg.moveTo(tx + jx, ty + jy, dur / steps)
        cd(0.1, 0.3)
    if rd.random() > 0.7:
        pg.click()

def si():
    print("Taking a break...")
    tm.sleep(rd.uniform(60, 600))

def sa():
    sp.call(["osascript", "-e", 'tell application "Finder" to activate'])
    cd(1, 2)
    if rd.random() > 0.5:
        sp.call(["osascript", "-e", 'tell application "Slack" to activate'])
    elif rd.random() > 0.4:
        sp.call(["osascript", "-e", 'tell application "Microsoft Outlook" to activate'])
    elif rd.random() > 0.3:
        sp.call(["osascript", "-e", 'tell application "Microsoft Teams" to activate'])
    else:
        sp.call(["osascript", "-e", 'tell application "Visual Studio Code" to activate'])
    cd(1, 3)
    if rd.random() > 0.5:
        pg.press('space')
    elif rd.random() > 0.3:
        pg.write("Taking notes", interval=0.2)

acts = [mm, kp, ob, sa, si]

while True:
    act = rd.choices(acts, weights=[0.2, 0.2, 0.2, 0.2, 0.2], k=1)[0]
    print(f"Performing action: {act.__name__}")
    act()
    cd(60, 300)