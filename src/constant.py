#! python3

POSITION_PLAY_BUTTON = {'x': 1000, 'y': 658}
POSITION_CLIP_SIZE_INCREASE = {'x': 600, 'y': 464}
POSITION_SNIPER_RIFLE = {'x': 850, 'y': 464}
POSITION_DONE_MENU_BUTTON = {'x': 800, 'y': 760}

GAME_BOX_COORDINATES = {"x_top_left": 540, "y_top_left": 640, "x_bottom_right": 1040, "y_bottom_right": 765} # {"top": 540, "left": 540, "width": 500, "height": 225}
AMMO_PIXEL_COORDINATES = {"x_top_left": 575, "y_top_left": 379, "x_bottom_right": 576, "y_bottom_right": 380} # {"top": 540, "left": 540, "width": 500, "height": 225}

BLACK_PIXEL_THRESHOLD = 10
DISTANCE_FROM_LAST_CLICK = {'x': 35, 'y': 35} # Dead stickmans are 64 x 10 and standing ones are 25 x 53
STICKER_SPEED_ADJUSTMENT = 0
NUMBER_OF_PIXEL_ANALYSE_PER_SCREENSHOT = 3

TIME_SLEEPING_BETWEEN_SHOOTINGS = 0.1
SLEEP_AFTER_SHOOT = 0.00001
SLEEP_AFTER_RELOAD = 1.00
CLICK_POSITION_LATENCY = 0.00001

GAME_LINK = "https://www.crazygames.com/game/storm-the-house"

SPOTLIGHT_CHROME = "google chrome.app"

SPACE = "space"
COMMAND = "command"
ENTER = "enter"
T_KEY = "t"

PYAUTOGUI_ACTION_DELAY = 0