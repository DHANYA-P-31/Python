from turtle import Turtle

class Score(Turtle):
    def __init__(self,x,y):
        super().__init__()
        self.color("blue")
        self.penup()
        self.hideturtle()
        self.goto(x,y)
        self.write(f"{0}",False,"center",("Arial",16,"bold"))

    def update(self,score):
        self.clear()
        self.write(f" {score}", False, "center",("Arial",16,"bold") )

    def win1(self):
        self.goto(0,0)
        self.write(f"GAME OVER PLAYER1 WON",False, "center",("Arial",20,"bold"))

    def win2(self):
        self.goto(0,0)
        self.write(f"GAME OVER PLAYER2 WON",False, "center",("Arial",20,"bold"))


