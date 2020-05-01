import sys

wheel = [ list(map(int, list(sys.stdin.readline().rstrip()))) for _ in range(4) ]
wheel.insert(0, [])
k = int(sys.stdin.readline().rstrip())
#print(wheel[1:])
check_rotated = [0]*5


def rotate(_i, _d):
    global wheel
    if _d == 1:  # 시계방향
        wheel[_i] = [wheel[_i][7]] + wheel[_i][0:7]
    else:  # 반시계방향 (-1)
        wheel[_i] = wheel[_i][1:] + [wheel[_i][0]]
    check_rotated[_i] = 1


def go(_n, _r):
    global wheel
    check = [ [0]*5 for _ in range(5) ]
    # 맞물린 톱니의 숫자가 서로 다른 톱니바퀴 쌍을 2차원 배열에 저장한다
    for i in range(1, 4):
        if wheel[i][2] != wheel[i+1][6]:
            check[i][i+1] = 1
            check[i+1][i] = 1
    # 톱니바퀴를 회전시킨다
    rotate(_n, _r)
    # 회전한 톱니바퀴의 왼쪽에 있는 톱니바퀴들 중에 돌릴 수 있는 것은 모두 돌린다
    # (맨 오른쪽 톱니바퀴를 돌렸을 때, 맨 왼쪽 톱니바퀴까지 모두 돌아갈 수 있는 경우를 생각 (예제 3))
    if _n-1 >= 1 and check[_n][_n-1] and not check_rotated[_n-1]:
        #print("go again", _n - 1, -1 * _r)
        go(_n-1, -1*_r)
    # 회전한 톱니바퀴의 오른쪽에 있는 톱니바퀴들 중에 돌릴 수 있는 것은 모두 돌린다
    if _n+1 <= 4 and check[_n][_n+1] and not check_rotated[_n+1]:
        #print("go again", _n + 1, -1 * _r)
        go(_n+1, -1*_r)
    #print("wheel:", wheel[1:])


for _ in range(k):
    num, rot = map(int, sys.stdin.readline().rstrip().split())
    #print("go:", num, rot)
    go(num, rot)
    check_rotated = [0]*5

answer = 0
for i in range(1, 5):
    answer += wheel[i][0] * (2**(i-1))
print(answer)