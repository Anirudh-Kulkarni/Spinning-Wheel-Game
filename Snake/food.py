#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Aug 14 15:35:48 2024

@author: anirudhkulkarni
"""

import random
from turtle import Turtle
SCREEN_W = 600
SCREEN_H = 600

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.posn = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(self.posn)
        self.shape("circle")
        self.shapesize(stretch_len = 0.5,stretch_wid = 0.5)
        self.color("blue")

    def move_food(self):
        self.posn = (random.randint(-280, 280), random.randint(-280, 280))
        self.goto(self.posn)
        