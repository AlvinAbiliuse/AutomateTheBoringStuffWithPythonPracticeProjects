import pyautogui, time

pyautogui.FAILSAFE = True
time.sleep(5)
pyautogui.click()

def arch():
	radius = 45
	vertices = 45
	length = 300
	
	newRad = radius / vertices
	newLen = length / vertices
	
	x = newLen
	y = 0
	for i in range(vertices):
		pyautogui.dragRel(x, y, duration=0.2)
		x = x - newLen
		y = y + newLen

arch()
