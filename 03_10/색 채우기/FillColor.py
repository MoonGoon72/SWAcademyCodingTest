n, m = map(int, input().split(' '))
y, x = map(int, input().split(' '))

graph = [list(map(str, input().rstrip())) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(y, x):
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        graph[y][x] = "@"
        for num in range(4):
            nx = x + dx[num]
            ny = y + dy[num]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[ny][nx] == ".":
                    stack.append((ny, nx))

dfs(y-1, x-1)
for i in range(n):
    for j in range(m):
        print(graph[i][j], end='')
    print()
print()