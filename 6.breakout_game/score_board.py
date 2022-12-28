from turtle import Turtle


class ScoreBoard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.width(7)
        self.color("white")
        self.create_border()
        self.penup()
        self.goto(-230, 250)
        self.hideturtle()
        self.write("Score: 0", align="Left", font=("Arial", 15, "bold"))

    def create_border(self):
        self.goto(-250, 230)
        for i in range(50):
            if i % 2 == 0:
                self.pendown()
            else:
                self.penup()

            self.fd(20)
