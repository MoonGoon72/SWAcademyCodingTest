n, m = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
cnt = 0

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def dfs(start):
    isTrue = False
    stack = [start]
    while stack:
        now = stack.pop()
        if not visited[now]:
            visited[now] = True
            isTrue = True
        graph[now].sort(reverse=True)
        for num in graph[now]:
            if not visited[num]: stack.append(num)
    if isTrue:
        return 1
    else:
        return 0

for i in range(1, n + 1):
    cnt += dfs(i)

print(cnt)