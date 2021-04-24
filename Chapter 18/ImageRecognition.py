import pyautogui
locatedImage = pyautogui.locateOnScreen('ImageRecognitionScreenshot.png')

print(pyautogui.center(locatedImage))
