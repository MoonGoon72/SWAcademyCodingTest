n, m = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
isTrue = True
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)
for i in graph:
    if len(list(set(i))) != len(i): isTrue = False
print("YES") if isTrue else print("NO")