N = int(input())
P = [0] + list(map(int, input().split()))
D = [10001] * (N+1)
D[0] = 0
D[1] = P[1] 

#print("P:", P)
#print("D:", D)

for n in range(2, N+1):
    for i in range(1, n+1):
        if n-i < 0:
            break
        D[n] = min(D[n], D[n-i] + P[i])
        #print(D)

print(D[N])
