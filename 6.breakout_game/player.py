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
        """
        Moves player to left direction
        :return:
        """
        self.setheading(180)
        self.fd(20)

    def move_right(self):
        """
        Moves player to right direction
        :return:
        """
        self.setheading(0)
        self.fd(20)

    def decrease_size(self):
        """
        Decrease size of player paddle
        :return:
        """
        self.shapesize(1, 3, 1)
