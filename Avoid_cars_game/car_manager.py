COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5

import random
from turtle import Turtle

class CarManager(Turtle):
    def __init__(self):
        super().__init__()
        self.color(random.choice(COLORS))
        self.shape("square")
        self.shapesize(stretch_wid=1,stretch_len=2)
        self.penup()
        self.goto((290, random.randint(-280,280)))
        self.setheading(180)
        
    def move_car(self, car_speed):
        self.forward(car_speed)
        
    
        

