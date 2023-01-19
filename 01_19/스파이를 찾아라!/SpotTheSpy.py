testCase = int(input())

for _ in range(testCase):
    sequenceLen = int(input())
    sequence = list(map(int, input().split(' ')))
    sequenceSet = list(set(sequence))
    
    print(sequence.index(sequenceSet[0]) + 1) if sequence.count(sequenceSet[0]) < sequence.count(sequenceSet[1]) else print(sequence.index(sequenceSet[1]) + 1)
