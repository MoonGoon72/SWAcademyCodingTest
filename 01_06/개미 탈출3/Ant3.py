testCase = int(input())
for _ in range(testCase):

    n, m = map(int, input().split(' '))


    arr = input()
    portal = arr.index("O")
    junsic = arr.index("@")
    guntlet = arr.index("G")

    if portal < junsic:
        wall = arr.count("#", portal, junsic)
        if wall > m:
            if junsic < guntlet:
                wall = arr.count("#", junsic, guntlet)
                print("HAHA!") if wall <= m else print("HELP!")
            else:
                wall = arr.count("#", guntlet, junsic)
                print("HAHA!") if wall <= m else print("HELP!")
        else:
            print("HAHA!")
    else:
        wall = arr.count("#", junsic, portal)
        if wall > m:
            if junsic < guntlet:
                wall = arr.count("#", junsic, guntlet)
                print("HAHA!") if wall <= m else print("HELP!")
            else:
                wall = arr.count("#", guntlet, junsic)
                print("HAHA!") if wall <= m else print("HELP!")
        else:
            print("HAHA!")
