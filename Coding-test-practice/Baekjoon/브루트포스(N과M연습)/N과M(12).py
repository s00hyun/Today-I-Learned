from itertools import combinations_with_replacement

n, m = map(int, input().split())
pool = list(map(int, input().split()))
pool.sort()

ans = list(combinations_with_replacement(pool, m))
ans2 = sorted(list(set(ans)))

for a in ans2:
    for num in a:
        print(num, end=' ')
    print()