def square_list(input_list):
    return [x**2 for x in input_list]

if __name__ == "__main__":
    input_list = [1, 2, 3, 4, 5]
    print(f"결과 리스트 = {square_list(input_list)}")