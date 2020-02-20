#-*- coding: utf-8 -*-

# n: 정점의 개수, m: 간선의 개수
n, m = map(int, input().split())

g = [ [] for _ in range(n+1) ]
connected = 0
visited = []

def bfs(v):
    queue = [v]
    while queue:
        #print("queue:",queue)
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(set(g[vertex]) - set(queue) - set(visited))

for i in range(m):
    v1, v2 = map(int, input().split())
    g[v1].append(v2)
    g[v2].append(v1)

for i in range(1, n+1):
    if i not in visited:
        bfs(i)
        connected += 1
        #print("visited:", visited)

print(connected)
