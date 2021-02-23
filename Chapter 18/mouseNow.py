#!/usr/bin/env python3

# mouseNow.py
# this version uses sys to use backspace but apparently this could be
# achieved with print statements as well. Will learn how to do so.


import pyautogui
import sys

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

try:
	print('Press Ctrl + C to exit')
	while True:
		x, y = pyautogui.position()
		position = f'x={x}, y={y}  '
		sys.stdout.write(position)
		sys.stdout.flush()
		sys.stdout.write('\b' * len(position))
except KeyboardInterrupt:
	print('', end='')
