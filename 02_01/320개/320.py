n = int(input())
susis = list(map(int, input().split(' ')))
susis = list(map(lambda x:x -320, susis))
susis = list(map(lambda x:abs(x), susis))

result = susis.index(min(susis)) + 1
print(result)
