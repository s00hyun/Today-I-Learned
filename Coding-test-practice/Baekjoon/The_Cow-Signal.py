m, n, k = map(int, input().split())
p1 = [ list(input().split()) for _ in range(m) ]
p2 = []

#print(p1)
temp = []
for i in range(m):
    for j in range(n):
        temp += p1[i][0][j] * k
    for h in range(k):
        p2.append(temp)
    temp = []

for i in range(k*m):
    print("".join(p2[i]))
    