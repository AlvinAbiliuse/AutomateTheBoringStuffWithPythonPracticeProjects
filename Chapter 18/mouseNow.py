import pyautogui
import sys
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

while True:
	x, y = pyautogui.position()
	position = f'x={x}, y={y}'
	sys.stdout.write(position)
	sys.stdout.flush()
	sys.stdout.write('\b' * len(position))
