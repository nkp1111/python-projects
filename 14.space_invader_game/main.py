"""
Space Invader Game
"""
from turtle import Screen
from player import Player, magazine
from time import sleep


# screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# player
player = Player()
screen.update()

# screen events
screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkey(player.trigger_press, "space")


while True:
    sleep(.1)
    screen.update()
    magazine.move_bullets()


screen.exitonclick()

