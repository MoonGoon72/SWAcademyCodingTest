arr1 = list(map(int,input().split()))
arr2 = list(map(int,input().split()))

arr3 = []
arr4 = []
i = 0
while i < len(arr1):
    arrSum = arr1[i] + arr2[i]
    if arrSum != 0:
        arr3.append(arr1[i] + arr2[i])
        arr3.append(arr1[i+1])
    i += 2

i = 0
while i < len(arr1):
    arrMinus = arr1[i] - arr2[i]
    if arrMinus != 0:
        arr4.append(arr1[i] - arr2[i])
        arr4.append(arr1[i+1])
    i += 2

for i in arr3:
    print(i,end=" ")
print()
for i in arr4:
    print(i,end=" ")
print()
