#!/usr/bin/env python3

# mouseNow2.py
# version of mouseNow that uses print statements instead of sys

import pyautogui
import time

try:
	print('Press Ctrl + C to close')
	while True:
		x, y = pyautogui.position()
		r, g, b = pyautogui.screenshot().getpixel((x, y))
		tt = f'x: {x}, y: {y}  RGB: {str(r)}, {str(g)}, {str(b)}'
		print(tt, end='', flush=True)
		print('\b' * len(tt), end='')
except KeyboardInterrupt:
	print('', end='')
