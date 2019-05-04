import time

import cv2
import pyautogui

from constant import BLACK_PIXEL_THRESHOLD, GAME_BOX_COORDINATES, STICKER_SPEED_ADJUSTMENT, \
    SPACE, TIME_SLEEPING_BETWEEN_SHOOTINGS, \
    PYAUTOGUI_ACTION_DELAY, SLEEP_AFTER_SHOOT, SLEEP_AFTER_RELOAD, AMMO_PIXEL_COORDINATES, POSITION_SNIPER_RIFLE, \
    POSITION_CLIP_SIZE_INCREASE, POSITION_DONE_MENU_BUTTON, DISTANCE_FROM_LAST_CLICK, \
    NUMBER_OF_PIXEL_ANALYSE_PER_SCREENSHOT
from macControllers import MouseController, ScreenController, KeyboardController
from utils import Utils


class StormTheHouseAutoClicker:

    def __init__(self):
        self.game_coordinates = GAME_BOX_COORDINATES
        pyautogui.PAUSE = PYAUTOGUI_ACTION_DELAY
        self.startTime = time.time()


    def start(self, activateOnLeftScreenTouch, automaticMenuSkipping):
        self.automaticMenuSkipping = automaticMenuSkipping
        while True:
            mouse_pos = MouseController.queryPosition()
            if mouse_pos.x <= 0 or not activateOnLeftScreenTouch:
                print(str(round(time.time() - self.startTime, 3)) + ": Auto clicker activated")
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
        time. sleep(0.25)
        MouseController.moveTo(self.game_coordinates["x_top_left"], self.game_coordinates["y_top_left"])

    def __startAutoClicker(self):
        while (True):
            time.sleep(TIME_SLEEPING_BETWEEN_SHOOTINGS)
            mousePosition = MouseController.queryPosition()

            if(self.game_coordinates["x_top_left"] <= mousePosition.x <= self.game_coordinates["x_bottom_right"]
                    and self.game_coordinates["y_top_left"] <= mousePosition.y <= self.game_coordinates["y_bottom_right"]):
                print("\n" + str(round(time.time() - self.startTime, 3)) + ": Mouse in the correct position for the autoclicker to analyse screen")
                screen = ScreenController.screenshot(Utils.convertCoordinatesToBox(self.game_coordinates))
                greyScreen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

                if self.__inMenu(greyScreen):
                    if self.automaticMenuSkipping:
                        self.__upgradeStuff()
                else:
                    self.__shootStickmans(greyScreen)
                    if self.__isEmptyAmmo():
                        self.__reloadGun()

    def __reloadGun(self):
        print(str(round(time.time() - self.startTime, 3)) + ": Reloading the gun")
        KeyboardController.keyDown(SPACE)
        time.sleep(0.03)
        KeyboardController.keyUp(SPACE)
        time.sleep(SLEEP_AFTER_RELOAD)

    def __shootStickmans(self, screen):
        print(str(round(time.time() - self.startTime, 3)) + ": Analysing the given screen of the game state and clicking on the black pixels")

        last_found_x = len(screen[0])
        last_found_y = len(screen)

        # Go through the screen from right top doing each column toward the left
        for x in range(len(screen[0]) - 2, -2, -NUMBER_OF_PIXEL_ANALYSE_PER_SCREENSHOT):
            for y in range(0, len(screen), NUMBER_OF_PIXEL_ANALYSE_PER_SCREENSHOT):
                if screen[y][x] < BLACK_PIXEL_THRESHOLD and not (last_found_x - x < DISTANCE_FROM_LAST_CLICK["x"] * 2 and last_found_y - y < DISTANCE_FROM_LAST_CLICK["y"] * 2):
                    actual_x = self.game_coordinates["x_top_left"] + Utils.resizeCoordinateToActualScreen(x)
                    actual_y = self.game_coordinates["y_top_left"] + Utils.resizeCoordinateToActualScreen(y)

                    # print(str(round(time.time() - self.startTime, 3)) + ": Found a black pixel at position (x: " + str(actual_x) + ", y: " + str(actual_y) + ")")

                    self.__shoot(actual_x + STICKER_SPEED_ADJUSTMENT, actual_y)
                    self.__shoot(actual_x + STICKER_SPEED_ADJUSTMENT, actual_y)

                    last_found_x = x
                    last_found_y = y

    def __shoot(self, x, y):
        MouseController.click(x, y)
        time.sleep(SLEEP_AFTER_SHOOT)

    def __inMenu(self, screen):
        mean_gray_scale = sum(sum(y for y in x) for x in screen) / (len(screen) * len(screen[0]))
        return mean_gray_scale < 100 # Value is 49.5 for menu

    def __isEmptyAmmo(self):
        ammoPixel = ScreenController.screenshot(Utils.convertCoordinatesToBox(AMMO_PIXEL_COORDINATES))
        greyAmmoPixel = cv2.cvtColor(ammoPixel, cv2.COLOR_BGR2GRAY)
        print(str(round(time.time() - self.startTime, 3)) + ": Ammo with bar color " + str(greyAmmoPixel[0][0]))

        return greyAmmoPixel[0][0] > 195 # 219 for the empty and 194 for full

    def __upgradeStuff(self):
        MouseController.click(POSITION_SNIPER_RIFLE["x"], POSITION_SNIPER_RIFLE["y"])
        for i in range(0, 200):
            MouseController.click(POSITION_CLIP_SIZE_INCREASE["x"], POSITION_CLIP_SIZE_INCREASE["y"])
        time.sleep(0.25)
        MouseController.click(POSITION_DONE_MENU_BUTTON["x"], POSITION_DONE_MENU_BUTTON["y"])
