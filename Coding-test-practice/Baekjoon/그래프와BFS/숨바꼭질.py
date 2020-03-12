from collections import deque

n, k = map(int, input().split())
check = [0] * 200001
ans = [0] * 200001
q = deque()

check[n] = 1
q.append(n)
while q:
    v = q.popleft()
    if v == k:
        print(ans[v])
        break
    for e in [v-1, v+1, v*2]:
        if 0<=e<=200000 and check[e] != 1:
            check[e] = 1
            ans[e] = ans[v] + 1
            q.append(e)