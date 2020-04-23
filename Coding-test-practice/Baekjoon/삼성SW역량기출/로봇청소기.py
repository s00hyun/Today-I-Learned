import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
r, c, d = map(int, sys.stdin.readline().rstrip().split())
g = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]

dx = [-1, 0, 1, 0]  # 북, 동, 남, 서
dy = [0, 1, 0, -1]  # 회전: -1

lx = [0, -1, 0, 1]  # 북/동/남/서 기준 각각 왼쪽에 해당하는 방향
ly = [-1, 0, 1, 0]

answer = 0
finish = 0


def turn_left(_d):
    _d -= 1
    if _d < 0:
        _d += 4
    else:
        _d %= 4
    return _d


def check_cleaned_or_wall_around(x, y):
    for i in range(4):
        if 0<=x+dx[i]<n and 0<=y+dy[i]<m:
            if not g[x+dx[i]][y+dy[i]]:
                return 0
    return 1  # 청소되었거나(2) 벽인 (1) 방향이 존재


def go(x, y, _d):
    global answer, finish
    # 1번
    if not g[x][y]:
        g[x][y] = 2
        answer += 1
        #for row in g:
        #    print(row)
        #print(x,y,"cleaned. until now answer:", answer)
        #print("direction:", _d)
        #print()

    # 2번
    while True:
        if check_cleaned_or_wall_around(x, y):
            if g[x + dx[_d]*(-1)][y + dy[_d]*(-1)] == 1:  # 뒤쪽 방향이 벽
                finish = 1
                return
            # 한 칸 후진
            x += dx[_d]*(-1)
            y += dy[_d]*(-1)
            continue

        left = g[x+lx[_d]][y+ly[_d]]
        #print("left:", x+lx[_d], y+ly[_d], "val:", left)
        if not left:
            _d = turn_left(_d)
            x += dx[_d]
            y += dy[_d]
            #print("turn left. direction:", _d, "now on", x, y)
            go(x, y, _d)
            if finish == 1:
                return
        else:
            _d = turn_left(_d)
            #print("turn left. direction:", _d)
            continue


go(r, c, d)
print(answer)


'''
6 6
2 1 3
1 1 1 1 1 1
1 0 0 0 0 1
1 0 1 1 1 1
1 0 1 1 1 1
1 0 1 1 1 1
1 1 1 1 1 1

정답: 7
'''