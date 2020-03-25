import sys

n = int(sys.stdin.readline().rstrip())
wine = [ int(sys.stdin.readline().rstrip()) for _ in range(n) ]
D = [ [0]*3 for _ in range(n) ]


def go():
    D[0] = [ 0, wine[0], wine[0] ]
    if n == 1:
        return wine[0]
    else:
        D[1] = [ wine[0], wine[1], wine[0]+wine[1] ]

    for i in range(2, n):
        D[i][0] = max(D[i-1])
        D[i][1] = max(D[i-2]) + wine[i]
        D[i][2] = D[i-1][1] + wine[i]

    #print(D)
    return max(D[n-1])


print(go())
