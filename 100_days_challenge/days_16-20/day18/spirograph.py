from turtle import Turtle, Screen
from random import randint

tim = Turtle()
tim.speed(1000)
my_screen = Screen()
my_screen.colormode(255)

for _ in range(60):
    tim.color((randint(0, 255)), (randint(0, 255)), (randint(0, 255)))
    tim.circle(100)
    tim.right(6)    

my_screen.exitonclick()