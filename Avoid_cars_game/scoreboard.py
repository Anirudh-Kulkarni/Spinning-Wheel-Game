FONT = ("Courier", 24, "normal")

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level= 1
        self.hideturtle()
        self.penup()
        self.goto((-200, 250))
        self.write(f"Level : {self.level}", align="center", font=FONT)
        
    def score_increase(self):
        self.clear()
        self.level += 1
        self.write(f"Level : {self.level}", align="center", font=FONT)
        
        
    
    def game_over(self):
        self.penup()
        self.goto(0,0)
        self.write("GAME OVER", align="center", font=FONT)
        