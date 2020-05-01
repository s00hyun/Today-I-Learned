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
    for i in range(1, 4):
        if wheel[i][2] != wheel[i+1][6]:
            check[i][i+1] = 1
            check[i+1][i] = 1
    rotate(_n, _r)
    if _n-1 >= 1 and check[_n][_n-1] and not check_rotated[_n-1]:
        #print("go again", _n - 1, -1 * _r)
        go(_n-1, -1*_r)
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