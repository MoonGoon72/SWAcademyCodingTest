testCase = int(input())

for _ in range(testCase):
    day, upPrice, buyDay = map(int, input().split(' '))
    stocks = list(map(int, input().split(' ')))
    isSell = False
    buyPrice = stocks[buyDay-1]
    for i in range(buyDay, day, 1):
        if buyPrice + upPrice <= stocks[i]:
            print(i+1)
            isSell = True
            break
    if not isSell: print("JB")
