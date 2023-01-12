n = int(input())
songs = list(input() for _ in range(n))
times = list(int(input()) for _ in range(n))
question = int(input())

index = 0
accumulateTime = times[index]

for _ in range(question):
    time = int(input())

    while True:
        if accumulateTime >= time:
            print(songs[index])
            break
        else:
            index += 1
            accumulateTime += times[index]
