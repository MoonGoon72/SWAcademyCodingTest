n = int(input())
arr = []
for _ in range(n):
    oper = input()

    if oper.find("pop") != -1:
        if len(arr) == 0:
            print("-1")
        else:
            print(arr.pop())
    elif oper.find("push") != -1:
        a, b = oper.split(' ')
        arr.append(b)
