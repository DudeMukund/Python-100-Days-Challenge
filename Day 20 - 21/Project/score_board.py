from turtle import Turtle

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()

        self.score = 0

        self.color("yellow")
        self.penup()
        self.hideturtle()
        self.goto(4, 270)
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))
    def score_update(self):
        self.score += 1
               
        self.clear()
        self.write(f"Score: {self.score}", align="center", font=("Courier", 20, "normal"))

    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER!", align="center", font=("Courier", 20, "normal"))





