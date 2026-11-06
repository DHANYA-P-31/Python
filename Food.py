import turtle
import random

class Food(turtle.Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("yellow")
        self.penup()
        x = random.randint(-250,250)
        y = random.randint(-250,250)
        self.goto(x,y)

    def generate(self):
            x = random.randint(-250,250)
            y = random.randint(-250,250)
            self.goto(x,y)



