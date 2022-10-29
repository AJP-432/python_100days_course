
from turtle import Turtle

class Ball(Turtle):
    def __init__(self): 
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.X_AMOUNT = 0.25
        self.Y_AMOUNT = 0.25

    def move(self):
        self.goto(x=self.xcor()+self.X_AMOUNT, y=self.ycor()+self.Y_AMOUNT)