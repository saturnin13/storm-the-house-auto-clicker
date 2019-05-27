#! python3
import numpy

import mss
import pyautogui
from pynput.mouse import Button, Controller
import time
from constant import BLACK_PIXEL_THRESHOLD, CLICK_POSITION_LATENCY

print(pyautogui.size())
print(pyautogui.position())


class MouseController:
    mouse = Controller()

    @staticmethod
    def queryPosition():
        return pyautogui.position()

    @staticmethod
    def click(x, y):
        # pyautogui.click(x, y)
        MouseController.mouse.position = (x, y)
        time.sleep(CLICK_POSITION_LATENCY)
        MouseController.mouse.click(Button.left, 1)

    @staticmethod
    def moveTo(x, y):
        # pyautogui.moveTo(x, y)
        MouseController.mouse.position = (x, y)


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
            if box_coordinates:
                return numpy.array(sct.grab(box_coordinates))
            else:
                return numpy.array(sct.grab())





