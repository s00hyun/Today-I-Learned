T = int(input())
cases = [ int(input()) for i in range(T) ]
D = [ [0, 0, 0, 0] for i in range(100001) ]
D[1][1] = 1
D[2][2] = 1
D[3] = [0, 1, 1, 1]

def go(n):
    if n <= 3:
        return sum(D[n])
    for i in range(4, n+1):
        D[i][1] = (D[i-1][2] + D[i-1][3]) % 1000000009
        D[i][2] = (D[i-2][1] + D[i-2][3]) % 1000000009 
        D[i][3] = (D[i-3][1] + D[i-3][2]) % 1000000009
    return sum(D[n]) % 1000000009
        

for c in cases:
    print(go(c))