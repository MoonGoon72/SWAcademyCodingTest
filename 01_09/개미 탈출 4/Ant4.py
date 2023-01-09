testCase = int(input())

for _ in range(testCase):
    n, m = map(int,input().split(' '))
    arr = input()
    atkJ, hpJ = map(int, input().split(' '))
    atkM, hpM = map(int, input().split(' '))
    
    isEscapable = False
    umLocation = arr.index("@")
    monster = arr.index("&")
    escapeNum = arr.count("O")
    escapes = []
    for i in range(len(arr)):
        if arr[i] == 'O':
            escapes.append(i)
    
    for escape in escapes:
        tmpHpJ = hpJ
        tmpHpM = hpM
        # 준식이와 탈출구 사이의 벽과 몬스터를 찾기 위함
        if umLocation < escape:
            wall = arr.count("#", umLocation, escape)
            if wall > m: continue
            else:
                if umLocation < monster and monster < escape:
                    while (tmpHpJ > 0 or tmpHpM > 0):
                        tmpHpM -= atkJ
                        if tmpHpM <= 0:
                            isEscapable = True
                            break
                        tmpHpJ -= atkM
                        if tmpHpJ <= 0:
                            break
                # 준식이와 탈출구 사이에 몬스터가 없음
                else: isEscapable = True
        elif escape < umLocation:
            wall = arr.count("#", escape, umLocation)
            if wall > m: continue
            else:
                if escape < monster and monster < umLocation:
                    while (tmpHpJ > 0 or tmpHpM > 0):
                        tmpHpM -= atkJ
                        if tmpHpM <= 0:
                            isEscapable = True
                            break
                        tmpHpJ -= atkM
                        if tmpHpJ <= 0:
                            break
                # 준식이와 탈출구 사이에 몬스터가 없음
                else: isEscapable = True
    print("HAHA!") if isEscapable else print("HELP!")
