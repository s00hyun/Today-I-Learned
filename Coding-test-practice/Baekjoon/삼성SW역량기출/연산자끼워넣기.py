import sys
from itertools import permutations

n = int(sys.stdin.readline().rstrip())
A = list(map(int, sys.stdin.readline().rstrip().split()))
oper = list(map(int, sys.stdin.readline().rstrip().split()))  # +, -, *, / 각 갯수
opers = []
results = []

for i in range(4):  # +, -, *, / => 0, 1, 2, 3
    o = oper[i]
    for _ in range(o):
        opers.append(i)

permu = list(set(list(permutations(opers, n-1))))

for p in permu:
    temp = A[0]
    for i in range(1, n):
        if p[i-1] == 0:  # +
            temp += A[i]
        elif p[i-1] == 1:  # -
            temp -= A[i]
        elif p[i-1] == 2:  # *
            temp *= A[i]
        else:  # /
            if temp < 0:
                temp //= -A[i]
                temp *= -1
            else:
                temp //= A[i]
    results.append(temp)

#print(results)
print(max(results))
print(min(results))
