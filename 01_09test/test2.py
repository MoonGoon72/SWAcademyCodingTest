tmp_stack = map(int, input().split())
stack = []
for i in tmp_stack:
    stack.append(int(i))
target = []
result = 0

while (len(stack) > 1):
    small = min(stack)
    index = stack.index(small)
    a = stack.pop(index)
    small = min(stack)
    index = stack.index(small)
    b = stack.pop(index)
    tmp = a + b
    target.append(tmp)
    stack.append(tmp)
for i in target:
    result += i
print(result)