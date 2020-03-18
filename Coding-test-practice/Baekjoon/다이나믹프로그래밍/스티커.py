import sys

T = int(sys.stdin.readline().rstrip())

def sticker():
    n = int(sys.stdin.readline().rstrip())
    A = [ [0] + list(map(int, list(sys.stdin.readline().rstrip().split(' ')))) for _ in range(2) ]
    D = [ [0]*3 for _ in range(n+1) ]
    
    for i in range(1, n+1):
        D[i][0] = max(D[i-1][0], D[i-1][1], D[i-1][2])
        D[i][1] = max(D[i-1][0], D[i-1][2]) + A[0][i]
        D[i][2] = max(D[i-1][0], D[i-1][1]) + A[1][i]
        #print(D)
    
    return max(D[n])
 
for _ in range(T):
    print(sticker()) 
