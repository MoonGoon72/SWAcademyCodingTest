n, m = map(int, input().split(' '))

arr = list(map(lambda x: x + 1, range(n)))
for _ in range(m):
    a, b = map(int, input().split(' '))
    arr[a - 1], arr[b - 1] = arr[b - 1], arr[a - 1]

for i in arr:
    print(i, end=" ")
print()