import random
pb = 30
row_num = 10
col_num = 10

matrix = [["#" if random.randint(1,100) < pb else '.' \
            for col in range(col_num)] for row in range(row_num)]

def set_count(row,col):
    global matrix
    if row >= row_num or row < 0:
        return
    if col >= col_num or col < 0:
        return

    
    if matrix[row][col] == ".":
        matrix[row][col] = 1
    elif matrix[row][col] == '#':
        pass
    else:
        matrix[row][col] += 1

for i in range(row_num):
    for j in range(len(matrix[i])):
        if matrix[i][j] == "#":
            set_count(i-1,j)
            set_count(i+1,j)
            set_count(i,j-1)
            set_count(i,j+1)
            set_count(i-1,j-1)
            set_count(i+1,j+1)
            set_count(i+1,j-1)
            set_count(i-1,j+1)
            
for row in matrix:
    for cell in row:
        print(cell, end = " ")
    print()


