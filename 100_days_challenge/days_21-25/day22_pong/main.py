
from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Scoreboard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=800, height=600)
my_screen.title("AJ's Pong Game")
my_screen.tracer(0)
my_screen.listen()


l_paddle = Paddle((-350, 0))
r_paddle = Paddle((350, 0))
l_player_score = Scoreboard(X_LOCATION=-200, Y_LOCATION=200)
r_player_score = Scoreboard(X_LOCATION=200, Y_LOCATION=200)
ball = Ball()

my_screen.onkey(fun=l_paddle.move_up, key="w")
my_screen.onkey(fun=l_paddle.move_down, key="s")
my_screen.onkey(fun=r_paddle.move_up, key="Up")
my_screen.onkey(fun=r_paddle.move_down, key="Down")

game_is_on = True

while game_is_on: 
    ball.move()
    my_screen.update()

    # Ball collision with wall top
    if abs(ball.ycor()) >= 290: ball.Y_AMOUNT *= -1

    # Ball collision with  paddle
    if abs(ball.xcor()) >= 340 and (ball.distance(r_paddle) <= 50 or ball.distance(l_paddle) <= 50): 
        ball.X_AMOUNT *= -1.1 
        ball.Y_AMOUNT *= 1.1

    # Point to Players
    if ball.xcor() <= -390: 
        r_player_score.increase()
        ball.goto(x=0, y=0)
        ball.X_AMOUNT *= -1
        ball.Y_AMOUNT *= -1
        ball.X_AMOUNT, ball.Y_AMOUNT = 0.25, 0.25

    if ball.xcor() >= 390: 
        l_player_score.increase()
        ball.goto(x=0, y=0)
        ball.X_AMOUNT *= -1
        ball.Y_AMOUNT *= -1
        ball.X_AMOUNT, ball.Y_AMOUNT = 0.25, 0.25


my_screen.exitonclick()