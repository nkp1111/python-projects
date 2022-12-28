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
def create_border():
    """
    Creates a border across the top level of screen
    :return:
    """
    border = Turtle()
    border.penup()
    border.width(5)
    border.color("white")
    border.goto(-250, 230)
    for i in range(50):
        if i % 2 == 0:
            border.pendown()
        else:
            border.penup()
        border.fd(20)


# color score scheme
color_score = {
    "red": 7,
    "orange": 5,
    "green": 3,
    "yellow": 1,
}

# ------------------------------------------
# turtle components

# screen
screen = Screen()
screen.title("Breakout Game")
screen.bgcolor("#000")
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.tracer(0)

# border
create_border()

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
        score.game_over()

    if ball.ycor() <= -285:
        ball.reset_ball()
        score.update_lives()

    if ball.ycor() > 250:
        player.decrease_size()

    ball.detect_player_collision(player)

    color = ball.detect_wall_collision(brick_manager.bricks)

    if color:
        hit_score = color_score.get(color[0], 0)
        score.update_score(hit_score)

screen.exitonclick()
print(score.score)
