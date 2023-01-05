testCase = int(input())

for _ in range(testCase):
    n, m = map(int, input().split(" "))
    arr = input()
    umLocation = arr.index("@")
    escape = arr.index("O")
    if (umLocation > escape):
        wall = arr.count("#", escape, umLocation)
        print("HAHA!") if wall <= m else print("HELP!")
    else:
        wall = arr.count("#", umLocation, escape)
        print("HAHA!") if wall <= m else print("HELP!")
