import time

from constant import SPACE, COMMAND, ENTER, T_KEY, GAME_LINK, POSITION_PLAY_BUTTON, SPOTLIGHT_CHROME
from macControllers import KeyboardController, MouseController
from stormthehouseautoclicker import StormTheHouseAutoClicker


class ActionController:
    @staticmethod
    def launchStormTheHouse():
        KeyboardController.hotkey(COMMAND, SPACE)
        time.sleep(0.05)
        KeyboardController.typeWrite(SPOTLIGHT_CHROME)
        time.sleep(0.05)
        KeyboardController.press(ENTER)
        time.sleep(0.05)
        KeyboardController.hotkey(COMMAND, T_KEY)
        time.sleep(0.05)
        KeyboardController.typeWrite(GAME_LINK)
        time.sleep(0.05)
        KeyboardController.press(ENTER)
        time.sleep(5)
        MouseController.click(POSITION_PLAY_BUTTON['x'], POSITION_PLAY_BUTTON['y'])

    @staticmethod
    def playStormTheHouse(activateOnLeftScreenTouch, automaticMenuSkipping):
        StormTheHouseAutoClicker().start(activateOnLeftScreenTouch, automaticMenuSkipping)
