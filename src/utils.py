class Utils:
    @staticmethod
    def convertCoordinatesToBox(coordinates):
        return {"top": coordinates["y_top_left"],
                "left": coordinates["x_top_left"],
                "width": coordinates["x_bottom_right"] - coordinates["x_top_left"],
                "height": coordinates["y_bottom_right"] - coordinates["y_top_left"]}

    @staticmethod
    def resizeCoordinateToActualScreen(coordinate):
        return coordinate / 2
