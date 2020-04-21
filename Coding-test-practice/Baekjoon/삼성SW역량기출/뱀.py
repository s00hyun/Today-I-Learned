import sys

n = int(sys.stdin.readline().rstrip())
board = [ [-1] + [0]*n + [-1] for _ in range(n) ]  # (n+2) x (n+2)  (0 ~ n+1)
board.insert(0, [-1]*(n+2))
board.insert(n+1, [-1]*(n+2))
change_t = []
change_dir = []
dx = [0, 1, 0, -1]  # 우, 하, 좌, 상 (정방향: 오른쪽으로 90도씩 / 역방향: 왼쪽으로 90도씩)
dy = [1, 0, -1, 0]

a = int(sys.stdin.readline().rstrip())
for _ in range(a):
    i, j = map(int, sys.stdin.readline().rstrip().split())
    board[i][j] = 2  # 사과

l = int(sys.stdin.readline().rstrip())
for _ in range(l):
    x, c = sys.stdin.readline().rstrip().split()
    change_t.append(int(x))
    if c == 'L':
        change_dir.append(-1)
    else:
        change_dir.append(1)


head = [1, 1]
tail = [1, 1]
d = 0  # right (default)
d_tail = 0

board[1][1] = 1  # 출발지점
t = 0
while True:
    if t in change_t:
        d += change_dir[change_t.index(t)]  # 다음 방향을 가리키는 인덱스
        if d >= 4:
            d %= 4
        elif d < 0:
            d += 4

    # 이동 전 위치 기록
    x, y = head
    # 다음 위치로 이동
    nx = x + dx[d]
    ny = y + dy[d]
    head = [nx, ny]

    head_val = board[nx][ny]

    # 벽을 만나면 종료
    if head_val == -1:
        print(t+1)
        break
    # 자기 몸에 닿으면 종료
    if head_val == 1:
        print(t+1)
        break

    if board[nx][ny] != 2:  # 사과가 없음
        # 꼬리가 위치한 칸을 비움
        tx, ty = tail[0], tail[1]
        board[tx][ty] = 0
        # !주의! 꼬리는 머리와 방향이 동일해질 때에만 변경한다
        if tx == head[0] or ty == head[1]:
            d_tail = d
        tail = [tx + dx[d_tail], ty + dy[d_tail]]

    # 머리가 위치한 칸을 채움
    board[nx][ny] = 1

    t += 1
    '''
    print(t, "초")
    for i in range(n+2):
        print(board[i])
    print("tail:", tail, "\n")
    '''
