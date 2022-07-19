from turtle import Turtle, Screen
from random import choice, randint

tim = Turtle()
tim.pensize(5)
tim.speed(1000)
my_screen = Screen()
my_screen.colormode(255)

for _ in range(1000): 
    tim.color(randint(0, 255), randint(0, 255), randint(0, 255))
    tim.forward(50)
    tim.right(choice([0, 90, 180, -90]))

my_screen.exitonclick()
