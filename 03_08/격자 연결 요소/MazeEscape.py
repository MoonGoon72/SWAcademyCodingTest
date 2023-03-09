n, m = map(int, input().split(' '))

graph = [list(map(str, input().rstrip())) for _ in range(n)]

result = 0

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

def dfs(y, x):
    isWall = False
    if graph[y][x] == ".": return 0
    stack = [(y, x)]
    while stack:
        y, x = stack.pop()
        if graph[y][x] == "#":
            isWall = True
            graph[y][x] = "."
        for num in range(4):
            nx = x + dx[num]
            ny = y + dy[num]
            if nx >= 0 and nx < m and ny >= 0 and ny < n:
                if graph[ny][nx] == "#":
                    stack.append((ny, nx))
    if isWall: return 1
    else: return 0

for i in range(n):
    for j in range(m):
        result += dfs(i, j)
print(result)