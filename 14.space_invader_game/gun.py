from turtle import Turtle


class Gun:

    def __init__(self):
        self.magazine = []

    def load_bullet(self):
        bullet = Turtle()
        bullet.penup()
        bullet.shape("square")
        bullet.turtlesize(0.5, 1.5, 1)
        bullet.color("red")
        bullet.setheading(90)
        bullet.initiated = True
        self.magazine.append(bullet)

    def shoot_bullet(self, pos):
        if len(self.magazine) < 6:
            self.load_bullet()
            for bullet in self.magazine:
                if bullet.initiated:
                    bullet.initiated = False
                    bullet.setpos(pos[0], pos[1] + 40)

    def move_bullets(self):
        for bullet in self.magazine:
            if not bullet.initiated:
                if bullet.ycor() < 330:
                    bullet.setpos(bullet.xcor(), bullet.ycor() + 40)
                else:
                    self.magazine.remove(bullet)
