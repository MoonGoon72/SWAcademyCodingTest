text = input()
dic = {'{':'}', '(':')', '[':']'}
stack = []
isTrue = True
for s in text:
    if s == "(": stack.append("(")
    elif s == "{": stack.append("{")
    elif s == "[": stack.append("[")
    else:
        if not stack:
            isTrue = False
            break
        else:
            n = stack.pop()
            if s == dic[n]:
                continue
            else:
                isTrue = False
                break

print("YES") if isTrue and not stack else print("NO")
