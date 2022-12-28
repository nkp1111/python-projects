from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.width(7)
        self.color("white")
        self.create_border()
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.goto(-230, 250)
        self.write(f"Score: {self.score}", align="Left", font=("Arial", 15, "bold"))
        self.update_lives()

    def create_border(self):
        self.goto(-250, 230)
        for i in range(50):
            if i % 2 == 0:
                self.pendown()
            else:
                self.penup()

            self.fd(20)

    def update_lives(self):
        self.goto(230, 250)
        self.clear()
        self.write(f"Lives left: {self.lives}", align="Right", font=("Arial", 15, "bold"))
        self.lives -= 1

    def game_over(self):
        self.clear()
        self.color("red")
        self.home()
        self.write(f"Game Over", align="Center", font=("Arial", 30, "bold"))
        self.goto(0, -50)
        self.color("white")
        self.write(f"Final Score: {self.score}", align="Center", font=("Arial", 20, "normal"))