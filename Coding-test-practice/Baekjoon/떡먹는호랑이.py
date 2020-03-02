import sys

d, k = map(int, input().split())

def fibo(n):
    if n == 1:
        return 1
    elif n == 2:
        return 1
    return fibo(n-2) + fibo(n-1)

def tteok(a, b, d):
    if d == 1:
        return a
    elif d == 2:
        return b
    elif d >= 3:
        return a*fibo(d-2) + b*fibo(d-1)

#for i in range(1, 10+1):
#    print("fibo({}) = {}".format(i, fibo(i)))

for a in range(1, k+1):
    for b in range(1, k+1):
        t = tteok(a, b, d)
        if t == k:
            print(a)
            print(b)
            sys.exit(0)
        elif t > k:
            break 
     