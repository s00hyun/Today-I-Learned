import sys

n = int(sys.stdin.readline().rstrip())
S = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]
team_check = [0] * n

result = 100000


def go(idx, cnt):
    global result
    if idx == n:
        return
    if cnt == n // 2:  # 팀을 다 나눔
        # 각 팀의 점수 계산
        s1 = 0
        s2 = 0
        for i in range(n):
            for j in range(i, n):
                if team_check[i] and team_check[j]:
                    s1 += S[i][j]
                    s1 += S[j][i]
                elif not team_check[i] and not team_check[j]:
                    s2 += S[i][j]
                    s2 += S[j][i]
        result = min(result, abs(s1 - s2))
        return

    team_check[idx] = 1
    go(idx+1, cnt+1)
    team_check[idx] = 0
    go(idx+1, cnt)


go(0, 0)
print(result)
