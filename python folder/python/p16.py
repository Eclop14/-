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