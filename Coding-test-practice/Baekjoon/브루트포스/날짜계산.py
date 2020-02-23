E, S, M = map(int, input().split())
max_y = 15*28*19

e = 1
s = 1
m = 1
y = 1

while y <= max_y:
    if e == 16:
        e = 1
    if s == 29:
        s = 1
    if m == 20:
        m = 1

    if e == E and s == S and m == M:
        print(y)
        break

    e += 1
    s += 1
    m += 1
    y += 1
                