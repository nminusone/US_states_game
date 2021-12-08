from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.goto(0, 0)
        self.ht()

    # TODO increment score
    def score_keeper(self):
        pass
