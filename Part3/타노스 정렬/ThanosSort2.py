import math
testCase = int(input())

for _ in range(testCase):
    arrLen = int(input())
    arr = list(map(int, input().split(" ")))
    i = arrLen - 1

    while i > 0:
        if arr[i] < arr[i-1]:
            arr[i-1] = math.floor(arr[i-1] / 2)
            i += 1
        i -= 1
        print(arr)
    for i in arr:
        print(i, end=" ")
    print()
    