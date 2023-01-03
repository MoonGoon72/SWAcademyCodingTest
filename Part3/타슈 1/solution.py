testCase = int(input())

for _ in range(testCase):
    rent_place = int(input())
    rent_bicycle = list(map(int, input().split()))
    rent_number = int(input())
    for _ in range(rent_number):
        a, b = map(int, input().split())
        a = a - 1
        b = b -1
        rent_bicycle[a] = rent_bicycle[a] - 1
        rent_bicycle[b] = rent_bicycle[b] + 1
    for i in rent_bicycle:
        print(i, end=" ")
    print()

