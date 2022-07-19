
from turtle import Turtle

MOVE_DISTANCE, UP, DOWN, LEFT, RIGHT = 20, 90, 270, 180, 0
STARTING_POSITIONS = (0, 0), (-20, 0), (-40, 0)

class Snake():
    def __init__(self):
        self.segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS: self.add_segment(position)
        self.snake_head = self.segments[0]

    def move(self):
        
        for i in range(len(self.segments)-1, 0, -1):
            self.segments[i].goto(x=self.segments[i-1].xcor(), y=self.segments[i-1].ycor())

        self.snake_head.forward(MOVE_DISTANCE)

    def add_segment(self, position):

        new_segment = Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def up(self): 
        if self.snake_head.heading() != DOWN: 
            self.snake_head.setheading(UP)
    def down(self): 
        if self.snake_head.heading() != UP: 
            self.snake_head.setheading(DOWN)
    def left(self): 
        if self.snake_head.heading() != RIGHT: 
            self.snake_head.setheading(LEFT)
    def right(self): 
        if self.snake_head.heading() != LEFT: 
            self.snake_head.setheading(RIGHT)


        