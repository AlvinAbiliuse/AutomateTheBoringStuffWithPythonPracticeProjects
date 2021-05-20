import pyautogui
import time

pyautogui.PAUSE = 1
def formFiller():
	pyautogui.click(20, 80)
	pyautogui.hotkey('ctrl', 't')

	msg = list('https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform')
	msg.append('enter')
	pyautogui.typewrite(msg)
	time.sleep(5)
	pyautogui.click(281, 173)
	for i in range(2):
		pyautogui.typewrite('\t')
	pyautogui.typewrite('Alvin')
	pyautogui.typewrite('\t')
	pyautogui.typewrite('Heights')
	pyautogui.typewrite('\t')
	pyautogui.typewrite('enter')
	for i in range(2):
		pyautogui.typewrite('down')
	pyautogui.typewrite('enter')
	pyautogui.typewrite('\t')
	for i in range(4):
		pyautogui.typewrite('right')
	for i in range(2):
		pyautogui.typewrite('\t')
	pyautogui.typewrite('No additional comments!')
	
	

if __name__ == "__main__":
	formFiller()
