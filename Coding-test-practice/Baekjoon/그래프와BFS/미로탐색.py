from collections import deque

n, m = map(int, input().split())
g = []
g_check = [ [0] * m for _ in range(n) ]
g_check[0][0] = 1

for i in range(n):
    arr = list(map(int, list(input())))
    g.append(arr)
    arr = []

def bfs(v):
    queue = deque([v])
    visited = []
    #print("n:{}, m:{}".format(n, m))
    while queue:
        #print(queue)
        #print("g_check:\n", g_check)
        vertex = queue.popleft()
        #print("vertex:", vertex)
        visited.append(vertex)
        #print("visited:", visited)
        #if g[vertex[0]][vertex[1]] == 1:  
        #print("vertex:{}, cnt:{}".format(vertex, cnt))
        dx = [0, 0, 1, -1]
        dy = [1, -1, 0, 0]
        for i in range(4):
            next_v = (vertex[0]+dx[i], vertex[1]+dy[i])
            if (next_v[0]>=0 and next_v[0]<n) and (next_v[1]>=0 and next_v[1]<m) :
                if (next_v not in visited) and g[next_v[0]][next_v[1]]==1 :
                    queue.append(next_v)
                    cnt = g_check[vertex[0]][vertex[1]]
                    g_check[next_v[0]][next_v[1]] = cnt + 1
                    visited.append(next_v)
                    
        
bfs((0,0))
print(g_check[n-1][m-1])
