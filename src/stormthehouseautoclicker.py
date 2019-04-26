import time

import cv2
import pyautogui

from constant import BLACK_PIXEL_THRESHOLD, GAME_BOX_COORDINATES, STICKER_SPEED_ADJUSTMENT, \
    DISTANCE_FROM_LAST_CLICK_X, DISTANCE_FROM_LAST_CLICK_Y, SPACE, TIME_SLEEPING_BETWEEN_SHOOTING, \
    PYAUTOGUI_ACTION_DELAY
from macControllers import MouseController, ScreenController, KeyboardController
from utils import Utils



class StormTheHouseAutoClicker:

    def __init__(self):
        self.game_coordinates = GAME_BOX_COORDINATES
        pyautogui.PAUSE = PYAUTOGUI_ACTION_DELAY


    def start(self, activateOnLeftScreenTouch):
        while True:
            mouse_pos = MouseController.queryPosition()
            if mouse_pos.x <= 0 or not activateOnLeftScreenTouch:
                print("Auto clicker activated")
                self.__circleAroundGameCoordinates()
                self.__startAutoClicker()

    def __circleAroundGameCoordinates(self):
        time.sleep(0.25)
        MouseController.moveTo(self.game_coordinates["x_top_left"], self.game_coordinates["y_top_left"])
        time.sleep(0.25)
        MouseController.moveTo(self.game_coordinates["x_bottom_right"], self.game_coordinates["y_top_left"])
        time.sleep(0.25)
        MouseController.moveTo(self.game_coordinates["x_bottom_right"], self.game_coordinates["y_bottom_right"])
        time.sleep(0.25)
        MouseController.moveTo(self.game_coordinates["x_top_left"], self.game_coordinates["y_bottom_right"])
        time.sleep(0.25)
        MouseController.moveTo(self.game_coordinates["x_top_left"], self.game_coordinates["y_top_left"])

    def __startAutoClicker(self):
        while (True):
            time.sleep(TIME_SLEEPING_BETWEEN_SHOOTING)
            mousePosition = MouseController.queryPosition()

            if(self.game_coordinates["x_top_left"] <= mousePosition.x <= self.game_coordinates["x_bottom_right"]
                    and self.game_coordinates["y_top_left"] <= mousePosition.y <= self.game_coordinates["y_bottom_right"]):
                print("Mouse in the correct position for the autoclicker to analyse screen")
                screen = ScreenController.screenshot(Utils.convertCoordinatesToBox(self.game_coordinates))
                greyScreen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)
                self.__shootStickmans(greyScreen)
                self.__reloadGun()

    def __reloadGun(self):
        print("Reloading the gun")
        KeyboardController.keyDown(SPACE)
        time.sleep(0.05)
        KeyboardController.keyUp(SPACE)

    def __shootStickmans(self, screen):
        print("Analysing the given screen of the game state and clicking on the black pixels")

        last_found_x = 0
        last_found_y = 0

        for y in range(0, len(screen), 2):
            for x in range(0, len(screen[y]), 2):
                if screen[y][x] < BLACK_PIXEL_THRESHOLD and not (x - last_found_x < DISTANCE_FROM_LAST_CLICK_X and y - last_found_y < DISTANCE_FROM_LAST_CLICK_Y):
                    actual_x = self.game_coordinates["x_top_left"] + Utils.resizeCoordinateToActualScreen(x)
                    actual_y = self.game_coordinates["y_top_left"] + Utils.resizeCoordinateToActualScreen(y)

                    # print("Found a black pixel at position (x: " + str(actual_x) + ", y: " + str(actual_y) + ")")

                    start = time.time()
                    MouseController.click(actual_x + STICKER_SPEED_ADJUSTMENT, actual_y)
                    MouseController.click(actual_x + STICKER_SPEED_ADJUSTMENT, actual_y)
                    end = time.time()


                    print(end - start)

                    last_found_x = x
                    last_found_y = y



