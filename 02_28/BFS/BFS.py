from collections import deque
n, m = map(int, input().split(' '))
graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque()
    queue.append(start)
    while queue:
        now = queue.popleft()
        if not visited[now]: print(now, end=' ')
        visited[now] = True
        graph[now].sort()
        for i in graph[now]:
            if not visited[i]:
                queue.append(i)
bfs(1)