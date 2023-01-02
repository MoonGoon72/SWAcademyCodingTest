arr1 = list(map(int, input().split()))
arr2 = list(map(int, input().split()))

arr1_len = len(arr1)
arr2_len = len(arr2)

if arr1_len == arr2_len :
    for i in range(arr1_len):
        print(arr1[i], end=' ')
        print(arr2[i], end=' ')
elif arr1_len > arr2_len :
    for i in range(arr2_len):
        print(arr1[i], end=' ')
        print(arr2[i], end=' ')
    for i in range(arr2_len, arr1_len):
        print(arr1[i], end=' ')
elif arr1_len < arr2_len :
    for i in range(arr1_len):
        print(arr1[i], end=' ')
        print(arr2[i], end=' ')
    for i in range(arr1_len, arr2_len):
        print(arr2[i], end=' ')
