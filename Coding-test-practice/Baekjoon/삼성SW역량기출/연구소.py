import sys, copy
from itertools import combinations
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
g = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]
answer = 0
free = []
virus = []
q = deque()
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]

for i in range(n):
    for j in range(m):
        _g = g[i][j]
        if _g == 0:
            free.append((i, j))
        elif _g == 2:
            virus.append((i, j))


def check_free(_g):
    result = 0
    for row in _g:
        result += row.count(0)
    return result


def go(_v1, _v2, _v3):
    global answer
    check = copy.deepcopy(g)
    q.extend(virus)

    # 벽 세우기
    for v in [_v1, _v2, _v3]:
        check[v[0]][v[1]] = -1

    while q:
        v = q.popleft()
        #print("v:",v)
        x = v[0]
        y = v[1]
        #print(x, y)
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m:
                if g[nx][ny] == 0 and not check[nx][ny]:
                    check[nx][ny] = 1
                    q.append((nx, ny))

    temp = check_free(check)
    answer = max(answer, temp)


for v1, v2, v3 in combinations(free, 3):
    #print(v1, v2, v3)
    go(v1, v2, v3)

print(answer)
