import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
board = [ list(sys.stdin.readline().rstrip()) for _ in range(n) ]
visited = [ [[[0]*m for _ in range(n)] for _ in range(m)] for _ in range(n) ]
blue = (0, 0)
red = (0, 0)
hole = (0, 0)
dx = [1, -1, 0, 0]
dy = [0, 0, -1, 1]

for i in range(n):
    for j in range(m):
        if board[i][j] == 'B':
            blue = (i, j)
        elif board[i][j] == 'R':
            red = (i, j)
        elif board[i][j] == '0':
            hole = (i, j)


# 상/하/좌/우 방향 각각에 대해 벽을 만날 때까지 각 구슬을 굴리고 벽을 만나기 직전의 좌표를 큐에 넣는다
# 이동 중 빨간구슬이 구멍에 들어가면 정답을 출력
# 단, 빨간 구슬과 파란 구슬이 동시에 구멍에 들어갈 수 있으며, 이 경우 -1을 출력한다

### 주의: 구멍을 제외한 모든 좌표에 대해, 한 좌표에 두 구슬이 동시에 위치할 수는 없다.
# => 구슬을 굴릴 때 두 구슬의 이동 거리를 각각 기록한다!
#    만약 구슬이 같은 위치로 이동했다면, 이동 거리가 더 긴 구슬의 위치를 한 칸 이전으로 되돌린다.
# => (rx, ry, bx, by, count) 이용!

visited[red[0]][red[1]][blue[0]][blue[1]] = 1
q = deque([ (red[0], red[1], blue[0], blue[1], 0) ])


def rolling(_x, _y, _dx, _dy, cnt):
    while True:
        _x += _dx
        _y += _dy
        cnt += 1
        if board[_x][_y] == '#':
            return _x - _dx, _y - _dy, cnt
        elif board[_x][_y] == 'O':
            return _x, _y, cnt


def bfs():
    while q:
        rx, ry, bx, by, count = q.popleft()
        if count >= 10:
            break
        for i in range(4):
            ## 각 공을 굴려 '#'이나 'O'에 도달했을 때의 좌표와 이동거리
            nrx, nry, rc = rolling(rx, ry, dx[i], dy[i], 0)
            nbx, nby, bc = rolling(bx, by, dx[i], dy[i], 0)

            if board[nbx][nby] == 'O':
                continue

            if board[nrx][nry] == 'O':
                if (nrx, nry) == (nbx, nby):
                    return -1
                if count <= 10:
                    return count + 1

            #print(nrx, nry, nbx, nby)
            if (nrx, nry) == (nbx, nby):
                if board[nrx][nry] == 'O':
                    return -1
                if rc > bc:  # 빨간 공이 파란 공 뒤에서 움직인 경우
                    nrx -= dx[i]
                    nry -= dy[i]
                else:
                    nbx -= dx[i]
                    nby -= dy[i]

            if not visited[nrx][nry][nbx][nby]:
                visited[nrx][nry][nbx][nby] = 1
                q.append((nrx, nry, nbx, nby, count+1))
                #print(q)
    return -1


print(bfs())
