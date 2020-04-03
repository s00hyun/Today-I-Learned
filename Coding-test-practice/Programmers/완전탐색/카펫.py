def solution(brown, red):
    for i in range(1, red+1):
        if red % i != 0:
            continue
        r = [red // i, i]
        b = [r[0] + 2, r[1] + 2]
        if b[0]*b[1] - red == brown:
            return b
        