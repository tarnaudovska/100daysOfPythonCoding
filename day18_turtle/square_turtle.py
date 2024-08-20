#####Turtle Square######

import turtle as t

timmy_the_turtle = t.Turtle()
timmy_the_turtle.shape("turtle")
timmy_the_turtle.color("yellow")
t.bgcolor("grey")

for _ in range(4):
    timmy_the_turtle.forward(100)
    timmy_the_turtle.right(90)

t.exitonclick()