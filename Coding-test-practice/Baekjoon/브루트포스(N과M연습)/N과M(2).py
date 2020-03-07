# 조합

import itertools

n, m = map(int, input().split())
pool = [ i for i in range(1, n+1) ]

ans = list(itertools.combinations(pool, m))

#print(ans)
for i in range(len(ans)):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()

"""
ans = list(itertools.permutations(pool, m))
#print(ans)
for j in range(len(ans)):
    #print("ans[{}]: {}".format(j, ans[j]))#, end=' ')
    for i in range(m-1):
        #print("ans[j][i]={} > ans[j][i+1]={}?".format(ans[j][i], ans[j][i+1]))
        if ans[j][i] > ans[j][i+1]:
            ans[j] = (0,0)
            #print("replace. ans:", ans)
            break
#print(ans)
for a in ans:
    if a != (0,0):
        for i in range(m):
            print(a[i], end= ' ')
        print()
"""