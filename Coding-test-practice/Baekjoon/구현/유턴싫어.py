import sys
import copy

r, c = map(int, input().split())

arr = []  # input + 상하좌우 1줄씩 추가
temp = []
n = 0
pos = (0,0)
way = [] 


arr.append(['X'] * (c+2))
for i in range(r):
    temp = list(input())
    if temp.count('.') != 0 and n == 0:
        pos = (i+1, temp.index('.')+1)  # 첫번째 길의 좌표 (시작점)
    n += temp.count('.')
    temp.insert(0, 'X')
    temp.insert(c+1, 'X')
    arr.append(temp)
    temp = []
arr.append(['X'] * (c+2))
#print("n=", n)
print("arr:\n", arr)

# 리스트 복사
#arr_check = copy.deepcopy(arr)

# 모든 길(.)에 대해 이동가능한 방향이 1 이하인지(막다른 길인지) 확인
for i in range(1, r+1):
    for j in range(1, c+1):
        if arr[i][j] == 'X':
            continue
        cnt = 0
       
        if arr[i-1][j] == 'X':
            cnt += 1
        if arr[i+1][j] == 'X':
            cnt += 1
        if arr[i][j-1] == 'X':
            cnt += 1
        if arr[i][j+1] == 'X':
            cnt += 1
        
        if cnt >= 3:
            print(1)
            sys.exit()
print(0)
sys.exit()


'''
# 이동가능한 방향이 1 이하이면 막다른 길

road_exists = 0

while way.count('X') < 3:
    print("Current position: {}".format(pos))

    for i in range(1, r+1):  # 모두 방문했는지 체크
        print("for문:", arr_check[i])
        if '.' in arr_check[i]:
            road_exists = 1
    print("road_exists=", road_exists)
    if road_exists == 0:
        print(0)
        sys.exit()

    arr_check[pos[0]][pos[1]] = 'X'  # 방문
    print("방문현황: \n", arr_check)
    print("원본 arr: \n", arr)

    way_coord = [ (pos[0]-1,pos[1]), (pos[0]+1,pos[1]), (pos[0], pos[1]-1), (pos[0], pos[1]+1) ]  # 상,하,좌,우
    way = []
    for p in way_coord:
        way.append(arr[p[0]][p[1]])  # 상하좌우 길 정보 저장
    print("갈 수 있는 길:", way)

    if way.count('X') >= 3:  # 막다른 길
        print(1)
        sys.exit()
    else:  # 막다른 길이 아님
        # 다음 길의 좌표로 pos값을 업데이트

        for p in way_coord:
            x = p[0]
            y = p[1]
            if arr[x][y] != '.':
                continue
            else:
                pos = (x,y)
            if arr_check[x][y] == 'X':
                continue

        print("next position:",pos)     
'''