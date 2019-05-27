#! python3


########### Hardcoded ###########

POSITION_PLAY_BUTTON = {'x': 1000, 'y': 658}


def get_constant(constant, player):
    return {
        'sat': {
            'GAME_BOX_COORDINATES': {
                "x_top_left": 540, "y_top_left": 640, "x_bottom_right": 1040, "y_bottom_right": 765
            },
            'AMMO_PIXEL_COORDINATES': {
                "x_top_left": 575, "y_top_left": 379, "x_bottom_right": 576, "y_bottom_right": 380
            },
            'POSITION_CLIP_SIZE_INCREASE': {
                'x': 600, 'y': 464
            },
            'POSITION_SNIPER_RIFLE': {
                'x': 850, 'y': 464
            },
            'POSITION_DONE_MENU_BUTTON': {
                'x': 800, 'y': 760
            },
        },
        'louis': {
            'GAME_BOX_COORDINATES': {
                "x_top_left": 170, "y_top_left": 600, "x_bottom_right": 665, "y_bottom_right": 786
            },
            'AMMO_PIXEL_COORDINATES': {
                "x_top_left": 179, "y_top_left": 379, "x_bottom_right": 180, "y_bottom_right": 380
            },
            'POSITION_CLIP_SIZE_INCREASE': {
                'x': 236, 'y': 460
            },
            'POSITION_SNIPER_RIFLE': {
                'x': 490, 'y': 460
            },
            'POSITION_DONE_MENU_BUTTON': {
                'x': 470, 'y': 760
            },
        },
    }[player][constant]


########### Ingame distance ###########

BLACK_PIXEL_THRESHOLD = 10
DISTANCE_FROM_LAST_CLICK = {'x': 15, 'y': 15}  # Dead stickmans are 64 x 10 and standing ones are 25 x 53
STICKER_SPEED_ADJUSTMENT = 0
NUMBER_OF_PIXEL_ANALYSE_PER_SCREENSHOT = 3


########### Time-related ###########

TIME_SLEEPING_BETWEEN_SHOOTINGS = 0
SLEEP_AFTER_SHOOT = 0.00001
SLEEP_AFTER_RELOAD = 1.00
CLICK_POSITION_LATENCY = 0.00001
PYAUTOGUI_ACTION_DELAY = 0


########### Links ###########

GAME_LINK = "https://www.crazygames.com/game/storm-the-house"
SPOTLIGHT_CHROME = "google chrome.app"


########### Keyboard ###########

SPACE = "space"
COMMAND = "command"
ENTER = "enter"
T_KEY = "t"

