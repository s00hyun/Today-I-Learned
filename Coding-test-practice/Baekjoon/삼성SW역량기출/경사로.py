import sys

n, l = map(int, sys.stdin.readline().rstrip().split())
road_map = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]
road_map_rotate = [ [0]*n for _ in range(n) ]
answer = 0

for i in range(n):
    for j in range(n):
        road_map_rotate[j][i] = road_map[i][j]


def count_walkable_roads(_map, _n, _l):
    global answer
    for road in _map:
        i = 0
        check = [0]*_n
        while i < n-1:
            now = road[i]
            next = road[i + 1]
            diff = now - next

            if abs(diff) > 1:
                break  # 건널 수 없는 길
            elif diff == 1:  # 내리막길
                flag = 0
                for j in range(_l):
                    if not 0<=i+j+1<n:
                        flag = 1
                        break
                    else:
                        if road[i+1+j] != next or check[i+1+j]:
                            flag = 1
                            break
                        else:
                            check[i+1+j] = 1
                if flag == 1:
                    break  # 건널 수 없는 길
                else:
                    i += _l
                    if i == n - 1:
                        answer += 1
                        #print(road, "is crossable")
                    continue
            elif next-now == 1:  # 오르막길
                    flag = 0
                    for j in range(_l):
                        if not (0<=i-j<n):
                            flag = 1
                            break
                        else:
                            if road[i-j] != now or check[i-j]:
                                flag = 1
                                break
                            else:
                                check[i-j] = 1
                    if flag == 1:
                        break  # 건널 수 없는 길
            i += 1
            if i == n-1:
                answer += 1
                #print(road, "is crossable")


count_walkable_roads(road_map, n , l)
count_walkable_roads(road_map_rotate, n, l)
print(answer)
