import turtle
import random

t = turtle.Turtle()
t.shape("turtle")

for i in range(10):
    x = random.randint(-350, 350)
    y = random.randint(-250, 250)
    t.penup()
    t.goto(x, y)
    t.pendown()
    
    r = random.randint(1, 100)
 
    t.circle(r)
