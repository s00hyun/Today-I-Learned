import sys

m, c = map(int, sys.stdin.readline().rstrip().split())
message = []  # 길이: m
for _ in range(m):
    message.append(int(sys.stdin.readline().rstrip()))


def go():
    consumer = [ [] for _ in range(c) ]

    for i in range(m):
        t = message[i]
        if i < c:
            consumer[i].append(t)
        else:
            time_sum = [ sum(list) for list in consumer ]
            #print("time_sum:", time_sum)
            idx = time_sum.index(min(time_sum))
            consumer[idx].append(t)
    #print(consumer)
    return max([sum(list) for list in consumer])


print(go())
