days = dict()

def add_days():
    global days
    when = input("날짜:(ex:10.21)")
    what = input("일정:")

    infos[name] = phone
    
def del_days():
    global days
    when = input("삭제할 날짜:")
    if when in days:
        days.pop(when)
    

def print_days():
    for when, what in days.items():
        print(when, "일정:",what)
    pass
def main():
    while True:
        show_menu()
        sel = int(input("메뉴 항목을 선택하시오:"))
        if sel == 4:
            break
    munu = [add_days,del_days,print_days]
    menu[sel-1]()
def show_menu():
    print("1. 일정 추가")
    print("2. 일정 삭제")
    print("3. 일정 보기")
    print("4. 종료")
    
