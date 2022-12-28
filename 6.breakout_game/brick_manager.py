from turtle import Turtle

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
MARGIN = 130
X_POSITION = tuple(range(-SCREEN_WIDTH // 2 + 20, SCREEN_WIDTH // 2 - 20, 50))
COLORS = ("red", "orange", "green", "yellow")


class BrickManager:

    def __init__(self):
        self.bricks = []
        self.create_brick_set()
        self.brick_number = len(self.bricks)

    def create_brick_set(self):
        """
        Creates brick sets of different colors
        :return:
        """
        for i in range(len(COLORS)):
            y_pos = (SCREEN_HEIGHT // 2 - MARGIN) - (30 * i)
            self.create_brick(y_pos, COLORS[i])

    def create_brick(self, y, color):
        """
        Create multiple bricks of one color
        :param y:
        :param color:
        :return:
        """
        for i in range(len(X_POSITION)):
            new_brick = Turtle()
            new_brick.color(color)
            new_brick.penup()
            new_brick.shape("square")
            new_brick.shapesize(1, 2, 1)
            new_brick.sety(y)
            new_brick.setx(X_POSITION[i])
            self.bricks.append(new_brick)
