# product 이용하면 메모리 초과 난다

import sys


N, K = map(int, sys.stdin.readline().rstrip().split())
D = [ [0] * (N+1) for _ in range(K+1) ]
D[1] = [1] * (N+1)

# D[K][N]: 0~N까지의 정수 K개를 더해서 그 합이 N이 되는 경우의 수
# D[K][N] = sum of (D[K-1][N-L]) for 0<=L<=N
for k in range(2, K+1):
    for n in range(0, N+1):
        for l in range(n+1):
            D[k][n] += D[k-1][n-l]
            D[k][n] %= 1000000000
        #print("D[{}][{}] = {}".format(k, n, D[k][n]))

#print(D)
print(D[K][N])
