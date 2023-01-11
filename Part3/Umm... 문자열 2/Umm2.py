import sys
input = sys.stdin.readline
testCase = int(input())

for _ in range(testCase):
    strLen, observe = map(int,input().split(' '))
    str = input()
    isUmm = 0
    possibles = []
    for _ in range(observe):
        a, b = map(int, input().split(' '))
        if possibles.count((a,b)):
            isUmm += 1
            continue
        #배열은 0부터 시작하니 맞춰주기 위함
        a -= 1
        b -= 1
        if strLen < 3: continue
        if b - a + 1 < 3: continue
        else:
            if str[a] == "U":
                if str.count("m", a, b+1) == b - a:
                    isUmm += 1
                    possibles.append((a+1,b+1))
    print(isUmm)
