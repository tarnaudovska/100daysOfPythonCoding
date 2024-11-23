#####Turtle Square######

import turtle as t
import random

tim = t.Turtle()
tim.shape("turtle")
t.bgcolor("lavender")
tim.pensize(10)
tim.speed("fastest")

t.colormode(255)
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)
    
directions = [0, 90, 180, 270]

for _ in range(100):
    tim.color(random_color())
    tim.forward(50)
    tim.setheading(random.choice(directions))
    

t.exitonclick()