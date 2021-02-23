import pyautogui

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

while True:
	print(pyautogui.position())
