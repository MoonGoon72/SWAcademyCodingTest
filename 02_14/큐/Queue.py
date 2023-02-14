from collections import deque
n = int(input())
queue = deque()
for _ in range(n):
    oper = input()

    if oper.find("pop") != -1:
        if len(queue) == 0:
            print("-1")
        else:
            print(queue.popleft())
    elif oper.find("push") != -1:
        a, b = oper.split(' ')
        queue.append(b)
