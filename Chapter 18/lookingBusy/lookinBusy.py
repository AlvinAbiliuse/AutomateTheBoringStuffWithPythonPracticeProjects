#!/usr/bin/env python3

# lookingBusy.py

import pyautogui

pyautogui.FAILSAFE = True
pyautogui.PAUSE = 10
def busy():
	while True:
		pyautogui.moveRel((0, 5))
		pyautogui.moveRel((0, -5))

if __name__ == "__main__":
	busy()
		
