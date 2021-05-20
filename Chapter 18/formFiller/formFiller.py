import pyautogui

def formFiller():
	pyautogui.click(20, 80)
	pyautogui.hotkey('ctrl', 't')

	msg = list('https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform')
	msg.append('enter')
	pyautogui.typewrite(msg)



if __name__ == "__main__":
	formFiller()
