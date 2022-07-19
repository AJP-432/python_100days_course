from turtle import Screen
from time import sleep
from snake import Snake
from food import Food
from scoreboard import Scoreboard

my_screen = Screen()
my_screen.setup(width=600, height=600)
my_screen.bgcolor("black")
my_screen.title("My Snake Game")
my_screen.tracer(0)
my_screen.listen()

jim, food, board, game_is_on = Snake(), Food(), Scoreboard(), True 

# Snake movement
my_screen.onkey(fun=jim.up, key="Up")
my_screen.onkey(fun=jim.down, key="Down")
my_screen.onkey(fun=jim.left, key="Left")
my_screen.onkey(fun=jim.right, key="Right")

while game_is_on: 
    my_screen.update()
    sleep(0.1)
    jim.move()

    # Detecting collision with food
    if jim.snake_head.distance(food) < 15: 
        food.refresh()
        board.increase()
        jim.extend()
    
    # Detecting collision with wall
    if abs(jim.snake_head.xcor()) > 280 or abs(jim.snake_head.ycor()) > 280: 
        game_is_on = False
        board.game_over()
    
    # Detecting snake head collision with tail 
    for segment in jim.segments[1:]:    
        if jim.snake_head.distance(segment) < 10: 
            game_is_on = False
            board.game_over()




my_screen.exitonclick()