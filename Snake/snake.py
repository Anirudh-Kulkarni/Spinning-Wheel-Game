#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 14:39:07 2024

@author: anirudhkulkarni
"""

from turtle import Turtle
START_POS = [(0,0), (-20,0), (-40,0)]
MOVE_DIST = 20

class Snake:
    
    def __init__(self):
        self.snake_body = []
        self.create_snake()
        
    def create_snake(self):    
        self.pos = START_POS
        for snake_idx in range(len(START_POS)):
            self.snake_body.append(Turtle("square"))
            self.snake_body[snake_idx].penup()
            self.snake_body[snake_idx].color("white")
            self.snake_body[snake_idx].setpos(START_POS[snake_idx])
            
    def move(self):
        for snake_idx in range(len(self.snake_body)):
            if snake_idx != 0:
                self.snake_body[snake_idx].goto(self.pos[snake_idx-1])
            else: 
                self.snake_body[snake_idx].forward(MOVE_DIST)
        
        self.pos = [snake.pos() for snake in self.snake_body]
        

    def move_up(self):
        if self.snake_body[0].heading() != 270:
            self.snake_body[0].setheading(90)
        
    def move_down(self):
        if self.snake_body[0].heading() != 90:
            self.snake_body[0].setheading(270)
        
    def move_left(self):
        if self.snake_body[0].heading() != 0:
            self.snake_body[0].setheading(180)
        
    def move_right(self):
        if self.snake_body[0].heading() != 180:
            self.snake_body[0].setheading(0)
            
    def lengthen_snake(self):
        self.snake_body.append(Turtle("square"))
        self.snake_body[-1].penup()
        self.snake_body[-1].color("white")
        self.snake_body[-1].setpos(self.snake_body[-2].pos())
        
            
        
        
        