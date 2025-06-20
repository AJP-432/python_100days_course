

from turtle import Turtle

class Paddle(Turtle): 
    def __init__(self, position): 
        super().__init__()
        self.color("white")
        self.shape("square")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.goto(position)

    def move_up(self): self.goto(x=self.xcor(), y=(self.ycor()+40))
    def move_down(self): self.goto(x=self.xcor(), y=(self.ycor()-40))



