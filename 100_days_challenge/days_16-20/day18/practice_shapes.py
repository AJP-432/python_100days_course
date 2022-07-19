
from turtle import Turtle, Screen
from random import randint

tim = Turtle()
screen = Screen()
screen.colormode(255)

def shape(num_sides):
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(360/num_sides)

for i in range(3, 11):
    shape(i)

screen.exitonclick()