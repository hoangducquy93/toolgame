import pyautogui
import numpy as np 
import time 
import cv2
import matplotlib.pyplot as plt 
import matplotlib.image as mpimg

pyautogui.PAUSE = 1

iteration = 100
#x,y = pyautogui.position()
#print(x,y)
for i in range(iteration):
	count=0
	click_forge = pyautogui.click(x=763,y=566,clicks = 1)
	img = pyautogui.screenshot('img1.png',region=(1017,567,25,16))

	img = cv2.imread('img1.png',1)
	print(img.shape)
	height = 16
	width = 25
	hsv_img = cv2.cvtColor(img,cv2.COLOR_BGR2HSV)

	low_green = np.array([25, 52, 72])
	high_green = np.array([102, 255, 255])
	green_mask = cv2.inRange(hsv_img, low_green, high_green)
	green = cv2.bitwise_and(img, img, mask=green_mask)
	cv2.imwrite('img1.png',green)
	'''
	for m in range(height):
		if count==1:
			break
		for n in range(width):
			if green[m][n][1] != 0:
				move_to_change = pyautogui.click(x=833,y=567,clicks = 1)	
				count=count + 1
				print('i am at m:',m,'n:',n,'iteration=',i)
				break
	time.sleep(0.5)
	'''
if pyautogui.doubleClick(button='right') == True:
	pyautogui.hotkey('ctrl','c')



'''
print('Img Dimension:',dimension)
print('Img Height:',height)
print('Img Width:',width)
print('Img Channel:',channel)
'''

'''	

pyautogui.PAUSE = 2
for i in range(10):
	move_to_1 = pyautogui.click(x=308,y=525,clicks = 1)
	if pyautogui.pixelMatchesColor(309, 662, (0, 120, 0)) == True:
		move_to_plus = pyautogui.click(x=663,y=528,clicks = 1)
	elif pyautogui.pixelMatchesColor(309, 662, (0, 120, 0)) == False:
		move_to_minus = pyautogui.click(x=661,y=459,clicks=1)
	move_to_1 = pyautogui.click(x=308,y=525,clicks = 1)
	move_to_equal = pyautogui.click(x=671,y=590,clicks = 1)
'''