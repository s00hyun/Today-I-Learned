import itertools

n, m = map(int, input().split())
pool = list(map(int, list(input().split(' '))))
pool.sort()
ans = list(itertools.permutations(pool, m))

for i in range(len(ans)):
    for j in range(m):
        print(ans[i][j], end=' ')
    print()