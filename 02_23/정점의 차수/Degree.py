n, m = map(int, input().split(' '))

graph = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

result = 0
for arr in graph:
    result += len(arr)
print(result)