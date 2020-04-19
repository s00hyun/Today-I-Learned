import sys

m = int(sys.stdin.readline().rstrip())
S = set()

for j in range(m):
    args = list(sys.stdin.readline().rstrip().split())
    func = args[0]
    x = -1
    if len(args) == 2:
        x = int(args[1])
    #print(func, x)
    #print(S)

    if func == 'add':
        if x not in S:
            S.add(x)
    elif func == 'remove':
        if x in S:
            S.remove(x)
    elif func == 'check':
        if x in S:
            print(1)
        else:
            print(0)
    elif func == 'toggle':
        if x in S:
            S.remove(x)
        else:
            S.add(x)
    elif func == 'all':
        S = { i for i in range(1, 21) }
    elif func == 'empty':
        S = set()
