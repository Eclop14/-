def calculate_product(numbers):
    result = 1
    for num in numbers:
        result *= num
    return result

if __name__ == "__main__":
    input_list = [1, 2, 3, 4]
    print(f"결과값 = {calculate_product(input_list)}")

