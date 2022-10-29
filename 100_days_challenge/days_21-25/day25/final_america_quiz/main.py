# Ajlal F. Paracha
# Oct 11, 2022

import turtle, pandas

# Setting up GUI
my_screen = turtle.Screen()
my_screen.title("US States Games")
# Setting background
image = "blank_states_img.gif"
my_screen.addshape(image)
turtle.shape(image)

# Basic data
count, data, state_name_turtles = 0, pandas.read_csv("50_states.csv"), []
list_of_states = data.state.to_list()

# Looping until user guesses all the states
while count < 50: 
    anwser_state = my_screen.textinput(title=f"Guess the state {count}/50", prompt="What's another states name?").title()
    if anwser_state == "Exit": 
        # Makes a csv containing all the states that the user missed
        pandas.DataFrame(list_of_states).to_csv("states_to_learn.csv")
        break
    
    if anwser_state in list_of_states: 
        count += 1
        list_of_states.remove(anwser_state)
        state_title = turtle.Turtle()
        state_title.color("black")
        state_title.hideturtle()
        state_title.penup()
        x, y = int(data.loc[data.state == anwser_state].x), int(data.loc[data.state == anwser_state].y)
        state_title.goto(x, y)
        state_title.write(anwser_state)
        state_name_turtles.append(state_title)
        

    



