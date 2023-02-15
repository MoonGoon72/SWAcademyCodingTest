import sys
input = sys.stdin.readline
n = int(input())
songs = list(map(int, input().split(' ')))
question = int(input())
times = list(map(int, input().split(' ')))

index = 0
accumulateTime = songs[index]
result = 0
totalSongTime = sum(songs)

for time in times:
    while True:
        if accumulateTime >= time:
            result = (result + index + 1) % 1000000007
            break
        else:
            index += 1
            index %= n
            accumulateTime += songs[index]
print(result)



# import sys
# input = sys.stdin.readline
# n = int(input())
# songs = list(map(int, input().split(' ')))
# question = int(input())
# times = list(map(int, input().split(' ')))

# index = 0
# accumulateTime = songs[index]
# result = 0
# totalSongTime = sum(songs)
# for time in times:
#     while True:
#         if accumulateTime >= time:
#             result = (result + index + 1) % 1000000007
#             break
#         else:
#             index += 1
#             index %= n
#             accumulateTime += songs[index]
# print(result)
