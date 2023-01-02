x, y = map(int, input().split())

def euclid(x, y):
    if x % y == 0:
        return y
    return euclid(y, x % y)
    
print(euclid(x,y))
