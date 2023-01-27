size = int(input())

graph = list(list("*" for _ in range(size)) for _ in range(size))

r1, c1, r2, c2 = map(int, input().split(' '))

if r1 < r2:
    if c1 > c2:
        # 왼쪽 아래, 오른쪽 위
        for i in range(abs(r1 - r2) + 1):
            for j in range(abs(c1 - c2) + 1):
                graph[r1 - 1 + i][c2 - 1 + j] = "."
    else:
        for i in range(abs(r1 - r2) + 1):
            for j in range(abs(c1 - c2) + 1):
                graph[r1 - 1 + i][c1 - 1 + j] = "."
        
        # 왼쪽 위, 오른쪽 아래
else:
    if c1 < c2:
        for i in range(abs(r1 - r2) + 1):
            for j in range(abs(c1 - c2) + 1):
                graph[r2 - 1 + i][c1 - 1 + j] = "."
        # 오른 쪽 위, 왼쪽 아래
    else:
        for i in range(abs(r1 - r2) + 1):
            for j in range(abs(c1 - c2) + 1):
                graph[r2 - 1 + i][c2 - 1 + j] = "."
        # 오른 쪽 아래, 왼쪽 위

for row in graph:
    for index in row:
        print(index, end = '')
    print()
