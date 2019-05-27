import logging
import time
from datetime import datetime


def resizeCoordinateToActualScreen(coordinate):
    return coordinate / 2


def convertCoordinatesToBox(coordinates):
    return {"top": coordinates["y_top_left"],
            "left": coordinates["x_top_left"],
            "width": coordinates["x_bottom_right"] - coordinates["x_top_left"],
            "height": coordinates["y_bottom_right"] - coordinates["y_top_left"]}


class ElapsedFormatter(object):
    def __init__(self):
        self.start_time = time.time()

    def format(self, record):
         # using timedelta here for convenient default formatting
        elapsed = datetime.utcfromtimestamp(record.created - self.start_time)
        return "{} {}".format(elapsed.strftime("%H:%M:%S"), record.getMessage())

    @staticmethod
    def add_handler(logger):
        """Add custom formatter to root logger for simple demonstration"""
        handler = logging.StreamHandler()
        handler.setFormatter(ElapsedFormatter())
        logger.addHandler(handler)
