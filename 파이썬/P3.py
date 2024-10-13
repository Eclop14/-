import turtle
import math

screen = turtle.Screen()
screen.setworldcoordinates(-360, -2, 360, 2)  

t = turtle.Turtle()
t.speed(0)  
t.penup()

t.goto(360, math.sin(3.14 * 360 / 180))
t.shape("turtle")
t.color("red","yellow")

t.penup()  
for degree in range(-360, 361): 
    radian = 3.14 * degree / 180  
    y = math.sin(radian)  
    t.goto(degree, y)  
    t.pendown()  

turtle.done()
