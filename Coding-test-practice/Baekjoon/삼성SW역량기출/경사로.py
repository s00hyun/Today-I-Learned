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
        count = 0
        y = 1
        for i in range(_n-1):
            now = road[i]
            if i < n:
                after = road[i+1]
            count += 1

            diff = abs(now-after)
            if diff == 0:
                continue
            elif diff == 1:
                if count < l:  # 경사로 놓을 수 없음
                    y = 0
                    break
                else:  # 경사로 놓을 수 있음
                    if after-now == 1:  # 오르막길
                        count = 0
                    elif 내리막길:  # ㅠㅠ


                    y = 1
                    count = 0
            elif diff > 1:
                y = 0
                break
        if y == 1:
            answer += 1
            print(road, "can be acrossed")


count_walkable_roads(road_map, n , l)
count_walkable_roads(road_map_rotate, n, l)
print(answer)