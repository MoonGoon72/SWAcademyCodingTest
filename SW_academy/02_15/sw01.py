import math
a, b = map(int, input().split(' '))

div = math.ceil((a + b) / 2)

diff = (a + b) % 2

num = max(a, b) - div

print(diff, num)