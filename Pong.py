from turtle import Turtle,Screen

class Paddle(Turtle):

    def __init__(self,x):
        super().__init__()
        self.shape("square")
        self.shapesize(1, 5)
        self.color("blue")
        self.penup()
        self.setpos(x, 0)
        self.setheading(90)

    def up(self):
        self.forward(20)

    def down(self):
        self.backward(20)