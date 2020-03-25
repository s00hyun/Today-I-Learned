import sys

N = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
D = [1] * N
C = [ [0] * N for _ in range(N) ]
for i in range(N):
    C[i][i] = 1


def go():
    if N == 1:
        print(1)
        print(A[0])
        return
    for i in range(1, N):
        idx = -1
        for j in range(i):
            if A[i] > A[j]:
                if D[i] < D[j] + 1:
                    D[i] = D[j] + 1
                    idx = j
        if idx != -1:
            C[i] = C[idx][:]  # 리스트를 복사해서 대입해야 함!!!!!
            C[i][i] = 1
            #print("i:{}, idx:{}, C:{}".format(i, idx, C))

    #print(C)
    #print(D)
    length = max(D)
    ans_index = D.index(length)
    print(length)
    for i in range(len(C[ans_index])):
        if C[D.index(length)][i] == 1:
            print(A[i], end=' ')
    return


go()
