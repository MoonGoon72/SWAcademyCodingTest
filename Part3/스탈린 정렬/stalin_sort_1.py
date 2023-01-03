import sys
input = sys.stdin.readline
testCase = int(input())
for _ in range(testCase):
    sequenceNum = int(input())
    sequence = list(map(int, input().split()))
    index = 0
    while True:
        if index == len(sequence) - 1: break
        if sequence[index] > sequence[index+1]:
            sequence.pop(index+1)
        else :
            index += 1
    for i in sequence:
        print(i, end=" ")
    print()
