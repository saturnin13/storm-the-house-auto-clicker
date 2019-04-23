#! python3

import numpy as np
from PIL import ImageGrab
import cv2
from macDirectKeys import click, queryMousePosition, PressKey, ReleaseKey, moveMouseTo
import time
import math

SPACE = "space"

actual_game_coords = [653, 585, 1142, 803]
# game_coords = [653, 347, 1142, 763]
game_coords = [538, 609, 961, 796]
test_coord = [0, 0, 2880, 1800]

screen = np.array(ImageGrab.grab(bbox=test_coord))
cv2.imshow("screen", screen)
cv2.waitKey(5) & 0xFF
print("showing picture")

previous_clicks = []

stage_no = 0

no_of_clicks_this_level = 0
start_time_of_level = time.time()

print("stage no {}".format(stage_no))

def dist(x1, y1, x2, y2):
    return math.sqrt((x1 - x2) ** 2 + (y1 - y2) ** 2)


def shoot_some_fuckers(screen):
    print("shoot some fuckers")
    global game_coords, previous_clicks, stage_no, no_of_clicks_this_level

    for y in range(0, len(screen), 2):
        for x in range(0, len(screen[y]), 2):
            if screen[y][x] < 10:
                print("success")
                actual_x = x + game_coords[0]
                actual_y = y + game_coords[1]

                click_bubble_range = 30
                if stage_no == 3:
                    click_bubble_range = 0

                too_close = False
                for pos in previous_clicks:
                    if dist(actual_x, actual_y, pos[0], pos[1]) < click_bubble_range:
                        too_close = True
                        break
                if too_close:
                    continue

                click(actual_x, actual_y)
                no_of_clicks_this_level += 1

                if stage_no == 0:
                    print("la")
                    # time.sleep(0.03)
                    click(actual_x + 3, actual_y)
                    print("clicked " + str(actual_x) + " 3 and " + str(actual_y))
                    no_of_clicks_this_level += 1

                    # time.sleep(0.03)
                    max_previous_click_length = 3

                if stage_no == 1:
                    max_previous_click_length = 5

                if stage_no == 2:
                    max_previous_click_length = 5

                if stage_no == 3:
                    max_previous_click_length = 1

                previous_clicks.append([actual_x, actual_y])
                if len(previous_clicks) > max_previous_click_length:
                    del previous_clicks[0]

                if stage_no < 2:
                    return


def upgrade_gun():
    for i in range(40):
        click(804, 425)
        click(806, 425)
    for j in range(5):
        time.sleep(0.1)
        for i in range(200):
            click(718, 435)
            click(720, 435)
            click(720, 437)
            click(718, 437)

    click(918, 736)

def circle_around_gamecoordinate():
    time.sleep(0.25)
    moveMouseTo(game_coords[0], game_coords[1])
    time.sleep(0.25)
    moveMouseTo(game_coords[2], game_coords[1])
    time.sleep(0.25)
    moveMouseTo(game_coords[2], game_coords[3])
    time.sleep(0.25)
    moveMouseTo(game_coords[0], game_coords[3])

# only start the program after the mouse is on the left screen
while True:
    mouse_pos = queryMousePosition()
    if mouse_pos.x <= 0:
        circle_around_gamecoordinate()
        break

print("alright we good to go")
while True:
    mouse_pos = queryMousePosition()

    if game_coords[0] < mouse_pos.x < game_coords[2] and game_coords[1] < mouse_pos.y < game_coords[3]:
        start_time = time.time()
        print(game_coords)
        screen = np.array(ImageGrab.grab(bbox=game_coords))
        print("showing picture")
        cv2.imshow("screen", screen)
        cv2.waitKey(5) & 0xFF
        screen = cv2.cvtColor(screen, cv2.COLOR_BGR2GRAY)


        if screen[609 - game_coords[1], 538 - game_coords[0]] > 180:
            print("Pressing space")
            PressKey(SPACE)
            time.sleep(0.05)
            ReleaseKey(SPACE)

        shoot_some_fuckers(screen)
        # if screen[732 - game_coords[1], 872 - game_coords[0]] < 150:
        #     shoot_some_fuckers(screen)
        #     clicks_per_second = no_of_clicks_this_level / (time.time() - start_time_of_level)
        #     print("Clicks per second {}".format(clicks_per_second))

        # elif screen[732 - game_coords[1], 872 - game_coords[0]] > 250:
        if screen[732 - game_coords[1], 872 - game_coords[0]] > 250:
            print("sleeping 3 seconds")
            time.sleep(3)
            upgrade_gun()
            time.sleep(3)
            start_time_of_level = time.time()
            no_of_clicks_this_level = 0

        # print("Frame took {} seconds".format((time.time() - start_time)))

    print("sleeping 5 second")
    time.sleep(5)
