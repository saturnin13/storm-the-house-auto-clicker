#! python3
# mouseNow.py - Displays the mouse cursor's current position.
import pyautogui

print('Press Ctrl-C to quit.')

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

def queryMousePosition():
    return pyautogui.position()

def click(x, y):
    pyautogui.click(x, y)

def moveMouseTo(x, y):
    pyautogui.moveTo(x, y)

def PressKey(keyCode):
    pyautogui.keyDown(keyCode)

def ReleaseKey(keyCode):
    pyautogui.keyUp(keyCode)