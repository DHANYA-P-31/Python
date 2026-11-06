from operator import index

import random
from turtle import Turtle
COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

class CarManager():

    def __init__(self):
        self.car = []
        self.newcar()

    def newcar(self):
        car = Turtle()
        car.shape("square")
        car.shapesize(1, 2)
        car.color(random.choice(COLORS))
        car.penup()
        car.setheading(180)
        Y = random.randint(-250, 250)
        car.setpos(300, Y)
        self.car.append(car)

    def frwd(self):
        for i in self.car:
            i.forward(STARTING_MOVE_DISTANCE)

    def checkcollide(self,x,y):
        for i in self.car:
            if abs(i.xcor()-x)<30 and abs(i.ycor() - y)<10:
                return True
