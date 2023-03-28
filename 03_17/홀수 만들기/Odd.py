import heapq

n = int(input())
queue = []
arr = map(int, input().split(' '))
for num in arr:
    heapq.heappush(queue, num)

while len(queue) >= 2:
    a = heapq.heappop(queue)
    b = heapq.heappop(queue)
    tmp = a + b
    if (tmp % 2) == 1:
        heapq.heappush(queue, tmp)
if queue:
    print(heapq.heappop(queue))
else:
    print(-1)
