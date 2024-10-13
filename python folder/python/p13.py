import turtle

def draw_squares():
    colors = ["yellow", "red", "purple", "blue"]
    
    screen = turtle.Screen()
    screen.setup(400, 400)
    
    t = turtle.Turtle()
    t.speed(0)  # Fastest speed
    
    for i, color in enumerate(colors):
        t.penup()
        t.goto(50 * i, 50 * i)
        t.pendown()
        t.fillcolor(color)
        t.begin_fill()
        for _ in range(4):
            t.forward(100)
            t.right(90)
        t.end_fill()
    
    screen.exitonclick()

if __name__ == "__main__":
    draw_squares()
