#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Aug 12 15:06:00 2024

@author: anirudhkulkarni
"""

import colorgram
import turtle as t
from turtle import Turtle, Screen
import random



def hirst_painting():
    
    
    timmy = Turtle()
    t.colormode(255)
    
    # Extract 6 colors from an image.
    colors = colorgram.extract('Hirst/hirst.jpg', 1000)
    
    # colorgram.extract returns Color objects, which let you access
    # RGB, HSL, and what proportion of the image was that color.
    
    list_colors= []
    for color in colors:
    
        rgb = color.rgb # e.g. (255, 151, 210)
        
        # RGB and HSL are named tuples, so values can be accessed as properties.
        # These all work just as well:
    
        list_colors.append((rgb.r, rgb.g, rgb.b))
     
    screen = Screen()    
    screen.title("Hirst Painting")

    start_pos = [-220, -250]
    timmy.hideturtle()
    timmy.penup()
    timmy.goto(start_pos)
    timmy.pendown()
    timmy.speed("fastest")
    for row_num in range(0,10):
        for col_num in range(0,10):
            timmy.color(random.choice(list_colors))
            timmy.begin_fill()
            timmy.circle(10)
            timmy.end_fill()
            timmy.penup()
            timmy.forward(50)
            timmy.pendown()
        timmy.penup()
        timmy.left(180)
        timmy.forward(500)
        timmy.right(90)
        timmy.forward(50)
        timmy.right(90)
        timmy.pendown()
    
    
    
    screen.exitonclick(close_turtle)
    
    
        
def close_turtle():
    t.bye()  # Close the Turtle graphics window without logs