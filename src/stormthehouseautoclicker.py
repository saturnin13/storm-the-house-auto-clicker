import logging
import time

import cv2
import pyautogui

from constant import BLACK_PIXEL_THRESHOLD, STICKER_SPEED_ADJUSTMENT, \
    SPACE, TIME_SLEEPING_BETWEEN_SHOOTINGS, PYAUTOGUI_ACTION_DELAY, \
    SLEEP_AFTER_SHOOT, SLEEP_AFTER_RELOAD, \
    DISTANCE_FROM_LAST_CLICK, NUMBER_OF_PIXEL_ANALYSE_PER_SCREENSHOT, \
    get_constant
from macControllers import MouseController, ScreenController, KeyboardController
from utils import ElapsedFormatter, convertCoordinatesToBox, resizeCoordinateToActualScreen


class StormTheHouseAutoClicker:
    def __init__(self, player='sat', log_level=logging.INFO):
        self.game_coordinates = get_constant('GAME_BOX_COORDINATES', player)
        self.ammo_coordinates = get_constant('AMMO_PIXEL_COORDINATES', player)
        self.clip_button_coordinates = get_constant('POSITION_CLIP_SIZE_INCREASE', player)
        self.done_button_coordinates = get_constant('POSITION_DONE_MENU_BUTTON', player)
        self.sniper_button_coordinates = get_constant('POSITION_SNIPER_RIFLE', player)
        pyautogui.PAUSE = PYAUTOGUI_ACTION_DELAY
        self.startTime = time.time()
        self.logger = logging.getLogger()
        ElapsedFormatter.add_handler(self.logger)
        self.logger.setLevel(log_level)

    def start(self, activateOnLeftScreenTouch, automaticMenuSkipping):
        self.automaticMenuSkipping = automaticMenuSkipping
        while True:
            mouse_pos = MouseController.queryPosition()
            if mouse_pos.x <= 0 or not activateOnLeftScreenTouch:
                self.logger.info("Auto clicker activated")
                self.__circleAroundGameCoordinates()
                self.__startAutoClicker()

    def __circleAroundGameCoordinates(self):
        sleep_sec = 0.5
        MouseController.moveTo(self.game_coordinates["x_top_left"], self.game_coordinates["y_top_left"])
        time.sleep(sleep_sec)
        MouseController.moveTo(self.game_coordinates["x_bottom_right"], self.game_coordinates["y_top_left"])
        time.sleep(sleep_sec)
        MouseController.moveTo(self.game_coordinates["x_bottom_right"], self.game_coordinates["y_bottom_right"])
        time.sleep(sleep_sec)
        MouseController.moveTo(self.game_coordinates["x_top_left"], self.game_coordinates["y_bottom_right"])
        time.sleep(sleep_sec)
        MouseController.moveTo(self.game_coordinates["x_top_left"], self.game_coordinates["y_top_left"])

    def __startAutoClicker(self):
        while True:
            time.sleep(TIME_SLEEPING_BETWEEN_SHOOTINGS)
            mouse_position = MouseController.queryPosition()

            if not self.is_mouse_in_game_box(mouse_position):
                self.logger.info("Mouse NOT in game box - skipping.")
                continue

            screen = ScreenController.screenshot(convertCoordinatesToBox(self.game_coordinates))
            grey_screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)

            if self.__inMenu(grey_screen):
                if self.automaticMenuSkipping:
                    self.__upgradeStuff()
            else:
                self.__shootStickmans(grey_screen)

    def is_mouse_in_game_box(self, mousePosition):
        return self.game_coordinates["x_top_left"] <= mousePosition.x <= \
               self.game_coordinates["x_bottom_right"] \
               and self.game_coordinates["y_top_left"] <= mousePosition.y <= \
               self.game_coordinates["y_bottom_right"]

    def __reloadGun(self):
        self.logger.info("Reloading the gun")
        KeyboardController.keyDown(SPACE)
        time.sleep(0.03)
        KeyboardController.keyUp(SPACE)
        time.sleep(SLEEP_AFTER_RELOAD)

    def __shootStickmans(self, screen):
        self.logger.info("Analysing the given screen of the game state and clicking on the black pixels")

        last_found_x = len(screen[0])
        last_found_y = len(screen)
        did_shoot = False

        # Go through the screen from right top doing each column toward the left
        for x in reversed(range(0, len(screen[0]), NUMBER_OF_PIXEL_ANALYSE_PER_SCREENSHOT)):
            for y in range(0, len(screen), NUMBER_OF_PIXEL_ANALYSE_PER_SCREENSHOT):

                if screen[y][x] < BLACK_PIXEL_THRESHOLD and \
                        not (last_found_x - x < DISTANCE_FROM_LAST_CLICK["x"] * 2 and
                             last_found_y - y < DISTANCE_FROM_LAST_CLICK["y"] * 2):
                    actual_x = self.game_coordinates["x_top_left"] + resizeCoordinateToActualScreen(x)
                    actual_y = self.game_coordinates["y_top_left"] + resizeCoordinateToActualScreen(y)

                    self.logger.debug("Found a black pixel at position (x:%d, y:%d)", actual_x, actual_y)

                    self.__shoot(actual_x + STICKER_SPEED_ADJUSTMENT, actual_y)
                    self.__shoot(actual_x + STICKER_SPEED_ADJUSTMENT, actual_y)

                    did_shoot = True
                    last_found_x = x
                    last_found_y = y

        # Reload when idle or empty ammo
        if not did_shoot or self.__isEmptyAmmo():
            self.__reloadGun()

    def __shoot(self, x, y):
        MouseController.click(x, y)
        time.sleep(SLEEP_AFTER_SHOOT)

    def __inMenu(self, screen):
        mean_gray_scale = sum(sum(y for y in x) for x in screen) / (len(screen) * len(screen[0]))
        return mean_gray_scale < 100  # Value is 49.5 for menu

    def __isEmptyAmmo(self):
        ammo_pixel = ScreenController.screenshot(convertCoordinatesToBox(self.ammo_coordinates))
        grey_ammo_pixel = cv2.cvtColor(ammo_pixel, cv2.COLOR_BGR2GRAY)[0][0]
        self.logger.info("Ammo with bar color %d", grey_ammo_pixel)

        # return grey_ammo_pixel <= 120  # 114 for the empty and 243 for full <-- for Louis Blin's Mac
        return grey_ammo_pixel > 195  # 219 for the empty and 194 for full

    def __upgradeStuff(self):
        MouseController.click(self.sniper_button_coordinates["x"], self.sniper_button_coordinates["y"])
        for i in range(200):
            MouseController.click(self.clip_button_coordinates["x"], self.clip_button_coordinates["y"])
        time.sleep(0.25)
        MouseController.click(self.done_button_coordinates["x"], self.done_button_coordinates["y"])
