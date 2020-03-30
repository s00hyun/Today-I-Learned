import sys

N = int(sys.stdin.readline().rstrip())
score = [ [i+1] + list(map(int, sys.stdin.readline().rstrip().split())) for i in range(N) ]


#print(score)
def go(score):
    score = sorted(score, key=lambda x: (-x[1], x[2], x[3]))
    #print(score)
    return score[0][0]


print(go(score))
