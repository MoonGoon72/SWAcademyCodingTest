num = int(input())
numbers = list(map(int, input().split(' ')))
maxNum = max(numbers)
minNum = min(numbers)

arr = list(map(lambda x:x - minNum, numbers))
print(sum(arr))
