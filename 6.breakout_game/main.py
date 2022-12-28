"""
Breakout Game
Ball will move randomly player have to strike ball with paddle to break all the tiles on top.
"""
from turtle import Turtle, Screen
from player import Player
from game_ball import Ball
from brick_manager import BrickManager
from score_board import ScoreBoard
from time import sleep

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 600


# ------------------------------------------
# funtions





# ------------------------------------------
# turtle components

# screen
screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("#000")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

# player
player = Player()
screen.update()
screen.listen()
screen.onkeypress(player.move_left, "a")
screen.onkeypress(player.move_right, "d")

# ball
ball = Ball()

# brick manager
brick_manager = BrickManager()

# score board
score = ScoreBoard()

game_over = False

while not game_over:
    sleep(.1)
    ball.start_move()
    screen.update()

    if score.lives < 0:
        game_over = True


    if ball.ycor() <= -285:
        ball.reset_ball()
        score.update_lives()


screen.exitonclick()
print(score.score)
