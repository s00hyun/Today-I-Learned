import sys
sys.setrecursionlimit(1000000)

t = int(input())
cases = [ int(input()) for i in range(t) ]
ans = [0] * 1000001
ans[1] = 1
ans[2] = 2
ans[3] = 4

def a(n):
    if n <= 3:
        return ans[n]
    for i in range(4, 1000001):
        ans[i] = (ans[i-3] + ans[i-2] + ans[i-1]) % 1000000009
        if i==n:
            return ans[i]

for c in cases:
    print(a(c))

