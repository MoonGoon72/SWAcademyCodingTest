book = input()
action = int(input())
left = list(book[:1])
right = list(book[:0:-1])

for _ in range(action):
    whatToDo = input()
    if whatToDo == "move left":
        if len(left) != 1:
            right.append(left.pop())
    elif whatToDo == "move right":
        if len(right) != 1:
            left.append(right.pop())
    elif whatToDo == "tear left":
        if len(left) != 1:
            left.pop()
    elif whatToDo == "tear right":
        if len(right) != 1:
            right.pop()
print(left.pop(), right.pop())
