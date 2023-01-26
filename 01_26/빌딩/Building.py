number = int(input())
buildings = list(map(int, input().split(' ')))


tmp = buildings[0]
leftNum = 1
for i in range(number):
    if tmp < buildings[i]:
        leftNum += 1
        tmp = buildings[i]

buildings.reverse()

tmp = buildings[0]
rightNum = 1
for i in range(number):
    if tmp < buildings[i]:
        rightNum += 1
        tmp = buildings[i]

print(leftNum, rightNum)
