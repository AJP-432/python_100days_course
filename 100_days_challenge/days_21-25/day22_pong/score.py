

from turtle import Turtle

ALIGNMENT, FONT = "center", ("Courier", 24, "bold")


class Scoreboard(Turtle): 
    def __init__(self, X_LOCATION, Y_LOCATION):
        super().__init__()
        self.color("white")
        self.score = 0
        self.hideturtle()
        self.penup()
        self.goto(x=X_LOCATION, y=Y_LOCATION)
        self.display_text()

    def display_text(self):
        self.write(arg=self.score, align=ALIGNMENT, font=FONT)

    def increase(self):
        self.clear()
        self.score += 1
        self.display_text()