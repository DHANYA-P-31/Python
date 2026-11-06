from turtle import Turtle,Screen

class Snake:

    def __init__(self):

        self.body = []
        self.initialize()

    def initialize(self):
        next_xcor = 0
        self.body = []
        for i in range(3):
            new_body = Turtle("square")
            new_body.penup()
            new_body.color("red")
            new_body.setx(next_xcor)
            self.body.append(new_body)
            next_xcor -= 20
        self.body[0].color("maroon")

    def move(self):
        # here wew are moving from last segment of body to first
        for i in range(len(self.body) - 1, 0, -1):
            new_x = self.body[i - 1].xcor()
            new_y = self.body[i - 1].ycor()
            self.body[i].goto(new_x, new_y)
        self.body[0].forward(20)

    def up(self):
        if self.body[0].heading() != 270:
            self.body[0].setheading(90)

    def down(self):
        if self.body[0].heading() != 90:
            self.body[0].setheading(270)

    def right(self):
        if self.body[0].heading() != 180:
            self.body[0].setheading(0)

    def left(self):
        if self.body[0].heading() != 0:
            self.body[0].setheading(180)

    def append(self):
        next_pos = self.body[-1].position()
        new_body = Turtle("square")
        new_body.penup()
        new_body.color("red")
        new_body.setposition(next_pos)
        self.body.append(new_body)

    def reset(self):
        for body in self.body:
            body.hideturtle()
        self.body.clear()
        self.initialize()



