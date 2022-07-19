from turtle import Turtle, Screen

tim = Turtle()
my_screen = Screen()

my_screen.listen()

def move_forward(): tim.forward(10)
def move_backward(): tim.backward(10)
def clockwise(): tim.right(10)
def counter_clockwise(): tim.left(10)

def clear(): my_screen.resetscreen()

my_screen.onkey(fun=move_forward, key="w")
my_screen.onkey(fun=move_backward, key="s")
my_screen.onkey(fun=clockwise, key="d")
my_screen.onkey(fun=counter_clockwise, key="a")
my_screen.onkey(fun=clear, key="c")

my_screen.exitonclick() 