from collections import deque

n, m, v = map(int, input().split())
edge = [ [] for _ in range(n+1) ]
for i in range(m):
    v1, v2 = map(int, input().split())
    edge[v1].append(v2)
    edge[v2].append(v1)
for e in edge:
    e.sort()
#print("edge:", edge)

dfs_visited = [0] * (n+1)
bfs_visited = [0] * (n+1)

def dfs(v):
    dfs_visited[v] = 1
    print(v, end=' ')
    for e in edge[v]:
        if dfs_visited[e] == 0:
            dfs(e)

def bfs(v):
    q = deque()
    bfs_visited[v] = 1
    q.append(v)
    while q:
        #print("q:", q)
        v0 = q.popleft()
        print(v0, end=' ')
        for e in edge[v0]:
            if bfs_visited[e] != 1:
                bfs_visited[e] = 1
                q.append(e)

dfs(v)
print()
bfs(v)