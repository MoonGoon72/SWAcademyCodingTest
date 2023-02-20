n, m = map(int, input().split(' '))
graph = [list(0 for _ in range(n)) for _ in range(n)]

for _ in range(m):
    a, b = map(int, input().split(' '))
    a -= 1
    b -= 1
    graph[a][b] = 1
    graph[b][a] = 1
for row in graph:
    for i in row:
        print(i, end=" ")
    print()