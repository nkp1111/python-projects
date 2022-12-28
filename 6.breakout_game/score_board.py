from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.width(7)
        self.color("white")
        self.penup()
        self.hideturtle()
        self.score = 0
        self.lives = 3
        self.update_board()

    def update_board(self):
        self.goto(-230, 250)
        self.write(f"Score: {self.score}", align="Left", font=("Arial", 15, "bold"))
        self.goto(230, 250)
        self.write(f"Lives left: {self.lives}", align="Right", font=("Arial", 15, "bold"))

    def update_lives(self):
        self.clear()
        self.lives -= 1
        self.update_board()

    def game_over(self):
        self.clear()
        self.color("red")
        self.home()
        self.write(f"Game Over", align="Center", font=("Arial", 30, "bold"))
        self.goto(0, -50)
        self.color("white")
        self.write(f"Final Score: {self.score}", align="Center", font=("Arial", 20, "normal"))