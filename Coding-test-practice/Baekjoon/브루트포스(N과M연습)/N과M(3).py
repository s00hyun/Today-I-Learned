# 중복을 허락한 순열 (itertools.product 이용)
# product(A, repeat=4) == product(A, A, A, A)

import itertools

n, m = map(int, input().split())

pool = [ i for i in range(1, n+1) ]
ans = list(itertools.product(pool, repeat=m))

#print(ans)
for i in range(len(ans)):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()