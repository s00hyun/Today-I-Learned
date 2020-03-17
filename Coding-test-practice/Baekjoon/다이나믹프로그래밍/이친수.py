import sys

N = int(sys.stdin.readline().rstrip())
D = [ [0,0] for _ in range(N+1) ]

# D[i][j]: j로 끝나는 i자리 이친수
D[1][1] = 1
D[1][0] = 0
i = 2
while i<=N:
    D[i][0] = D[i-1][0] + D[i-1][1]
    D[i][1] = D[i-1][0]
    i += 1

print(sum(D[N]))
