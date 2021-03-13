#!/usr/bin/env python3

# mouseNow2.py
# version of mouseNow that uses print statements instead of sys

import pyautogui

try:
	print('Press Ctrl + C to close')
	while True:
		x, y = pyautogui.position()
		r, g, b = pyautogui.screenshot().getpixel((x, y))
		tt = f'x: {x}, y: {y}  RGB: {str(pixelColor[0])}, {str(pixelColor[1])}, {str(pixelColor[2])}'
		print(tt, end='')
		print('\b' * len(tt), end='')
except KeyboardInterrupt:
	print('', end='')
