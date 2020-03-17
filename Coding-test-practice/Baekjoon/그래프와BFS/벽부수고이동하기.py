import sys
from collections import deque

n, m = map(int, sys.stdin.readline().split())
g = [ list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(n) ]
dist = [[[0]*2 for _ in range(m)] for _ in range(n)]

def bfs():
    q = deque()
    dist[0][0][0] = 1
    q.append((0,0,0))
    d = [(0,1), (1,0), (0, -1), (-1, 0)]
    while q:
        #print(q)
        v = q.popleft()
        x = v[0]
        y = v[1]
        z = v[2] 
        for i in range(4):
            nx = x + d[i][0]
            ny = y + d[i][1]
            if 0<=nx<n and 0<=ny<m: 
                # 다음 칸이 빈 칸이면: 체크하고 큐에 넣는다
                if g[nx][ny] == 0 and dist[nx][ny][z] == 0:
                    dist[nx][ny][z] = dist[x][y][z] + 1
                    q.append((nx, ny, z))
                # 다음 칸이 벽이고, 부순 적 없으면: 체크하고 부순다(큐에 넣는다)
                if g[nx][ny] == 1 and z == 0 and dist[nx][ny][1] == 0:
                    dist[nx][ny][1] = dist[x][y][z] + 1
                    q.append((nx, ny, 1))
                # 다음 칸이 벽이고, 부순 적 있으면: pass

bfs()
#print(dist)
if dist[n-1][m-1][0] != 0 and dist[n-1][m-1][1] != 0:
    print(min(dist[n-1][m-1]))
elif dist[n-1][m-1][0] != 0:
    print(dist[n-1][m-1][0])
elif dist[n-1][m-1][1] != 0:
    print(dist[n-1][m-1][1])
else:
    print(-1)
