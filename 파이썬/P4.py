def great(a,b):
    great = 1
    for k in range(1,min(a,b)+1):
        if a % k == 0 and b % k == 0:
            great = k
    return great

a = int(input("첫 번쨰 정수를 입력하시오:"))
b = int(input("두 번쨰 정수를 입력하시오:"))

result = great(a,b)
print(f"{a}와 {b}의 최대 공약수는 {result}입니다")