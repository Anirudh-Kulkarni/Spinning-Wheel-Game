#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 16:59:42 2024

@author: anirudhkulkarni
"""

from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score= 0
        self.hideturtle()
        self.goto((0, 280))
        self.color("White")
        self.write(f"Score = {self.score}", align="center", font=('Times New Roman', 15, 'normal'))
        
    def score_increase(self):
        self.clear()
        self.score += 1
        self.write(f"Score = {self.score}", align="center", font=('Times New Roman', 15, 'normal'))
        
        
    
    def game_over(self):
        self.penup()
        self.goto(0,0)
        
        self.write("GAME OVER", align="center", font=('Times New Roman', 15, 'normal'))
        