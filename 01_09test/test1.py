testCase = int(input())

for _ in range(testCase):
    a, b = input().split(' ')
    a = int(a)

    result = 0
    if b == 'K':
        result = a / 1.6
        result = round(result + 0.000001, 2)
    else:
        result = 1.6 * a
    print(result)