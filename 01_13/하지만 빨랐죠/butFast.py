questionNum = int(input())
# 유클리드 호제법을 사용해야함
def euclid(a, b):
    while b:
        a, b = b, a % b
    return a
    

for _ in range(questionNum):
    a, b = map(int, input().split(' '))
    if b > a: a, b = b, a
    gcd = euclid(a, b)
    print("Perfect") if gcd == 1 else print("Not even close")
