import turtle
import pandas

screen = turtle.Screen()
screen.title("U.S. States Game")
image = "E:/PROGRAMING/PYTHON/100daysOfPythonCoding/day_25_CSVs/us_states/blank_states_img.gif" #put the path to the map image
screen.addshape(image)
turtle.shape(image)

t=turtle.Turtle()

data = pandas.read_csv("E:/PROGRAMING/PYTHON/100daysOfPythonCoding/day_25_CSVs/us_states/50_states.csv") #put the path tp the csv file
states_list = data.state.to_list()
guessed_states = []

while len(guessed_states) <50:
    answer_state = screen.textinput(title=f"{len(guessed_states)}/50", prompt="What's another state").title()

    if answer_state == "Exit":
        check_list =[]
        for state in states_list:
            if state not in guessed_states:
                t.hideturtle()
                t.penup()
                state_data = data[data.state == state]
                t.goto(state_data.x.item(), state_data.y.item())
                t.write(state_data.state.item())
                t.color("red")
                check_list.append
            
    if answer_state in states_list and answer_state not in guessed_states:
        guessed_states.append(answer_state)
        t.hideturtle()
        t.penup()
        state_data = data[data.state == answer_state]
        t.goto(state_data.x.item(), state_data.y.item())
        t.write(answer_state)
        print(guessed_states)

screen.exitonclick()

