'''
시간초과
'''

import sys

n, q = map(int, sys.stdin.readline().split())
A = list(map(int, list(sys.stdin.readline().split(' '))))
Q = list(map(int, list(sys.stdin.readline().split(' '))))
sum_arr = []
ans = 0


for j in range(n):
    idx_list = [j, j+1, j+2, j+3]
    if n in idx_list:
        idx = idx_list.index(n)
        idx_list[idx] = 0
    if n+1 in idx_list:
        idx = idx_list.index(n+1)
        idx_list[idx] = 1
    if n+2 in idx_list:
        idx = idx_list.index(n+2)
        idx_list[idx] = 2
    #print(idx_list)
    sum_arr.append( A[idx_list[0]]*A[idx_list[1]]*A[idx_list[2]]*A[idx_list[3]] )

# Point: 각 Ai는 4번씩만 계산식에 포함된다.
for q_ in Q:
    i = q_-1
    i_list = [i, i-1, i-2, i-3]

    for j in i_list:
        if j<0:
            j += n
        sum_arr[j] *= -1
        
    print(sum(sum_arr))
