n = int(input())
sequences = list(map(int, input().split(' ')))

result = -100
pSum = 0
for i in range(n):
    pSum = max(pSum, 0) + sequences[i]
    result = max(result, pSum)
print(result)
