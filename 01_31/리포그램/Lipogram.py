from string import ascii_lowercase
alphabet = list(ascii_lowercase)
s = input().lower()
s = s.replace(' ', '')

s = list(set(s))

if len(s) == 26:
    print("NO")
else:
    result = list(set(alphabet).difference(s))
    result.sort()
    print("YES")
    for i in result:
        print(i, end="")
    print()
