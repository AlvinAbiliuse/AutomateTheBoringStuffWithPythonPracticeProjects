import pyautogui, time

pyautogui.FAILSAFE = True
time.sleep(5)
pyautogui.click()

def arc():
	radius = 45
	vertices = 10
	length = 300
	
	newRad = radius / vertices
	newLen = length / vertices
	
	print(f'newRad: {newRad}')
	print(f'newLen: {newLen}', end='\n\n')
	
	x = newLen
	y = 0
	for i in range(vertices):
		pyautogui.dragRel(x, y, duration=0.2)
		print(f'x: {x}')
		print(f'y: {y}', end='\n\n')
		x = x - newRad
		y = y + newRad
		

arc()
