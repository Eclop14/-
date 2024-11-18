import tkinter as tk
import random

WIDTH = 1200
HEIGHT = 600
BALL_RADIUS = 5

root = tk.Tk()
canvas = tk.Canvas(root, width=WIDTH, height=HEIGHT)
canvas.pack()

x1 = WIDTH // 2
y1 = HEIGHT // 2
ball = canvas.create_oval(x1, y1, x1+BALL_RADIUS, y1+BALL_RADIUS,
                         fill="red", outline="red")

dx = 10
dy = 10

balls = []
balls.append([ball, dx, dy])

def create_ball(e):
    ball = canvas.create_oval(e.x, e.y, e.x+BALL_RADIUS, e.y+BALL_RADIUS,
                            fill="red", outline="red")
    dx = random.choice([-10, 10])
    dy = random.choice([-10, 10])
    balls.append([ball, dx, dy])

def move_ball():
    for ball_info in balls:
        ball, dx, dy = ball_info
        x1, y1, x2, y2 = canvas.coords(ball) #현재 좌표 확인
        
        if x2 >= WIDTH or x1 <= 0:
            ball_info[1] = -ball_info[1]
        
        if y2 >= HEIGHT or y1 <= 0:
            ball_info[2] = -ball_info[2]
        
        canvas.move(ball, ball_info[1], ball_info[2])
    
    root.after(100, move_ball)
    print(x1,y1,x2,y2)

canvas.bind("<Button-1>", create_ball)
root.after(100, move_ball)
root.mainloop()
