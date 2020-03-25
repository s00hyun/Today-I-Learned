import sys
from collections import deque
from itertools import combinations

N, M, G, R = map(int, sys.stdin.readline().rstrip().split())
garden = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(N) ]
fluid = []
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

# 0: 호수, 1: 배양액 뿌릴 수 없는 땅, 2: 배양액 뿌릴 수 있는 땅
for i in range(N):
    for j in range(M):
        if garden[i][j] == 2:
            fluid.append((i, j))


def go(gs, rs):
    g_check = [[-1] * M for _ in range(N)]
    r_check = [[-1] * M for _ in range(N)]
    flower = 0
    q = deque()
    for g in gs:
        g_check[g[0]][g[1]] = 0
        q.append(list(g)+['GREEN'])
    for r in rs:
        r_check[r[0]][r[1]] = 0
        q.append(list(r)+['RED'])
    #print(q)
    while q:
        #print(q)
        x, y, color = q.popleft()
        for i in range(0, 4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<N and 0<=ny<M:
                if garden[nx][ny] != 0:
                    if color == 'GREEN' and g_check[nx][ny] == -1 and g_check[x][y] != 'F':
                        g_check[nx][ny] = g_check[x][y] + 1
                        q.append([nx, ny, 'GREEN'])
                    elif color == 'RED' and r_check[nx][ny] == -1 and r_check[x][y] != 'F':
                        r_check[nx][ny] = r_check[x][y] + 1
                        if r_check[nx][ny] == g_check[nx][ny]:
                            flower += 1
                            r_check[nx][ny] = 'F'
                            g_check[nx][ny] = 'F'
                            #print("F on", [nx, ny])
                        else:
                            q.append([nx, ny, 'RED'])
    #print("g_check:",g_check)
    #print("r_check:",r_check)
    return flower


#print("fluid:",fluid)
green = list(combinations(fluid, G))
#print("green:",green)
red = []
for g in green:
    red.append(list(combinations(list(set(fluid) - set(g)), R)))
#print("red:",red)

ans = 0
for i in range(len(green)):
    for j in range(len(red[0])):
        result = go(green[i], red[i][j])
        if result > ans:
            ans = result
print(ans)
