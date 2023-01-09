from collections import deque
col, row = map(int, input().split())
feed = int(input())

graph = list(list(0 for _ in range(col)) for _ in range(row))
snake = 0
feeds = deque()
for _ in range(feed):
    a, b = map(int, input().split())
    feeds.append((a, b))

y, x = feeds.popleft()
graph[y][x] = 1

orders = input()
nowX = 0
nowY = 0

for order in orders:
    if order == 'R':
        nowX += 1
        if nowX == col:
            print(-1)
            break
        if graph[nowY][nowX] == 1:
            snake += 1
            graph[nowY][nowX] == 0
            if len(feeds) != 0:
                y, x = feeds.popleft()
                graph[y][x] = 1
        print(snake)
    elif order == 'L':
        nowX -= 1
        if nowX < 0:
            print(-1)
            break
        if graph[nowY][nowX] == 1:
            snake += 1
            graph[nowY][nowX] == 0
            if len(feeds) != 0:
                y, x = feeds.popleft()
                graph[y][x] = 1
        print(snake)
    if order == 'U':
        nowY -= 1
        if nowY < 0:
            print(-1)
            break
        if graph[nowY][nowX] == 1:
            snake += 1
            graph[nowY][nowX] == 0
            if len(feeds) != 0:
                y, x = feeds.popleft()
                graph[y][x] = 1
        print(snake)
    elif order == 'D':
        nowY += 1
        if nowY == row:
            print(-1)
            break
        if graph[nowY][nowX] == 1:
            snake += 1
            graph[nowY][nowX] == 0
            if len(feeds) != 0:
                y, x = feeds.popleft()
                graph[y][x] = 1
        print(snake)
