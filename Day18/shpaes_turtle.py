from random import choice
from turtle import Turtle

tim = Turtle()

colors = ["royal blue", "medium turquoise", "lime", "gold", "orange", "magenta","dark orchid", "medium slate blue","red"]

for num_sides in range(3,11):
    angle = 360 / num_sides
    tim.color(choice(colors))
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)
        



   
