import sys

m = int(sys.stdin.readline().rstrip())
S = 0

for j in range(m):
    args = list(sys.stdin.readline().rstrip().split())
    func = args[0]
    x = -1
    if len(args) == 2:
        x = int(args[1])
    #print(func, x)
    #print(S)

    if func == 'add':
        if S & (1 << x) == 0:  # if x not in S
            S |= (1 << x)  # add x
            #print("add", x, ":", S | (1 << x))
    elif func == 'remove':
        if S & (1 << x) == (1 << x):  # if x in S
            S &= ~(1 << x)  # remove x
    elif func == 'check':
        if S & (1 << x) == (1 << x):
            print(1)
        else:
            print(0)
    elif func == 'toggle':
        S ^= (1 << x)
    elif func == 'all':
        S = (1 << 21) - 1  # 1 <= x <= 20
        #print(S)
    elif func == 'empty':
        S = 0
    #print("S:", bin(S))
