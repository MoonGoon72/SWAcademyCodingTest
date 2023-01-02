from collections import deque

row, col = map(int, input().split())

i, j, color = input().split()
i, j = int(i), int(j)

graph = [list(input().rstrip()) for _ in range(row)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]
now_color = graph[i][j]

queue = deque()
queue.append((i,j))
def bfs():
    while queue:
        a, b = queue.popleft()

        for k in range(4):
            nx = a + dx[k]
            ny = b + dy[k]
            if ((nx >= 0 and nx < row) and (ny >= 0 and ny < col)):
                if graph[nx][ny] == now_color:
                    graph[nx][ny] = color;
                    queue.append((nx,ny))
    for i in graph:
        for j in i:
            print(j, end="")
        print()
bfs()
