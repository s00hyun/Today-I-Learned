# 71.0/100.0

def check(k, lock, N, M, blank_to_fill):
    #print("### For", k)
    for i in range(-M+1, (N-1)+1):
        for j in range(-M+1, (N-1)+1):
            cnt = 0
            flag = 0
            #print("i:", i, "j:", j)
            for x in range(M):
                for y in range(M):
                    if 0<=x+i<M and 0<=y+j<M:
                        #print("k[{}][{}]: {}, lock[{}][{}]: {}".format(x, y, k[x][y], x+i, y+j, lock[x+i][y+j]))
                        if k[x+i][y+j] == 1:
                            if lock[x][y] == 0:
                                cnt += 1
                            else:
                                flag = 1
                                break
                if flag == 1:
                    break
            if cnt == blank_to_fill:
                return 0
    return 1


def solution(key, lock):
    M = len(key[0])
    N = len(lock[0])
    key90 = [[0] * M for _ in range(M)]
    key180 = [[0] * M for _ in range(M)]
    key270 = [[0] * N for _ in range(M)]  # 0, 90, 180, 270도 회전
    keys = [key, key90, key180, key270]

    for i in range(M):
        for j in range(M):
            key90[j][M - 1 - i] = key[i][j]
            key180[M - 1 - i][M - 1 - j] = key[i][j]
            key270[M - 1 - j][i] = key[i][j]
    #print(key90)
    #print(key180)
    #print(key270)

    blank_to_fill = 0
    for row in lock:
        blank_to_fill += row.count(0)
    #print(blank_to_fill)

    for k in keys:
        if check(k, lock, N, M, blank_to_fill) == 0:  # 열쇠 사용 가능한 경우가 존재
            #print(k)
            return True
    return False


#print(solution([[0, 0, 0], [1, 0, 0], [0, 1, 1]], [[1, 1, 1], [1, 1, 0], [1, 0, 1]]))
print(solution([[0, 0, 0], [0, 0, 0], [0, 0, 1]], [[0, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1], [1, 1, 1, 1]]))