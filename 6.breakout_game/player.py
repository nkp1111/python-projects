from turtle import Turtle


class Player(Turtle):
    """
    Creates a player object paddle that moves.
    """
    def __init__(self):
        super().__init__()
        self.shape("square")
        self.penup()
        self.color("blue")
        self.shapesize(1, 5, 1)
        self.goto(0, -230)
        self.speed = "fastest"

    def move_left(self):
        self.setheading(180)
        self.fd(15)

    def move_right(self):
        self.setheading(0)
        self.fd(15)

    def decrease_size(self):
        self.shapesize(1, 3, 1)
