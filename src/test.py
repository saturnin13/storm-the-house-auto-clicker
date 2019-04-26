# import pyscreenshot as ImageGrab
import pyautogui
import cv2
import numpy as np
import time
import os
from PIL import Image

print(cv2.__version__)
# print(pyautogui.size())
time.sleep(1)

# test_coord = (538, 609, 961, 796) #[0, 0, 1680, 1050]
# test_coord = (1080, 590, 1200, 992) # Game coordinate when in "more space" mode
test_coord = (1080, 1080, 1000, 450) # Game coordinate game area

start = time.time()

# im = ImageGrab.grab()

# os.system("screencapture -x -R540,540,500,225 filename.png")
# im = Image.open("filename.png")

im = pyautogui.screenshot(region=test_coord)
# im = pyautogui.screenshot()

end = time.time()
print(end - start)
# print(pyautogui.locateOnScreen("../ressources/game_screenshot.png"))
im.show()

screen = np.array(im)
# print("Shape is:" + str(screen.shape))
screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

# cv2.imshow("screen", screen)
# cv2.waitKey()

















