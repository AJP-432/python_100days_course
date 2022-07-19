from turtle import Turtle, Screen
from random import randint

my_screen = Screen()
my_screen.setup(width=500, height=400)

user_bet = my_screen.textinput(title="Make your bet", prompt="Which turtle will win the race? Enter a color: ")

colors = ["red", "blue", "green", "orange", "purple", "black"]
turts, y_pos, is_race_on = [], -100, False

for i in range(len(colors)): 
    turts.append(Turtle(shape="turtle"))
    turts[i].color(colors[i])
    turts[i].penup()
    turts[i].goto(-230, y_pos)
    y_pos += 40

if user_bet: is_race_on = True

while is_race_on: 
    for turtle in turts: 
        turtle.forward(randint(0, 10))
        if turtle.xcor() >= 230: 
            winner = turtle.pencolor()
            is_race_on = False

if winner == user_bet: print(f"You win! The winner is {winner}")
else: print(f"You lose! The winner is {winner}")

my_screen.exitonclick()