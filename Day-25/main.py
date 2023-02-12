from multiprocessing.connection import answer_challenge
import turtle
import pandas as pd

screen = turtle.Screen()
screen.title("U.S. States Game")
img = "blank_states_img.gif"

screen.addshape(img)
turtle.shape(img)

data = pd.read_csv("50_states.csv")
all_states = data.state.to_list()
guessed_states = []

while len(guessed_states) < 50:
    answer_state = screen.textinput(title =f"{len(guessed_states)}/ 50 States Correct", prompt="What's another state's names?").title()
    print(answer_state)

    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in guessed_states:
                missing_states.append(state)
        new_data = pd.DataFrame(missing_states)
        new_data.to_csv("states_to_learn.csv")
        break

    if answer_state in all_states:
        guessed_states.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(int(state_data.x), int(state_data.y))
        t.write(state_data.state.item())
    #create a turtle to write the name of the state at the state's x and y coordate
