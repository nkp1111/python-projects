from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.move_x = 10
        self.move_y = -10

    def start_move(self):
        x, y = self.pos()
        self.setpos(x + self.move_x, y + self.move_y)
        self.bounce()

    def bounce(self):
        x, y = self.pos()
        if y >= 285 or y <= -285:
            self.move_y *= -1
        if x >= 240 or x <= -240:
            self.move_x *= -1





