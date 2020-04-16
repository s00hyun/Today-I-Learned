# 실패
# 각 step마다 board 정보를 저장하고 있어야 하는데, 단순 DFS로는 불가능..?
# 재귀로 다시 짜기

import sys, copy

n = int(sys.stdin.readline().rstrip())
board = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]
check = [[-1] * n for _ in range(n)]
#print(board)

for i in range(n):
    for j in range(n):
        if board[i][j] != 0:
            check[i][j] = 1
#print(check)


def move(d, s, _board, _check):
    #print("####", (d, s))
    for i in range(n):
        arr = []
        if d == 1:  # 상
            arr = [ _board[j][i] for j in range(n) ]
            chk = [ _check[j][i] for j in range(n)  ]
        elif d == 2:  # 하
            arr = list(reversed([ _board[j][i] for j in range(n) ]))
            chk = list(reversed([ _check[j][i] for j in range(n) ]))
        elif d == 3:  # 좌
            arr = [ _board[i][j] for j in range(n) ]
            chk = [ _check[i][j] for j in range(n) ]
        elif d == 4:  # 우
            arr = list(reversed([ _board[i][j] for j in range(n) ]))
            chk = list(reversed([ _check[i][j] for j in range(n) ]))

        # 블록을 차례대로 비교하기 전에 블록을 한 방향으로 모아야 함!!!
        # 테스트케이스: 그림2 -> 그림3
        arr = [val for val in arr if val != 0]
        chk = [val for val in chk if val != -1]
        #print("arr:", arr)
        if d == 1 or d == 3:
            arr.extend([0] * (n - len(arr)))
            chk.extend([-1] * (n - len(chk)))
        elif d == 2 or d == 4:
            temp = [0] * (n - len(arr))
            temp.extend(list(reversed(arr)))
            arr = copy.deepcopy(temp)
            temp = [-1] * (n - len(chk))
            temp.extend(list(reversed(chk)))
            chk = copy.deepcopy(temp)
        print("moved arr:", arr)
        print("moved chk:", chk)

        # 합칠 블록이 있는지 체크
        match = 0
        for idx in range(n-1):
            if arr[idx] == arr[idx+1] and chk[idx] == 1:
                match = 1
                arr[idx+1] *= 2
                arr[idx] = -1  # 삭제할 위치 표시
                chk[idx] = 2  # 삭제할 위치 표시
                chk[idx+1] = 0
        #print(arr)

        # 합칠 블록이 없을 경우, 해당 step을 위해 복사된 board와 check 배열에 이동된 블록을 업데이트한다.
        if not match:
            #print("not match")
            for j in range(n):
                if d == 1:
                    _board[j][i] = arr[j]
                    _check[j][i] = chk[j]
                elif d == 2:
                    _board[j][i] = arr[(n - 1) - j]
                    _check[j][i] = chk[(n - 1) - j]
                elif d == 3 or d == 4:
                    _board[i] = arr
                    _check[i] = chk
            continue

        # 합칠 블록이 있을 경우, 합친 후, 해당 step을 위해 복사된 board와 check 배열에 블록을 업데이트한다.
        arr = [ val for val in arr if val != -1 ]
        chk = [ val for val in chk if val != 2 ]

        if d == 1 or d == 3:
            arr.extend([0] * (n - len(arr)))
            chk.extend([-1] * (n - len(chk)))
        elif d == 2 or d == 4:
            temp = [0] * (n - len(arr))
            temp.extend(arr)
            arr = copy.deepcopy(temp)
            temp = [-1] * (n - len(chk))
            temp.extend(chk)
            chk = copy.deepcopy(temp)
        print("match:", match, "arr:", arr, "chk:", chk)

        for j in range(n):
            if d == 1:
                _board[j][i] = copy.deepcopy(arr[j])
                _check[j][i] = copy.deepcopy(chk[j])
            elif d == 2:
                _board[j][i] = copy.deepcopy(arr[(n-1)-j])
                _check[j][i] = copy.deepcopy(chk[(n-1)-j])
            elif d == 3 or d == 4:
                _board[i] = copy.deepcopy(arr)
                _check[i] = copy.deepcopy(chk)


    if s == 2:  # For debugging
    #if s == 5:
        print("vertex:", (d,s), "_board:", _board)
        max_val = 0
        for i in range(n):
            #print("max(_board[i])", max(_board[i]))
            max_val = max(max_val, max(_board[i]))
        #print("max_val:", max_val)
        return max_val
    else:
        #if d == 3:
        #    print("vertex:", (d,s), "_board:", _board)
        return 0


def dfs():
    # 상: 1, 하: 2, 좌:3, 우:4
    stack = [(4, 1), (3, 1), (2, 1), (1, 1)]
    board_copy = copy.deepcopy(board)
    check_copy = copy.deepcopy(check)
    answer = 0
    count = []

    while stack:
        direction, step = stack.pop()
        count.append(move(direction, step, board_copy, check_copy))
        if step == 5:
            board_copy = copy.deepcopy(board)
            check_copy = copy.deepcopy(check)
            answer = max(answer, max(count))
        elif step < 5:
            stack.extend( list(reversed([ (i, step+1) for i in range(1, 5) ])) )

    return answer


#print(dfs())
move(1, 1, board, check)