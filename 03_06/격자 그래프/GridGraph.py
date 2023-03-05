n, m = map(int, input().split(' '))
graph = [list(input()) for _ in range(n)]

dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0

for row in range(n):
    for col in range(m):
        if graph[row][col] != "#":
            for num in range(4):
                nx = col + dx[num]
                ny = row + dy[num]
                if nx >= 0 and nx < m and ny >= 0 and ny < n:
                    if graph[ny][nx] == ".":
                        result += 1
print(n * m, result // 2)
