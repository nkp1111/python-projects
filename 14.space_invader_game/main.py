"""
Space Invader Game
"""
from turtle import Screen, Turtle
from player import Player, gun
from time import sleep
from enemies import Enemies


# game over
def game_over():
    game_board = Turtle()
    game_board.penup()
    game_board.color("red")
    game_board.write(f"GAME OVER", align="center", font=("Arial", 40, "bold"))


scr_board = Turtle()

# screen
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600
screen = Screen()
screen.setup(SCREEN_WIDTH, SCREEN_HEIGHT)
screen.bgcolor("black")
screen.tracer(0)

# player
player = Player()

# enemies
enemies = Enemies()

# screen events
screen.listen()
screen.onkey(player.move_left, "Left")
screen.onkey(player.move_right, "Right")
screen.onkeypress(player.move_left, "Left")
screen.onkeypress(player.move_right, "Right")
screen.onkey(player.trigger_press, "space")


def score_board():
    scr_board.clear()
    scr_board.penup()
    scr_board.color("white")
    scr_board.goto(-250, 250)
    scr_board.hideturtle()
    scr_board.write(f"Score: {enemies.enemy_count - 20}", align="left", font=("Arial", 20, "normal"))


is_game_over = False
while not is_game_over:
    sleep(.1)
    screen.update()
    gun.move_bullets()
    enemies.move_enemy()
    enemies.bullet_hit(gun.magazine)
    score_board()
    if enemies.player_capture(player) or enemies.enemy_count == 500:
        is_game_over = True
        game_over()


screen.exitonclick()

