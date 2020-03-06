import sys

def find(n, m, x, y, arr):
    ans = 0
    x0 = int(x[0])
    y0 = int(y[0])
    for i in range(n):
        if arr[i] not in range(x0, y0+1):
            continue
        num = ''
        for j in range(m):
            idx = i+j
            if idx >= n:
                idx -= n
            num += str(arr[idx])
            #print("index {}: num += {}".format(idx, arr[idx]))
        num = int(num)
        #print("num:", num)
        if num >= int(x):
            if num <= int(y):
                #print("num {} in range".format(num))
                ans += 1
    print(ans)


t = int(sys.stdin.readline())
for i in range(t):
    n, m = map(int, sys.stdin.readline().split())
    x = sys.stdin.readline().rstrip().replace(' ', '')
    y = sys.stdin.readline().rstrip().replace(' ', '')
    arr = list(map(int, list(sys.stdin.readline().split())))
    #print("n={}, m={}, x={}, y={}, arr={}".format(n,m,x,y,arr))
    find(n, m, x, y, arr)