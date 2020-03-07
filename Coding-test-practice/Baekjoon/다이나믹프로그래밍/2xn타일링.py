# a[n] = a[n-1] + a[n-2]

n = int(input())
a = [0] * (n+1)

def go(n):
    if n == 1 or n == 2:
        return n

    a[1] = 1
    a[2] = 2
    i = 3
    while i <= n:
        a[i] = a[i-2] + a[i-1]
        i += 1
    return a[n] % 10007

print(go(n))