from turtle import Turtle,Screen
import random
screen = Screen()
screen.setup(width=500, height= 400)

#turtle draw
# def forward():
#     rocky.forward(10)
#
# def backward():
#     rocky.backward(10)
#
# def clock():
#     rocky.right(10)
#
# def counterclock():
#     rocky.left(10)
#
# def clear():
#     rocky.clear()
#     rocky.penup()
#     rocky.home()
#     rocky.pendown()
# screen.listen()
# screen.onkey(forward,"W")
# screen.onkey(backward,"S")
# screen.onkey(clock,"D")
# screen.onkey(counterclock,"A")
#screen.onkey(clear,"C")

#Turtle race
text = screen.textinput("Who will win?","Enter a color")
color = ["red","orange","yellow","green","blue","black","violet"]
y = [-150,-100,-50,0,50,100,150]
turtles = []
for i in range(7):
    rocky = Turtle()
    rocky.shape("turtle")
    rocky.penup()
    rocky.color(color[i])
    rocky.goto(-230,y[i])
    turtles.append(rocky)
if text:
    game = True
while game:
    for i in turtles:
        if i.xcor()>230:
            win = i.pencolor()
            print(f"{win} turtle won")
            game = False
        num = random.randint(0,10)
        i.forward(num)

if win == text:
    print("You won")
else:
    print("You Lose")

screen.exitonclick()