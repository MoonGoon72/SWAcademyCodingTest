n = int(input())
sequences = list(map(int, input().split(' ')))

prefixSum = 0
prefixArr = []
for seq in sequences:
    prefixSum += seq
    prefixArr.append(prefixSum)
result = -100
pSum = 0
for i in range(n):
    pSum = max(pSum, 0) + sequences[i]
    result = max(result, pSum)
print(result)
