infos = dict()

def add_info():
    global infos
    name = input("이름:")
    call = input("전화 번호:")

    infos[name] = phone
    
def del_info():
    global infos
    name = input("삭제할 연락처:")
    if name in infos:
        infos.pop(name)
    
def search_info():
    print("검색할 연락처 입력:")
    name = input("name:")
    if name in infos:
        print(name, " 의 연락처는",infos[name])
    else:
        print("전화번호를 찾을 수 없습니다")
    pass
def print_info():
    for name, phone in infos.items():
        print(name, "phone number:",phone)
    pass
def main():
    while True:
        show_menu()
        sel = int(input("메뉴 항목을 선택하시오:"))
        if sel == 5:
            break
    munu = [add_info,del_info,search_info,print_info]
    menu[sel-1]()
def show_menu():
    print("1. 연락처 추가")
    print("2. 연락처 삭제")
    print("3. 연락처 검색")
    print("4. 연락처 출력")
    print("5. 종료")
