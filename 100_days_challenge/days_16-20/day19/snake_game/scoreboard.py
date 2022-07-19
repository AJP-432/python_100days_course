
from turtle import Turtle

ALIGNMENT, FONT = "center", ("Courier", 24, "bold")

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0 
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=250)
        self.display_text()

    def display_text(self): 
        self.write(arg=f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def increase(self):
        self.score += 1 
        self.clear()
        self.display_text()
    
    def game_over(self):
        self.goto(x=0, y=0)
        self.write(arg="GAME OVER", align=ALIGNMENT, font=FONT)