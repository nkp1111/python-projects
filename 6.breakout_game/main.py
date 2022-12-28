"""
Breakout Game
Ball will move randomly player have to strike ball with paddle to break all the tiles on top.
"""
from turtle import Turtle, Screen
from player import Player
from game_ball import Ball

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300


# ------------------------------------------
# funtions





# ------------------------------------------
# turtle components

# screen
screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("#000")
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

# player
player = Player()
screen.update()
screen.listen()
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")

# ball
ball = Ball()

while True:
    screen.update()


screen.exitonclick()
