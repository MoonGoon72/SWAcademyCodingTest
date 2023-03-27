n, m, k = map(int, input().split(' '))
targets = [0] + list(map(int, input().split(' ')))
isWin = False

tmp = targets[k]
targets[k] = 0

if k == m:
    print("YES")
    isWin = True

if not isWin:
    for i in range(n):
        if m == tmp:
            isWin = True
            break
        elif targets[tmp] == 0:
            isWin = False
            break
        else:
            tmp = targets[tmp]
            targets[i] = 0
    if isWin:
        print("YES") 
    else: print("NO")