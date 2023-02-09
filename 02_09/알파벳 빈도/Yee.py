n, m = map(int, input().split(' '))
text = input()

for _ in range(m):
    left, right = map(int, input().split(' '))
    print(text.count('e', left - 1, right))