import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

def go(w, h):
    g = []
    start = (-1, -1, -1)  # ( x, y, f(=0 if person, =1 if fire) ) 
    start_list = []  # fire
    for i in range(h): 
        l = list(sys.stdin.readline().rstrip())
        #print("l:", l)
        g.append(l)
        for j in range(w):
            if l[j] == '@':
                start = (i, j, 0)
            elif l[j] == '*':
                start_list.append((i, j, 1))
    #print(start)
    #print(start_list)

    check = [ [-1]*w for _ in range(h) ]
    q = deque()
    for s in start_list:  # 불부터 지핀다
        q.append(s) 
        check[s[0]][s[1]] = 0
    q.append(start)  # 불이 퍼지지 않은 곳에 사람이 이동 가능
    check[start[0]][start[1]] = 0
    #print(q)
    #print(check)
    while q:
        v = q.popleft()
        x = v[0]
        y = v[1]
        f = v[2]
        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            # (헷갈린 부분) 현재 위치: 지도 가장자리, 다음 위치: 지도 밖
            if nx<0 or nx>=h or ny<0 or ny>=w:  
                if f == 1:
                    continue
                return check[x][y] + 1 
            if g[nx][ny] == '#':
                continue
            if check[nx][ny] == -1:  # not visited
                check[nx][ny] = check[x][y] + 1
                q.append((nx, ny, f))

    #print("check:",check)
    return('IMPOSSIBLE')
    

for i in range(n):
    w, h = map(int, sys.stdin.readline().rstrip().split())
    print(go(w, h))
