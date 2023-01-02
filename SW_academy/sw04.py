import bisect
prison_num = int(input())
prison = list(map(int,input().split()))
light_num = int(input())
light = list(map(int,input().split()))

prison = sorted(prison)
light = sorted(light)

alist = []
for i in light:
    blist = []
    for j in prison:
        blist.append(abs(i - j))
    alist.append(blist)



def binary(prison):
    index = bisect.biscect_left(light, prison)
    minimum = min(abs(light[index-1] % prison))

import bisect
def binary(prison):
    index = bisect.bisect_left(lights, prison)

    return min(abs(lights[(index-1)%light_length] - prison), abs(lights[(index)%light_length] - prison), abs(lights[(index+1)%light_length] - prison))

prison_length = int(input())
prisons = list(map(int, input().split()))
light_length = int(input())
lights = list(map(int, input().split()))

m = 0
prisons = sorted(prisons)
lights = sorted(lights)
for i in prisons:
    m = max(m,binary(i))
    
print(m)