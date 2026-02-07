import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "D:/100_Days_Code/Day25/blank_states_img.gif"
screen.addshape(image)
turtle.shape(image)

all_guesses = []

data = pandas.read_csv("D:/100_Days_Code/Day25/50_states.csv")

all_states = data.state.tolist()

while len(all_guesses) < 50:
    
    answer_state = screen.textinput(title=f"{len(all_guesses)}/50 States Correct", prompt="What's another state's name").title()
    if answer_state == "Exit":
        missing_states = []
        for state in all_states:
            if state not in all_guesses:
                missing_states.append(state)
        new_data = pandas.DataFrame(missing_states)
        new_data.to_csv("D:/100_Days_Code/Day25/states_to_learn.csv")
        break

    if answer_state in all_states:
        all_guesses.append(answer_state)
        t = turtle.Turtle()
        t.hideturtle()
        t.penup()
        states = data[data.state == answer_state]
        t.goto(states.x.item(), states.y.item())
        t.write(answer_state)

