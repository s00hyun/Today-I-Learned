from collections import deque
import copy

# n x m
m, n = map(int, input().split())
g = []
g_check = [ [-1]*m for _ in range(n) ]
temp = []
roots = []

q = deque()
ans = 0
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]

for i in range(n):
    temp = list(map(int, list(input().split()))) 
    g.append(temp)
    for j,x in enumerate(temp):
        if x==1:
            q.append((i, j))
            g_check[i][j] = 0

# Search (bfs)
while q:
    #print("queue: {}".format(q))
    vertex = q.popleft()
    ans = g_check[vertex[0]][vertex[1]]
    #print("now: {} with day={}".format(vertex, ans))
    for i in range(4):
        next_v = (vertex[0]+dx[i], vertex[1]+dy[i])
        if (next_v[0]>=0 and next_v[0]<n) and (next_v[1]>=0 and next_v[1]<m):
            if g[next_v[0]][next_v[1]] != -1 and g_check[next_v[0]][next_v[1]] == -1:  # not visited point
                q.append(next_v)
                g_check[next_v[0]][next_v[1]] = g_check[vertex[0]][vertex[1]] + 1

# If there is any unreached point, print -1
for i in range(n):
    for j in range(m):
        if g[i][j] == 0 and g_check[i][j] == -1:
            ans = -1

print(ans)
