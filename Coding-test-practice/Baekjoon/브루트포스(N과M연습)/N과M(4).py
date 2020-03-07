# 중복을 허용한 조합 (itertools.combinations_with_replacement 이용)
#     조합 -> 오름차순 수열
#     중복을 허용한 조합 -> 비내림차순 수열

import itertools

n, m = map(int, input().split())
pool = [ i for i in range(1, n+1) ]
ans = list(itertools.combinations_with_replacement(pool, m))

#print(ans)
for i in range(len(ans)):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()