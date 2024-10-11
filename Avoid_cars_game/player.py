STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle

class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.goto(0,-290)
        self.setheading(90)

    
    def move_up(self):
        self.forward(10)
        
    def reset_pos(self):
        self.penup()
        self.goto(0,-290)
        