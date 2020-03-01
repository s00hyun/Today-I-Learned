# 미해결

n, m = map(int, input().split())

for l in range(m):
    for i in range(1, n+1):
        for j in range(2, n+1):
            print(i, j)