import turtle
from random import choice

color_list = [(220, 158, 84), (39, 109, 150), (120, 163, 191), (150, 63, 87), (217, 232, 222), (203, 134, 157), (180, 160, 34), (32, 131, 95), (122, 179, 152), (235, 218, 225), (161, 79, 52), (213, 87, 61), (197, 85, 112), (208, 223, 231), (229, 199, 114), (57, 166, 135), (141, 33, 42), (8, 104, 80), (47, 158, 182), (234, 163, 181), (117, 115, 162), (32, 62, 111), (236, 171, 157), (126, 38, 34), (156, 210, 197), (32, 57, 78), (70, 41, 37), (25, 65, 56), (74, 37, 47)]

# Initiations
turtle.screensize(700, 700)

tim = turtle.Turtle()
tim.speed(100)
tim.hideturtle()


my_screen = turtle.Screen()
my_screen.colormode(255)

y_pos = -250

# Loopingly dotting canvas
for _ in range(10): 
    tim.penup()
    tim.goto(-250, y_pos)
    y_pos += 50
    
    for _ in range(10):
        tim.pendown()
        tim.dot(20, choice(color_list))
        tim.penup()
        tim.forward(50)


my_screen.exitonclick()
