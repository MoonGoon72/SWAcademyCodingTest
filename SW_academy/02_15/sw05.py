text = input().lower()
query = int(input())
for _ in range(query):
    a, b = map(int, input().split(' '))
    tmp = text[a - 1 : b]
    tmp = list(set(tmp))
    print(tmp)
    length = len(tmp)
    print(1, end="") if length == 26 else print(0, end="")