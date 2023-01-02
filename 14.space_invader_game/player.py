from turtle import Turtle
from time import sleep
from gun import Gun


# magazine object holds all bullets
gun = Gun()


class Player(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.color("white")
        self.setpos(0, -300 + 50)
        self.turtlesize(2, 2, 2)
        self.setheading(90)

    def move_left(self):
        if self.xcor() > -260:
            self.setpos(self.xcor() - 10, self.ycor())

    def move_right(self):
        if self.xcor() < 260:
            self.setpos(self.xcor() + 10, self.ycor())

    def trigger_press(self):
        gun.shoot_bullet(self.pos())
