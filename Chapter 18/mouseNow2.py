import pyautogui

try:
	print('Press Ctrl + C to close')
	while True:
		x, y = pyautogui.position()
		tt = f'x: {x}, y: {y}'
		print(tt, end='')
		print('\b' * len(tt), end='')
except KeyboardInterrupt:
	print('', end='')
