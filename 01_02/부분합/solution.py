num = int(input())
arr = list(map(int, input().split()))

question_num = int(input())

for _ in range(question_num):
    a, b = map(int, input().split())
    a = a - 1
    sum = 0
    for i in range(a, b):
        sum = sum + arr[i]
    print(sum)