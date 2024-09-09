import turtle
t= turtle.Turtle()
t.shape("turtle")

s = turtle.textinput("", "도형을 입력하시오: ")

if s == "사각형":
    w = int(turtle.textinput("","가로:"))
    h = int(turtle.textinput("","세로:"))
    for i in range(2):
        t.forward(w)
        t.left(90)
        t.forward(h)
        t.left(90)


        
    
    
