import random
from turtle import Turtle,Screen
import time
from Snake import Snake
import Food
import score

screen = Screen()
food = Food.Food()
scoreboard = score.Score()

screen.setup(width=600, height=600)
screen.bgcolor("white")
screen.title("Nokia Snakes")
screen.tracer(0)
screen.listen()

snake = Snake()
game_over = False
i = 0

while not game_over:
    screen.update()
    time.sleep(0.25)

    screen.onkey(snake.up,"Up")
    screen.onkey(snake.down, "Down")
    screen.onkey(snake.right, "Right")
    screen.onkey(snake.left, "Left")

    snake.move()

    if snake.body[0].distance(food) < 20:
        i+=1
        scoreboard.update(score=i)
        snake.append()
        food.generate()

    if abs(snake.body[0].xcor())>290 or abs(snake.body[0].ycor())>290:
            game_over = True

    for body in snake.body[1:]:
        if snake.body[0].distance(body)<2:
            game_over = True

screen.exitonclick()