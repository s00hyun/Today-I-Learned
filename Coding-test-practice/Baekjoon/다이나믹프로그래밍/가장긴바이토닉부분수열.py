import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A_reverse = A[::-1]
D1 = [1] * N
D2 = [1] * N


def go(D1, D2):
    if N == 1:
        return 1
    for i in range(N):
        for j in range(i):
            if A[i] > A[j] and D1[j] + 1 > D1[i]:
                D1[i] = D1[j] + 1
            if A_reverse[i] > A_reverse[j] and D2[j] + 1 > D2[i]:
                D2[i] = D2[j] + 1
    D2 = D2[::-1]
    ans = 0
    for i in range(N):
        temp = D1[i] + D2[i] - 1
        if temp > ans:
            ans = temp
    #print(D1)
    #print(D2)
    return ans


print(go(D1, D2))
