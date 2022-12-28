from turtle import Turtle


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("blue")
        self.shapesize(1, 5, 1)
        self.goto(0, -250)

