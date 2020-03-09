n = int(input())
a = [0] * (n+1)

def go(n):
    if n == 1:
        return 1
    elif n == 2:
        return 3
    a[1] = 1
    a[2] = 3
    for i in range(3, n+1):
        a[i] = a[i-2]*2 + a[i-1]
    return a[n]

print(go(n) % 10007)
