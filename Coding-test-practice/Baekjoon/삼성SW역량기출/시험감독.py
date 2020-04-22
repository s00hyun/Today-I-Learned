import sys, math

n = int(sys.stdin.readline().rstrip())
people = list(map(int, sys.stdin.readline().rstrip().split()))
b, c = map(int, sys.stdin.readline().rstrip().split())
answer = 0

for i in range(n):
    people[i] = max(people[i]-b, 0)
    answer += 1
#print(people)
for p in people:
    if p == 0:
        continue
    if p >= c:
        answer += math.ceil(p / c)
    else:
        answer += 1

print(answer)
