

import pyautogui
import random 
import time

pyautogui.PAUSE = 1
pyautogui.FAILSAFE = True

pyautogui.click(22, 82)
pyautogui.hotkey('ctrl', 't')
pyautogui.click(379, 86)
msg = list('https://docs.google.com/forms/d/e/1FAIpQLScSVDFU76rZvbO_tiIwSt6d9sOK0CZyS9KKMCP6cP5O5W5lVQ/viewform')
msg.append('enter')
pyautogui.typewrite((msg))
time.sleep(3)

# name 
pyautogui.click(270, 252)
pyautogui.typewrite('Dino')
# weakness 
pyautogui.click(277, 330)
pyautogui.typewrite('Handshakes')
# wizard 
pyautogui.click(285, 420)
choice = [(285, 452), (290, 479), (277, 500), (285, 526)]
random.shuffle(choice)
pyautogui.click(choice[0])
# escape 
pyautogui.click(448, 431)
robo  = [(318, 510), (346, 511), (375, 510), (404, 510), (434, 510)]
# addCom 
pyautogui.click(256, 604)
pyautogui.typewrite('No Additional Comments.')
# submit 
pyautogui.moveTo(240, 642)


