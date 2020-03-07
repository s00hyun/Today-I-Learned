import itertools

n, m = map(int, input().split())
pool = list(map(int, list(input().split(' '))))
pool.sort()
ans = list(itertools.combinations_with_replacement(pool, m))

for a in ans:
    for num in a:
        print(num, end=' ')
    print()