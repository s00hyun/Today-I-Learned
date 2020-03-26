import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
D = A[:]


def go():
    if N == 1:
        return A[0]
    for i in range(1, N):
        if D[i-1] + A[i] > D[i]:
            D[i] += D[i-1]
        else:
            continue
    #print(D)
    return max(D)


print(go())
