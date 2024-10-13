import turtle

def draw_clock(numbers):
    screen = turtle.Screen()
    screen.setup(400, 400)
    
    t = turtle.Turtle()
    t.penup()
    t.goto(0, -150)
    t.pendown()
    
    for num in numbers:
        t.forward(numbers)
        t.write(num, align="center", font=("Arial", 12, "normal"))
        t.backward(150)
        t.right(360 / len(numbers))
    
    screen.exitonclick()

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    draw_clock(numbers)
