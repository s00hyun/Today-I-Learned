import sys, copy
from itertools import product

n, m = map(int, sys.stdin.readline().rstrip().split())
office = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]
cctv_num = []
cctv_loc = []
direction_num = [0, 1, 2, 2, 3, 4]
direction_cases = [0, 4, 2, 4, 4, 1]
dx = [0, -1, 0, 1]  # 우, 하, 좌, 상 (오른쪽으로 90도씩 회전)
dy = [1, 0, -1, 0]
camera = [[], [0], [0, 2], [0, 3], [0, 2, 3], [0, 1, 2, 3]]
answer = 70

for i in range(n):
    for j in range(m):
        status = office[i][j]
        if status in [1,2,3,4,5]:
            cctv_num.append(status)
            cctv_loc.append((i, j))

pool = [ [ i for i in range(direction_cases[n]) ] for n in cctv_num ]
#print(pool)


def get_sagak(_office):
    result = 0
    for row in _office:
        result += row.count(0)
    return result


def go(_val):
    global cctv_num, cctv_loc, camera, answer, office, pool

    check = copy.deepcopy(office)
    for i in range(len(_val)):
        cnum = cctv_num[i]
        direction = _val[i]
        x, y = cctv_loc[i]
        for j in range(direction_num[cnum]):  # 해당 cctv가 바라보는 각 방향에 대해
            d = (camera[cnum][j] + direction) % 4  # 방향 인덱스 셋팅
            nx = x
            ny = y
            while True:  # 감시가능한 영역 모두 체크
                nx += dx[d]
                ny += dy[d]
                if not (0<=nx<n and 0<=ny<m):
                    break
                s = check[nx][ny]
                if s == 6:
                    break
                if s == 0:
                    check[nx][ny] = -1
    #for row in check:
    #    print(row)
    answer = min(answer, get_sagak(check))
    #print(answer)


for val in product(*pool):
    #print(val)
    go(val)
print(answer)
