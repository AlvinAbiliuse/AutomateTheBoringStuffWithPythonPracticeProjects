import pyautogui, time

pyautogui.FAILSAFE = True
time.sleep(5)
pyautogui.click()

def arch():
	radius = 60
	vertices = 5
	length = 200
	
	newRad = radius / 5
	newLen = length / 5
	
	x = length
	y = 0
	for i in range(vertices):
		pyautogui.dragRel(x, y, duration=0.2)
		x = x - vertices
		y = y + vertices

arch()
