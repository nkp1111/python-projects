"""
Breakout Game
Ball will move randomly player have to strike ball with paddle to break all the tiles on top.
"""
from turtle import Turtle, Screen
from player import Player

SCREEN_WIDTH = 300
SCREEN_HEIGHT = 300

screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("#000")
screen.screensize(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

player = Player()
screen.update()

screen.exitonclick()
