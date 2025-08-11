import turtle as t
import random


tim = t.Turtle()

t.colormode(255)
directions = [0,90,180,270]
tim.pensize(10)

for _ in range(200):
    r = random.randint(0,255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    tim.color(r,g,b)
    tim.forward(30)
    tim.setheading(random.choice(directions))




