import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split(' ')))
D = [1] * N


def go():
    if N == 1:
        return 1
    for i in range(N):
        for j in range(i):
            if A[i] < A[j]:
                if D[j] + 1 > D[i]:
                    D[i] = D[j] + 1
    #print(D)
    return max(D)


print(go())
