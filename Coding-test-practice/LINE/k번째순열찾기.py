import sys
from itertools import permutations

num = list(map(int, sys.stdin.readline().rstrip().split()))
num = sorted(num)
n = int(sys.stdin.readline().rstrip())

result = list(permutations(num, len(num)))
#print(result)

for i in result[n-1]:
    print(i, end='')
