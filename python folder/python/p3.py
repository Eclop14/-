    # problem1.py
def calculate_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    print(f"결과값 = {calculate_product(input_list)}")

# problem2.py
def remove_duplicates(input_list):
    return list(dict.fromkeys(input_list))

if __name__ == "__main__":
    input_list = [10, 20, 30, 20, 10, 50, 60]
    print(f"결과 리스트 = {remove_duplicates(input_list)}")

# problem3.py
def replace_ten_with_hundred(input_list):
    return [100 if x == 10 else x for x in input_list]

if __name__ == "__main__":
    input_list = [5, 10, 15, 20, 25]
    print(f"결과 리스트 = {replace_ten_with_hundred(input_list)}")

# problem4.py
def remove_tens(input_list):
    return [x for x in input_list if x != 10]

if __name__ == "__main__":
    input_list = [5, 10, 15, 10, 25]
    print(f"결과 리스트 = {remove_tens(input_list)}")

# problem5.py
def square_list(input_list):
    return [x**2 for x in input_list]

if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    print(f"결과 리스트 = {square_list(input_list)}")

# problem6.py
import random

def generate_random_list():
    return [random.randint(1, 100) for _ in range(10)]

if __name__ == "__main__":
    values = generate_random_list()
    print(f"생성된 리스트: {values}")

# problem7.py
def print_star_graph(values):
    for value in values:
        print(f"{value:2d} {'*' * value}")

if __name__ == "__main__":
    values = [20, 1, 12, 9, 18]
    print_star_graph(values)

# problem8.py
def count_same_first_last(words):
    return sum(1 for word in words if len(word) > 1 and word[0] == word[-1])

if __name__ == "__main__":
    words = ['aba', 'xyz', 'abc', '121']
    print(f"문자열의 개수 = {count_same_first_last(words)}")

# problem9.py
def has_common_item(list1, list2):
    return bool(set(list1) & set(list2))

if __name__ == "__main__":
    list1 = [1, 2, 3, 4, 5, 6]
    list2 = [6, 7, 8, 9, 10]
    print(f"공통 항목 존재: {has_common_item(list1, list2)}")

# problem10.py
import random

def select_random_item(items):
    return random.choice(items)

if __name__ == "__main__":
    list1 = ['a0', 'a1', 'a2', 'a3', 'a4', 'a5', 'a6', 'a7', 'a8', 'a9']
    print(f"선택된 항목: {select_random_item(list1)}")

# problem11.py
def find_common_elements(list1, list2):
    return list(set(list1) & set(list2))

if __name__ == "__main__":
    a = [1, 2, 3, 4, 5]
    b = [1, 3, 3, 4, 5, 6, 7]
    print(f"공통 요소: {find_common_elements(a, b)}")



# problem12.py
import turtle

def draw_clock(numbers):
    screen = turtle.Screen()
    screen.setup(400, 400)
    
    t = turtle.Turtle()
    t.penup()
    t.goto(0, -150)
    t.pendown()
    
    for num in numbers:
        t.forward(150)
        t.write(num, align="center", font=("Arial", 12, "normal"))
        t.backward(150)
        t.right(360 / len(numbers))
    
    screen.exitonclick()

if __name__ == "__main__":
    numbers = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100, 110, 120]
    draw_clock(numbers)

# problem13.py
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

# problem14.py
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
# problem15.py
def create_3d_array():
    return [[['#' for _ in range(5)] for _ in range(4)] for _ in range(3)]

if __name__ == "__main__":
    array_3d = create_3d_array()
    print("3차원 배열:")
    for layer in array_3d:
        for row in layer:
            print(row)
        print()

# problem16.py
def create_theater():
    return [[0 for _ in range(10)] for _ in range(10)]

def print_theater(theater):
    print("  1 2 3 4 5 6 7 8 9 10")
    print("-" * 23)
    for i, row in enumerate(theater, 1):
        print(f"{i}|{' '.join(str(seat) for seat in row)}")

def reserve_seat(theater, row, col):
    if theater[row-1][col-1] == 0:
        theater[row-1][col-1] = 1
        return True
    return False

if __name__ == "__main__":
    theater = create_theater()
    print_theater(theater)

    while True:
        row = int(input("원하시는 좌석의 행번호를 입력하세요(종료는 -1): "))
        if row == -1:
            break
        col = int(input("원하시는 좌석의 열번호를 입력하세요(종료는 -1): "))
        if col == -1:
            break
        
        if reserve_seat(theater, row, col):
            print("예약되었습니다.")
        else:
            print("이미 예약된 좌석입니다.")
        
        print_theater(theater)

    print("예약이 완료되었습니다.")