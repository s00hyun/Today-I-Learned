# 각 step마다 board 정보를 저장하고 있어야 한다
# 재귀로 다시 짜기

import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
board = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]
answer = 0
q = deque()
#print(board)

board_copy = [ x[:] for x in board ]
#print("board_copy:", board_copy)


def get_num(i, j):
    if board_copy[i][j] != 0:
        q.append(board_copy[i][j])
        board_copy[i][j] = 0


def move(d):
    if d == 1:  # 상
        for j in range(n):
            for i in range(n):
                get_num(i, j)
            i = 0
            while q:
                v = q.popleft()
                if board_copy[i][j] == 0:
                    board_copy[i][j] = v
                elif board_copy[i][j] == v:  # 합칠 수 있을 경우
                    board_copy[i][j] *= 2
                    i += 1
                else:  # 합칠 수 없을 경우
                    i += 1
                    board_copy[i][j] = v
    elif d == 2:  # 하
        for j in range(n):
            for i in range(n-1, -1, -1):  # 밑에서부터 읽어서 큐에 넣음
                get_num(i, j)
            i = n-1
            while q:
                v = q.popleft()
                if board_copy[i][j] == 0:
                    board_copy[i][j] = v
                elif board_copy[i][j] == v:  # 합칠 수 있을 경우
                    board_copy[i][j] *= 2
                    i -= 1
                else:  # 합칠 수 없을 경우
                    i -= 1
                    board_copy[i][j] = v
    elif d == 3:  # 좌
        for i in range(n):
            for j in range(n):
                get_num(i, j)
            j = 0
            while q:
                v = q.popleft()
                if board_copy[i][j] == 0:
                    board_copy[i][j] = v
                elif board_copy[i][j] == v:  # 합칠 수 있을 경우
                    board_copy[i][j] *= 2
                    j += 1
                else:  # 합칠 수 없을 경우
                    j += 1
                    board_copy[i][j] = v
    elif d == 4:  # 우
        for i in range(n):
            for j in range(n-1, -1, -1):
                get_num(i, j)
            j = n-1
            while q:
                v = q.popleft()
                if board_copy[i][j] == 0:
                    board_copy[i][j] = v
                elif board_copy[i][j] == v:  # 합칠 수 있을 경우
                    board_copy[i][j] *= 2
                    j -= 1
                else:  # 합칠 수 없을 경우
                    j -= 1
                    board_copy[i][j] = v

    #print("board_copy:", board_copy)


def solve(step):
    # 상: 1, 하: 2, 좌:3, 우:4
    global board_copy, answer

    if step == 5:
        # 최댓값 계산
        for i in range(n):
            answer = max(answer, max(board_copy[i]))
        return

    ### 중요:
    # 다음 step을 탐색한 후 현재 step으로 돌아가는 경우도 있으므로, board를 복사해둔다.
    board_copy2 = [x[:] for x in board_copy]  # 부모 노드에서의 보드 정보 (!지역변수!)
    for direction in range(1, 5):
        move(direction)  # board_copy 사용
        solve(step + 1)  # step 끝까지 갔는지 체크
        board_copy = [x[:] for x in board_copy2]  # 자식 노드들은 모두 부모 노드의 보드를 이용해 연산을 수행해야 한다.


solve(0)
print(answer)
