import colorgram

rgb_colours = []

colours = colorgram.extract('D:/100_Days_Code/Day18/img1.jpg',30)

for color in colours:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    new_color = (r,g,b)
    rgb_colours.append(new_color)
    
print(rgb_colours)

import turtle as t
import random 
color_list = [(236, 35, 108), (145, 28, 66), (230, 237, 232), (239, 75, 35), (7, 148, 95), (220, 171, 45), (183, 158, 47), (45, 191, 232), (28, 127, 194), (254, 223, 0), (125, 192, 78), (85, 27, 91), (243, 218, 56), (178, 40, 98), (44, 170, 114), (211, 132, 166), (206, 57, 35), (239, 162, 193), (145, 27, 25), (243, 167, 156), (163, 211, 178), (26, 187, 225), (6, 116, 54), (138, 210, 232), (74, 135, 184), (170, 191, 221), (114, 10, 8)]

t.penup()

t.hideturtle()

t.speed("fastest")

t.colormode(255)
t.setheading(225)
t.forward(300)
t.setheading(0)
number_of_dots = 100

for dot_count in range(1,number_of_dots + 1):
    t.dot(20,random.choice(color_list))
    t.forward(50)

    if dot_count % 10 == 0:
        t.setheading(90)
        t.forward(50)
        t.setheading(180)
        t.forward(500)
        t.setheading(0)

s = t.Screen()
s.exitonclick()


