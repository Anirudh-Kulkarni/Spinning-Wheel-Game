import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
import random
import turtle as t

def avoid_cars_game():
    screen = Screen()
    screen.title("Race to the End")
    screen.setup(width=600, height=600)
    screen.tracer(0)
    screen.listen()
    car_speed = 5
    increment_speed = 10
    
    scoreboard = Scoreboard()
    player = Player()
    list_cars =[]
    
    game_is_on = True
    while game_is_on:
        time.sleep(0.1)
        screen.update()
        screen.onkey(player.move_up, "Up")
        if random.random()<0.25: # creating a car with 25% probability every 10th of a second
            list_cars.append(CarManager())
        
        for car in list_cars: 
            car.move_car(car_speed) 
            if player.distance(car) < 15:
                game_is_on = False
                scoreboard.game_over()
                       
        if player.ycor()>290:
            scoreboard.score_increase()
            player.reset_pos()
            car_speed += increment_speed
        
        
        
    screen.exitonclick(close_turtle)
    
    
def close_turtle():
    t.bye()  # Close the Turtle graphics window without logs