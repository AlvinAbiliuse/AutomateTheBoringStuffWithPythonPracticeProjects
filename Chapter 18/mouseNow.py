import pyautogui
import sys
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

while True:
	position = str(pyautogui.position())
	sys.stdout.write(position)
	sys.stdout.flush()
	sys.stdout.write('\b' * len(position))
