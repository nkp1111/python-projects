from turtle import Turtle
from random import randint


class Enemies:

    def __init__(self):
        self.enemy_base = []
        self.first_wave()

    def first_wave(self):
        for x in range(-5, 5):
            for y in range(1, 3):
                self.add_enemy((x * 40, 300 - y * 30))

    def add_enemy(self, pos=(randint(-250, 250), randint(200, 270))):
        enemy = Turtle()
        enemy.shape("turtle")
        enemy.color("blue")
        enemy.penup()
        enemy.setpos(pos)
        enemy.setheading(270)
        enemy.move_x = 10
        enemy.move_y = -20
        self.enemy_base.append(enemy)

    def move_enemy(self):
        for enemy in self.enemy_base:
            if enemy.xcor() > 260 or enemy.xcor() < -260:
                enemy.move_x *= -1
                enemy.setpos(enemy.xcor() + enemy.move_x, enemy.ycor() + enemy.move_y)
            else:
                enemy.setpos(enemy.xcor() + enemy.move_x, enemy.ycor())







