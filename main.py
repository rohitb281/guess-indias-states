import pandas
import turtle

IMG = "Outline-Map-of-India-with-States.gif"
screen = turtle.Screen()
screen.title("States")
screen.addshape(IMG)
turtle.shape(IMG)

data = pandas.read_csv("states_data.csv")
state_list = data.state.to_list()
correct_guesses = []
while len(correct_guesses) < len(state_list):
    answer_state = screen.textinput(title=f"{len(correct_guesses)}/{len(state_list)} states correctly guessed",
                                    prompt="What is another state's name?").title()
    if answer_state in state_list:
        t = turtle.Turtle()
        correct_guesses.append(answer_state)
        t.penup()
        t.hideturtle()
        state_row = data[data.state == answer_state]
        t.goto(state_row.x.item(), state_row.y.item())
        t.write(f"{answer_state}")

    elif answer_state == "Exit":
        unguessed_states = []
        for state in state_list:
            if state not in correct_guesses:
                unguessed_states.append(state)
        new_data = pandas.DataFrame(unguessed_states)
        new_data.to_csv("Missed states.csv")
        break
