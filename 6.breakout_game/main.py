"""
Breakout Game
Ball will move randomly
Player have move paddle to strike ball and break all the tiles on top.
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
def create_border():
    """
    Creates a border across the top level of screen
    :return:
    """
    border = Turtle()
    border.penup()
    border.hideturtle()
    border.width(5)
    border.color("white")
    border.goto(-250, 230)
    for i in range(25):
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
screen.onkey(player.move_left, "a")
screen.onkey(player.move_right, "d")
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

    if score.lives < 0 or brick_manager.brick_number == 0:
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
        brick_manager.brick_number -= 1

screen.exitonclick()
print(f"Final score: {score.score}")
