#####Turtle Square######

import turtle as t
from colors_options import color_options
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("yellow")
t.bgcolor("lavender")
tim.goto(0,0)
colors_list = color_options

number_of_turns = 3

while tim not in tim.position() and number_of_turns < 15:
    turn_for = 360 / number_of_turns
    pick_random_color = random.choice(colors_list)
    tim.color(pick_random_color)
    for i in range(number_of_turns):
        tim.right(turn_for)
        tim.forward(100)

    number_of_turns += 1

t.exitonclick()