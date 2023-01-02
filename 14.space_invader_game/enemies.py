from turtle import Turtle
from random import randint


class Enemies:

    def __init__(self):
        self.enemy_base = []
        self.first_wave()
        self.enemy_count = len(self.enemy_base)

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
        enemy.move_x = 30
        enemy.move_y = -30
        self.enemy_base.append(enemy)

    def move_enemy(self):
        for enemy in self.enemy_base:
            if enemy.xcor() > 260 or enemy.xcor() < -260:
                enemy.move_x *= -1
                enemy.setpos(enemy.xcor() + enemy.move_x, enemy.ycor() + enemy.move_y)
            else:
                enemy.setpos(enemy.xcor() + enemy.move_x, enemy.ycor())

    def bullet_hit(self, bullets):
        for bullet in bullets:
            for enemy in self.enemy_base:
                if enemy.distance(bullet) < 20:
                    enemy.reset()
                    self.add_enemy()
                    self.enemy_count += 1
                    self.enemy_base.remove(enemy)

    def stop_movement(self):
        for enemy in self.enemy_base:
            enemy.move_x = 0
            enemy.move_y = 0

    def player_capture(self, player):
        for enemy in self.enemy_base:
            if enemy.distance(player) < 45:
                self.stop_movement()
                return True






