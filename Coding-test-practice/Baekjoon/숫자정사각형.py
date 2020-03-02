import sys

n, m = map(int, input().split())
rec = [ list(map(int, list(input()))) for _ in range(n) ]
#print("rec:", rec)

ans = 1

for i1 in range(n):
    for j1 in range(m):
        for j2 in range(j1+1, m):
            num = rec[i1][j1]
            if rec[i1][j2] == num :
                i2 = i1 + (j2 - j1)
                if i2 < n:
                    if (rec[i2][j1] == num) and (rec[i2][j2] == num):
                        if ans < pow(i2-i1+1, 2) :
                            ans = pow(i2-i1+1, 2)
                        #print("i1={}, i2={}, j1={}, j2={}, ans={}".format(i1, i2, j1, j2, ans))
print(ans)
