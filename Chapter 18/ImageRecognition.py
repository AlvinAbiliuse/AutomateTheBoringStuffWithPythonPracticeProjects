import pyautogui
locatedImage = pyautogui.locateOnScreen('ImageRecognitionScreenshot.png')

pyautogui.moveTo(pyautogui.center(locatedImage))
