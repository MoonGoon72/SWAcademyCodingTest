people = int(input())
moneys = list(map(int, input().split(' ')))
filterArr = []

for i in range(people):
    minArr = list(filter(lambda x: x < moneys[i], moneys))
    filterArr.append(len(minArr))
    

for num in filterArr:
    print(num, (people - 1 - num))
