import heapq
n = int(input())
pq = []
for _ in range(n):
    question = input().split()
    if question[0] == 'pop':
        if len(pq) == 0: print(-1)
        # push 의 경우
        else:
            print(heapq.heappop(pq))
    elif question[0] == 'push':
        heapq.heappush(pq, int(question[1]))