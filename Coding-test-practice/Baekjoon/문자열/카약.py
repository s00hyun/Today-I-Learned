import sys

r, c = map(int, sys.stdin.readline().split())
dic = {}
ans = [0]*10

for i in range(r):
    cnt = 0
    s = sys.stdin.readline().rstrip()
    for j in range(c):
        if s[j] == '.':
            cnt += 1
        elif s[j] != 'S' and s[j] != 'F':
            dic[s[j]] = cnt

sort_result = sorted(dic.items(), key=lambda x: x[1], reverse=True)
#print(sort_result)
j = 0
score = -1
for i in range(len(sort_result)):
    if sort_result[i][1] != score:
        j += 1
    ans[ int(sort_result[i][0]) ] = j
    score = sort_result[i][1]

for i in range(1, 10):
    print(ans[i])
    