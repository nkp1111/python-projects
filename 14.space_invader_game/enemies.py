from turtle import Turtle
from random import randint


class Enemies:

    def __init__(self):
        self.enemy_base = []
        self.first_wave()

    def first_wave(self):
        for x in range(-5, 5):
            for y in range(1, 3):
                self.add_enemy((x * 30, 300 - y * 30))

    def add_enemy(self, pos=(randint(-250, 250), randint(200, 270))):
        enemy = Turtle()
        enemy.shape("turtle")
        enemy.color("blue")
        enemy.penup()
        enemy.setpos(pos)
        enemy.setheading(270)
        self.enemy_base.append(enemy)








