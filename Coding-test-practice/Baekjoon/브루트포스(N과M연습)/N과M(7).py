import itertools

n, m = map(int, input().split())
pool = list(map(int, list(input().split(' '))))
pool.sort()
ans = list(itertools.product(pool, repeat=m))

# 인덱스 이용하지 않고 직접 각 요소에 접근하면 시간초과에 걸리지 않았음
for a in ans:
    for num in a:
        print(num, end=' ')
    print()