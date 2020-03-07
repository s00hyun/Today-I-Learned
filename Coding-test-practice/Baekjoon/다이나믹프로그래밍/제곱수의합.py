n = int(input())

c = [0]
c.extend([ i for i in range(1, n+1) ])

for i in range(4, n+1):
    for j in range(2, n+1):
        if i-j*j < 0:
            break
        if i-j*j == 0:
            c[i] = 1
            break
        else:
            c[i] = min(c[i], c[i-j*j]+1)

print(c[n])
