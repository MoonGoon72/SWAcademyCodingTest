firstBreadName = input()
firstBreadPrice = int(input())
secondBreadName = input()
secondBreadPrice = int(input())

print(firstBreadName if firstBreadPrice > secondBreadPrice else secondBreadName)