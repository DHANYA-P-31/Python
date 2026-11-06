from turtle import Turtle,Screen
from Pong import Paddle
from board import Score
from ball import Ball
import random

screen = Screen()
screen.setup(height = 600, width = 800)
screen.bgcolor("white")
screen.title("PingPong")
screen.tracer(0)
screen.listen()

line = Turtle()
line.hideturtle()
line.setpos(0,300)
line.goto(0,-300)

score1 = Score(-30,275)
score2 = Score(30,275)

pong = Paddle(-380)
bot = Paddle(380)

ball = Ball()

gameOver = False
sc1 = sc2 = 0

ballAngle = [45,135]
ball_speed = 0.05
ball.initial()

while not gameOver:

    screen.update()
    screen.onkey(pong.up,"w")
    screen.onkey(pong.down,"s")
    screen.onkey(bot.up,"Up")
    screen.onkey(bot.down,"Down")

    if (abs(ball.xcor() - pong.xcor()) < 20 and abs(ball.ycor() - pong.ycor()) < 80) or (
                abs(ball.xcor() - bot.xcor()) < 20 and abs(ball.ycor() - bot.ycor()) < 80):
        b = random.choice(ballAngle)
        ball_speed *= 0.9
        ball.setheading((ball.heading() + b) % 360)

    elif abs(ball.ycor()) > 270:
        b = random.choice(ballAngle)
        ball.setheading((ball.heading()+b)%360)

    elif ball.xcor() > 390:
        ball.initial()
        ball_speed= 0.05
        b = random.choice(ballAngle)
        sc1+=1
        score1.update(sc1)

    elif ball.xcor() < -390:
        ball.initial()
        ball_speed= 0.05
        sc2+=1
        score2.update(sc2)

    if sc1>10:
        score1.win1()
        score2.win1()
        gameOver=True

    if sc2>10:
        score1.win2()
        score2.win2()
        gameOver=True

    ball.move(ball_speed)

screen.exitonclick()
