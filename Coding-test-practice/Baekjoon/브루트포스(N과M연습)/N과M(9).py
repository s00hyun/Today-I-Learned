import itertools

n, m = map(int, input().split())
pool = list(map(int, list(input().split(' '))))
#print(pool)
ans = list(itertools.permutations(pool, m))
ans.sort()
#print(ans)
a0 = ()
for a in ans:
    if a != a0:
        for num in a:
            print(num, end=' ')
        print()
    a0 = a
