import sys
from itertools import combinations

n = int(sys.stdin.readline().rstrip())
S = [ list(map(int, sys.stdin.readline().rstrip().split())) for _ in range(n) ]
n_team = [ i for i in range(n) ]

result = 10000

for comb in combinations(n_team, n//2):
    team1 = 0
    team2 = 0
    n_team2 = list(set(n_team) - set(comb))
    for pair in combinations(comb, 2):
        i = pair[0]
        j = pair[1]
        team1 += S[i][j]
        team1 += S[j][i]
    for pair in combinations(n_team2, 2):
        i = pair[0]
        j = pair[1]
        team2 += S[i][j]
        team2 += S[j][i]
    result = min(result, abs(team1 - team2))


print(result)