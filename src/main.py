import time

from actionController import ActionController


def main():
    time.sleep(1)
    ActionController.launchStormTheHouse()
    ActionController.playStormTheHouse(False, True)


if __name__ == '__main__':
    main()
