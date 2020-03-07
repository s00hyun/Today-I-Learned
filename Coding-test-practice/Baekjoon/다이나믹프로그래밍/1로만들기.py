import sys

n = int(input())
a = [0] * (n+1)  # memoization
#a[1] = 0

if n == 1:
    print(0)
    sys.exit(0)

i = 2
while i <= n:
    temp = [ a[i-1]+1 ]
    if i % 3 == 0:
        temp.append(a[i//3] + 1)
    if i % 2 == 0:
        temp.append(a[i//2] + 1)
    a[i] = min(temp)
    i += 1

print(a[n])