user = int(input("선택하시오(1: 가위 2:바위 3:보)"))

import random
computer = random.randint(1,3)
print("컴퓨터의 선택:",computer)

if user is 1:
    if computer is 1:
        print("draw")
    elif computer is 2:
        print("lose")
    else:
        print("win")

if user is 2:
    if computer is 2:
        print("draw")
    elif computer is 3:
        print("lose")
    else:
        print("win")
else:
    if computer is 3:
        print("draw")
    elif computer is 1:
        print("lose")
    else:
        print("win")
