import time
import random
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
level = 1
i =0
speed = 0.25
game_is_on = True
car = CarManager()
while game_is_on:
    if i % 4 ==0:
        car.newcar()
    if player.win():
        speed*=0.5
        level += 1
        score.update(level)
    x = player.xcor()
    y = player.ycor()
    if car.checkcollide(x,y):
        score.lose(level)
        game_is_on = False
    car.frwd()
    screen.onkey(player.move,"Up")
    time.sleep(speed)
    screen.update()
    i+=1

screen.exitonclick()