import turtle
import random

def draw_dice_roll():
    screen = turtle.Screen()
    screen.setup(600, 300)
    
    die = [1, 2, 3, 4, 5, 6]
    distance = random.choice(die)
    
    t1 = turtle.Turtle()
    t2 = turtle.Turtle()
    
    t1.penup()
    t2.penup()
    
    t1.goto(-250, 0)
    t2.goto(-250, -50)
    
    t1.pendown()
    t2.pendown()
    
    t1.forward(50 * distance)
    t1.dot(20)
    
    t2.forward(50 * distance)
    t2.dot(20, "red")
    
    screen.exitonclick()

if __name__ == "__main__":
    draw_dice_roll()