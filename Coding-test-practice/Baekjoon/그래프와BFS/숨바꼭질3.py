from collections import deque
#import sys, itertools
MAX = 200000

n, k = map(int, input().split())
q = deque()
visited = [0] * (MAX+1)
time = [-1] * (MAX+1)

visited[n] = 1
time[n] = 0
t=0
q.append(n)
while q:
    x = q.popleft()
    t = time[x]
    if x == k:
        print(t)
        break

    # x*2를 가장 먼저 체크해주어야 함!!
    # 반례: n=1, k=2
    if 0<=x*2<=MAX and visited[x*2]==0:
        visited[x*2] = 1
        time[x*2] = t
        q.appendleft(x*2)
    if 0<=x-1<=MAX and visited[x-1]==0:
        visited[x-1] = 1
        time[x-1] = t+1  
        q.append(x-1)
    if 0<=x+1<=MAX and visited[x+1]==0:
        visited[x+1] = 1
        time[x+1] = t+1
        q.append(x+1)
        
    #print(list(itertools.islice(q, 0, 5)))
    #print("time:", time[:5])