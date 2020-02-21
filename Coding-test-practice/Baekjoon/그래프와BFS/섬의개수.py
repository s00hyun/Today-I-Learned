# g: h x w
w, h = map(int, input().split())
g = []
ans = []

def bfs(i, j, g):
    queue = [(i,j)]
    visited = []
    
    while queue:
        #print(queue)
        v = queue.pop(0)

        if g[v[0]][v[1]] == 1:
            g[v[0]][v[1]] = -1  # visited
            visited.append( (v[0], v[1]) )
            dx = [-1, 1, 0, 0, -1, -1, 1, 1]
            dy = [0, 0, -1, 1, -1, 1, -1, 1]
            for k in range(8):
                next_loc = (v[0]+dx[k], v[1]+dy[k])
                if next_loc not in visited and (next_loc[0]>=0 and next_loc[0]<h) and (next_loc[1]>=0 and next_loc[1]<w):
                    queue.append( (next_loc[0], next_loc[1]) )

    return 1


while w!=0 and h!=0:
    #print("w:{}, h:{}".format(w, h))
    for i in range(h):
        g.append( list(map(int, input().split())) ) 
    
    #print("map:\n", g)

    cnt = 0
    # Find # of islands and print it
    for i in range(h):
        for j in range(w):
            if g[i][j] == 1:
                cnt += bfs(i, j, g)
    ans.append(cnt)
    w, h = map(int, input().split())
    g = []
    
#print(ans)
for a in ans:
    print(a)
                