from collections import deque

m, n = map(int, input().split())
g = [ list(map(int, list(input()))) for _ in range(n) ]
check = [ [-1]*m for _ in range(n) ]

def bfs():
    start = (0,0)
    q = deque()
    q.append(start)
    check[0][0] = 0
    while q:
        v = q.popleft()
        x = v[0]
        y = v[1]
        for d in [(1,0), (0,1), (-1,0), (0, -1)]:
            x1 = x+d[0]
            y1 = y+d[1]
            if (0<=x1<n and 0<=y1<m) and check[x1][y1] == -1:
                if g[x1][y1] == 0:
                    check[x1][y1] = check[x][y]
                    q.appendleft((x1,y1))
                elif g[x1][y1] == 1:
                    check[x1][y1] = check[x][y] + 1
                    q.append((x1,y1))

bfs()
print(check[n-1][m-1])  
