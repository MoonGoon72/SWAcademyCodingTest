testCase = int(input())

for _ in range(testCase):
    row, col = map(int, input().split(' '))
    graph = [list(map(str, input().rstrip())) for _ in range(row)]
    move = int(input())
    moving = input()

    umX = 0  # Col
    umY = 0  # Row
    for i in range(row):
        if graph[i].count("@") == 1:
            umY = i
            umX = graph[i].index("@")
            break
    
    for index in moving:
        if index == "U":
            if umY > 0 and graph[umY -1][umX] != "#":
                umY -= 1
        elif index == "D":
            if umY < row - 1 and graph[umY + 1][umX] != "#":
                umY += 1
        elif index == "L":
            if umX > 0 and graph[umY][umX - 1] != "#":
                umX -= 1
        elif index == "R":
            if umX < col - 1 and graph[umY][umX + 1] != "#":
                umX += 1
    print(umY + 1, umX + 1)
