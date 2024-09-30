SHOW_MONEY = 1
WIHTHDRAW = 2
DEPOSIT = 3
EXIT = 4

money = 0


def show_money():
    print(f"잔액은 {money} 입니다")

def deposit_menu():
    delta = int(input("입금할 금액을 입력하세요"))
    deposit(delta)

def deposit(delta):
    if delta < 0:
        print("입금할 금액이 0보다 작습니다")
        return
    
    global money
    money += delta
    show_money()
    

def withdraw_menu():
    delta = int(input("인출할 금액을 입력하세요"))
    withdraw(delta)
    show_money()
def withdraw(delta):
    if delta < 0:
        print("인출할 금액이 0보다 작습니다")
        return
    global money
    if money < delta:
        print("돈이 부족합니다")
        return
    money -= delta
    

def show_menu():
    user_input = int(input("1. 잔액 보기 2.인출 3.저금 4. 종료"))
    return user_input

def main():
    while True:
        user_input = int(show_menu())

        if(user_input == SHOW_MONEY):
            show_money()
        elif(user_input == WIHTHDRAW):
            withdraw_menu()
        elif(user_input == DEPOSIT):
            deposit_menu()
        elif(user_input == EXIT):
            break
        else:
            print("잘못된 입력입니다.")

if __name__ == "__main__":
    main()



        
