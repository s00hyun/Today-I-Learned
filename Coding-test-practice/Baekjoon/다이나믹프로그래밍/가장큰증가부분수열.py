import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split(' ')))
D = A[:]
D[0] = A[0]


def go():
    if N == 1:
        return A[0]
    for i in range(1, N):
        for j in range(0, i):
            if A[j] < A[i]:
                if A[i] + D[j] > D[i]:
                    D[i] = A[i] + D[j]
    #print(D)
    return max(D)


print(go())
