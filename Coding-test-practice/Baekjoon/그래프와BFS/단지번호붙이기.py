n = int(input())
loc = []
ans_list = []

for i in range(n):
    l = list(map(int, list(input())))
    loc.append(l)
    l = []

#print("loc:\n", loc)

def bfs(i, j):
    cnt = 0
    queue = [(i,j)]
    loc[i][j] = -1
    while queue:
        #print(queue)
        v = queue.pop(0)
        cnt += 1
        dx = [1, -1, 0, 0]  # up, down, left, right
        dy = [0, 0, -1, 1]
        for k in range(4):  # For all directions
            v2 = (v[0]+dx[k], v[1]+dy[k])
            if (v2[0]>=0 and v2[0]<n) and (v2[1]>=0 and v2[1]<n):  # within valid ranges,
                if loc[v2[0]][v2[1]] == 1:  # if not visited, push into the queue and check as visited
                    queue.append(v2)
                    loc[v2[0]][v2[1]] = -1
    return cnt
    
for i in range(n):
    for j in range(n):
        if loc[i][j] == 1:
            ans_list.append(bfs(i, j))

ans_list.sort()
print(len(ans_list))
for i in range(len(ans_list)):
    print(ans_list[i])