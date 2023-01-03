
testCase = int(input())

for _ in range(testCase):
    sequenceNum = int(input())
    sequence = list(map(int, input().split()))

    bigger = sequence[0]
    # 맨 처음 원소는 무조건 들어감
    stalin = [bigger]
    # 배열을 한번만 순회하므로 n의 시간이 걸린다
    for i in range(1, sequenceNum):
        # 뒤 인덱스가 더 크면 삭제가 안되니까 배열에 넣어줌
        if sequence[i] >= bigger:
            stalin.append(sequence[i])
            bigger = sequence[i]
    # bigger조차 없애는 방법
    # result = [sequence[0]]
    # for i in range(1, sequenceNum, 1):
    #     if stalin[-1] <= sequence[i]:  # 파이썬 배열에서 -1은 맨 뒤 인덱스
                                         # 결국 정답 배열에 맨 뒤(가장 큰) 인덱스와 비교하면 되기 때문!
    #         stalin.append(sequence[i])
    for i in stalin:
        print(i, end=" ")
    print()
