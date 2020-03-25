import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
D = [1] * N


def go():
    ans = 1
    if N == 1:
        return 1
    for i in range(1, N):
        for j in range(i):
            if A[i] > A[j]:
                D[i] = max(D[i], D[j] + 1)
                ans = max(ans, D[i])
    #print(D)
    return ans


print(go())
