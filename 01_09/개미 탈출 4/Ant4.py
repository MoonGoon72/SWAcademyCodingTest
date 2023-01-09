testCase = int(input())

for _ in range(testCase):
    n, m = map(int,input().split(' '))

    arr = input()
    atkJ, hpJ = map(int, input().split(' '))
    atkM, hpM = map(int, input().split(' '))
    
    umLocation = arr.index("@")
    escape = arr.index("O")
    monster = arr.index("&")

    if (umLocation > escape):
        wall = arr.count("#", escape, umLocation)
        if wall > m: print("HELP!")
        else:
            if escape < monster and monster < umLocation:
                while (hpJ > 0 or hpM > 0):
                    hpM -= atkJ
                    if hpM <= 0:
                        print("HAHA!")
                        break
                    hpJ -= atkM
                    if hpJ <=0:
                        print("HELP!")
                        break
            else: print("HAHA!")
    else:
        wall = arr.count("#", umLocation, escape)
        if wall > m: print("HELP!")
        if umLocation < monster and monster < escape:
            while (hpJ > 0 or hpM > 0):
                hpM -= atkJ
                if hpM <= 0:
                    print("HAHA!")
                    break
                hpJ -= atkM
                if hpJ <=0:
                    print("HELP!")
                    break
        else: print("HAHA!")