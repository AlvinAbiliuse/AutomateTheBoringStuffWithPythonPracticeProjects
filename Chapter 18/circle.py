import pyautogui, time

pyautogui.FAILSAFE = True

def arch():
	radius = 60
	vertices = 5
	length = 200
	
	newRad = radius / 5
	newLen = length / 5
	
	x = length
	y = 0
	for i in range(vertices):
		pyautogui.drawRel(x, y, duration=0.2)
		x = x - vertices
		y = y + vertices

arch()
