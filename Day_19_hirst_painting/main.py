import turtle as t
import random

t.colormode(255)
#list of colors created with colors_from_image.py
colors = [(118, 166, 197), (126, 90, 58), (188, 242, 251), (121, 227, 251), (200, 156, 106), (143, 182, 155), (210, 212, 96), (61, 41, 21), (197, 234, 216), (59, 83, 9), (54, 27, 37), (154, 161, 57), (242, 228, 191), (128, 72, 80), (186, 147, 173), (159, 212, 184), (69, 108, 65), (20, 41, 12), (31, 39, 53), (99, 49, 38), (69, 105, 126), (185, 102, 90), (95, 46, 55), (164, 106, 125), (43, 83, 20), (91, 144, 157), (98, 155, 118), (224, 170, 188), (235, 199, 209), (115, 123, 163)]
tim = t.Turtle()
tim.screen.title('Painting with dots')
tim.screen.setup (width=600, height=600, startx=450, starty=200)
tim.hideturtle()
tim.penup()
tim.speed("fastest")

for i in range(10):
    tim.goto(-225, (50*i)-225)
    for _ in range(10):
        tim.dot(20, random.choice(colors))
        tim.forward(50)
    
t.exitonclick()