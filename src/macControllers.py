#! python3
import numpy

import mss
import pyautogui
import time
import constant

# print(pyautogui.__version__)
# print('Press Ctrl-C to quit.')

# try:
#     while True:
#         # Get and print the mouse coordinates.
#         print("la")
#         x, y = pyautogui.position()
#         positionStr = 'X: ' + str(x).rjust(4) + ' Y: ' + str(y).rjust(4)
# except KeyboardInterrupt:
#     print('\nDone.')
#
# print(positionStr, end='')
# print('\b' * len(positionStr), end='', flush=True)

# for i in range(2):
#   pyautogui.moveTo(100, 100, duration=0.25)
#   pyautogui.moveTo(200, 100, duration=0.25)
#   pyautogui.moveTo(200, 200, duration=0.25)
#   pyautogui.moveTo(100, 200, duration=0.25)
#
# print(pyautogui.position())

print(pyautogui.size())
print(pyautogui.position())

class MouseController:
    @staticmethod
    def queryPosition():
        return pyautogui.position()

    @staticmethod
    def click(x, y):
        pyautogui.click(x, y)

    @staticmethod
    def moveTo(x, y):
        pyautogui.moveTo(x, y)

class KeyboardController:
    @staticmethod
    def keyDown(keyCode):
        pyautogui.keyDown(keyCode)

    @staticmethod
    def keyUp(keyCode):
        pyautogui.keyUp(keyCode)

    @staticmethod
    def press(keyCode):
        pyautogui.press(keyCode)

    @staticmethod
    def typeWrite(text):
        pyautogui.typewrite(text)

    @staticmethod
    def hotkey(*keyCodes):
        pyautogui.hotkey(*keyCodes)

class ScreenController:
    @staticmethod
    def screenshot(box_coordinates=None):
        with mss.mss() as sct:
            if(box_coordinates):
                return numpy.array(sct.grab(box_coordinates))
            else:
                return numpy.array(sct.grab())





