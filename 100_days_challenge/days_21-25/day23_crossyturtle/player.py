
STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()  
        self.shape("turtle")
        self.color("red")
        self.penup()
        self.restart()
        self.setheading(90)

    def move_up(self): self.forward(10)
    def move_down(self): self.backward(10)
    
    def restart(self): self.goto(STARTING_POSITION)

    def at_finish_line(self): 
        if (self.ycor() >= FINISH_LINE_Y): return True
        else: return False