n, m = map(int, input().split(' '))
arr = list(map(int, input().split(' ')))
for _ in range(m):
    left, right = map(int, input().split(' '))
    print(sum(arr[left-1:right]))
