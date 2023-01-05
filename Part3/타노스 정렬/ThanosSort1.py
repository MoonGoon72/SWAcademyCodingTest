import math
testCase = int(input())

for _ in range(testCase):
    arrLen = int(input())
    arr = list(map(int, input().split(" ")))

    while True:
        change = 0
        for i in range(0, arrLen - 1, 1):
            if arr[i] > arr[i+1]: 
                arr[i] = math.floor(arr[i] / 2)
                change += 1
        if change == 0 : break
    for i in arr:
        print(i, end=" ")
    print()
