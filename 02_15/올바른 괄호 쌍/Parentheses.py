text = input()

stack = []
isTrue = True
for s in text:
    if s == "(": stack.append("(")
    else:
        if not stack:
            isTrue = False
            break
        if stack.pop() != "(":
            isTrue = False
            break
print("YES") if isTrue and not stack else print("NO")
