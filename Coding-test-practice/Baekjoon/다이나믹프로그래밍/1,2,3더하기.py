n = int(input())
cases = [ int(input()) for i in range(n) ]
ans = [0] * 12
ans[1] = 1
ans[2] = 2
ans[3] = 4

def a(n):
    if ans[n] != 0:
        return ans[n]
    elif ans[n] != 0 and ans[n-2] != 0 and ans[n-1] != 0:
        ans[n] = ans[n-3] + ans[n-2] + ans[n-1]
        #print("ans:", ans)
    #print("a({}) + a({}) + a({})".format(n-3, n-2, n-1))  
    return a(n-3) + a(n-2) + a(n-1)

for c in cases:
    print(a(c))

