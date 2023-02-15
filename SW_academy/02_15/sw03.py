n = int(input())
arr = list(map(int, input().split(' ')))
isOkey = False
for i in range(n):
    if sum(arr[ : i]) == sum(arr[i + 1 : ]):
        print(i + 1)
        isOkey = True
        break

if not isOkey : print(-1)