def create_3d_array():
    return [[['#' for _ in range(4)] for _ in range(4)] for _ in range(6)]

if __name__ == "__main__":
    array_3d = create_3d_array()
    print("3차원 배열:")
    print(array_3d)