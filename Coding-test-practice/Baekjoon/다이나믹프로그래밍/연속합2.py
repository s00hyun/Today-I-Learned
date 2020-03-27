import sys

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
A_reverse = A[::-1]
D_l = A[:]
D_r = A[::-1]


def go(D_l, D_r):
    if n == 1:
        return A[0]
    for i in range(1, n):
        dl_candidate = D_l[i-1] + A[i]
        dr_candidate = D_r[i-1] + A_reverse[i]
        if dl_candidate > A[i]:
            D_l[i] = dl_candidate
        if dr_candidate > A_reverse[i]:
            D_r[i] = dr_candidate
    D_r = D_r[::-1]

    ans = -1001
    for i in range(0, n):
        if i == 0:
            temp = D_r[i+1]
        elif i == n-1:
            temp = D_l[i-1]
        else:
            temp = D_l[i-1] + D_r[i+1]
        if temp > ans:
            ans = temp
    #print(D_l)
    #print(D_r)
    return max(ans, max(D_l))


print(go(D_l, D_r))
