from turtle import Turtle
global highscore


class Score(Turtle):
    def __init__(self):
        with open("my.txt") as file:
            self.highscore = int(file.read())
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(0,275)
        self.write(f"Score : {0}, High score : {self.highscore}",False,"center",("Arial",16,"bold"))

    def update(self,score):
        self.clear()
        self.write(f"Score : {score}, High score : {self.highscore}", False, "center",("Arial",16,"bold") )

    def reset(self,score):
        self.clear()
        if score>self.highscore:
            self.highscore=score
            with open("my.txt","w") as file:
                file.write(str(self.highscore))
        self.write(f"Score : {0}, High score : {self.highscore}", False, "center", ("Arial", 16, "bold"))

