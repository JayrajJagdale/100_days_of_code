from turtle import Turtle
import random

class Food(Turtle):
     
    COLORS = ["red","orange","yellow","green","blue","purple"]

    def __init__(self):
        super().__init__()
        self.shape("turtle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choices(self.COLORS))
        self.speed("fastest")
        self.refreash()

    def refreash(self):
          random_x = random.randint(-280, 280)
          random_y = random.randint(-280, 280)
          self.goto(random_x, random_y)