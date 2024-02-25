# -*- coding: utf-8 -*-
"""
Created on Sat Feb 24 21:08:37 2024

@author: iamrs
"""

import turtle

# Function to draw a circle
def draw_circle(t, color, radius, x, y):
    t.penup()
    t.goto(x, y-radius)
    t.pendown()
    t.color(color)
    t.begin_fill()
    t.circle(radius)
    t.end_fill()

# Function to draw a rectangle
def draw_rectangle(t, color, width, height, x, y):
    t.penup()
    t.goto(x-width/2, y-height/2)
    t.pendown()
    t.color(color)
    t.begin_fill()
    for _ in range(2):
        t.forward(width)
        t.left(90)
        t.forward(height)
        t.left(90)
    t.end_fill()

# Function to draw Cristiano Ronaldo's face
def draw_ronaldo_face():
    screen = turtle.Screen()
    screen.bgcolor("white")

    t = turtle.Turtle()
    t.speed(0)

    # Drawing the head
    draw_circle(t, "tan", 100, 0, 0)

    # Drawing the eyes
    draw_circle(t, "white", 15, -35, 30) # Left eye
    draw_circle(t, "white", 15, 35, 30)  # Right eye

    # Drawing the pupils
    draw_circle(t, "black", 8, -35, 30)  # Left pupil
    draw_circle(t, "black", 8, 35, 30)   # Right pupil

    # Drawing the nose
    t.penup()
    t.goto(0, 10)
    t.pendown()
    t.setheading(-90)
    t.forward(25)
    t.left(135)
    t.forward(35)

    # Drawing the mouth
    t.penup()
    t.goto(-25, -20)
    t.pendown()
    t.setheading(-60)
    t.circle(30, 120)

    # Drawing the eyebrows
    draw_rectangle(t, "brown", 30, 5, -35, 80)  # Left eyebrow
    draw_rectangle(t, "brown", 30, 5, 5, 80)     # Right eyebrow

    t.hideturtle()
    screen.mainloop()

# Main function
def main():
    draw_ronaldo_face()

if __name__ == "__main__":
    main()
