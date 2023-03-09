from collections import deque
n, m = map(int, input().split(' '))

graph = [list(map(str, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(y, x):
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        for num in range(4):
            nx = x + dx[num]
            ny = y + dy[num]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[ny][nx] == ".":
                    stack.append((ny, nx))
                    graph[ny][nx] = graph[y][x] + 1
                elif graph[ny][nx] == "#":
                    graph[ny][nx] = -1
def bfs(y, x):
    queue = deque()
    queue.append((y, x))
    while queue:
        y, x = queue.popleft()
        for num in range(4):
            nx = x + dx[num]
            ny = y + dy[num]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[ny][nx] == ".":
                    queue.append((ny, nx))
                    graph[ny][nx] = graph[y][x] + 1
                elif graph[ny][nx] == "#":
                    graph[ny][nx] = -1
graph[0][0] = 0
bfs(0, 0)
for i in range(n):
    for j in range(m):
        if graph[i][j] == "#" or graph[i][j] == ".": print(-1, end=" ")
        else: print(graph[i][j], end=" ")
    print()
print()