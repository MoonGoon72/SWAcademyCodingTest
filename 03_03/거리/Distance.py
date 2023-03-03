from collections import deque
from collections import defaultdict

n, m = map(int, input().split(' '))
dic = defaultdict(int)

graph = [[] for _ in range(n + 1)]
visited = [False for _ in range(n + 1)]
dist = [0 for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split(' '))
    graph[a].append(b)
    graph[b].append(a)

def bfs(start):
    queue = deque([start])
    visited[start] = True
    while queue:
        now = queue.popleft()
        graph[now].sort()
        for i in graph[now]:
            if not visited[i]:
                visited[i] = True
                queue.append(i)
                dic[i] = dic[now] + 1

bfs(1)
for num in range(1, n + 1):
    print(dic[num], end=' ')
print()