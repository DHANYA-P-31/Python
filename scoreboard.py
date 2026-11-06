from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.goto(-225,260)
        self.write(f"Level: {1}",False,"center",FONT)

    def update(self,score):
        self.clear()
        self.write(f"Level: {score}", False, "center",FONT)

    def lose(self,score):
        self.color("red")
        self.goto(0,0)
        self.write(f"GAME OVER YOUR FINAL SCORE IS {score}",False, "center",FONT)
