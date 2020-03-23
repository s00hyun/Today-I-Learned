import sys
from collections import deque

R, C = map(int, sys.stdin.readline().rstrip().split())
g = [ list(input()) for _ in range(R) ]
# 비버의 굴: 'D', 고슴도치의 위치: 'S'
water = [ [-1]*C for _ in range(R) ]
docci = [ [-1]*C for _ in range(R) ]
w_start = []
d_start = (-1, -1)
dx = [0, 0, -1, 1]
dy = [1, -1, 0, 0]

for i in range(R):
    for j in range(C):
        if g[i][j] == '*':
            w_start.append((i, j))
            water[i][j] = 0
        elif g[i][j] == 'S':
            d_start = (i, j)
            docci[i][j] = 0
            
def go():
    # 물('*')은 돌('X')을 통과할 수 없고, 비버의 소굴('D')로 이동할 수 없다.
    # 고슴도치('S')는 돌('X')을 통과할 수 없다.
    q = deque()
    for w in w_start:
        q.append(w)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C: 
                if g[nx][ny] == 'X' or g[nx][ny] == 'D':
                    continue
                if water[nx][ny] == -1:  # not visited
                    water[nx][ny] = water[x][y] + 1
                    q.append((nx, ny))
    #print(water)

    q.append(d_start)
    while q:
        x, y = q.popleft()
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<R and 0<=ny<C: 
                if g[nx][ny] == 'X':
                    continue
                if docci[nx][ny] == -1:
                    # (중요) "물이 이동할 칸이 비버의 집('D')이거나" 물이 나중에 차서 이동할 수 있을 경우
                    if water[nx][ny] == -1 or water[nx][ny] > docci[x][y] + 1:
                        if g[nx][ny] == 'D':
                            #print(docci)
                            return docci[x][y] + 1
                        q.append((nx, ny))
                        docci[nx][ny] = docci[x][y] + 1
    #print(docci)
    return "KAKTUS"

print(go())
