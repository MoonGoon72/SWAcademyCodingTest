testCase = int(input())

for _ in range(testCase):
    strLen = int(input())
    str = input()
    a, b = map(int, input().split(' '))
    #배열은 0부터 시작하니 맞춰주기 위함
    a -= 1
    b -= 1
    if strLen < 3: print("NO")
    else:
        if str[a] != "U": print("NO")
        else:
            print("YES") if str.count("U", a+1, b+1) == 0 and str.count("m", a, b+1) >= 2 else print("NO")
# .count(x,_start,_end) 메소드는 _start 포함, _end 미포함이다ㅠ