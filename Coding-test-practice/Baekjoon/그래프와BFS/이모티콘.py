from collections import deque

S = int(input())
visited = []
q = deque()
time = [ ([0] * 2001) for _ in range(2001) ]

visited.append((1,0))
q.append((1,0))
while q:
    v0 = q.popleft()
    s = v0[0]
    c = v0[1]
    if s == S:
        print(time[s][c])
        break
    for v in [(s, s), (s+c, c), (s-1, c)]:
        if 1<=v[0]<=2000 and 0<=v[1]<=2000:
            if v not in visited:
                visited.append(v)
                q.append(v)
                time[v[0]][v[1]] = time[s][c] + 1
