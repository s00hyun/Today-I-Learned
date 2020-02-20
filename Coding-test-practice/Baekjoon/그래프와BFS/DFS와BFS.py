#-*- coding: utf-8 -*-

# n: 정점의 수, m: 간선의 수, v: 탐색을 시작할 정점 번호
n, m, v = map(int, input().split())
g = {}
for i in range(n):
    g[i+1] = [] 

for i in range(m):
    n1, n2 = map(int, input().split())
    g[n1].append(n2)
    g[n2].append(n1)

#print("graph:\n", g)


def dfs(g, v):
    visited = []
    stack = [v]

    # 작은 번호가 stack에서 먼저 pop 되도록 정렬
    for i in range(n):
        g[i+1].sort(reverse=True)

    while stack:  # stack이 빌 때까지 돈다
        vertex = stack.pop()
        if vertex not in visited:
            visited.append(vertex)
            stack.extend(g[vertex]) 

    return visited


def bfs(g, v):
    visited = []
    queue = [v]

    # 작은 번호가 queue에서 먼저 pop 되도록 정렬
    for i in range(n):
        g[i+1].sort(reverse=False)

    while queue:
        vertex = queue.pop(0)
        if vertex not in visited:
            visited.append(vertex)
            queue.extend(g[vertex])
            
    return visited


dfs_visited = dfs(g, v)
bfs_visited = bfs(g, v)

for v in dfs_visited:
    print(v, end=' ')

print()

for v in bfs_visited:
    print(v, end=' ')