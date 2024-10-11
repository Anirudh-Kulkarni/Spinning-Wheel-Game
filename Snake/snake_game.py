#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 10:46:52 2024

@author: anirudhkulkarni
"""

from turtle import Screen
import time
from snake import Snake
from food import Food
import turtle as t
from scoreboard import Scoreboard


def snake_game():
    screen = Screen()
    
    
    screen.setup(width = 600, height = 600)
    screen.bgcolor("black")
    screen.title("Snake")
    END_SCREEN = 280
    
    screen.tracer(0)
    my_snake = Snake()
    food = Food()
    my_score = Scoreboard()
    
    screen.listen()
    screen.update()
    game_on = True
    
    
    
    while(game_on):
        
        my_snake.move();
        time.sleep(0.1)        
        screen.onkey(my_snake.move_up, "Up")
        screen.onkey(my_snake.move_down, "Down")
        screen.onkey(my_snake.move_left, "Left")
        screen.onkey(my_snake.move_right, "Right")
        
        if my_snake.snake_body[0].distance(food) <15:  
            my_snake.lengthen_snake()
            food.move_food()
            my_score.score_increase()
        
        my_snake_x_coord = my_snake.snake_body[0].pos()[0]
        my_snake_y_coord = my_snake.snake_body[0].pos()[1]
        
        game_over_cond1 = my_snake_x_coord < -END_SCREEN or my_snake_x_coord > END_SCREEN or my_snake_y_coord < -END_SCREEN or my_snake_y_coord > END_SCREEN
        
        for snake_idx in range(1,len(my_snake.snake_body)):    
            game_over_cond2 = False
            if my_snake.snake_body[0].pos() == my_snake.snake_body[snake_idx].pos():
                game_over_cond2 = True
            
        if game_over_cond1 or game_over_cond2:
            game_on = False
            my_score.game_over()
            
            
            
            
        screen.update()
        
    
    
        
    
    
    screen.exitonclick(close_turtle)
    
    
def close_turtle():
    t.bye()  # Close the Turtle graphics window without logs