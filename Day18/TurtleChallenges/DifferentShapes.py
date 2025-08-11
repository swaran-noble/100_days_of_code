import turtle
from turtle import Turtle
from random import randint

turtle.colormode(255)
tim = Turtle()

def draw_shape(num_sides):
    angle = 360/num_sides
    for _ in range(num_sides):
        tim.forward(100)
        tim.right(angle)

for shape in range(3,11):
    r = randint(0,255)
    g = randint(0, 255)
    b = randint(0, 255)
    tim.color(r,g,b)
    draw_shape(shape)

