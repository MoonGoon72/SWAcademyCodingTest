n = int(input())
diversity = input()
result = 2
for div in range(1, n -1):
    left = len(list(set(diversity[:div])))
    right = len(list(set(diversity[div:])))
    result = max(result, left + right)
print(result)
