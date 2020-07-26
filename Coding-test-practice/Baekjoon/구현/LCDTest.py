import sys

s, n = sys.stdin.readline().rstrip().split()
s = int(s)
n_len = len(n)
row_num = s + 3
height_num = 2*s + 3

answer = [[] for _ in range(height_num)]

for i in range(n_len):
    num = int(n[i])
    lcd = [ [' ']*row_num for _ in range(height_num) ]  # 공백 포함

    '''가로'''
    # 상
    if num not in [1, 4]:
        for j in range(1, 1+s):
            lcd[0][j] = '-'
    # 중
    if num not in [1, 7, 0]:
        for j in range(1, 1+s):
            lcd[s+1][j] = '-'
    # 하
    if num not in [1, 4, 7]:
        for j in range(1, 1+s):
            lcd[2*s + 2][j] = '-'

    '''세로'''
    # 오른쪽 위
    if num not in [5, 6]:
        for j in range(1, 1+s):
            lcd[j][s+1] = '|'
    # 오른쪽 아래
    if num != 2:
        for j in range(s+2, 2*s+2):
            lcd[j][s+1] = '|'
    # 왼쪽 위
    if num not in [1, 2, 3, 7]:
        for j in range(1, 1+s):
            lcd[j][0] = '|'
    # 왼쪽 아래
    if num in [2, 6, 8, 0]:
        for j in range(s + 2, 2 * s + 2):
            lcd[j][0] = '|'

    for r in range(height_num):
        answer[r].extend(lcd[r])

for y in range(height_num):
    for x in range(row_num * n_len):
        print(answer[y][x], end='')
    print()
