import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
board = [ [-1] + [0]*n + [-1] for _ in range(n) ]  # (n+2) x (n+2)  (0 ~ n+1)
board.insert(0, [-1]*(n+2))
board.insert(n+1, [-1]*(n+2))
change = deque()
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상 (정방향: 오른쪽으로 90도씩 / 역방향: 왼쪽으로 90도씩)
dy = [1, 0, -1, 0]

a = int(sys.stdin.readline().rstrip())
for _ in range(a):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    board[i][j] = 2  # 사과가 있는 곳

l = int(sys.stdin.readline().rstrip())
for _ in range(l):
    x, c = sys.stdin.readline().rstrip().split()
    if c == 'L':
        change.append((int(x), -1))
    else:
        change.append((int(x), 1))


head = (1, 1)
d = 0  # right (default)
snake = deque([head])

board[1][1] = 1  # 출발지점
t = 0
tc, dc = change.popleft()
while True:
    if t == tc:
        d += dc  # 다음 방향을 가리키는 인덱스
        if d >= 4:
            d %= 4
        elif d < 0:
            d += 4
        if change:  # not empty
            tc, dc = change.popleft()

    # 이동 전 위치 기록
    x, y = snake[0]
    # 다음 위치로 이동
    nx = x + dx[d]
    ny = y + dy[d]
    snake.appendleft((nx, ny))

    head_val = board[nx][ny]

    # 벽을 만나면 종료
    if head_val == -1:
        print(t+1)
        break
    # 자기 몸에 닿으면 종료
    elif head_val == 1:
        print(t+1)
        break

    if head_val != 2:  # 머리가 위치한 칸에 사과가 없음 (head_val == 0)
        # 꼬리가 위치한 칸을 비움
        tx, ty = snake.pop()
        board[tx][ty] = 0

    # 머리가 위치한 칸을 채움 (head_val == 0 or 2)
    board[nx][ny] = 1

    t += 1
    '''
    print(t, "초")
    print(snake)
    for i in range(n+2):
        print(board[i])
    '''
