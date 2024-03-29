from turtle import Turtle
from random import randint


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("red")
        self.penup()
        self.move_x = 10
        self.move_y = -10

    def start_move(self):
        """
        Moves the ball
        :return:
        """
        x, y = self.pos()
        self.setpos(x + self.move_x, y + self.move_y)
        self.bounce()

    def bounce(self):
        """
        Bounces ball from wall by sides and top
        :return:
        """
        x, y = self.pos()
        if y >= 285:
            self.move_y *= -1
        if x <= -240 or x >= 240:
            self.move_x *= -1

    def reset_ball(self):
        """
        Resets ball position on crossing player zone
        :return:
        """
        self.home()

    def detect_player_collision(self, player):
        """
        Detect ball collision with player
        :param player:
        :return:
        """
        if self.distance(player) < 30:
            self.move_y *= -1

    def detect_wall_collision(self, bricks):
        """
        Detect ball collision with bricks and return brick color for score.
        :param bricks:
        :return: (color, color)
        """
        for brick in bricks:
            if self.distance(brick) < 20:
                b_color = brick.color()
                brick.reset()
                brick.goto(1000, 1000)
                self.move_y *= -1
                return b_color
