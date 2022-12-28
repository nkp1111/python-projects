from turtle import Turtle

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600
MARGIN = 130
X_POSITION = tuple(range(-SCREEN_WIDTH // 2 + 20, SCREEN_WIDTH // 2 - 20, 50))
COLORS = ("red", "blue", "yellow", "green")


class BrickManager:

    def __init__(self):
        self.bricks = []
        self.create_brick_set()

    def create_brick_set(self):
        for i in range(len(COLORS)):
            y_pos = (SCREEN_HEIGHT // 2 - MARGIN) - (30 * i)
            self.create_brick(y_pos, COLORS[i])

    def create_brick(self, y, color):
        for i in range(len(X_POSITION)):
            new_brick = Turtle()
            new_brick.color(color)
            new_brick.penup()
            new_brick.shape("square")
            new_brick.shapesize(1, 2, 1)
            new_brick.sety(y)
            new_brick.setx(X_POSITION[i])
            self.bricks.append(new_brick)
