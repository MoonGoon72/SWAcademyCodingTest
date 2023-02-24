n, m = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
isTrue = True
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

edge = int(input())
edges = list(map(int, input().split(' ')))

vertex = edges[0]
for i in range(1, edge):
    existVertex = edges[i]
    if graph[vertex].count(existVertex) != 0:
        vertex = existVertex
    else:
        print("NO")
        isTrue = False
        break
if isTrue: print("YES")
