n = int(input())
arr = list(map(int, input().split(' ')))

num = 0
for seq in arr:
    num += seq
    print(num, end=' ')
print()
