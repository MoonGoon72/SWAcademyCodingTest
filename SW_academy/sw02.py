num = int(input())

for _ in range(num):
    braket = input()
    braket_len = len(braket)
    alist = list()
    stack = list()
    tf = True
    for i in range(braket_len):
        alist.append(braket[i])
    for i in alist:
        if i == '[' or i == '{' or i == '(':
            stack.append(i)
        else:
            if len(stack) == 0 :
                break
            now = stack.pop()
            if now == '[':
                if i == ']':
                    continue
            elif now == '{':
                if i == '}':
                    continue
            elif now == '(':
                if i == ')':
                    continue
            tf = False
    if len(stack) != 0 :
        tf = False
    if tf: print("YES")
    else: print("NO")

