from turtle import Turtle,Screen
import random
rocky  = Turtle()
screen = Screen()

rocky.shape("turtle")

#drawing a square
# for i in range(4):
#     rocky.forward(100)
#     rocky.left(90)

#Drawing a dashed line
# for i in range(20):
#     rocky.forward(10)
#     rocky.penup()
#     rocky.forward(10)
#     rocky.pendown()

#Drawing various shapes
# screen.colormode(255)
#
# for i in range(3,11):
#     r = random.randint(1,255)
#     b = random.randint(1,255)
#     g = random.randint(1,255)
#     rocky.pencolor(r, b, g)
#     for j in range(i):
#         rocky.forward(100)
#         rocky.right(360/i)

#Random walk
# rocky.pensize(8)
# walk = [0, 90, 180, 270]
#
# screen.colormode(255)
# rocky.speed(9)
#
# for i in range(100):
#     r = random.randint(1, 255)
#     b = random.randint(1,255)
#     g = random.randint(1,255)
#     rocky.pencolor(r, b, g)
#     choice = random.choice(walk)
#     rocky.setheading(choice)
#     rocky.forward(20)

#spirograph

# rocky.speed(12)
# screen.colormode(255)
# for i in range(72):
#     r = random.randint(1, 255)
#     b = random.randint(1,255)
#     g = random.randint(1,255)
#     rocky.pencolor(r, b, g)
#     rocky.circle(100)
#     rocky.left(5)
#     angle = rocky.heading()

screen.exitonclick()
