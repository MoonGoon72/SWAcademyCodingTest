x = int(input())

lo, hi = -1, x

def arithmeticSequence(num):
    return num * (num + 1) / 2

while lo + 1 < hi:
    mid = (lo + hi) // 2

    if arithmeticSequence(mid) < x:
        lo = mid
    else:
        hi = mid
print(hi)