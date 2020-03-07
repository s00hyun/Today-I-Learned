import itertools

n, m = map(int, input().split())
pool = list(map(int, input().split()))
pool.sort()
ans = list(itertools.product(pool, repeat=m))
ans2 = sorted(list(set(ans)))
#print(ans2)

for a in ans2:
    for num in a:
        print(num, end=' ')
    print()