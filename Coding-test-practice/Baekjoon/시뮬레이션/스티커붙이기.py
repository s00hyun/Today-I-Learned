import sys

n, m, K = map(int, sys.stdin.readline().rstrip().split(' '))
g = [ [0]*m for _ in range(n) ]  # N x M
size = []
sticker1 = []  # 원본
sticker2 = []  # 90도
sticker3 = []  # 180도
sticker4 = []  # 270도

for i in range(K):
    r, c = map(int, sys.stdin.readline().rstrip().split(' '))
    size.append((r,c))
    temp = [ list(map(int, list(sys.stdin.readline().rstrip().split(' ')))) for _ in range(r) ]
    sticker1.append(temp)
    
    temp2 = [ [0]*r for _ in range(c) ]  # 90도
    temp3 = [ [0]*c for _ in range(r) ]  # 180도
    temp4 = [ [0]*r for _ in range(c) ]  # 270도
    for j in range(r):
        for k in range(c):
            temp2[k][r-1-j] = sticker1[i][j][k]
            temp3[r-1-j][c-1-k] = sticker1[i][j][k]
            temp4[c-1-k][j] = sticker1[i][j][k]
    sticker2.append(temp2)
    sticker3.append(temp3)
    sticker4.append(temp4)

#print(sticker1)
#print(sticker2)
#print(sticker3)
#print(sticker4)    

def paste(sticker):
    x = len(sticker)
    y = len(sticker[0])
    count_1 = 0
    
    for row in sticker:
        count_1 += row.count(1)
    if x > n or y > m:
        return 0
    for i in range(0, n-x+1):
        for j in range(0, m-y+1):
            c = 0
            for si in range(x):
                for sj in range(y):
                    if g[i+si][j+sj] == 1:
                        continue
                    elif g[i+si][j+sj] == 0 and sticker[si][sj] == 1:  # 색칠이 안 되어있는 자리에 스티커를 붙일 수 있는지 계산
                        c += 1
            #print("For now, c:", c)
            #print("i, j:", i, j)
            if c == count_1:
                break
        if c == count_1:
            break

    if c != count_1:
        return 0

    #print("i, j:", i, j)            
    # 색칠 시작할 좌표 == (i, j)
    for si in range(x):
        for sj in range(y):
            if sticker[si][sj] == 1:
                g[i+si][j+sj] = 1
    #print(g)            
    return c

#print(paste(sticker1[0]))    

ans = 0
#print("K:", K)
for i in range(K): 
    for s in [sticker1[i], sticker2[i], sticker3[i], sticker4[i]]:
        #print("s:",s)
        result = paste(s)
        #print("result:", result)
        if result != 0:
            ans += result 
            break
print(ans)
