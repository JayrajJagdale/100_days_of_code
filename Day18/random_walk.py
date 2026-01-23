import turtle as t
import random

direction = [0,90,180,270]
t.colormode(255)
def random_color():
    r = random.randint(0,255)
    g = random.randint(0,255)
    b = random.randint(0,255)
    random_colour = (r,g,b)
    return random_colour
# colors = ["royal blue", "medium turquoise", "lime", "gold", "orange", "magenta","dark orchid", "medium slate blue","red"]

t.speed("fastest")
t.pensize(8)

for _ in range(300):
    # t.color(random.choice(colors))
    t.color(random_color())
    t.forward(30)
    t.setheading(random.choice(direction))
    




 

