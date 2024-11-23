# Creating a list of colors from an image
import colorgram

colors = colorgram.extract('image.jpg', 30) #import your image here
rgb_colors = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r, g, b)
    rgb_colors.append(new_color)

print(rgb_colors)