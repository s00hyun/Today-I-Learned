# n: # of nodes, m: # of edges, v: root
n, m, v = map(int, input().split())

g = [ [] for _ in range(n+1) ]
visited = []

for i in range(m):
    n1, n2 = map(int, input().split())
    g[n1].append(n2)
    g[n2].append(n1)

for i in g:
    i.sort()

#print("graph:\n", g)

def dfs(g, x):
    visited.append(x)
    print(x, end=' ')
    for i in range(len(g[x])):
        x2 = g[x][i]
        if x2 not in visited:
            dfs(g, x2)

def bfs(g, x):
    queue = [x]
    visited.append(x)
    while queue:
        #print(queue)
        vertex = queue.pop(0)
        print(vertex, end=' ')
        for ver in g[vertex]:
            if ver not in visited:
                queue.append(ver)
                visited.append(ver)
    

dfs(g, v)
visited = []
print('')
bfs(g, v)
            