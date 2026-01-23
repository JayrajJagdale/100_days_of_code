import random
import turtle as t

angle = 360
t.speed("fastest")
colors = ["royal blue", "medium turquoise", "lime", "gold", "orange", "magenta","dark orchid", "medium slate blue","red"]

for _ in range(50):
    t.color(random.choice(colors))
    angle -= 10
    t.circle(100)
    t.setheading(angle)


def draw_spirograph(size_of_gap):
    for _ in range(int(360/size_of_gap)):
         t.color(random.choice(colors))
         t.circle(100)
         t.setheading(t.heading() + size_of_gap)

draw_spirograph(5)
    

screen = t.Screen()
screen.exitonclick()