#####Turtle Square######

import turtle as t
from colors_options import color_options
import random

tim = t.Turtle()
tim.shape("turtle")
tim.color("yellow")
t.bgcolor("lavender")
tim.pensize(10)
tim.speed("fastest")

directions = [0, 90, 180, 270]

for _ in range(100):
    tim.color(random.choice(color_options))
    tim.forward(50)
    tim.setheading(random.choice(directions))
    

t.exitonclick()