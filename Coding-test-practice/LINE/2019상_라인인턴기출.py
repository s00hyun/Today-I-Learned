import sys
from collections import deque

## 주의 ##
# 일반적인 BFS 방식으로 풀게 되면 답을 구할 수 없다. (반례: c=11, b=1 => 답: 6초. 1->2->3->4->8->16->32)
# 왜냐하면, 예를 들어 t초에 x를 방문했을 경우, t+2초에는 x를 방문할 수 있지만 t+1초에는 방문할 수 없다.
# 따라서 t+1초에 x를 방문하는 경우도 포함할 수 있도록 코드를 짜야 한다.


def go(c, b):
    visit = [ [0]*2 for _ in range(200001) ]
    q = deque()
    q.append(b)
    t = 0
    while q:
        c += t
        if visit[c][t % 2] == 1:  # visit[위치] = 방문 시간
            return t

        v = q.popleft()
        current_pos = v[0]
        for next_pos in [current_pos-1, current_pos+1, 2*current_pos]:
            if 0 <= next_pos <= 200000 and visit[next_pos] == -1:  # 브라운이 아직 방문하지 않은 위치일 경우
                visit[next_pos][(t+1) % 2] = visit[current_pos][t % 2] + 1
                q.append((next_pos, (t+1) % 2))
                #print(b_check[:42])
            if next_pos > 200000:
                return -1


c, b = map(int, sys.stdin.readline().rstrip().split())
print(go(c, b))