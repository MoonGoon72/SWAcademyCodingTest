n, m = map(int, input().split(' '))
adj = [[] for _ in range(n + 1)]

for _ in range(m):
    a, b = map(int, input().split(' '))
    adj[a].append(b)
    adj[b].append(a)

for i in range(1, n + 1, 1):
    adj[i].sort()
    if adj[i]:
        for j in adj[i]:
            print(j, end=" ")
    else: print("-1", end=" ")
    print()
