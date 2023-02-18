from collections import deque

n, m = map(int, input().split(' '))
queue = deque(map(lambda x:x, range(1, n+1)))

for _ in range(m):
    text = input()
    if text == "raise":
        if queue:
            tmp = queue.popleft()
            queue.append(tmp)
    elif text == "discard":
        if len(queue) > 1:
            queue.popleft()
print(queue.popleft())