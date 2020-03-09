N = int(input())
D = [ [0]*10 for i in range(1001) ]
D[1] = [1]*10

def ans(n):
    if n == 1:
        return sum(D[1])
    for i in range(2, n+1):
        for j in range(10):
            D[i][j] = sum(D[i-1][:j+1]) % 10007
    return sum(D[N]) % 10007

print(ans(N) % 10007)