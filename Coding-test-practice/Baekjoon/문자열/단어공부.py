string = input()
string = string.lower()
d = {}

for s in string:
    if s not in d.keys():
        d[s] = 1
    else:
        d[s] += 1

max_cnt = max(d.values())
if list(d.values()).count(max_cnt) != 1:
    print('?')
else:
    for s, c in d.items():
        if c == max_cnt:
            print(s.upper())