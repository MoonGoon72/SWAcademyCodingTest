import sys
from bisect import bisect_left
input = sys.stdin.readline
n = int(input())
lenOfSongs = list(map(int, input().split(' ')))
q = int(input())
questions = list(map(int, input().split(' ')))

# 이전 원소를 더한 값을 누적해서 만든 배열
times = []
tmp_song = 0
for i in lenOfSongs:
    tmp_song += i
    times.append(tmp_song)
result = 0

for quest in questions:
    tmp = 0
    if quest >= times[-1] and quest % times[-1] == 0:
        tmp = times[-1]
    elif quest > times[-1]:
        tmp = quest % times[-1]
    else: tmp = quest
    result = (result + bisect_left(times, tmp) +1) % 1000000007
print(result)