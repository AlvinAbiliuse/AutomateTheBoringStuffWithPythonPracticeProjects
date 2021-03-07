import pyautogui, time

time.sleep(5)

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True
pyautogui.click()
distance = 200
while distance > 0:
	pyautogui.dragRel(distance, 0, duration=0.2) # Move Right
	distance = distance - 5
	pyautogui.dragRel(0, distance, duration=0.2) # Move Down
	pyautogui.dragRel(-distance, 0, duration=0.2) # Move Left
	distance = distance - 5
	pyautogui.dragRel(0, -distance, duration=0.2) # Move Up
