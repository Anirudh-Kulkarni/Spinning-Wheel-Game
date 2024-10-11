#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 09:21:27 2024

@author: anirudhkulkarni
"""

#Drawing a Sprigraph

import turtle as t
from turtle import Turtle, Screen
import random

def create_spirograph():
    timmy = Turtle()
    t.colormode(255)
    
    def color_fn():
        r = random.randint(0,255)
        g = random.randint(0,255)
        b = random.randint(0,255)
        return (r,g,b)
        
    for angle in range(0,72):
        timmy.speed("fastest")
        timmy.shape("turtle")
        timmy.color(color_fn())
        
        timmy.circle(50)
        timmy.left(5)
        
    screen = Screen()
    screen.title("Spirograph")
    screen.exitonclick(close_turtle)
    
def close_turtle():
    t.bye()  # Close the Turtle graphics window without logs