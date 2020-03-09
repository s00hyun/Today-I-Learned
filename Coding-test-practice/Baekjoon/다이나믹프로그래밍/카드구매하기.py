N = int(input())
P = [0] + list(map(int, input().split()))
D = [0] * (N+1)
D[1] = P[1]

for n in range(2, N+1):
    for i in range(1, n+1):
        if n-i < 0:
            break
        #print("n=", n, "i=", i)
        D[n] = max(D[n], D[n-i] + P[i])
        #print("D[n]: {}, temp: {}".format(D[n], D[n-i] + P[i]))
        #print(D)

print(D[N])