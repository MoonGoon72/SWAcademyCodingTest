INF = float('inf')
NINF = float('-inf')
n, x = map(int, input().split())
a = list(map(int, input().split(' ')))
lo, hi = -1, n

while lo + 1 < hi:
    print(lo, hi)
    mid = (lo + hi) // 2

    if a[mid] < x:
        lo = mid
    else:
        hi = mid
print(hi) if x <= a[n - 1] else print(n)