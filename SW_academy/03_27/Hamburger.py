a, b = map(int, input().strip().split(' '))
result = 0

while True:
    a -= 2
    b -= 1
    if a >= 0 and b >= 0:
        result += 1
    else:
        break
print(result)