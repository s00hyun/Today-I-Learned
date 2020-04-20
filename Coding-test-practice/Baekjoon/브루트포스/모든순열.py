# permutations를 사용하려면, permutations를 저장해두면 안 되고, 각각 하나씩 호출하면서 프린트해주어야 런타임 에러가 나지 않는다.

from itertools import permutations

n = int(input())
source = [ i for i in range(1, n+1) ]

for next_permu in permutations(source):
    temp = map(str, list(next_permu))
    print(' '.join(temp))


# 다음순열을 계속 찾기
'''
n = int(input())
permu = [ i for i in range(1, n+1) ]
target = list(reversed(permu))

for per in permu:
    print(per, end=' ')
while permu != target:
    print()
    if len(permu) == 1:
        print(permu[0])
        break

    i = n-1
    while permu[i-1] >= permu[i]:
        i -= 1
        if i == 0:
            break

    j = n-1
    while permu[i-1] >= permu[j]:
        j -= 1

    temp = permu[i-1]
    permu[i-1] = permu[j]
    permu[j] = temp

    p = permu[i:]
    p.reverse()
    permu[i:] = p
    for per in permu:
        print(per, end=' ')
'''