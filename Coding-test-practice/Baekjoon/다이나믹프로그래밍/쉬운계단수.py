N = int(input())
D = [ [0]*10 for i in range(101) ]
D[1] = [0] + [1]*9
#print(D[:3])

def ans(n):
    if n == 1:
        return sum(D[1])
    for i in range(2, n+1):
        for j in range(10):
            if j == 0:
                D[i][j] = D[i-1][j+1] % 1000000000
            elif j == 9:
                D[i][j] = D[i-1][j-1] % 1000000000
            else:
                D[i][j] = D[i-1][j-1] + D[i-1][j+1] % 1000000000
            #print(D[:3])
    return sum(D[n])

print(ans(N) % 1000000000)