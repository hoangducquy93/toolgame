import pyautogui
target = pyautogui.locateOnScreen('capture.png')
print(target)
print(pyautogui.position())

if pyautogui.doubleClick(button='right') == True:
	pyautogui.hotkey('ctrl','c')
if pyautogui.doubleClick(button='right') == True:
	pyautogui.hotkey('ctrl','c')
