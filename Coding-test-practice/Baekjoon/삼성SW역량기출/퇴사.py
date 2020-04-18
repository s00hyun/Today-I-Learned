import sys

n = int(sys.stdin.readline().rstrip())
#tp = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]
#tp.insert(0, [-1, -1])
t = [0]*(n+1)
p = [0]*(n+1)
ans = 0
for i in range(1, n+1):
    t[i], p[i] = map(int, sys.stdin.readline().rstrip().split())


def count(i, _sum):
    global ans

    if i == n+1:
        #print("return with", _sum)
        ans = max(ans, _sum)
        return
    elif i > n :
        return

    #t = tp[i][0]
    #p = tp[i][1]
    count(i+t[i], _sum+p[i])  # i일에 상담을 진행할 경우
    count(i+1, _sum)    # i일에 상담을 하지 않을 경우


count(1, 0)  # 첫째 날
print(ans)
