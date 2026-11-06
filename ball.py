from turtle import Turtle
import random
import time

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.penup()

    def initial(self):
        dir = random.randint( a=1, b=359)
        self.goto(0,0)
        self.setheading(dir)
        time.sleep(1)

    def move(self,ball_speed):
        self.forward(10)
        time.sleep(ball_speed)
