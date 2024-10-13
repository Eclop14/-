import random

def generate_random_list():
    return [random.randint(1, 100) for _ in range(10)]

if __name__ == "__main__":
    values = generate_random_list()
    print(f"생성된 리스트: {values}")